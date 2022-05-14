"""Chat implementation."""

# Standard Library
import json

# 3rd-party
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

# Project
from backend.chat.models import Message
from backend.chat.utils import get_conversation


class ChatConsumer(AsyncWebsocketConsumer):
    """Chat consumer async websocket."""

    def __init__(self, *args, **kwargs):  # noqa: D107
        super().__init__(*args, **kwargs)
        self.conv_name = ''
        self.conv_group_name = ''
        self.user = None

    async def connect(self):  # noqa: D102
        self.conv_name = self.scope['url_route']['kwargs']['conv_name']
        self.conv_group_name = f'chat_{self.conv_name}'
        self.user = self.scope['user']
        if self.user and self.user.is_authenticated:
            # Join room group
            await self.channel_layer.group_add(
                self.conv_group_name,
                self.channel_name,
            )

            await self.accept()

    async def disconnect(self, close_code):  # noqa: D102
        # Leave room group
        await self.channel_layer.group_discard(
            self.conv_group_name,
            self.channel_name,
        )

    def parse_message(self, message):  # noqa: D102
        return f'{self.user.username}: {message}'

    def create_message_log(self, conv, message):  # noqa: D102
        Message.objects.create(
            conversation=conv,
            user=self.user,
            content=message,
        )

    # Receive message from WebSocket
    async def receive(self, text_data):  # noqa: D102
        conv = await database_sync_to_async(get_conversation)(self.conv_name)
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        if message and conv and self.user and self.user.is_authenticated:
            # Send message to room group
            await self.channel_layer.group_send(
                self.conv_group_name,
                {
                    'type': 'chat_message',
                    'message': self.parse_message(message),
                },
            )
            await database_sync_to_async(self.create_message_log)(conv, message)

    # Receive message from room group
    async def chat_message(self, event):  # noqa: D102
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
        }))
