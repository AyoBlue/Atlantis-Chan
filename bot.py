from discord.ext import commands
import discord
import asyncio
import os

from dotenv import load_dotenv
load_dotenv()

client = commands.Bot(command_prefix="_", intents=discord.Intents.all())

async def load_extensions():
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            await client.load_extension(f"cogs.{file[:-3]}")

@client.event
async def on_ready():
    await client.tree.sync()

asyncio.run(load_extensions())
client.run(os.getenv("DISCORD_TOKEN"))