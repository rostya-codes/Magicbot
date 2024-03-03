from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    """ Questionnaire form """

    name = State()
    age = State()
    sex = State()
    about = State()
    photo = State()
