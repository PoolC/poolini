import discord

from .logger import logger


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready() -> None:
    logger.info(f"Logged in as {client.user}")


@client.event
async def on_message(message) -> None:
    if message.author == client.user:
        return

    if message.content.startswith(".ping"):
        await message.channel.send("pong")
