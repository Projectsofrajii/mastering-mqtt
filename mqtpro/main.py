import json
from django.http import JsonResponse
from .mqtt import client as mqtt_client
from rest_framework import views


def publish_message(request):
    request_data = json.loads(request.body)
    rc, mid = mqtt_client.publish(request_data['msg'])
    return JsonResponse({'code': rc})


# Define MQTT settings
MQTT_BROKER_HOST = "122.176.28.40"
MQTT_PORT = 1883
MQTT_TOPIC = 'synergy/mqtt/dcu/meterdata'

# Initialize MQTT client
mqtt_client = mqtt.Client()

# Define callback for MQTT message received
def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    print("MQTT message received: ", payload)
    # Publish the MQTT message to the WebSocket
    for connection in connections.all():
        connection.send(payload)

# Connect to the MQTT broker and subscribe to the topic
mqtt_client.connect(MQTT_BROKER_HOST, MQTT_PORT)
mqtt_client.subscribe(MQTT_TOPIC)
mqtt_client.on_message = on_message

# Define the Django view that will handle the MQTT messages
@require_GET
@csrf_exempt
def mqtt_subscribe(request):
    return render(request, "mqtt_subscribe.html")

# Define the WebSocket connection handler
@websocket
def ws_mqtt_subscribe(request):
    # Add the connection to the group
    connections.add(request.websocket)

    # Wait for messages from the WebSocket
    while True:
        message = request.websocket.receive()
        if not message:
            break

    # Remove the connection from the group
    connections.remove(request.websocket)

    return HttpResponse()

'''from django.conf import settings
import paho.mqtt.client as mqtt
from django.conf import settings
from django.http import HttpResponse


mqtt_client = mqtt.Client()
mqtt_client.connect("122.176.28.40", 1883)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

mqtt_client.on_connect = on_connect
mqtt_client.publish("synergy/mqtt/dcu/meterdata", "Hello from Django!")
mqtt_client.loop_start()
mqtt_client.disconnect()

def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    print("MQTT message received: ", payload)
    # Process the MQTT message as needed

mqtt_client = mqtt.Client()# Create MQTT client
mqtt_client.connect(settings.MQTT_BROKER_HOST, settings.MQTT_BROKER_PORT)# Connect to MQTT broker using settings from Django settings
mqtt_client.subscribe('synergy/mqtt/dcu/meterdata')# Subscribe to a topic
mqtt_client.on_message = on_message
mqtt_client.loop_start()# Start MQTT loop
mqtt_client.disconnect()

# Django view function
def my_view(request):
    mqtt_client.publish("synergy/mqtt/dcu/meterdata", "Hello from Django!") # Publish message to MQTT broker
    return HttpResponse("Message published to MQTT broker.")'''
