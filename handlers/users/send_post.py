import asyncio
import logging
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from data.config import ADMINS, CHANNELS
from keyboards.inline.manage_post import confirmation_keyboard, post_callback
from loader import dp, db, bot
from states.send_post import NewPost


@dp.message_handler(Command("create_post"))
async def create_post(message: Message):
	await message.answer("Reklamani chop etish uchun: \n1)🖼 Post rasmini \n2)📝 Post matnini yuboring.")
	await NewPost.NewMessage.set()


@dp.message_handler(state=NewPost.NewMessage, content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
	global photo_id
	photo_id = message.photo[-1].file_id
	if photo_id:
		await message.answer('Done!!! Photo download')
	else: 
		pass


@dp.message_handler(state=NewPost.NewMessage)
async def enter_message(message: Message, state: FSMContext):
	await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
	await message.answer(f"Postni tekshirish uchun yuboraymi?",
						 reply_markup=confirmation_keyboard)
	await NewPost.next()


@dp.callback_query_handler(post_callback.filter(action="post"), state=NewPost.Confirm)
async def confirm_post(call: CallbackQuery, state: FSMContext):
	async with state.proxy() as data:
		global text
		text = data.get("text")
		mention = data.get("mention")
	await state.finish()
	await call.message.edit_reply_markup()
	await call.message.answer("Post Adminga yuborildi")
	await bot.send_message(ADMINS[0], f"Foydalanuvchi {mention} quyidagi postni chop etmoqchi:")
	await bot.send_message(ADMINS[0], text, parse_mode="HTML", reply_markup=confirmation_keyboard)


@dp.callback_query_handler(post_callback.filter(action="cancel"), state=NewPost.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
	await state.finish()
	await call.message.edit_reply_markup()
	await call.message.answer("Post rad etildi.")


@dp.message_handler(state=NewPost.Confirm)
async def post_unknown(message: Message):
	await message.answer("Chop etish yoki rad etishni tanlang")


@dp.callback_query_handler(post_callback.filter(action="post"), user_id=ADMINS)
async def approve_post(call: CallbackQuery):
	await call.answer("Chop etishga ruhsat berdingiz.", show_alert=True)
	target_channel = CHANNELS[0]
	message = await call.message.edit_reply_markup()

	for_channel = 0
	users = db.select_all_users()
	for user in users:
		user_id = user[0]

		post = await bot.send_photo(chat_id=user_id, photo=photo_id, caption=text, parse_mode="HTML")
		await asyncio.sleep(0.05)
		for_channel += 1
		if for_channel == 1:		
			await post.send_copy(chat_id=target_channel)


@dp.callback_query_handler(post_callback.filter(action="cancel"), user_id=ADMINS)
async def decline_post(call: CallbackQuery):
	await call.answer("Post rad etildi.", show_alert=True)
	await call.message.edit_reply_markup()    
