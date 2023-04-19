'''from mqtapp.mqtt import *

client.loop_start()
from django.db import connections
import websocket

@websocket
def ws_mqtt_subscribe(request):
    connections.add(request.websocket)# Add the connection to the group
    while True:# Wait for messages from the WebSocket
        message = request.websocket.receive()
        if not message:
            break
    connections.remove(request.websocket)# Remove the connection from the group'''