from discord.ext import commands, tasks
import discord

import brawlhalla

class PatchNotes(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.check_patch_notes.start()

    @tasks.loop(minutes=1)
    async def check_patch_notes(self):
        guild = self.bot.get_guild(1289017735631867945)
        if not(guild):
            return
        
        channel = guild.get_channel(1316958104096739369)
        if not(channel):
            return

        patch_notes = await brawlhalla.get_patch_notes()
        messages = [message async for message in channel.history(limit=10)]

        for patch in patch_notes:
            sent = False
            for message in messages:
                if message.embeds[0] and message.embeds[0].title == patch["title"]:
                    sent = True
                    break

            if sent:
                continue

            info = await brawlhalla.get_patch(patch["slug"])
            if not(info):
                continue

            embed = discord.Embed(
                title = patch["title"],
                url = f"https://cms.brawlhalla.com/patch-notes/{patch['slug']}",
                description = info["yoast_head_json"]["og_description"],
                color = discord.Color.blue()
            )
            embed.set_image(url=patch["featuredImage"])
            embed.set_author(name="Atlantis Chan", icon_url=self.bot.user.avatar.url)
            embed.set_footer(text="Brawlhalla Patch Notes")

            await channel.send(embed=embed)
            
async def setup(bot: commands.Bot):
    await bot.add_cog(PatchNotes(bot))