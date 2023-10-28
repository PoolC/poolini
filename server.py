import os
import logging

import discord
from dotenv import load_dotenv


load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN', "")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

log_handler = logging.getLogger("discord.client")


@client.event
async def on_ready() -> None:
    log_handler.info(f"Logged in as {client.user}")


@client.event
async def on_message(message) -> None:
    if message.author == client.user:
        return

    if message.content.startswith(".ping"):
        await message.channel.send("pong")


client.run(token=DISCORD_TOKEN)
