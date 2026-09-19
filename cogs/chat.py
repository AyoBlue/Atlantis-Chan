from discord.ext import commands
import discord
import ollama

class Chat(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        if self.bot.user in message.mentions:
            async with message.channel.typing():
                prompt = ollama.chat(
                    model = "llama3.2",
                    messages = [
                        {"role": "system", "content": "Respond to the user as a cute anime girl with a playful, teasing, and flirty personality. Keep responses short and sweet."},
                        {"role": "user", "content": message.content}
                    ]
                )
                await message.reply(content=prompt["message"]["content"])

async def setup(bot: commands.Bot):
    await bot.add_cog(Chat(bot))