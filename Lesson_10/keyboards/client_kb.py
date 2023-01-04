from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# главные кнопки
b1 = KeyboardButton('/новости')
b2 = KeyboardButton('/расписание')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(b1, b2)

# кнопки открытия новостей
b10 = KeyboardButton('/back')
b11 = KeyboardButton('/1')
b12 = KeyboardButton('/2')
b13 = KeyboardButton('/3')
b14 = KeyboardButton('/4')
b15 = KeyboardButton('/5')
b16 = KeyboardButton('/6')
b17 = KeyboardButton('/7')
b18 = KeyboardButton('/8')
b19 = KeyboardButton('/9')

kb_client_news = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_news.row(b11, b12, b13).row(b14, b15, b16).row(b17, b18, b19).add(b10)

# кнопки выбора действия в расписании
b20 = KeyboardButton('/back')
b21 = KeyboardButton('/add')
# b22 = KeyboardButton('/change')
b23 = KeyboardButton('/show')
b24 = KeyboardButton('/find')

kb_client_schedule = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_schedule.row(b21,
                       # b22,
                       b23).add(b20)
