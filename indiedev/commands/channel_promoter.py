from typing import Dict

from discord import Message, CategoryChannel, TextChannel
from discord.ext import commands
from discord.ext.commands import Bot


class ChannelPromoter(commands.Cog):
    def __init__(self, bot):
        self.bot: Bot = bot
        self.hot_category: CategoryChannel = None
        self.fallback_category: CategoryChannel = None
        self.frequency: Dict = {}

    # @commands.Cog.listener()
    # async def on_message(self, ctx):
    #     if ctx.author.bot and self.hot_category is None:
    #         return
    #
    #     if ctx.channel in self.watching:
    #         print("test")
    #         await ctx.channel.send("pong")

    @commands.command(name='link')
    async def link_categories(self, ctx, hot_category: CategoryChannel, fallback_category: CategoryChannel):
        self.hot_category = hot_category
        self.fallback_category = fallback_category
        # Todo: Respond

    @commands.command(name='unlink')
    async def unlink_categories(self, ctx):
        self.hot_category = None
        self.fallback_category = None

    @commands.command(name='sticky')
    async def fix_channel(self, ctx, channel: TextChannel):
        # Todo: implement
        pass

    @commands.command(name='unsticky')
    async def unfix_channel(self, ctx, channel: TextChannel):
        # Todo: implement
        pass
