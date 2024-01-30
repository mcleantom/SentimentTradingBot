from pydantic import BaseModel
from .stock import Stock
from enum import Enum


__all__ = ["ESentiment", "PreTradeData"]


class ESentiment(Enum):
    POSITIVE = 1
    NEGATIVE = 2
    NEUTRAL = 3


class PreTradeData(BaseModel):
    stock: Stock
    news_str: str
    sentiment: ESentiment
