import random

from aiogram import Bot, Router
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.types import Message
from icecream import ic

from filters.is_admin import IsAdmin
from filters.is_digit_or_float import CheckForDigit
from keyboards import reply

router = Router()


@router.message(CommandStart(), IsAdmin(6083807927))
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"hello, <b>{message.from_user.full_name}</b>!", reply_markup=reply.main)


@router.message(Command('pay'), CheckForDigit())  # /pay 1234
async def pay_the_order(message: Message, command: CommandObject) -> None:
    await message.answer('You have successfully paid for the item!')


@router.message(Command(commands=['random', 'rn', 'random-number', 'r', 'randomize', 'randint', 'randnum']))
async def get_random_number_handler(message: Message, command: CommandObject) -> None:
    """
    This handler generates and prints random numbers to the chat.
    """
    if command.args:
        try:
            a, b = [int(n) for n in command.args.split('-')]
            random_number = random.randint(a, b)
            await message.reply(f'random number: {random_number}')
        except ValueError:
            # Обработка случая, когда аргументы не являются числами
            await message.reply(
                'Ошибка. Пожалуйста, укажите два числовых аргумента после команды /rn, например, /rn 1-100')
        except AttributeError:
            await message.reply(
                'Ошибка. Пожалуйста, укажите два числовых аргумента после команды /rn, например, /rn 1-100')
    else:
        # Обработка случая, когда аргументы отсутствуют
        await message.reply('Ошибка. Пожалуйста, укажите два числовых аргумента после команды /rn, например, /rn 1-100')


@router.message(Command(commands=['play', 'pl', 'game', 'play-game', 'games']))
async def play_games_handler(message: Message):
    """Handler to throw a dice and print result"""
    x = await message.answer_dice(DiceEmoji.DICE)
    ic(f'Результат падения кубика: {x.dice.value}')


@router.message(Command('dice'))
async def cmd_dice(message: Message, bot: Bot):
    """Send dice🎲 to the tg channel"""
    await bot.send_dice(-1002131022276, emoji=DiceEmoji.DICE)  # (-channel_id, emoji)
