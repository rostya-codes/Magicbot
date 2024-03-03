import os

import aiofiles
from ujson import loads


async def get_json(filename: str) -> list:
    """ Function to read and load json file if it exists, else return empty list """
    path = f'data/{filename}'
    if os.path.exists(path):
        async with aiofiles.open(path, 'r', encoding='utf-8') as file:
            return loads(await file.read())
    return []
