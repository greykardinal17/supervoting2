import asyncio
import logging
from typing import Dict, List, Optional, Tuple, Any

# from  import config
import config

from handlers.control_commands import router, options_4

from refine_form_text import refine_form_text

from like_counter import like_counter

# новый импорт
from aiogram import F

from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentType

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from aiogram.utils.formatting import (Pre)
from aiogram.utils.formatting import Text, as_line, Bold

from my_types import AnalysisResult
from utils.usefull_utils import generate_test_content_message, analysis_message_and_rating_calculation
from handlers import control_commands

summaru: List[str] = ["Анкета"]

like_maximum: int = 93
super_like_maximum: int = 33

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота
bot: Bot = Bot(
    token=config.token,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML,
    )
)


def setup_dispatcher(bot: Bot, dispatcher: Dispatcher) -> None:
    """Configure dispatcher with handlers and middlewares."""
    dispatcher.include_router(router)


async def add_bottom_bar_encourages_clicking_buttons(
    mesage_id_value: str,
    like_value: int,
    super_like_value: int,
    message_text_value: str = 'test_text',
    info_line_value: str = '',
    from_user_first_name_value: str = '',
    user_reputation: int = 50
) -> str:

    integral_grade: float = round(like_value * 0.0003 * 10 +
                                  super_like_value * 0.7 * 10
                                    , 4)

    print('integral_grade is', integral_grade)

    if (integral_grade > 259
            or integral_grade > 50
            or integral_grade > 100
            or integral_grade > 150
            or integral_grade > 15):
        if (integral_grade > 50
            or integral_grade > 100
            or integral_grade > 150):

            info_line_value = ('Поздравляем пользователя '+ from_user_first_name_value +
                               'с репутацией = ' + str(user_reputation) +
                           ' Его голос увеличил популярность анкеты и ввел его в список претендентов на общения! '
                               + info_line_value
                           )
        else:
            info_line_value = ('Поздравляем пользователя ' + from_user_first_name_value +
                               ' с репутацией = ' + str(user_reputation) +
                               ' Благодаря нему увеличена популярность анкеты! ' + info_line_value
                               )

    content: Text = Text(
        as_line('_________________'),
        as_line(Pre(Bold(info_line_value))),
        as_line('Популярность',
                # f"({integral_grade:.19}"
                f"({integral_grade}"
                f")"
                ),
        as_line(' Отдай симпатию ❣', like_value),
        as_line(' ⁸¹²⁰⁹⁷⁹'),
        as_line(' Отдай супер симпатию ❤', super_like_value),
        as_line(' ¹²⁹⁰⁹⁸⁷'),
    )
    return_value: str = message_text_value + content.as_html()

    return return_value


async def process_message(
    message: types.Message,
    dictionary_storing_message_ratings: Dict[str, Dict[str, int]],
    from_user_id_value: Optional[int] = None,
    origin_message_id_value: Optional[str] = None,
    from_user_first_name_value: str = '',
    local_dictionary_storing_user_ratings: Optional[Dict] = None,
    content_source: str = 'text'
) -> Tuple[Dict[str, Dict[str, int]], Optional[Dict]]:
    """
    Unified handler for processing both text and photo messages.
    Returns updated dictionaries.
    
    Args:
        message: The incoming message
        dictionary_storing_message_ratings: Message ratings dictionary
        from_user_id_value: User ID
        origin_message_id_value: Original message ID
        from_user_first_name_value: User's first name
        local_dictionary_storing_user_ratings: User ratings dictionary
        content_source: Either 'text' or 'photo'
    """
    global summaru

    print(f'Processing {content_source} message')

    (result,
     builder,
     origin_message_id,
     local_dictionary_storing_user_ratings,
     dictionary_storing_message_ratings) = await analysis_message_and_rating_calculation(
        from_user_id_value,
        message,
        origin_message_id_value,
        local_dictionary_storing_user_ratings,
        dictionary_storing_message_ratings
    )

    like_value: int = dictionary_storing_message_ratings[origin_message_id]["like"]
    super_like_value: int = dictionary_storing_message_ratings[origin_message_id]["super_like"]

    # Get content based on source
    if content_source == 'photo':
        caption: str = getattr(message, 'caption', None) or ""
        image_url: str = 'https://ravagaren.wordpress.com/wp-content/uploads/2023/03/photo_2023-08-19_11-36-11.jpg?w=640'
        content = await generate_test_content_message(image_url, caption)
    else:  # text
        text: str = getattr(message, 'text', None) or ""
        summaru.append(text)
        summaru_refined = refine_form_text(summaru)
        image_anket_url: str = summaru_refined[0]
        print('image_anket_url', image_anket_url)
        content = await generate_test_content_message(image_anket_url, text)

    print('content - ', content.as_html())

    if '_________________' not in content.as_html():
        # New message - add bottom bar and send
        content_text: str = await add_bottom_bar_encourages_clicking_buttons(
            origin_message_id,
            like_value,
            super_like_value,
            content.as_html()
        )

        print('content_text is', content_text)

        await bot.send_message(
            chat_id=message.chat.id,
            text=content_text,
            link_preview_options=options_4,
            reply_markup=builder.as_markup(),
        )
    else:
        # Message already has separator - update existing message
        html_text: str = getattr(message, 'html_text', None) or ""

        if (html_text.find('Рейтинг анкеты(0.0)') == -1
                and like_value == 0
                and super_like_value == 0):
            print('Нашли готовую интегральную оценку')
            like_value, super_like_value = await like_counter(origin_message_id, html_text)

        # Extract text before separator
        idx: int = html_text.find('_________________')
        common_text: str = html_text[0:idx] if idx != -1 else html_text
        print('common_text - ', common_text)

        common_text = await add_bottom_bar_encourages_clicking_buttons(
            origin_message_id,
            like_value,
            super_like_value,
            common_text,
            from_user_first_name_value=from_user_first_name_value,
            user_reputation=43
        )

        print('common_text -', common_text)

        await bot.edit_message_text(
            text=common_text,
            chat_id=message.chat.id,
            message_id=message.message_id,
            link_preview_options=options_4,
            reply_markup=builder.as_markup(),
        )

    print('Изменяем лайк и суперлайк')
    print('like_value - ', like_value)
    print('super_like_value - ', super_like_value)

    dictionary_storing_message_ratings[origin_message_id]["like"] = like_value
    dictionary_storing_message_ratings[origin_message_id]["super_like"] = super_like_value

    return dictionary_storing_message_ratings, local_dictionary_storing_user_ratings


@router.message(F.content_type == ContentType.PHOTO)
async def add_bottom_and_buttons_from_photo(
    message: types.Message,
    from_user_id_value: Optional[int] = None,
    origin_message_id_value: Optional[str] = None,
    from_user_first_name_value: str = '',
    local_dictionary_storing_user_ratings: Optional[Dict] = None
) -> None:
    """Handle incoming photo messages."""
    # Get global state
    global dictionary_storing_message_ratings
    
    dictionary_storing_message_ratings, local_dictionary_storing_user_ratings = await process_message(
        message,
        dictionary_storing_message_ratings,
        from_user_id_value,
        origin_message_id_value,
        from_user_first_name_value,
        local_dictionary_storing_user_ratings,
        content_source='photo'
    )


@router.message(F.text)
async def add_bottom_and_buttons_from_text(
    message: types.Message,
    from_user_id_value: Optional[int] = None,
    origin_message_id_value: Optional[str] = None,
    from_user_first_name_value: str = '',
    local_dictionary_storing_user_ratings: Optional[Dict] = None
) -> None:
    """Handle incoming text messages."""
    # Get global state
    global dictionary_storing_message_ratings
    
    dictionary_storing_message_ratings, local_dictionary_storing_user_ratings = await process_message(
        message,
        dictionary_storing_message_ratings,
        from_user_id_value,
        origin_message_id_value,
        from_user_first_name_value,
        local_dictionary_storing_user_ratings,
        content_source='text'
    )


@router.callback_query(F.data.startswith("✅"))
async def callbacks_calculation_of_likes(callback: types.CallbackQuery) -> None:
    global dictionary_storing_user_ratings
    global dictionary_storing_message_ratings

    print('callback.from_user.first_name - ', callback.from_user.first_name)
    print('callback.data - ', callback.data)
    action: str = callback.data.split(":")[0]
    print('action - ', action)

    questionnaire_message_id: str = str(callback.data.split(":")[1])
    print('questionnaire_message_id - ', questionnaire_message_id)

    dictionary_storing_user_ratings.setdefault(callback.from_user.id, None)
    dictionary_storing_message_ratings.setdefault(questionnaire_message_id, None)

    if dictionary_storing_user_ratings[callback.from_user.id] is None:
        dictionary_storing_user_ratings[callback.from_user.id] = \
            {questionnaire_message_id:
                {
                    'like': 0,
                    'super_like': 0,
                    'Wish': 0
                }
            }

    dictionary_storing_user_ratings[callback.from_user.id].setdefault(questionnaire_message_id, None)

    print('user_ratings_dict before check -', dictionary_storing_user_ratings)

    if dictionary_storing_user_ratings[callback.from_user.id][questionnaire_message_id] is None:
        dictionary_storing_user_ratings[callback.from_user.id][questionnaire_message_id] = \
            {
                    'like': 0,
                    'super_like': 0,
                    'Wish': 0
            }

    if dictionary_storing_message_ratings[questionnaire_message_id] is None:
        dictionary_storing_message_ratings[questionnaire_message_id] = \
            {
                'like': 0,
                'super_like': 0,
            }

    print('dict_of_questionnaire_evaluation is', dictionary_storing_message_ratings)
    print('user_ratings_dict -', dictionary_storing_user_ratings)

    like_value: int = dictionary_storing_message_ratings[str(questionnaire_message_id)]['like']
    super_like_value: int = dictionary_storing_message_ratings[str(questionnaire_message_id)]['super_like']

    # Normalize callback message html_text to avoid AttributeError when it's None
    cb_html: str = getattr(callback.message, 'html_text', None) or ""

    if (cb_html.find('Рейтинг анкеты(0.0)') == -1
            and like_value == 0
            and super_like_value == 0):
        print('Нашли готовую интегральную оценку')
        like_value, super_like_value = await like_counter(questionnaire_message_id, cb_html)

        dictionary_storing_message_ratings[str(questionnaire_message_id)]['like'] = like_value
        dictionary_storing_message_ratings[str(questionnaire_message_id)]['super_like'] = super_like_value

    if action == "✅like":

        print('dict_of_questionnaire_evaluation is', dictionary_storing_message_ratings)
        dictionary_storing_message_ratings[str(questionnaire_message_id)]['like'] += 1
        dictionary_storing_user_ratings[callback.from_user.id][questionnaire_message_id]['like'] += 1
        print('in callback user_data -', dictionary_storing_user_ratings)

        await callback.answer()
        dictionary_storing_message_ratings, dictionary_storing_user_ratings = await process_message(
            callback.message,
            dictionary_storing_message_ratings,
            callback.from_user.id,
            questionnaire_message_id,
            callback.from_user.first_name,
            dictionary_storing_user_ratings,
            content_source='text'
        )

    elif action == "✅super_like":
        print('dict_of_questionnaire_evaluation is', dictionary_storing_message_ratings)
        print('user_ratings_dict[callback.from_user.id][questionnaire_message_id]["super_like"] is',
              dictionary_storing_user_ratings[callback.from_user.id][questionnaire_message_id]['super_like']
              )
        if dictionary_storing_user_ratings[callback.from_user.id][questionnaire_message_id]['super_like'] > 0:
            await callback.answer(text="Супер симпатия пока недоступна",
                                  show_alert=True
                                  )
        else:
            dictionary_storing_message_ratings[str(questionnaire_message_id)]['super_like'] += 1
            print('dict_of_questionnaire_evaluation is', dictionary_storing_message_ratings)
            dictionary_storing_user_ratings[callback.from_user.id][questionnaire_message_id]['super_like'] += 1
            print('in callback user_data -', dictionary_storing_user_ratings)

            await callback.answer()
            dictionary_storing_message_ratings, dictionary_storing_user_ratings = await process_message(
                callback.message,
                dictionary_storing_message_ratings,
                callback.from_user.id,
                questionnaire_message_id,
                callback.from_user.first_name,
                dictionary_storing_user_ratings,
                content_source='text'
            )


async def main() -> None:
    """Start the bot and polling for updates."""
    dispatcher: Dispatcher = Dispatcher()
    setup_dispatcher(bot, dispatcher)

    try:
        await dispatcher.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
