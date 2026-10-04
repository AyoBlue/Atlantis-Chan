from discord.ext import commands
import discord

REGION_ROLES = {
    "use": 1556417920488308858,
    "usw": 1556417926918053988,
    "eu": 1556417931179593769,
    "sea": 1556417934942019584,
    "brz": 1556417938918080654,
    "aus": 1556417941719883866,
    "jpn": 1556417944387321887,
    "saf": 1556417947050704916,
    "me": 1556417949441720411
}

GAME_ROLES = {
    "brawlhalla": 1556417761469800458,
    "minecraft": 1556417768083955712,
    "roblox": 1556441213949706301,
    "among_us": 1556417771695378505
}

BRAWLHALLA_ROLES = {
    "tin": 1556417887919546451,
    "bronze": 1556417831644569690,
    "silver": 1556417811633672322,
    "gold": 1556417808324239440,
    "platinum": 1556417805417447554,
    "diamond": 1556417802347348119,
    "valhallan": 1556417792985534474
}

class SelfRoles(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        if not(interaction.type == discord.InteractionType.component):
            return

        value_list = next(iter(interaction.data.values()))

        guild_roles = interaction.guild.roles
        roles: list[discord.Role]
        exception_list: list[discord.Role]

        if interaction.custom_id == "brawlhalla_roles":
            roles = [discord.utils.get(guild_roles, id=BRAWLHALLA_ROLES[value_list[0]])]
            exception_list = [discord.utils.get(guild_roles, id=role_id) for role_id in BRAWLHALLA_ROLES.values() if role_id != roles[0].id]
        elif interaction.custom_id == "game_roles":
            roles = [discord.utils.get(guild_roles, id=role_id) for key, role_id in GAME_ROLES.items() if key in value_list]
            exception_list = [discord.utils.get(guild_roles, id=role_id) for role_id in GAME_ROLES.values() if role_id not in [role.id for role in roles]]
        elif interaction.custom_id == "region_roles":
            roles = [discord.utils.get(guild_roles, id=REGION_ROLES[value_list[0]])]
            exception_list = [discord.utils.get(guild_roles, id=role_id) for role_id in REGION_ROLES.values() if role_id != roles[0].id]
        else:
            return

        await interaction.response.defer(thinking=True, ephemeral=True)

        await interaction.user.remove_roles(*exception_list)
        await interaction.user.add_roles(*roles)

        await interaction.followup.send("Your roles have been updated!")
    
async def setup(bot: commands.Bot):
    await bot.add_cog(SelfRoles(bot))