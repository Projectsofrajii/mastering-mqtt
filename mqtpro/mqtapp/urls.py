from django.urls import path
from .import views

urlpatterns = [
    path('subscribe/', views.subscribe, name="subscribe"),
    path('pub_msg/', views.publish_message, name="pub_msg"),
    path('pub_file/', views.publish_file, name="pub_file"),
    path('sub/', views.mqtt_subscribe, name="sub"),
    path('on_message/', views.on_message, name='on_message'),
    path('on_disconnect/', views.on_disconnect, name='on_disconnect'),
]
