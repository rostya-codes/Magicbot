from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

links = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='YouTube', url='https://youtu.be'),
            InlineKeyboardButton(text='Telegram', url='tg://resolve?domain=rmpyc'),
        ]
    ]
)

sub_channel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Subscribe', url='https://t.me/rmpyc')
        ]
    ]
)
