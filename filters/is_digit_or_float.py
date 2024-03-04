from typing import Any

from aiogram.filters import BaseFilter, CommandObject
from aiogram.types import Message
from icecream import ic


class CheckForDigit(BaseFilter):
    """ Check for digit """

    async def __call__(self, message: Message, **data: Any) -> bool:
        ic(data)
        command: CommandObject = data.get('command')
        arg = command.args

        if arg.isnumeric() or (arg.count('.') == 1 and arg.replace('.', '').isnumeric()):
            return True
        return False
