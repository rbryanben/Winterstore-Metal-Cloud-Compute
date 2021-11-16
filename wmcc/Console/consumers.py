# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ServerConsumer(WebsocketConsumer):

    def connect(self):
        self.client = self.scope['url_route']['kwargs']['client']
        self.client_group_name = 'session_%s' % self.client
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.client_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.client_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.client_group_name,
            {
                'type': 'control_message',
                'message': message
            }
        )

    # Receive message from room group
    def control_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))