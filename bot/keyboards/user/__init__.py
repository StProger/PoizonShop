from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton


def menu():

    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="💵Рассчитать стоимость")
            ],
            [
                KeyboardButton(text="🎯Отзывы"),
                KeyboardButton(text="📲Связь с менеджером")
            ],
            [
                KeyboardButton(text="🚚Как заказать?"),
                KeyboardButton(text="❓F.A.Q")
            ],
            [
                KeyboardButton(text="‼️Акции‼️"),
                KeyboardButton(text="🎒Товары в наличии")
            ]
        ]
    )

def menu_admin():

    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="💹Изменить курс")
            ],
            [
                KeyboardButton(text="💵Рассчитать стоимость")
            ],
            [
                KeyboardButton(text="🎯Отзывы"),
                KeyboardButton(text="📲Связь с менеджером")
            ],
            [
                KeyboardButton(text="🚚Как заказать?"),
                KeyboardButton(text="❓F.A.Q")
            ],
            [
                # KeyboardButton(text="‼️Акции‼️"),
                KeyboardButton(text="🎒Товары в наличии")
            ]
        ]
    )


def button_menu():

    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="♻️Меню")
            ]
        ]
    )

def categories():

    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="👟Обувь/Верхняя одежда"),
                KeyboardButton(text="👖Толстовки/Штаны")
            ],
            [
                KeyboardButton(text="👕Футболка/Шорты"),
                KeyboardButton(text="🧦Носки/Нижнее белье")
            ],
            [
                KeyboardButton(text="♻️Меню")
            ]
        ]
    )
