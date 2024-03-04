from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message
from cachetools import TTLCache


class AntiFloodMiddleware(BaseMiddleware):
    """ To avoid flood """

    def __init__(self, time_limit: int = 2) -> None:
        """В параметре time_limit указывается время в секундах для предотвращения флуда(спама)"""
        self.limit = TTLCache(maxsize=10_000, ttl=time_limit)  # ttl - time to live (сколько кэш будет жить в памяти)

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        if event.chat.id in self.limit:
            return
        else:
            self.limit[event.chat.id] = None
        return await handler(event, data)
