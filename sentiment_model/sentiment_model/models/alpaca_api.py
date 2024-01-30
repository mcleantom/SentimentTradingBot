from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class AlpacaAPISettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='alpaca_')

    api_key: SecretStr
    api_secret: SecretStr
