from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, LinkPreviewOptions

from utils.usefull_utils import generate_test_content_message

options_4 = (
    LinkPreviewOptions
        (
        prefer_large_media=True,
        show_above_text=True,
        # url="https://telegra.ph/file/94a1f3a5a8ec1e9e57597.jpg",
    )
)

router = Router()

@router.message(Command("start", ignore_case=True))
async def generate_start_message(message: Message):
    await message.answer("Use /Test",)

@router.message(Command("test", ignore_case=True))
async def generate_test_message(message: Message,
                                # from_user_id_value: int = None
                                ):

    global options_4

    content = await generate_test_content_message()

    await message.answer(
        **content.as_kwargs(),
        link_preview_options=options_4,
    )