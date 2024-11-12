from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

shablon = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Tugma nomi", url="URL"),
            InlineKeyboardButton(text="Tugma nomi", callback_data="URL"),
        ],
    ]
)
