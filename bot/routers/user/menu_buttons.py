from aiogram import Router, F, types
from aiogram.filters import StateFilter

from bot.service.misc.misc_messages import main_menu_button

router = Router()


@router.message(
    ~StateFilter("order:get_price", "rate:get"),
    ~F.text.in_({"/start",
                 "♻️Меню",
                 "💹Изменить курс",
                 "👟Обувь/Верхняя одежда",
                 "👖Толстовки/Штаны",
                 "👕Футболка/Шорты",
                 "🧦Носки/Нижнее белье"
                 }
                )
)
async def buttons_menu(message: types.Message):
    await main_menu_button(message=message,
                           text=message.text,
                           user_id=message.from_user.id)


@router.callback_query(~F.data.in_({"menu"}))
async def buttons_menu(callback: types.CallbackQuery):
    await main_menu_button(message=callback.message,
                           text=callback.data,
                           user_id=callback.from_user.id)
    await callback.answer()
