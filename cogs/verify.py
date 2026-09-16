from discord.ext import commands
import discord

class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        if interaction.custom_id == "verify_button":
            role = discord.utils.get(interaction.guild.roles, id=1295952331933745256)
            if role:
                await interaction.user.add_roles(role)

            await interaction.response.defer()

    @commands.Cog.listener()
    async def on_ready(self):
        guild = self.bot.get_guild(1289017735631867945)
        if not(guild):
            return
        
        channel = discord.utils.get(guild.channels, id=1549575851073605733)
        if not(channel):
            return

        messages = [message async for message in channel.history(limit=1)]
        if len(messages) > 0:
            return

        view = discord.ui.View(timeout=None)
        view.add_item(discord.ui.Button(
            label = "Verify",
            custom_id = "verify_button",
            style = discord.ButtonStyle.green
        ))

        await channel.send("Welcome to Atlantis!", view=view)

async def setup(bot: commands.Bot):
    await bot.add_cog(Events(bot))