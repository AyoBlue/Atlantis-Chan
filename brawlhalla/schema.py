from datetime import datetime

class GuildSchema:
    def __init__(self, data: dict):
        self.guild_id: int = data["guild_id"]
        self.name: str = data.get("name", "")
        self.rank: int = data.get("rank", 0)
        self.xp: int = data.get("xp", 0)
        self.create_date: int = data.get("create_date", 0)
        self.member_count: int = data.get("member_count", 0)
        self.tags: list[str] = data.get("tags", [])

class Player:
    def __init__(self, data: dict):
        self.brawlhalla_id: int = data.get("brawlhalla_id") or data.get("id")
        self.username: str = data.get("name", data.get("username", ""))

class GuildMember(Player):
    def __init__(self, data: dict):
        super().__init__(data)
        self.guild_id: int = data["guild_id"]
        self.rank: str = data.get("rank", "")
        self.join_date: int = data.get("join_date", 0)
        self.xp: int = data.get("xp", 0)
        self.guild_points: int = data.get("guild_points", 0)

class GuildPlayer:
    def __init__(self, data: dict):
        self.guild_id: int = data["guild_id"]
        self.guild_name: str = data.get("guild_name", "None")
        self.personal_xp: int = data["personal_xp"]
        self.personal_xp_this_week: int = data["personal_xp_this_week"]
        self.personal_points: int = data["personal_points"]
        self.join_date: datetime = datetime.fromtimestamp(data["join_date"])
        self.rank: str = data["rank"]