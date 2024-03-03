from aiogram import F, Router
from aiogram.types import Message

from data.subloader import get_json
from keyboards import builders, fabrics, inline, reply

router = Router()


@router.message(F.text.lower().in_(['hi', 'hello', 'hola']))
async def hello_handler(message: Message):
    """Hello message"""
    await message.reply('hello!')


@router.message()  # Обработка сработает, если предыдущие не сработали
async def else_handler(message: Message) -> None:
    """
    :param message: aiogram Message object to answer
    :return: None

    If previous handlers didn't work - use this handler
    """
    msg = message.text
    if msg is not None:
        msg = msg.lower()
    emoji = await get_json('emoji.json')

    if msg == 'links':
        await message.answer('your links: ', reply_markup=inline.links)
    elif msg == 'special buttons':
        await message.answer('special buttons: ', reply_markup=reply.special)
    elif msg == 'calculator':
        await message.answer('Calculating...', reply_markup=builders.calculator_kb())  # Call keyboard builder function
    elif msg == 'emoji':
        await message.answer(f'{emoji[0][0]} <b>{emoji[0][1]}</b>', reply_markup=fabrics.paginator())
    else:
        try:
            # Send a copy of the received message
            await message.send_copy(chat_id=message.chat.id)
        except TypeError:
            # But not all the types is supported to be copied so need to handle it
            await message.answer("Nice try!")
