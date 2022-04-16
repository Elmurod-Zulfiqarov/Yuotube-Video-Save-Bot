from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
	text = ("Commands: 🆘",
			"/start - Run the bot",
			"/help - Help",
			"/about - About Bot",
			"/audio - <a href='https://t.me/video_to_audio_converterbot'>YouTube Audio Save Bot</a>",
			"Contact - <a href='https://t.me/Elmurod_010409'>Admin</a>")
	
	await message.answer("\n".join(text))


@dp.message_handler(text="/about")
async def about_video_bot(message: types.Message):
	await message.answer("👋 Welcome to YouTube Audio Save Bot🤖\n\n"
		"✅ Bot - YouTubedan videolarini yuklaydi\n"
		"🇺🇿 YouTubedan botga 🎞video 🔗 havolasini yuboring - bot sizga 📹video yuboradi\n\n"
		"✅ Bot - Uploads YouTube videos\n"
		"🇬🇧 Send a 🎞video 🔗 link from YouTube to the bot - the bot will send you 📹video\n\n"
		"✅ Бот - Скачать видео с Youtube\n"
		"🇷🇺 Отправьте ссылку на 🎞видео 🔗 боту с YouTube - бот пришлет вам 📹видео\n")


@dp.message_handler(text="/audio")
async def audio_bot(message: types.Message):
	text = "<b>❗️ Subscribe to @your_music_youtube channel</b>\n"
	text += f"<u>✅ All the music you are looking for is here! 🙂🙃😉</u>\n"
	text += f"<b>Use the <a href='https://t.me/Youtube_music_savebot'>YouTube Music Save Bot</a>🎵 @Youtube_music_savebot</b>\n"
	text += f"<b>Use the <a href='https://t.me/Youtube_video_savebot'>YouTube Video Save Bot</a>📹 @Youtube_video_savebot</b>\n"

	await message.answer(text)
