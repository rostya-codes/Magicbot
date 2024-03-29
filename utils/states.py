from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    """ Questionnaire form """

    name = State()
    age = State()
    sex = State()
    about = State()
    photo = State()
