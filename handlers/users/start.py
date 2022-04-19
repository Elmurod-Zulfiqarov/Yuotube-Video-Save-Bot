import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    await message.answer(f"<b> Hello👋, {message.from_user.full_name}!</b>\n"
                        f" <i>🤖 Send me a youtube video link!</i>\n"
                        f" <u>❗️🔴 max video size = 50mb ‼️</u>\n")
    # Adminga xabar beramiz
    count = db.count_users()[0]
    if message.from_user.username:
        user_n = message.from_user.username
    else:
        user_n = "username-not available"
    msg = f"{message.from_user.full_name} and {user_n} max video size a dded to the database.\nThere are {count} users in the database."
    await bot.send_message(chat_id=ADMINS[0], text=msg)
    