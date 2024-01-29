import click
from .config import APIConfig
from .api import create_api
import uvicorn
from pathlib import Path


@click.group()
def main():
    pass


@main.command("launch")
@click.option("--host", default="0.0.0.0", help="Host to run the API on")
@click.option("--port", default=8000, help="Port to run the API on")
@click.option("--config", default="config.json", help="Path to config file", type=click.Path(exists=True))
def launch_api(host: str, port: int, config: str):
    config = APIConfig.model_validate_json(Path(config).read_text())
    api = create_api(config)
    uvicorn.run(api, host=host, port=port)
