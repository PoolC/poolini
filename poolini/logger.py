import logging

from .config import config

LEVEL = logging.DEBUG if config["poolini"]["debug"] else logging.INFO

logger = logging.getLogger("discord.log")
logger.setLevel(LEVEL)

access_logger = logging.getLogger("discord.access")
access_logger.setLevel(LEVEL)
