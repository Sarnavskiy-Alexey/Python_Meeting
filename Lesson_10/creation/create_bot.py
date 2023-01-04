from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from Lesson_10.creation.credits import bot_token

bot = Bot(bot_token)
dp = Dispatcher(bot)
