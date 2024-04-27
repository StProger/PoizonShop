from bot.service.redis_serv.base import redis_pool


async def set_rate(value) -> None:
    """ Установка сообщения на удаление (пользователю) """
    await redis_pool.set("rate", value)


async def get_rate() -> int:
    """ Получение сообщения, которое надо удалить у пользователя """
    return await redis_pool.get("rate")
