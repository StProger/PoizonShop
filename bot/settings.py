import json

from pydantic_settings import BaseSettings

from dotenv import load_dotenv

import os

from yarl import URL

load_dotenv()


class Settings(BaseSettings):

    BOT_TOKEN: str = os.getenv("BOT_TOKEN")

    FSM_REDIS_HOST: str = os.getenv("FSM_REDIS_HOST")
    FSM_REDIS_DB: int = os.getenv("FSM_REDIS_DB")

    REDIS_HOST: str = os.getenv("REDIS_HOST")
    REDIS_DB: int = os.getenv("REDIS_DB")

    photo_1: str = "AgACAgIAAxkDAAMCZitiT680E7s4lAQ8HqFtQpeRcNYAAnjaMRu2LGBJkO9I688Hw0UBAAMCAAN5AAM0BA"
    photo_2: str = "AgACAgIAAxkDAAMDZitiT4SCv1DwcNdeR7MkFAg33WoAAnnaMRu2LGBJmP3ORaiRSeMBAAMCAAN5AAM0BA"

    # Путь к логам
    PATH_LOGS: str = "bot/data/logs.log"

    ADMIN_IDS: list[int] = json.loads(os.getenv("ADMIN_IDS"))

    # Отзывы
    feedback: str = "@IPLfeedback"

    # Товары в наличии
    items_stock: str = "https://t.me/ipoizonshopl"

    # FAQ
    f_a_q: str = "https://t.me/ipoizonshopl/22"

    how_order: str = os.getenv("HOW_ORDER")

    class Config:

        env_file = "../.env"

    @property
    def fsm_redis_url(self) -> str:
        """
        создание URL для подключения к редису

        :return: redis connection url
        """
        return str(URL.build(
            scheme="redis",
            host=self.FSM_REDIS_HOST,
            path="/" + str(self.FSM_REDIS_DB)
        ))


settings = Settings()
