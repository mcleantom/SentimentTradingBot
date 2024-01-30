from fastapi import FastAPI
from .config import APIConfig, SentimentModelConfig
from .model_router import create_model_router


def create_api(api_config: APIConfig) -> FastAPI:
    app = FastAPI(
        title=api_config.app_name,
        description=api_config.app_description
    )

    app.include_router(create_model_router(api_config))
    return app
