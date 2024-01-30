from pydantic import BaseModel


__all__ = ["Stock"]


class Stock(BaseModel):
    ticker: str
