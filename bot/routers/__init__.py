from aiogram import Dispatcher

from bot.routers import start
from bot.routers.user import menu_buttons
from bot.routers.user import price

from bot.routers.admin import change_rate


def register_all_routers(dp: Dispatcher):

    dp.include_router(start.router)
    dp.include_router(menu_buttons.router)
    dp.include_router(price.router)
    dp.include_router(change_rate.router)
