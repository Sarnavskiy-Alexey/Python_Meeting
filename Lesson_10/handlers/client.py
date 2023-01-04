from aiogram import types, Dispatcher
from Lesson_10.creation.create_bot import bot
from Lesson_10.keyboards.client_kb import kb_client, kb_client_news, kb_client_schedule
from Lesson_10.parse_mail_ru_news import all_news
from Lesson_10.scheduler.scheduler_show_data import show_data
from Lesson_10.scheduler.scheduler_get_data import get_new_data


async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, """Добрый день! 👋
Выберите следующее место, куда хотите попасть""", reply_markup=kb_client)


async def command_scheduler(message: types.Message):
    await bot.send_message(message.from_user.id, """Выберите следующее действие!
Если хотите увидеть все занятия в расписании, то нажмите /show.
Для показа отфильтрованных данных напишите в первой строке команду "/show", в следующей строке название поля для поиска (одно из следующих слов): "дата", "курс", "урок", "тема", "заметка"; затем в следующей строке данные для поиска. Дата для поиска вводится в формате "dd-mm-yyyy" для поиска в течение одного дня или "dd-mm-yyyy : dd-mm-yyyy" для поиска в диапазоне дней.

Если хотите добавить новые данные о занятии, то напишите в первой строке команду "/add", далее в отдельных строках дайте следующую информацию:
1️⃣ дата и время в формате "dd-mm-yyyy hh:mm";
2️⃣ название курса;
3️⃣ номер урока;
4️⃣ тема урока;
5️⃣ заметка об уроке (если добавлять нечего, то поставьте -).""", reply_markup=kb_client_schedule)


async def command_scheduler_add(message: types.Message):
    mes = message.text.split('\n')
    if len(mes) == 6:
        get_new_data(mes[1:])
        await bot.send_message(message.from_user.id, 'Данные успешно добавлены!')
    else:
        await bot.send_message(message.from_user.id, 'Неправильное количество данных! Попробуйте еще разок!')


async def command_scheduler_show(message: types.Message):
    mes = message.text.split('\n')
    if len(mes) == 1:
        await bot.send_message(message.from_user.id, show_data([]))
    elif len(mes) == 3:
        await bot.send_message(message.from_user.id, show_data(mes[1:]))
    else:
        await bot.send_message(message.from_user.id, 'Неправильное количество данных! Попробуйте еще разок!')


# async def command_scheduler_change(message: types.Message):
#     pass


async def command_news(message: types.Message):
    await bot.send_message(message.from_user.id, all_news.all_news(), reply_markup=kb_client_news)


async def command_news_numbers(message: types.Message):
    await bot.send_message(message.from_user.id, all_news.one_tidings(int(message.text[1])))


async def command_back_to_main(message: types.Message):
    await bot.send_message(message.from_user.id, 'Возвращаемся в главное меню!', reply_markup=kb_client)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_scheduler, commands=['расписание', 'schedule'])
    dp.register_message_handler(command_news, commands=['новости', 'news'])
    dp.register_message_handler(command_news_numbers, commands=['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    dp.register_message_handler(command_back_to_main, commands='back')
    dp.register_message_handler(command_scheduler_add, commands='add')
    dp.register_message_handler(command_scheduler_show, commands='show')
    # dp.register_message_handler(command_scheduler_change, commands='change')
