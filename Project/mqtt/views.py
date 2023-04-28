import json
import paho.mqtt.client as mqtt
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from django.core.cache import cache

client = mqtt.Client(settings.MQTT_CLIENT_ID)
count = 0

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f'Connected to {settings.MQTT_BROKER_HOST} broker successfully  ')
    else:
        print('Bad connection./check username/password. Code:', rc)

latest_messages = []
def on_message(client, userdata, msg):
    latest_messages.append(msg.payload.decode('utf-8'))
    cache.set('latest_messages', latest_messages)
def my_view(request):
    global count
    count += 1
    time = timezone.now()
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    message_data = latest_messages
    #message_data = cache.get('latest_messages', [])
    context = {'message': message_data, 'time': current_time, 'count': count}
    return render(request, 'msg.html', context)
@require_GET
@csrf_exempt
def subscribe(request):
    request_data = json.loads(request.body)
    check_topic = settings.MQTT_TOPIC  # Subscribe to the desired topic
    get_topic = request_data['topic']
    if get_topic == check_topic:
        client.subscribe(settings.MQTT_TOPIC, qos=0)
        return JsonResponse({"Subscribed to MQTT topic": settings.MQTT_TOPIC},
                            safe=False)  # Return a response to the client

@require_GET
@csrf_exempt
def publish_message(request):
    request_data = json.loads(request.body)
    get_message = request_data['msg']
    client.publish(topic=settings.MQTT_TOPIC, payload=get_message, qos=0,
                   retain=False)  # Replace with desired QoS and retain settings
    return JsonResponse('Message published successfully to topic: {}'.format(get_message), safe=False)

@require_GET
@csrf_exempt
def publish_file(request):
    # file_path = os.path.join('mqtpro', 'mqtapp', 'static', 'received_file_04_04_2023_18_24_35.cdf')
    file_path = "/home/rajalakshmi/PycharmProjects/MQTT/mqtpro/mqtapp/static/received_file_04_04_2023_18_24_35.cdf"
    with open(file_path, 'r') as file:
        file_content = file.read()
        client.publish(settings.MQTT_TOPIC, payload=file_content, qos=0, retain=False)
        return JsonResponse('Message published successfully to topic: {}'.format(file_content), safe=False)

def on_disconnect(request):
    client.loop_stop()
    client.disconnect()
    return JsonResponse("Successfully disconnected from MQTT broker.", safe=False)

def unsubscribe(request):
    # Unsubscribe from a topic
    client.unsubscribe(settings.MQTT_TOPIC)
    return JsonResponse("Topic Unsubscribed Successfully", safe=False)

client.username_pw_set(settings.MQTT_USERNAME, settings.MQTT_PASSWORD)
client.connect(
        host=settings.MQTT_BROKER_HOST,
        port=settings.MQTT_BROKER_PORT,
        keepalive=settings.MQTT_KEEPALIVE
    )
client.subscribe(settings.MQTT_TOPIC)
client.loop_start()
client.subscribe = subscribe
client.on_connect = on_connect
client.on_message = on_message