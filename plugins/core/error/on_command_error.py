import discord
from discord.ext import commands

import utils


class CommandError(commands.Cog, name="Command Error"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, commands.NoPrivateMessage):
            response = discord.Embed(
                title="⛔ Access denied. This is a server only command.", color=0xBE1931
            )
            return await ctx.author.send(embed=response)

        if isinstance(error, commands.CommandNotFound):
            return

        # Note: New logging system implimented
        utils.log('error', "\nERROR: {}".format(
            error
        ))

def setup(bot):
    bot.add_cog(CommandError(bot))