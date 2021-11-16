# chat/routing.py
from django.urls import re_path , path

from . import consumers

websocket_urlpatterns = [
    path('ws/server/<str:client>/', consumers.ServerConsumer.as_asgi()),
]