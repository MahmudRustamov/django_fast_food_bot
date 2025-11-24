from aiogram import Router, F
from aiogram.enums import ContentType
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, BufferedInputFile

from bot.filters.admin import IsAdmin
from bot.keyboards.default import user_settings_en, user_settings_uz
from bot.keyboards.inline import inline_keyboard_test
from bot.utils.db_commands.user import get_language

router = Router()



@router.message((F.text == "⚙️Settings") | (F.text == "⚙️ Sozlamalar"))
async def settings_handler(message: Message, state: FSMContext):
    lang = await get_language(message.chat.id)
    if lang == "en":
        text = "Choose an action:"
        await message.answer(text=text, reply_markup=user_settings_en)
    else:
        text = "Amalni tanlang:"
        await message.answer(text=text, reply_markup=user_settings_uz)



@router.callback_query(F.data == 'inline_keyboard', IsAdmin())
async def settings_handler(call: CallbackQuery):
    message = call.message

    text = "Inline keyboard is working"
    await message.answer(text=text, reply_markup=inline_keyboard_test)


class FileStates(StatesGroup):
    waiting_for_file = State()


@router.message(Command('file'))
async def get_file_id(message: Message, state: FSMContext):
    text = "Enter file"
    await message.answer(text)
    await state.set_state(FileStates.waiting_for_file)


@router.message(FileStates.waiting_for_file, F.content_type == ContentType.PHOTO)
async def send_file_id(message: Message):
    with open('media/img.png', 'rb') as image_file:
        image_binary = image_file.read()

    # Create BufferedInputFile from binary data
    photo = BufferedInputFile(
        file=image_binary,
        filename='image.png')

    await message.answer_photo(photo=photo)
