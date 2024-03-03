from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.builders import profile
from keyboards.reply import rmk
from utils.states import Form

router = Router()


@router.message(Command('profile'))
async def fill_profile(message: Message, state: FSMContext):
    """To start filling out the form"""
    await state.set_state(Form.name)
    await message.answer(
        "It's Daywinechik - Dating bot ❤️‍🔥\nLet's get started, enter your name 💞",
        reply_markup=profile(message.from_user.first_name)  # Пользователь сможет ввести имя вручную или нажать на эту кнопку
    )


@router.message(Form.name)
async def form_name(message: Message, state: FSMContext):
    """To get name"""
    await state.update_data(name=message.text)
    await state.set_state(Form.age)
    await message.answer('Nice! Now enter your age 💕', reply_markup=rmk)


@router.message(Form.age)
async def form_age(message: Message, state: FSMContext):
    """To get age"""
    if message.text.isdigit():
        if 0 < int(message.text) <= 120:
            await state.update_data(age=int(message.text))
            await state.set_state(Form.sex)
            await message.answer(
                "Then select your gender 💘",
                reply_markup=profile(['Male', 'Female'])
            )
        else:
            await message.answer('Enter a number from 0 to 120! 💝')
    else:
        await message.answer('Enter a number! 💝')


@router.message(Form.sex, F.text.casefold().in_(['male', 'female']))
async def form_sex(message: Message, state: FSMContext):
    """To get gender"""
    await state.update_data(sex=message.text)
    await state.set_state(Form.about)
    await message.answer('Tell about yourself 💚', reply_markup=rmk)


@router.message(Form.sex)
async def incorrect_form_sex(message: Message):
    """Incorrect entered gender"""
    await message.answer('Press the button! 🧡')


@router.message(Form.about)
async def form_about(message: Message, state: FSMContext):
    """To get description"""
    if len(message.text) < 5:
        await message.answer('Enter something more interesting... 💜')
    else:
        await state.update_data(about=message.text)
        await state.set_state(Form.photo)
        await message.answer('Send me your photo 😻')


@router.message(Form.photo, F.photo)
async def form_photo(message: Message, state: FSMContext):
    """To get photo"""
    photo_file_id = message.photo[-1].file_id  # [-1] - последний елемент в списке это самое хорошее качество
    data = await state.get_data()
    await state.clear()

    formatted_text = []
    [
        formatted_text.append(f'{key}: {value}')
        for key, value in data.items()
    ]

    await message.answer_photo(
        photo_file_id,
        '\n'.join(formatted_text)
    )


@router.message(Form.photo, ~F.photo)
async def incorrect_form_photo(message: Message):
    """Incorrect photo"""
    await message.answer('Send photo!')
