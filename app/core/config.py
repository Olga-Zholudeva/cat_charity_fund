from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = "Сбор пожертвований"
    app_description: str = (
        "Приложение для Благотворительного фонда поддержки котиков QRKot"
    )
    database_url: str = "sqlite+aiosqlite:///./cat_charity_fund.db"
    secret: str = "SECRET"

    class Config:
        env_file = ".env"


settings = Settings()
