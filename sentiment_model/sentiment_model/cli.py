import click
from .models.alpaca_api import AlpacaAPISettings
from .models.config import SentimentModelConfig
from pathlib import Path


@click.group()
def main():
    pass


@main.command("alpaca-settings")
def alpaca_settings():
    print(AlpacaAPISettings().model_dump_json(indent=2))


@main.command("launch")
@click.option("--config", "-c", type=click.Path(exists=True), default="config.json")
def launch(config):
    config = Path(config)
    print(SentimentModelConfig.model_validate_json(config.read_text()).model_dump_json(indent=2))
