from aiogram import Router, F, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from bot.service.redis_serv.user import get_rate
from bot.keyboards.user import button_menu

router = Router()


@router.message(
    F.text.in_(
        {
            "👟Обувь/Верхняя одежда",
            "👖Толстовки/Штаны",
            "👕Футболка/Шорты",
            "🧦Носки/Нижнее белье"
        }
    )
)
async def price(message: types.Message, state: FSMContext):
    rate = await get_rate()
    await state.set_state("order:get_price")
    await message.answer(
        text=f"""Введите цену в ¥(Юань), а я рассчитаю для вас конечную стоимость.

⏩Курс ¥ - {rate}₽""",
        reply_markup=button_menu()
    )


@router.message(StateFilter("order:get_price"))
async def give_price(message: types.Message, state: FSMContext):

    price = message.text

    if not price.isdigit():
        await message.answer("❌Вводи только цифры")

    else:

        rate = await get_rate()
        total_price = float(rate) * int(price) + 500 + 500 + 500 + 1000

        text = f"""Итоговая стоимость позиции: {int(total_price)}


Стоимость включает: 

Доставка 🚚 по Китаю 
Доставка Китай-Москва
Комиссия нашего сервиса 
Курс ¥ - {float(rate)}₽

Стоимость рассчитана до склада в Москве

Уточняйте тут: @ImassageL @iabiryukofffPoizon"""

        await message.answer(
            text=text,
            reply_markup=types.InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        types.InlineKeyboardButton(
                            text="📲Менеджер", url="https://t.me/ImassageL"
                        )
                    ],
                    [
                        types.InlineKeyboardButton(
                            text="💵Рассчитать стоимость", callback_data="get_price"
                        ),
                        types.InlineKeyboardButton(
                            text="♻️Меню", callback_data="menu"
                        )
                    ]
                ]
            )
        )
        await state.clear()