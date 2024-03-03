from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

links = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='YouTube', url='https://youtu.be'),
            InlineKeyboardButton(text='Telegram', url='tg://resolve?domain=rmpyc'),
        ]
    ]
)
