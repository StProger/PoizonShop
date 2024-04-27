from aiogram import types
from aiogram.utils.media_group import MediaGroupBuilder

from bot.settings import settings
from bot.keyboards.user import button_menu, categories


async def main_menu(message: types.Message,
                    first_name,
                    keyboard: types.ReplyKeyboardMarkup):

    text = f"""Привет, {first_name}!

Тут ты можешь рассчитать сумму своего заказа💵 
Связаться с менеджерами
@ImassageL @iabiryukofffPoizon
Получить ответы на все свои вопросы🤔"""

    await message.answer(
        text=text,
        reply_markup=keyboard
    )


async def main_menu_button(message: types.Message,
                           text: str,
                           user_id: int):

    if text == "🎯Отзывы":

        await message.answer(
            text=f"Отзывы: {settings.feedback}",
            reply_markup=button_menu()
        )

    elif text == "📲Связь с менеджером":

        await message.answer(
            text=f"Менеджеры: @ImassageL @iabiryukofffPoizon",
            reply_markup=button_menu()
        )

    elif text == "❓F.A.Q":

        await message.answer(
            text=f"Ответы на все вопросы: {settings.f_a_q}",
            reply_markup=button_menu()
        )

    elif text == "🎒Товары в наличии":

        await message.answer(
            text=f"""Так же вы можете приобрести позиции, которые уже имеются в наличии 

Канал: {settings.items_stock}""",
            reply_markup=button_menu()
        )

    elif text == "🚚Как заказать?":

        await message.answer(
            text="Перед оформлением заказа прочтите данную статью👇",
            reply_markup=types.InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        types.InlineKeyboardButton(
                            text="Статья", url=settings.how_order
                        )
                    ]
                ]
            )
        )

    elif text == "💵Рассчитать стоимость" or text == "get_price":

        media_group = MediaGroupBuilder()
        media_group.add_photo(media=settings.photo_1)
        media_group.add_photo(media=settings.photo_2)
        await message.bot.send_media_group(
            chat_id=user_id,
            media=media_group.build()
        )

        await message.answer(
            text="Выбери категорию товара",
            reply_markup=categories()
        )