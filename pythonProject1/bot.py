import asyncio
import logging

from pythonProject1 import config
from pythonProject1.handlers.control_commands import router, options_4

from pythonProject1.refine_form_text import refine_form_text

from pythonProject1.like_counter import like_counter

# новый импорт
from aiogram import F

from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentType

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from aiogram.utils.formatting import (Pre)
from aiogram.utils.formatting import Text, as_line, Bold
from pythonProject1.utils.usefull_utils import generate_test_content_message, technical_processing_form
from pythonProject1.handlers import control_commands

summaru : list = ["Анкета"]

# questionnaire_eval: dict = {'like': 0,
#                             'super_like': 0,
#                             # 'Wish': 0
#                             }

dictionary_storing_message_ratings: dict = {}

# Здесь хранятся пользовательские данные.
# Т.к. это словарь в памяти, то при перезапуске он очистится
user_ratings_dict = {}

like_maximum: int = 93
super_like_maximum: int = 33

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(
    token=config.token,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML,
    )
)
# Диспетчер

def setup_dispatcher(bot: Bot, dispatcher: Dispatcher) -> None:
    """Configure dispatcher with handlers and middlewares."""
    dispatcher.include_router(router)


async def add_bottom(mesage_id_value,
                     like_value,
                     super_like_value,
                     message_text_value='test_text',
                     info_line_value='',from_user_first_name_value='',
                     user_reputation=50
                     ):

    # global questionnaire_eval
    global dictionary_storing_message_ratings
    global like_maximum

    integral_grade: float = round(like_value * 0.0003 * 10 +
                                  super_like_value * 0.7 * 10
                                    ,4)

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
                           ' Его голос увеличил популярность анкеты и ввел его в список претендентов на общение! '
                               + info_line_value
                           )
        else:
            info_line_value = ('Поздравляем пользователя ' + from_user_first_name_value +
                               ' с репутацией = ' + str(user_reputation) +
                               ' Благодаря нему увеличена популярность анкеты! ' + info_line_value
                               )

    content = Text(
        as_line('_________________'),
        as_line(Pre(Bold(info_line_value))),
        as_line('Популярность',
                # f"({integral_grade:.19}"
                f"({integral_grade}"
                f")"
                ),
        # as_line
        # (
        #     as_list
        #         (
        #         as_marked_section
        #             (
        #             # Bold(" Оцени анкету"),
        #             #print(f"{r2} ({r2:.2%})")
        #
        #             # as_key_value("Красота 💟",
        #             #         f"({dict_of_questionnaire_evaluation[mesage_id_value]["like"]/
        #             #                     like_maximum:.2%}"
        #             #               f")"
        #             #              ),
        #             as_key_value(" Интегральная оценка 💟",
        #                          f"({dict_of_questionnaire_evaluation[mesage_id_value]["like"] /
        #                              like_maximum:.2%}"
        #                          f")"
        #                          ),
        #             # as_key_value("Нужность практик 👩",
        #             #       f"({dict_of_questionnaire_evaluation[mesage_id_value]["super_like"] /
        #             #           super_like_maximum:.2%}"
        #             #       f")"
        #             #       ),
        #             # as_key_value("Хочу быть рядом 🔥",
        #             #              str(dict_of_questionnaire_evaluation[mesage_id_value]["Wish"])
        #             #              ),
        #             marker=" ",
        #         ),
        #     ),
        # ),
        as_line(' Отдай симпатию ❣',like_value),
        as_line(' ⁸¹²⁰⁹⁷⁹'),
        as_line(' Отдай супер симпатию ❤',super_like_value),
        as_line(' ¹²⁹⁰⁹⁸⁷'),
        # TextLink,TextMention,Code,Pre
        # as_line (Code(info_line_value)),

    )
    return_value: str = message_text_value + content.as_html()

    return return_value


# def get_keyboard():
#     buttons = [
#         [
#             types.InlineKeyboardButton(text="-1", callback_data="num_decr"),
#             types.InlineKeyboardButton(text="+1", callback_data="num_incr")
#         ],
#         [types.InlineKeyboardButton(text="Подтвердить", callback_data="num_finish")]
#     ]
#     keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
#     return keyboard


# async def update_grade_text(message: types.Message, new_value: int):
#     await message.edit_text(
#         f"Укажите число: {new_value}",
#         reply_markup=get_keyboard()
#     )

# from pythonProject1.handlers.photo_handler import PhotoHandler

# photo_handler = PhotoHandler(options_4=options_4)

@router.message(F.content_type == ContentType.PHOTO)
# async def photo_handler_message(message: types.Message):
#     """Handle incoming photo messages using PhotoHandler."""
    # await photo_handler.from_photo_add_bottom_and_buttons(message)
async def add_bottom_and_buttons_def_from_photo(message: types.Message,
                                                from_user_id_value: int = None,
                                                origin_message_id_value: str = None
                                                ):

    builder, origin_message_id = await technical_processing_form(from_user_id_value, message, origin_message_id_value)

    print('We are handling photo')
    print('Position _ ', message.caption.find('_________________'))

    image_url = 'https://ravagaren.wordpress.com/wp-content/uploads/2023/03/photo_2023-08-19_11-36-11.jpg?w=640'

    content = await generate_test_content_message(image_url, message.caption)

    print('content - ', content.as_html() )


    if content.as_html().find('_________________') == -1:
        content_text = await add_bottom(origin_message_id, content.as_html(), )

        print('content_text is', content_text)

        await message.answer(
            content_text,
            link_preview_options=options_4,
            reply_markup=builder.as_markup(),
        )


@router.message(F.text)
async def add_bottom_and_buttons_from_text(message: types.Message,
                                           from_user_id_value: int = None,
                                           origin_message_id_value: str = None,
                                           from_user_first_name_value='',
                                           local_user_ratings_dic=None):


    global summaru
    global dictionary_storing_message_ratings

    print('from_user_first_name_value -', from_user_first_name_value)

    (builder,
     origin_message_id,
     local_user_ratings_dic,
     dictionary_storing_message_ratings) = await technical_processing_form(from_user_id_value, message,
                                                                           origin_message_id_value,
                                                                           local_user_ratings_dic,
                                                                           dictionary_storing_message_ratings)

    like_value: int = dictionary_storing_message_ratings[origin_message_id]["like"]
    super_like_value: int = dictionary_storing_message_ratings[origin_message_id]["super_like"]

    print('Position _ ', message.text.find('_________________'))

    summaru.append(message.text)
    summaru = refine_form_text(summaru)

    image_anket_url: str = summaru[0]

    print ('image_anket_url', image_anket_url)

    content = await generate_test_content_message(image_anket_url, message.text)

    print('content - ', content.as_html())

    if content.as_html().find('_________________') == -1:

        content_text = await add_bottom(origin_message_id, like_value, super_like_value, content.as_html())

        print('content_text is', content_text)

        await message.answer(
            content_text,
            link_preview_options=options_4,
            reply_markup=builder.as_markup(),
        )
    else:

        if (message.html_text.find('Рейтинг анкеты(0.0)') == -1
                                                 and like_value == 0
                                           and super_like_value == 0) :

            print('Нашли готовую интегральную оценку')
            like_value, super_like_value = await like_counter(origin_message_id,message.html_text)
            # print()

        common_text: str = message.html_text[0:message.html_text.find('_________________')]
        print('common_text - ', common_text)

        common_text = await add_bottom(origin_message_id,
                                       like_value,
                                       super_like_value,
                                       common_text,
                                       from_user_first_name_value = from_user_first_name_value,
                                       user_reputation= 43
                                       )

        print('common_text -', common_text)


        await message.edit_text(
            common_text,
            link_preview_options=options_4,
            reply_markup=builder.as_markup(),
        )

    print('Изменяем лайк и суперлайк')
    print('like_value - ',like_value)
    print('super_like_value - ', super_like_value)

    dictionary_storing_message_ratings[origin_message_id]["like"] = like_value
    dictionary_storing_message_ratings[origin_message_id]["super_like"] = super_like_value

    # await message.delete()


# async def like_counter(origin_message_id, message_html_value):
#
#     # global dict_of_questionnaire_evaluation
#
#     message_html : str = message_html_value
#
#     like_value = 5
#     super_like_value = 3
#
#     # dict_of_questionnaire_evaluation[origin_message_id]["like"] = like_value
#     # dict_of_questionnaire_evaluation[origin_message_id]["super_like"] = super_like_value
#
#     return like_value, super_like_value

@router.callback_query(F.data.startswith("✅"))
async def callbacks_calculation_of_likes(callback: types.CallbackQuery):
    global user_ratings_dict
    global array_of_questionnaire_evaluation

    print('callback.from_user.first_name - ', callback.from_user.first_name)
    print('callback.data - ', callback.data)
    action = callback.data.split(":")[0]
    print('action - ', action)

    questionnaire_message_id: str = str(callback.data.split(":")[1])
    print('questionnaire_message_id - ', questionnaire_message_id)

    user_ratings_dict.setdefault(callback.from_user.id, None)
    dictionary_storing_message_ratings.setdefault(questionnaire_message_id, None)

    if user_ratings_dict[callback.from_user.id] is None:
        user_ratings_dict[callback.from_user.id] = \
            {questionnaire_message_id:
                {
                    'like': 0,
                    'super_like': 0,
                    'Wish': 0
                }
            }

    user_ratings_dict[callback.from_user.id].setdefault(questionnaire_message_id, None)

    print('user_ratings_dict before check -', user_ratings_dict)

    if user_ratings_dict[callback.from_user.id][questionnaire_message_id] is None:
        user_ratings_dict[callback.from_user.id][questionnaire_message_id] =  \
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
                # 'Wish': 0
            }


    print('dict_of_questionnaire_evaluation is', dictionary_storing_message_ratings)
    print('user_ratings_dict -', user_ratings_dict)

    like_value: str = dictionary_storing_message_ratings[str(questionnaire_message_id)]['like']
    super_like_value: str = dictionary_storing_message_ratings[str(questionnaire_message_id)]['super_like']

    if (callback.message.html_text.find('Рейтинг анкеты(0.0)') == -1
            and like_value == 0
            and super_like_value == 0):
        print('Нашли готовую интегральную оценку')
        like_value, super_like_value = await like_counter(questionnaire_message_id, callback.message.html_text)

        dictionary_storing_message_ratings[str(questionnaire_message_id)]['like'] = like_value
        dictionary_storing_message_ratings[str(questionnaire_message_id)]['super_like'] = super_like_value


    if action == "✅like":

        print('dict_of_questionnaire_evaluation is', dictionary_storing_message_ratings)
        dictionary_storing_message_ratings[str(questionnaire_message_id)]['like'] += 1
        user_ratings_dict[callback.from_user.id][questionnaire_message_id]['like'] += 1
        print('in callback user_data -', user_ratings_dict)

        await callback.answer()
        await add_bottom_and_buttons_from_text(callback.message,
                                               callback.from_user.id,
                                               str(questionnaire_message_id),
                                               callback.from_user.first_name,
                                               user_ratings_dict)

    elif action == "✅super_like":
        print('dict_of_questionnaire_evaluation is', dictionary_storing_message_ratings)
        print('user_ratings_dict[callback.from_user.id][questionnaire_message_id]["super_like"] is',
                user_ratings_dict[callback.from_user.id][questionnaire_message_id]['super_like']
            )
        if user_ratings_dict[callback.from_user.id][questionnaire_message_id]['super_like'] > 0:
            await callback.answer(text="Супер симпатия пока недоступна",
                                  show_alert=True
                                  )
        else:
            dictionary_storing_message_ratings[str(questionnaire_message_id)]['super_like'] += 1
            print('dict_of_questionnaire_evaluation is', dictionary_storing_message_ratings)
            user_ratings_dict[callback.from_user.id][questionnaire_message_id]['super_like'] += 1
            print('in callback user_data -', user_ratings_dict)

            await callback.answer()
            await add_bottom_and_buttons_from_text(callback.message,
                                                   callback.from_user.id,
                                                   str(questionnaire_message_id),
                                                   callback.from_user.first_name,
                                                   user_ratings_dict)

    # elif action == "✅Желание":
    #     if user_ratings_dict[callback.from_user.id][questionnaire_message_id]['Wish'] > 0:
    #         await callback.answer(text="Голосовать можно один раз",
    #                               show_alert=True
    #                               )
    #     else:
    #         dict_of_questionnaire_evaluation[str(questionnaire_message_id)]['Wish'] += 1
    #         print('dict_of_questionnaire_evaluation is', dict_of_questionnaire_evaluation)
    #         user_ratings_dict[callback.from_user.id][questionnaire_message_id]['Wish'] += 1
    #         print('in callback user_data -', user_ratings_dict)
    #
    #         await callback.answer()
    #         await from_text_add_bottom_and_buttons(callback.message, callback.from_user.id,
    #                                                str(questionnaire_message_id))


# Запуск процесса поллинга новых апдейтов
async def main():
    dp = Dispatcher()

    dp.include_routers(control_commands.router)

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())