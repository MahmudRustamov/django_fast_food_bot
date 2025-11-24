from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


inline_keyboard_test = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Test", callback_data="inline_keyboard")
        ]
    ]
)


proceed_button_en = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Proceed", callback_data="inline_keyboard", url="https://t.me/myexceptionns")
        ]
    ]
)

proceed_button_uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'tish", callback_data="inline_keyboard", url="https://t.me/myexceptionns")
        ]
    ]
)

support_en = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Contact us", callback_data="inline_keyboard", url="https://t.me/Mahmud_Rustamov")
        ]
    ]
)

support_uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Biz bilan aloqaga chiqing", callback_data="inline_keyboard", url="https://t.me/Mahmud_Rustamov")
        ]
    ]
)


rating_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        # product header
        [InlineKeyboardButton(text="Product / Mahsulot", callback_data="header_product")],

        # product row
        [
            InlineKeyboardButton(text="1 😖", callback_data="product_1"),
            InlineKeyboardButton(text="2 ☹️", callback_data="product_2"),
            InlineKeyboardButton(text="3 😕", callback_data="product_3"),
            InlineKeyboardButton(text="4 😐", callback_data="product_4"),
            InlineKeyboardButton(text="5 😍", callback_data="product_5"),
        ],

        # package header
        [InlineKeyboardButton(text="Package / Qadoqlash", callback_data="header_package")],


        [
            InlineKeyboardButton(text="1 👊", callback_data="package_1"),
            InlineKeyboardButton(text="2 👎", callback_data="package_2"),
            InlineKeyboardButton(text="3 👌", callback_data="package_3"),
            InlineKeyboardButton(text="4 🤙", callback_data="package_4"),
            InlineKeyboardButton(text="5 👍", callback_data="package_5"),
        ],

        # delivery header
        [InlineKeyboardButton(text="Delivery / Yetkazib berish", callback_data="header_delivery")],

        # delivery row
        [
            InlineKeyboardButton(text="1 🐌", callback_data="delivery_1"),
            InlineKeyboardButton(text="2 🐢", callback_data="delivery_2"),
            InlineKeyboardButton(text="3 🚚", callback_data="delivery_3"),
            InlineKeyboardButton(text="4 🏍️", callback_data="delivery_4"),
            InlineKeyboardButton(text="5 🚀", callback_data="delivery_5"),
        ],
    ]
)
