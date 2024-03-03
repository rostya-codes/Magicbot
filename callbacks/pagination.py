from contextlib import suppress

from aiogram import F, Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery

from data.subloader import get_json
from keyboards import fabrics

router = Router()


@router.callback_query(fabrics.Pagination.filter(F.action.in_(['prev', 'next'])))
async def pagination_handler(call: CallbackQuery, callback_data: fabrics.Pagination):
    """
    Handler to paginate

    callback_data - зарезервированное название в aiogram
    """
    emoji = await get_json('emoji.json')

    page_num = int(callback_data.page)
    page = page_num - 1 if page_num > 0 else 0  # Чтобы не было возможности переключаться на минусовые страницы

    if callback_data.action == 'next':
        page = page_num + 1 if page_num < (len(emoji) - 1) else page_num

    with suppress(TelegramBadRequest):
        await call.message.edit_text(
            f'{emoji[page][0]} <b>{emoji[page][1]}</b>',
            reply_markup=fabrics.paginator(page)
        )
    await call.answer()
