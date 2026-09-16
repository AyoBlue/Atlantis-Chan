from discord.ext import commands
import discord

class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        role = discord.utils.get(member.guild.roles, id=1295952331933745256)
        if role:
            await member.add_roles(role)

async def setup(bot: commands.Bot):
    await bot.add_cog(Events(bot))