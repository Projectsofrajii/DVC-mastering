import xmltodict
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings
import paho.mqtt.client as mqtt
from django.utils import timezone
from xml.etree import ElementTree as ET
import json

class MyConsumer(AsyncWebsocketConsumer):  # handshaking/connect/disconnect # receiving data status also getting
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_time = timezone.now().strftime("%Y-%m-%d %H:%M:%S")

        self.broker_address = settings.MQTT_BROKER_HOST
        self.broker_port = settings.MQTT_BROKER_PORT
        self.client_id = settings.MQTT_CLIENT_ID
        self.topic = settings.MQTT_TOPIC
        self.client = None

    async def connect(self):
        await self.accept()
        self.client = mqtt.Client(client_id=self.client_id)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.broker_address, self.broker_port, 60)
        self.client.loop_start()
    
    async def disconnect(self, close_code):
        print('close code ', close_code)
        await self.connect()

    def on_connect(self, client, userdata, flags, rc):
        print("Time", self.current_time, "Connected to MQTT broker with result code " + str(rc))
        self.client.subscribe(self.topic)


    def on_messages(self, client, userdata, msg):
        message = msg.payload.decode('utf-8')
        root = ET.fromstring(message)

        obj = {}
        obj[root.tag] = {}
        obj[root.tag] = self.generateobj(root.getchildren())
        for item in root.items():
            obj[root.tag][item[0]] = item[1]
        
        # meter_id = root.find(".//METER").get("ID")
        # print("Time", self.current_time, "Message Received","Meter_ID", meter_id)
        async_to_sync(self.send)(text_data = json.JSONEncoder().encode(obj))


    def generateobj(self, elemls):
        obj = {}
        for el in elemls:
            tag = el.tag
            if el.tag == 'METER':
                tag = f'{el.tag}_{el.get("ID")}'
            
            obj[tag] = {}

            if el.getchildren().__len__() > 0:
                obj[tag] = self.generateobj(el.getchildren())

            for i in el.items():
                    obj[tag][i[0]] = i[1]
                    
        return obj
    def on_message(self, client, userdata, msg):
        message = msg.payload.decode('utf-8')
        xml_dict = xmltodict.parse(message, attr_prefix='')
        json_data = json.dumps(xml_dict)
        async_to_sync(self.send)(text_data=json_data)