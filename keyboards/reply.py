from aiogram.types import (KeyboardButton, KeyboardButtonPollType,
                           ReplyKeyboardMarkup)

main = ReplyKeyboardMarkup(
    keyboard=[
        [  # первый ряд
            KeyboardButton(text='emoji'),
            KeyboardButton(text='links'),
        ],
        [  # второй ряд
            KeyboardButton(text='calculator'),
            KeyboardButton(text='special buttons'),
        ]
    ],
    resize_keyboard=True,  # Уменьшает кнопки
    one_time_keyboard=True,  # Скрывает клавиатуру после разового использования
    input_field_placeholder='Выберите действие из меню',  # Отображается в поле ввода
    selective=True,  # Клавиатура будет активироваться только у того кто ее вызвал (актуально в чатах)
)

special = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='send location (just from phone)', request_location=True),
            KeyboardButton(text='Send contact', request_contact=True),
            KeyboardButton(text='create a quiz/survey', request_poll=KeyboardButtonPollType())
        ],
        [
            KeyboardButton(text='BACK 🔙')
        ],
    ],
    resize_keyboard=True,
)
