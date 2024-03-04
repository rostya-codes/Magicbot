from typing import List

from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsAdmin(BaseFilter):
    """
    To check if a user is an admin
    Как параметр передается айдишник либо список из айдишников
    """

    def __init__(self, user_ids: int | list[int]) -> None:
        self.user_ids = user_ids

    async def __call__(self, message: Message) -> bool:
        if isinstance(self.user_ids, int):  # Проверка на тип данных
            return message.from_user.id == self.user_ids  # Если передан 1 айдишник
        return message.from_user.id in self.user_ids  # Если передан список айдишников
