from pydantic import BaseModel


__all__ = ["APIConfig", "SentimentModelConfig"]


class SentimentModelConfig(BaseModel):
    bert_model: str = "ProsusAI/finbert"
    encoding: dict[int, str] = {0: "positive", 1: "negative", 2: "neutral"}


class APIConfig(BaseModel):
    sentiment_model: SentimentModelConfig = SentimentModelConfig()
    app_name: str = "Sentiment Analysis API"
    app_description: str = "API to perform sentiment analysis on financial news headlines"
