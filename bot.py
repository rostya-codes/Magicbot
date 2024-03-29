import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from callbacks import pagination
from config_reader import config
from handlers import bot_messages, questionnaire, user_commands
from middlewares.antiflood import AntiFloodMiddleware
from middlewares.check_sub import CheckSubscription


async def main() -> None:
    """Initialize Bot instance with a default parse mode which will be passed to all API calls"""
    # Bot initialize
    bot = Bot(config.bot_token.get_secret_value(), parse_mode=ParseMode.HTML)
    # All handlers should be attached to the Router (or Dispatcher)
    dp = Dispatcher()

    # todo: Исправить этот мидлварь
    #dp.message.middleware(CheckSubscription())  # Регистрация middleware

    dp.message.middleware(AntiFloodMiddleware(3))  # Как аргумент указывается время в секундах для предотвращения флуда(спама)

    dp.include_routers(  # Порядок важен
        user_commands.router,
        pagination.router,
        questionnaire.router,
        bot_messages.router
    )

    # Не реагировать на сообщения которые были отправлены в то время когда бот был отключен
    await bot.delete_webhook(drop_pending_updates=True)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
