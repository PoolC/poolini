import io
import sys

import discord

from .cli.main import poolini
from .config import config
from .logger import logger

BOT_NAME = config["poolini"]["bot_name"]
START_CHARACTERS = config["poolini"]["start_characters"]
DISCORD_TOKEN = config["poolini"]["discord_token"]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready() -> None:
    logger.info("Captain [%s] on duty!", client.user)


@client.event
async def on_message(message) -> None:
    if message.author == client.user:
        return

    # (".풀린 ", "!풀린 ", "/풀린 ")
    # 끝에 의도적 띄어쓰기
    start_characters_plus_bot_name = tuple(list(map(lambda c: f"{c}{BOT_NAME} ", START_CHARACTERS)))
    if not message.content.startswith(start_characters_plus_bot_name):
        return

    original_stdout = sys.stdout
    sys.stdout = io.StringIO()

    args = message.content.split(" ")[1:]
    try:
        poolini.main(args=args)
    except SystemExit as e:
        output = str(e)

    output = sys.stdout.getvalue()
    sys.stdout = original_stdout

    await message.channel.send(output)


@client.event
async def on_error(event, *args) -> None:
    if event == "on_message":
        message = args[0]
        exc_type, exc_value, _ = sys.exc_info()

        logger.error(
            '%s: %s. (Author: %s / Message: %s)',
            ".".join([exc_type.__module__, exc_type.__name__]),
            exc_value,
            message.author,
            message.content,
        )


if __name__ == "__main__":
    client.run(token=DISCORD_TOKEN)
