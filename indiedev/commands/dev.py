from discord import CategoryChannel
from discord.ext import commands


class DevCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ls')
    async def list_channels(self, ctx):
        global guild
        await ctx.send("Waiting...")
        for group in guild.categories.values():
            await ctx.send(group.name)

    @commands.command(name='move')
    async def move_channel(self, ctx):
        test_cat_to: CategoryChannel = guild.categories[3]
        test_cat_from: CategoryChannel = guild.categories[4]
        await test_cat_from.channels[0].edit(position=0, category=test_cat_to)
