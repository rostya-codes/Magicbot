from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message
from icecream import ic

from keyboards.inline import sub_channel


class CheckSubscription(BaseMiddleware):
    """ To check channel subscription """

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        chat_member = await event.bot.get_chat_member('@rmpyc', event.from_user.id)

        ic(handler)
        print()  # Enter
        ic(event)
        print()  # Enter
        ic(data)
        print()  # Enter

        if chat_member.status == 'left':
            await event.answer(
                'Subscribe to the channel to use the bot!',
                reply_markup=sub_channel
            )
        else:
            return await handler(event, data)
