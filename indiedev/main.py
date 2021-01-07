import discord
from discord import CategoryChannel
from discord.ext import commands

from commands.dev import DevCommands
from indiedev.commands.channel_promoter import ChannelPromoter
from indiedev.data.guild import GuildInfo

bot_inst = commands.Bot(command_prefix='')


class IndieBot(commands.Cog):
    def __init__(self, cmd_prefix: str):
        bot_inst.command_prefix = cmd_prefix

    @bot_inst.listen(name='on_ready')
    async def init_routine(self):
        bot_inst.add_cog(DevCommands(bot_inst))
        bot_inst.add_cog(ChannelPromoter(bot_inst))


def setup(bot: commands.Bot):
    bot.add_cog(IndieBot('!'))


def start():
    import json
    with open("../token.json") as token_file:
        token = json.load(token_file)['token']
    bot_inst.run(token)


if __name__ == '__main__':
    start()
