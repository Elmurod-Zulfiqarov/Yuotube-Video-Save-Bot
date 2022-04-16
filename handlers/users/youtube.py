from aiogram import types
from loader import dp, bot
from aiogram.dispatcher.filters import Text
from pytube import YouTube
from data.config import ADMINS, CHANNELS


@dp.message_handler(Text(startswith='http'))
async def youtubeVideoConverterAudio(message: types.Message):
    youtube_link = message.text
    from io import BytesIO
    buffer = BytesIO()
    url = YouTube(youtube_link)
    if url.check_availability() is None:
        video = url.streams.get_highest_resolution()
        video.stream_to_buffer(buffer=buffer)
        buffer.seek(0)
        video_title = url.title
        channel_name = url.author
        link = "\n\n@Youtube_music_savebot 🎵 \n@Youtube_video_savebot 📹"
        caption = '📹 ' + video_title + '\n\n 👤 #' + channel_name + link
        await message.answer_video(video=buffer, caption=caption)
    else:
        await message.answer("🇺🇿 - Linkni qaytadan tekshirib ko'ring!\n🇬🇧 - Check the link again!\n🇷🇺 - Проверьте ссылку еще раз!")
