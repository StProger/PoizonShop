from aiogram import Router, types, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from bot.service.misc.misc_messages import main_menu
from bot.filters.admin_filter import IsAdmin
from bot.keyboards.user import menu, menu_admin


router = Router()


@router.message(IsAdmin(), StateFilter("*"), F.text.in_({"/start", "♻️Меню"}))
async def menu_handler(message: types.Message, state: FSMContext):

    await state.clear()
    await main_menu(message=message,
                    first_name=message.from_user.first_name,
                    keyboard=menu_admin())


@router.callback_query(IsAdmin(), StateFilter("*"), F.data == "menu")
async def menu_callback(callback: types.CallbackQuery, state: FSMContext):

    await state.clear()
    await main_menu(message=callback.message,
                    first_name=callback.from_user.first_name,
                    keyboard=menu_admin())
    await callback.answer()


@router.message(StateFilter("*"), F.text.in_({"/start", "♻️Меню"}))
async def menu_handler(message: types.Message, state: FSMContext):

    await state.clear()
    await main_menu(message=message,
                    first_name=message.from_user.first_name,
                    keyboard=menu())


@router.callback_query(StateFilter("*"), F.data == "menu")
async def menu_callback(callback: types.CallbackQuery, state: FSMContext):

    await state.clear()
    await main_menu(message=callback.message,
                    first_name=callback.from_user.first_name,
                    keyboard=menu())
    await callback.answer()
