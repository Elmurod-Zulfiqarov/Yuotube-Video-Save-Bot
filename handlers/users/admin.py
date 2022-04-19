import asyncio

from aiogram import types
from aiogram.utils import exceptions
from data.config import ADMINS
from loader import dp, db, bot

@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
	users = db.select_all_users()
	print(users[0][0])
	try:
		await message.answer(users)
	except exceptions.CantParseEntities:
		print("Can't parse entities: unsupported start tag '3',' at byte offset 772")
		pass

@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
	users = db.select_all_users()
	for user in users:
		user_id = user[0]
		text = "<b>❗️ Subscribe to @your_music_youtube channel</b>\n"
		text += f"<u>✅ All the music you are looking for is here! 🙂🙃😉</u>\n"
		text += f"<b>✅ Use the <a href='https://t.me/video_to_audio_converterbot'>YouTube Audio Save Bot!</a>🎵 @video_to_audio_converterbot</b>\n"
		text += f"<b>✅ Use the <a href='https://t.me/Youtube_music_savebot'>YouTube Music Save Bot!</a>🎵 @Youtube_video_savebot</b>\n"
		text += f"<b>✅ Use the <a href='https://t.me/Youtube_video_savebot'>YouTube Video Save Bot!</a>📹 @Youtube_video_savebot</b>\n"

		try:
			await bot.send_message(chat_id=user_id, text=text)
			await asyncio.sleep(0.05)
		except exceptions.ChatNotFound:
			print("ChatNotFound exception")

@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
	db.delete_users()
	await message.answer("Clean Database!")

	