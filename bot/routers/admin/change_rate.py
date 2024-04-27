from aiogram import Router, F, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from bot.keyboards.user import button_menu, menu_admin
from bot.service.redis_serv.user import set_rate

router = Router()


@router.message(StateFilter("*"), F.text == "💹Изменить курс")
async def change_rate(message: types.Message, state: FSMContext):

    await state.set_state("rate:get")
    await message.answer(
        text="Отправьте новый курс.",
        reply_markup=button_menu()
    )


@router.message(StateFilter("rate:get"))
async def set_new_rate(message: types.Message, state: FSMContext):

    new_rate = None
    try:
        new_rate = float(message.text)
    except ValueError:
        await message.answer("Введите число❌")
        return
    await set_rate(new_rate)

    await message.answer("Курс изменён.",
                         reply_markup=menu_admin())
    await state.clear()