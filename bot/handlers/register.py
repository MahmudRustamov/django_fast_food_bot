from aiogram import Router, F
from aiogram.enums import ContentType
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from asgiref.sync import sync_to_async

from bot.keyboards.default import phone_number, main_menu_en, main_menu_uz, \
    cities_en, cities_uz
from bot.keyboards.default import languages
from bot.states.register import RegisterState
from bot.utils.db_commands.user import add_user, get_user

router = Router()

@router.message(Command('start'))
async def start_handler(message: Message, state: FSMContext):
    user = await get_user(chat_id=message.chat.id)
    if user:
        if user.language == "en":
            text = "Welcome 😊"
            await message.answer(text=text, reply_markup=main_menu_en)
        else:
            text = "Xush kelibsiz 😊"
            await message.answer(text=text, reply_markup=main_menu_uz)
    else:
        text = "Assalomu alaykum! Les Ailes yetkazib berish xizmatiga xush kelibsiz.\nHello! Welcome to Les Ailes delivery service."
        text1 = "Iltimos tilni tanlang\nPlease select the language."
        await message.answer(text=text)
        await message.answer(text=text1, reply_markup=languages)
        await state.set_state(RegisterState.language)


@router.message(RegisterState.language)
async def language_handler(message: Message, state: FSMContext):
    lang = message.text
    await state.update_data(language=lang)
    if lang == "🇺🇸 English":
        lang = "en"
        await state.update_data(language=lang)
        text = "Please enter your full name"
    else:
        lang = "uz"
        await state.update_data(language=lang)
        text = "Iltimos to'liq ismingizni kiriting"
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await state.set_state(RegisterState.full_name)


@router.message(RegisterState.full_name)
async def full_name_handler(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    data = await state.get_data()
    lang = data.get('language')
    if lang == "en":
        text = "Please enter your phone number"
    else:
        text = "Iltimos telefon raqamingizni kiriting"
    await message.answer(text=text, reply_markup=phone_number)
    await state.set_state(RegisterState.phone_number)


@router.message(RegisterState.phone_number, F.content_type == ContentType.CONTACT)
async def phone_number_handler(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    data = await state.get_data()
    lang = data.get('language')
    if lang == "en":
        text = "Please, choose your city:"
        await message.answer(text=text, reply_markup=cities_en)
    else:
        text = "Iltimos shaharni tanlang:"
        await message.answer(text=text, reply_markup=cities_uz)
    await state.set_state(RegisterState.city)


@router.message(RegisterState.city)
async def city_handler(message: Message, state: FSMContext):
    await state.update_data(city=message.text, chat_id=message.chat.id, created_at=message.date)
    data = await state.get_data()
    lang = data.get('language')
    new_user = await sync_to_async(add_user)(data)

    if new_user:
        if lang == "en":
            await message.answer("Successfully registered ✅", reply_markup=main_menu_en)
        else:
            await message.answer("Muvaffaqqiyatli ro'yxatdan o'tdingiz ✅", reply_markup=main_menu_uz)
    else:
        if lang == "en":
            await message.answer("Not registered, something went wrong!")
        else:
            await message.answer("Botda muommo mavjud biz bilan bog'laning")

    await state.clear()
