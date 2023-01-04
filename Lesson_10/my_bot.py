"""
Используется библиотека aiogram
Прикрутить:
    1) парсер
    2) ежедневник
"""


from aiogram.utils import executor
from creation.create_bot import dp
from handlers import client, other


async def on_startup(_):
    print('Bot is alive!')


client.register_handlers_client(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
