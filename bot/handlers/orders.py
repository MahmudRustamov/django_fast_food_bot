from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from bot.keyboards.default import take_away_button_uz, order_en, order_uz, main_menu_en, \
    main_menu_uz, location_button, take_away_button_en, delivery_en, delivery_uz
from bot.utils.db_commands.user import get_language

router = Router()


@router.message(
    (F.text == "🛍 Order") | (F.text == "🛍 Buyurtma"),
    StateFilter(None)
)
async def order_button_handler(message: Message):
    lang = await get_language(message.chat.id)

    if lang == "en":
        text = "Take away  🙋‍♂️ or delivery 🚙"
        await message.answer(text=text, reply_markup=order_en)
    else:
        text = "Olib ketish  🙋‍♂️ yoki yetkazib berish 🚙"
        await message.answer(text=text, reply_markup=order_uz)


@router.message(
    (F.text == "🏃 Take away") | (F.text == "🏃 Olib ketish"),
    StateFilter(None)
)
async def take_away_button_handler(message: Message, state: FSMContext):
    lang = await get_language(message.chat.id)

    if lang == "en":
        text = "Where are you? Send your location and we determine the nearest branch to you"
        await message.answer(text=text, reply_markup=take_away_button_en)
    else:
        text = "Joylashuvingizni jo'nating. Biz sizga eng yaqin filialni aniqlab beramiz."
        await message.answer(text=text, reply_markup=take_away_button_uz)


@router.message(
    (F.text == "📍Determine nearest branch") | (F.text == "📍Eng yaqin filialni aniqlash"),
    StateFilter(None)
)
async def location_handler(message: Message, state: FSMContext):
    lang = await get_language(message.chat.id)
    if lang == "en":
        text = "Please, share your location"
        await message.answer(text=text, reply_markup=location_button)
    else:
        text = "Iltimos, joylashuvingizni jo'nating"
        await message.answer(text=text, reply_markup=location_button)


@router.message(
    (F.text == "Order here 🌐") | (F.text == "Bu yerda buyurtma berish 🌐"),
    StateFilter(None)
)
async def order_here_handler(message: Message, state: FSMContext):
    lang = await get_language(message.chat.id)
    if lang == "en":
        text = "Order with your location - - https://lesailes.uz/"
        await message.answer(text=text)
    else:
        text = "Bu yerdan buyurtma bering - https://lesailes.uz/"
        await message.answer(text=text)


@router.message(
    (F.text == "Select branch") | (F.text == "Filialni tanlash"),
    StateFilter(None)
)
async def branches_handler(message: Message, state: FSMContext):
    lang = await get_language(message.chat.id)
    if lang == "en":
        text = "Choose the nearest branch here"
        await message.answer(text=text)
    else:
        text = "Bu yerdan o'zingizga eng yaqin bo'lgan fillialni tanlang"
        await message.answer(text=text)


@router.message(
    (F.text == "🚙 Delivery") | (F.text == "🚙 Yetkazib berish"),
    StateFilter(None)
)
async def delivery_handler(message: Message, state: FSMContext):
    lang = await get_language(message.chat.id)
    if lang == "en":
        text = "Where to deliver? Send your location and we determine the nearest branch and delivery cost."
        await message.answer(text=text, reply_markup=delivery_en)
    else:
        text = "Qayerga yetkazib beramiz? Iltimos, joylashuvingizni yuboring, biz eng yaqin filial va yetkazib berish narxini aniqlaymiz"
        await message.answer(text=text, reply_markup=delivery_uz)


@router.message(
    (F.text == "🗺 My addresses") | (F.text == "🗺 Mening manzillarim"),
    StateFilter(None)
)
async def delivery_handler(message: Message, state: FSMContext):
    lang = await get_language(message.chat.id)
    if lang == "en":
        text = "You don't have any saved addresses"
        await message.answer(text=text, reply_markup=delivery_en)
    else:
        text = "Sizda saqlangan manzillar mavjud emas"
        await message.answer(text=text, reply_markup=delivery_uz)



@router.message((F.text == "🔥 Promotions") | (F.text == "🔥 Aksiya va chegirmalar"))
async def promotions_handler(message: Message):
    lang = await get_language(message.chat.id)
    if lang == "en":
        await message.answer("There is no promotions in your city", reply_markup=main_menu_en)
    else:
        await message.answer("Sizning shahringizda hech qanday chegirmalar mavjud emas!")


@router.message((F.text == "📖 My orders") | (F.text == "📖 Mening buyurtmalarim"))
async def my_orders_handler(message: Message):
    lang = await get_language(message.chat.id)
    if lang == "en":
        await message.answer("🚫 You do not have any orders yet", reply_markup=main_menu_en)
    else:
        await message.answer("🚫 Sizda hech qanday buyurtma yo'q", reply_markup=main_menu_uz)



@router.message((F.text == "⬅️ Back") | (F.text == "⬅️ Orqaga"), StateFilter(None))
async def back_button_handler(message: Message):
    lang = await get_language(message.chat.id)
    if lang == "en":
        await message.answer("Main menu", reply_markup=main_menu_en)
    else:
        await message.answer("Asosiy menyu", reply_markup=main_menu_uz)


