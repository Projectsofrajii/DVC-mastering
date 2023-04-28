# -*- coding: utf-8 -*-
__version__ = "0.0.2"

import json
import functools
from environs import Env
import redis
from redis.lock import LockError
from redis.sentinel import Sentinel, MasterNotFoundError
from urllib.parse import urlparse, parse_qs
import logging

logger = logging.getLogger()


class MySentinel(Sentinel):
    """Class to avoid MasterNotFoundError when using only one sentinel and get real error"""

    def discover_master(self, service_name):
        """
        Asks sentinel servers for the Redis master's address corresponding
        to the service labeled ``service_name``.

        Returns a pair (address, port) or raises MasterNotFoundError if no
        master is found.
        """
        if len(self.sentinels) > 1:
            return super().discover_master(service_name)
        sentinel = self.sentinels[0]
        masters = sentinel.sentinel_masters()
        state = masters.get(service_name)
        if state and self.check_master_state(state, service_name):
            return state['ip'], state['port']

        logger.error(f"No master found for {service_name}, masters: {masters}, state: {state}")

        raise MasterNotFoundError("No master found for %r" % (service_name,))


_redis_master = None
_redis_slave = None


def get_redis(master=True, reconnect=False, env=None):
    global _redis_master
    global _redis_slave

    if env is None:
        env = Env()

    if _redis_master is not None and not reconnect:
        return _redis_master if master else _redis_slave

    redis_url = env.str("REDIS_URL")
    url = urlparse(redis_url)

    if ":" in url.netloc:
        host, port = url.netloc.split(":", 1)
        port = int(port)
    else:
        host, port = url.netloc, None

    if len(url.path) > 1:
        db = int(url.path[1:])
    else:
        db = 0

    if url.scheme == "redis":
        if port is None:
            port = 6379
        _redis_slave = _redis_master = redis.Redis(host=host, port=port, db=db)
    elif url.scheme == "sentinel":
        if port is None:
            port = 26379

        params = parse_qs(url.query)
        REDIS_MASTER = params["master"][0] if "master" in params else env.str("REDIS_MASTER", "redis")
        REDIS_TIMEOUT = float(params["timeout"][0]) if "timeout" in params else env.float(
            "REDIS_TIMEOUT", 0.2
        )
        sentinel = MySentinel([(host, port)], socket_timeout=REDIS_TIMEOUT)
        _redis_master = sentinel.master_for(REDIS_MASTER, socket_timeout=REDIS_TIMEOUT, db=db)
        _redis_slave = sentinel.slave_for(REDIS_MASTER, socket_timeout=REDIS_TIMEOUT, db=db)

    return _redis_master if master else _redis_slave


def get_json(key, client=None):
    if client is None:
        client = get_redis(False)
    ret = client.get(key)
    if ret is None:
        return None
    return json.loads(ret)


def set_json(key, value, client=None, **kargs):
    if client is None:
        client = get_redis(True)
    value = json.dumps(value)
    return client.set(key, value, **kargs)


def one_at_a_time(lock_key=None, max_lock=None, lock_timeout=None, key_prefix="", client=None,
                  on_lock_error=None):
    def decorator(f):
        key = lock_key
        if key is None:
            key = "{}{}".format(key_prefix, f.__name__)

        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            if client is None:
                myclient = get_redis(True)
            else:
                myclient = client

            try:
                with myclient.lock(key, timeout=max_lock, blocking_timeout=lock_timeout):
                    return f(*args, **kwargs)
            except redis.exceptions.LockError:
                if on_lock_error is None:
                    raise
                else:
                    return on_lock_error()

        return wrapped
    return decorator


# From https://dev.to/astagi/rate-limiting-using-python-and-redis-58gk
def request_is_limited_timebucket(key, limit, period, client=None):
    if client is None:
        client = get_redis(True)
    if client.setnx(key, limit):
        client.expire(key, period)

    bucket_val = client.get(key)
    if bucket_val and int(bucket_val) > 0:
        client.decrby(key, 1)
        return False
    return True


def request_is_limited_gcra(key, limit, period, client=None):
    if client is None:
        client = get_redis(True)
    t = client.time()[0]
    separation = round(period / limit)
    client.setnx(key, 0)
    try:
        with client.lock('lock:' + key, blocking_timeout=5):
            tat = max(int(client.get(key)), t)
            if tat - t <= period - separation:
                new_tat = max(tat, t) + separation
                client.set(key, new_tat)
                return False
            return True
    except LockError:
        return True


def request_is_limited(key, limit, period, algorithm="gcra", client=None):
    return globals()["request_is_limited_{}".format(algorithm)](key, limit, period, client=client)


class TooManyRequests(Exception):
    """
    Occurs when the maximum number of requests is reached for a given resource
    of an specific user.
    """
    pass


def rate_limit(limit, period, key=None, key_prefix="", algorithm="gcra", client=None):
    def decorator(f):
        if key is None:
            request_key = "{}{}".format(key_prefix, f.__name__)
        else:
            request_key = key

        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            limited = request_is_limited(request_key, limit, period, algorithm, client)
            if limited:
                raise TooManyRequests(
                    f"Too many requests for {request_key} allowed {limit}/{period}secs"
                )
            else:
                return f(*args, **kwargs)
        return wrapped
    return decorator


class RateLimitLogFilter(logging.Filter):
    def __init__(self, key, limit, period, algorithm="gcra"):
        self.key = key
        self.limit = limit
        self.period = period
        self.algorithm = algorithm

    def filter(self, record):
        return not request_is_limited(self.key, self.limit, self.period, self.algorithm)
