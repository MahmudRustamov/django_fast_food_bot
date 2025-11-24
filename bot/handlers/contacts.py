from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import Message
from bot.keyboards.default import contact_en, contact_uz
from bot.keyboards.inline import proceed_button_en, proceed_button_uz, support_uz, support_en, rating_keyboard
from bot.utils.db_commands.user import get_language

router = Router()


@router.message((F.text == "🙋🏻‍♂️ Join to our team") | (F.text == "🙋🏻‍♂️ Jamoamizga qo'shilish"))
async def feedback_handler(message: Message):
    lang = await get_language(message.chat.id)
    print(lang)
    if lang == "en":
        text = """Join our friendly team our friendly team! Click on the button below to fill out the questionnaire right here, without leaving Telegram."""
        await message.answer(text=text, reply_markup=proceed_button_en)
    else:
        text = "Bizning do‘stona jamoamizga qo‘shiling! Quyidagi tugmani bosib, anketani aynan shu yerda, Telegram’dan chiqmasdan to‘ldiring."
        await message.answer(text=text, reply_markup=proceed_button_uz)


@router.message((F.text == "☎️ Contact") | (F.text == "☎️ Aloqa"))
async def contact_handler(message: Message):
    lang = await get_language(message.chat.id)
    if lang == "en":
        text = "We would be happy if you write to us or leave a comment."
        await message.answer(text=text, reply_markup=contact_en)
    else:
        text = "Agar siz bizga yozsangiz yoki sharh qoldirmoqchi bo'lsangiz, xursand bo'lamiz."
        await message.answer(text=text, reply_markup=contact_uz)


@router.message((F.text == "💬 Text us") | (F.text == "💬 Biz bilan aloqaga chiqing"))
async def support_handler(message: Message):
    lang = await get_language(message.chat.id)
    if lang == "en":
        text = "If you have any questions or suggestions, feel free to contact us."
        await message.answer(text=text, reply_markup=support_en)
    else:
        text = "Agar biron-bir savol yoki taklif bo'lsa, bizga aloqaga chiqing."
        await message.answer(text=text, reply_markup=support_uz)


@router.message((F.text == "✍️ Leave a feedback") | (F.text == "✍️ Fikr bildirish"))
async def feedback_handler(message: Message):
    lang = await get_language(message.chat.id)
    if lang == "en":
        text = "✅ Les Ailes Service control."
        await message.answer(text=text, reply_markup=rating_keyboard)
    else:
        text = "✅ Les Ailes xizmatini nazorat qilish"
        await message.answer(text=text, reply_markup=rating_keyboard)


@router.callback_query(
    F.data.startswith("product_") |
    F.data.startswith("package_") |
    F.data.startswith("delivery_")
)
async def rating_handler(callback: CallbackQuery):
    category, rating = callback.data.split("_")
    lang = await get_language(callback.message.chat.id)
    if lang == "en":
        messages = {
            "product": "You selected product rating:",
            "package": "You selected package rating:",
            "delivery": "You selected delivery rating:",
        }

        await callback.message.answer(f"{messages[category]} {rating}")
        await callback.answer()
    else:
        messages = {
            "product": "Siz mahsulot bahosini tanladingiz:",
            "package": "Siz qadoqlash bahosini tanladingiz:",
            "delivery": "Siz yetkazib berish bahosini tanladingiz:",
        }
        await callback.message.answer(f"{messages[category]} {rating}")
        await callback.answer()