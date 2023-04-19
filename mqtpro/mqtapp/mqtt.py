'''import paho.mqtt.client as mqtt
from django.conf import settings

client = mqtt.Client(settings.MQTT_CLIENT_ID)

def on_connect(mqtt_client, userdata, flags, rc):
   if rc == 0:
       print('Connected successfully')
   else:
       print('Bad connection. Code:', rc)

def on_message(mqtt_client, userdata, msg):
    print(f'Received message on topic: {msg.topic} with payload: {msg.payload}')

client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(settings.MQTT_USERNAME, settings.MQTT_PASSWORD)
client.connect(
    host=settings.MQTT_BROKER_HOST,
    port=settings.MQTT_BROKER_PORT,
    keepalive=settings.MQTT_KEEPALIVE
)
client.subscribe(settings.MQTT_TOPIC)
client.loop_start()

'''