from discord.ext import commands
from discord import app_commands
import discord
import ollama

class Profile(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="profile", description="View yours or someone's profile!")
    async def profile(self, interaction: discord.Interaction, user: discord.Member = None):
        ...

async def setup(bot: commands.Bot):
    await bot.add_cog(Profile(bot))