from pydantic import BaseModel
from .stock import Stock
from .alpaca_api import AlpacaAPISettings


__all__ = ["SentimentModelConfig"]


class SentimentModelConfig(BaseModel):
    alpaca_api: AlpacaAPISettings = AlpacaAPISettings()
    stocks: list[Stock]
