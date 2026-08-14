from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def keyborad_builder(questionnaire_evaluation: object, message_id_value: object) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()

    call_back_value = "✅like:" + str(message_id_value)
    print('call_back_value - ', call_back_value)

    builder.add(types.InlineKeyboardButton
        (
        text="❣",
        callback_data=call_back_value
    )
    )

    call_back_value = "✅super_like:" + str(message_id_value)
    print('call_back_value - ', call_back_value)
    builder.add(types.InlineKeyboardButton
        (
        text="❤",
        callback_data=call_back_value
    )
    )

    # call_back_value = "✅Желание:" + str(message_id_value)
    # print('call_back_value - ', call_back_value)
    # builder.add(types.InlineKeyboardButton
    #     (
    #     text="🔥",
    #     callback_data=call_back_value
    #     )
    #             )
    builder.adjust(3)

    return builder
