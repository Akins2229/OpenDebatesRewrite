import discord
from discord.ext import commands

import utils

class Login(commands.Cog, name="Login"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Logged in as: {0}, {1}".format(
            self.bot.user.name,
            self.bot.user.id
        ))

        # Note: new logging system implimented
        utils.log('info', "Logged in as: {0}, {1}".format(
            self.bot.user.name,
            self.bot.user.id
        ))

        await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching, name="over Debates"
            )
        )


def setup(bot):
    bot.add_cog(Login(bot))