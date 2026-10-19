"""Regression tests for the Channels 4 ASGI application."""

# Django
from django.contrib.auth import get_user_model
from django.test import TransactionTestCase
from django.test import override_settings

# 3rd-party
from channels.db import database_sync_to_async
from channels.testing import HttpCommunicator
from channels.testing import WebsocketCommunicator

# Project
from backend.chat.models import Message
from backend.project.asgi import application


@override_settings(CHANNEL_LAYERS={
    'default': {'BACKEND': 'channels.layers.InMemoryChannelLayer'},
})
class ASGIUpgradeTests(TransactionTestCase):
    """Check HTTP routing and authenticated WebSocket messaging."""

    def setUp(self):  # noqa: D102
        self.user = get_user_model().objects.create_user(
            username='chat-student', email='chat@example.com', account_type='student',
        )

    async def test_http_application(self):
        """Route HTTP through Django's ASGI application."""
        communicator = HttpCommunicator(application, 'GET', '/get_account_info/')
        response = await communicator.get_response()
        self.assertEqual(response['status'], 401)
        await communicator.wait()

    async def test_websocket_messages_are_broadcast_and_saved(self):
        """Keep chat working after replacing the removed Channels HTTP handler."""
        communicator = WebsocketCommunicator(application, '/ws/chat/upgrade/')
        communicator.scope['user'] = self.user
        connected, _ = await communicator.connect()
        self.assertTrue(connected)
        await communicator.send_json_to({'message': 'Hello from Python 3.15'})
        response = await communicator.receive_json_from()
        self.assertEqual(response, {'message': 'chat-student: Hello from Python 3.15'})
        await communicator.disconnect()
        saved = await database_sync_to_async(Message.objects.get)(user=self.user)
        self.assertEqual(saved.content, 'Hello from Python 3.15')
