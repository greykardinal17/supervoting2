"""Tests for the Telegram bot using aiogram-test-framework."""
import pytest
from aiogram import Bot, Dispatcher

from aiogram_test_framework import AsyncBotTestMixin

from pythonProject1.bot import setup_dispatcher


class TestBotHandlers(AsyncBotTestMixin):
    """Test class for bot handlers."""

    @pytest.fixture(autouse=True)
    async def setup(self):
        """Setup test client before each test."""
        self.client = await self.setup_client(
            setup_dispatcher_func=setup_dispatcher,
        )
        yield
        await self.client.close()
        self.reset_factories()

    async def test_test_command(self):
        """Test /test command handler."""
        user = self.client.create_user()
        await user.send_command("test")
        assert user.has_received_message_containing("Раскрыть")

    async def test_start_command(self):
        """Test /start command handler."""
        user = self.client.create_user()
        await user.send_command("Start")
        assert user.has_received_message_containing("Use /Test")
        await user.send_command("start")
        assert user.has_received_message_containing("Use /Test")

    async def test_regular_message(self):
        """Test regular message handler."""
        user = self.client.create_user()
        await user.send_message("Hello bot")
        assert user.has_received_message_containing("Популярность")
    #
    # async def test_send_photo_with_caption(self, client):
    #     """Test sending a photo message with a caption."""
    #     router = Router()
    #
    #     @router.message(lambda m: m.photo is not None and m.caption is not None)
    #     async def photo_handler(message: Message) -> None:
    #         await message.answer(f"Received photo with caption: {message.caption}")
    #
    #     client.dispatcher.include_router(router)
    #
    #     user = client.create_user()
    #     # Send a photo with a caption (photo can be a file id or path depending on implementation)
    #     responses = await user.send_photo(photo="photo_file_id", caption="Nice pic")
    #
    #     assert len(responses) == 1
    #     assert "Nice pic" in responses[0].text

    # async def test_help_command(self):
    #     """Test /help command handler."""
    #     user = self.client.create_user()
    #     await user.send_command("help")
    #     assert user.has_received_message_containing("Available commands")

    # async def test_echo_command_with_args(self):
    #     """Test /echo command with arguments."""
    #     user = self.client.create_user()
    #     await user.send_command("echo", args="Hello World")
    #     assert user.has_received_message_containing("Echo: Hello World")

    # async def test_echo_command_without_args(self):
    #     """Test /echo command without arguments."""
    #     user = self.client.create_user()
    #     await user.send_command("echo")
    #     assert user.has_received_message_containing("Please provide text")

    # async def test_multiple_users_interaction(self):
    #     """Test interaction with multiple users."""
    #     user1 = self.client.create_user(user_id=1, first_name="Alice")
    #     user2 = self.client.create_user(user_id=2, first_name="Bob")
    #
    #     # User1 interaction
    #     await user1.send_command("start")
    #     assert user1.has_received_message_containing("Welcome")
    #
    #     # User2 interaction
    #     await user2.send_command("help")
    #     assert user2.has_received_message_containing("Available commands")
    #
    #     # Check that messages are isolated
    #     assert not user1.has_received_message_containing("Available commands")
    #     assert not user2.has_received_message_containing("Welcome")

    # async def test_message_sequence(self):
    #     """Test sequence of messages from one user."""
    #     user = self.client.create_user()
    #
    #     # Send start command
    #     await user.send_command("start")
    #     assert user.has_received_message_containing("Welcome")
    #
    #     # Send regular message
    #     await user.send_message("Test message")
    #     assert user.has_received_message_containing("You said: Test message")
    #
    #     # Send echo command
    #     await user.send_command("echo", args="test echo")
    #     assert user.has_received_message_containing("Echo: test echo")