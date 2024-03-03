from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Pagination(CallbackData, prefix='pag'):
    """ Paginator describe model """
    action: str
    page: int


def paginator(page: int = 0):
    """Paginator to switch pages"""
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='⬅️', callback_data=Pagination(action='prev', page=page).pack()),
        InlineKeyboardButton(text='➡️', callback_data=Pagination(action='next', page=page).pack()),
        width=2  # 2 Кнопки в ряду
    )
    return builder.as_markup()
