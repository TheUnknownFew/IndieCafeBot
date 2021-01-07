from typing import List, Dict

from discord import ChannelType, Guild, CategoryChannel


class GuildInfo:
    def __init__(self, guild: Guild = None):
        self.guild: Guild = guild
        self.categories: Dict[int, CategoryChannel] = {
            category.id: category for category in guild.channels if category.type == ChannelType.category
        }
