from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/meter/", consumers.MyConsumer.as_asgi()),
]
'''
from django.urls import path

from .consumers import MyConsumer
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path("ws/meter/",MyConsumer.as_asgi()),
        ])
    ),
})'''