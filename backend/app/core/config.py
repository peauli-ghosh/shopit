import os
from pathlib import Path
from typing import Literal

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parents[3]


class BaseAppSettings(BaseSettings):
    database_url: str
    redis_url: str

    razorpay_key_id: str
    razorpay_key_secret: SecretStr
    razorpay_webhook_secret: SecretStr

    ai_api_key: SecretStr

    jwt_secret: SecretStr

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


class DevelopmentSettings(BaseAppSettings):
    environment: Literal["development"] = "development"
    debug: bool = True


class ProductionSettings(BaseAppSettings):
    environment: Literal["production"] = "production"
    debug: bool = False


def get_settings() -> BaseAppSettings:
    environment = os.getenv("ENVIRONMENT", "development").lower()

    if environment == "production":
        return ProductionSettings()

    return DevelopmentSettings()


settings = get_settings()