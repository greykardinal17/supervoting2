# from aiogram.utils.formatting import Text, as_line, TextLink, Url, HashTag, ExpandableBlockQuote, Bold
#
#
# async def generate_test_content_message(image_url_value=None, text_form_value=None):
# # def generate_test_content_message(image_url_value=None, text_form_value=None):
#     image_url : str
#
#     if image_url_value is None:
#         image_url = 'https://telegra.ph/file/94a1f3a5a8ec1e9e57597.jpg'
#     else:
#         image_url = image_url_value
#
#     if text_form_value is None:
#         content_form = (Text
#             (
#              as_line(TextLink('.', url=image_url)),
#                     as_line(Url("https://ift.tt/G2vJD1H")),
#                     as_line(HashTag("ж_верх "), HashTag("знакомства "),),
#                     as_line("1. Саша"),
#                     as_line("2. Леди"),
#                     as_line("3. #Москва"),
#                     ExpandableBlockQuote
#                     (
#                     as_line(Bold('Раскрыть ⬇⬇⬇')),
#                     as_line("4. свитч с уклоном вниз"),
#                     as_line("5.Ищу партнёра для сессионных отношений (цис-женщину, транс-мужчину Возраст: до 45 лет."),
#                     as_line("Фетиши: атлетизм и мускулистость, tomboy-style, андрогинность. "
#                                "Не обязательно быть профи-спортсменом, но хотя бы минимальная физическая "
#                          "развитость должна быть. Особая любовь к женщинам, которые занимаются единоборствами (любыми)"),
#                     as_line("6А) БДСМ-super_like:"),
#                     as_line("Общее настроение экшенов: пытки, избиение гопниками, армейская "
#                         "дедовщина, любое стихийное желание причинить боль"),
#                     as_line("Б) Сексуальные super_like: возможно всё, но не сразу, а по мере установления доверия "),
#                     as_line("Подробнее - https://ift.tt/d1z4Sqs"),
#                     as_line("id::!12345678"),
#                     as_line("РАНГ: Серебрянный"),
#                     as_line("~`!@#$%^&*()_`123456788900-"),
#                     ),
#             ))
#     else:
#
#         hash_tag_index : int =  text_form_value.find('#не_см_flog_ru')
#
#         print('image_url - ', image_url)
#         content_form = (Text
#             (
#             as_line(TextLink('.', url=image_url)),
#             as_line(text_form_value[0:hash_tag_index + 150]),
#             as_line(Bold('Раскрыть ⬇⬇⬇')),
#             ExpandableBlockQuote(text_form_value[hash_tag_index + 150:len(text_form_value) - 1]),
#             as_line('')
#
#             # ExpandableBlockQuote
#             #     (
#             #     as_line(Bold('Раскрыть ⬇⬇⬇')),
#             #     as_line("4. свитч с уклоном вниз"),
#             #     as_line("5.Ищу партнёра для сессионных отношений (цис-женщину, транс-мужчину Возраст: до 45 лет."),
#             #     as_line("Фетиши: атлетизм и мускулистость, tomboy-style, андрогинность. "
#             #             "Не обязательно быть профи-спортсменом, но хотя бы минимальная физическая "
#             #             "развитость должна быть. Особая любовь к женщинам, которые занимаются единоборствами (любыми)"),
#             #     as_line("6А) БДСМ-super_like:"),
#             #     as_line("Общее настроение экшенов: пытки, избиение гопниками, армейская "
#             #             "дедовщина, любое стихийное желание причинить боль"),
#             #     as_line("Б) Сексуальные super_like: возможно всё, но не сразу, а по мере установления доверия "),
#             #     as_line("Подробнее - https://ift.tt/d1z4Sqs"),
#             #     as_line("id::!12345678"),
#             #     as_line("РАНГ: Серебрянный"),
#             #     as_line("~`!@#$%^&*()_`123456788900-"),
#             # ),
#         ))
#
#
#     return content_form
from aiogram.utils.formatting import Text, as_line, TextLink, Url, HashTag, ExpandableBlockQuote, Bold


# ,questionnaire_eval,dict_of_questionnaire_evaluation


async def generate_test_content_message(image_url_value=None, text_form_value=None):
# def generate_test_content_message(image_url_value=None, text_form_value=None):
    image_url : str

    if image_url_value is None:
        image_url = 'https://telegra.ph/file/94a1f3a5a8ec1e9e57597.jpg'
    else:
        image_url = image_url_value

    if text_form_value is None:
        content_form = (Text
            (
             as_line(TextLink('.', url=image_url)),
                    as_line(Url("https://ift.tt/G2vJD1H")),
                    as_line(HashTag("ж_верх "), HashTag("знакомства "),),
                    as_line("1. Саша"),
                    as_line("2. Леди"),
                    as_line("3. #Москва"),
                    ExpandableBlockQuote
                    (
                    as_line(Bold('Раскрыть ⬇⬇⬇')),
                    as_line("4. свитч с уклоном вниз"),
                    as_line("5.Ищу партнёра для сессионных отношений (цис-женщину, транс-мужчину Возраст: до 45 лет."),
                    as_line("Фетиши: атлетизм и мускулистость, tomboy-style, андрогинность. "
                               "Не обязательно быть профи-спортсменом, но хотя бы минимальная физическая "
                         "развитость должна быть. Особая любовь к женщинам, которые занимаются единоборствами (любыми)"),
                    as_line("6А) БДСМ-super_like:"),
                    as_line("Общее настроение экшенов: пытки, избиение гопниками, армейская "
                        "дедовщина, любое стихийное желание причинить боль"),
                    as_line("Б) Сексуальные super_like: возможно всё, но не сразу, а по мере установления доверия "),
                    as_line("Подробнее - https://ift.tt/d1z4Sqs"),
                    as_line("id::!12345678"),
                    as_line("РАНГ: Серебрянный"),
                    as_line("~`!@#$%^&*()_`123456788900-"),
                    ),
            ))
    else:

        hash_tag_index : int =  text_form_value.find('#не_см_flog_ru')

        print('image_url - ', image_url)
        content_form = (Text
            (
            as_line(TextLink('.', url=image_url)),
            as_line(text_form_value[0:hash_tag_index + 150]),
            as_line(Bold('Раскрыть ⬇⬇⬇')),
            ExpandableBlockQuote(text_form_value[hash_tag_index + 150:len(text_form_value) - 1]),
            as_line('')

            # ExpandableBlockQuote
            #     (
            #     as_line(Bold('Раскрыть ⬇⬇⬇')),
            #     as_line("4. свитч с уклоном вниз"),
            #     as_line("5.Ищу партнёра для сессионных отношений (цис-женщину, транс-мужчину Возраст: до 45 лет."),
            #     as_line("Фетиши: атлетизм и мускулистость, tomboy-style, андрогинность. "
            #             "Не обязательно быть профи-спортсменом, но хотя бы минимальная физическая "
            #             "развитость должна быть. Особая любовь к женщинам, которые занимаются единоборствами (любыми)"),
            #     as_line("6А) БДСМ-super_like:"),
            #     as_line("Общее настроение экшенов: пытки, избиение гопниками, армейская "
            #             "дедовщина, любое стихийное желание причинить боль"),
            #     as_line("Б) Сексуальные super_like: возможно всё, но не сразу, а по мере установления доверия "),
            #     as_line("Подробнее - https://ift.tt/d1z4Sqs"),
            #     as_line("id::!12345678"),
            #     as_line("РАНГ: Серебрянный"),
            #     as_line("~`!@#$%^&*()_`123456788900-"),
            # ),
        ))


    return content_form


