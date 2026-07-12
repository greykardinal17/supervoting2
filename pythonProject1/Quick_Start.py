import pytest
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram_test_framework import AsyncBotTestMixin
from pythonProject1 import config

def setup_dispatcher(bot: Bot, dispatcher: Dispatcher) -> None:
    """Configure dispatcher with middlewares and handlers."""
    # Your setup code here
    bot = Bot(
        token=config.token,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
        )
    )
    # Диспетчер
    dispatcher = Dispatcher()
    pass


class TestMyHandler(AsyncBotTestMixin):
    @pytest.fixture(autouse=True)
    async def setup(self):
        self.client = await self.setup_client(
            setup_dispatcher_func=setup_dispatcher,
        )
        yield
        await self.client.close()
        self.reset_factories()

    async def test_start_command(self):
        user = self.client.create_user()
        await user.send_command("start")
        assert user.has_received_message_containing("Welcome")