from .config import config
from .discord_server import client

client.run(token=config["poolini"]["discord_token"])
