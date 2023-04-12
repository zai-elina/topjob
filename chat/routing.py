from django.template.defaulttags import url
from django.urls import path
from . import consumers

websocket_urlpatterns =  [
    path('chat/',consumers.ChatConsumer.as_asgi()),
]