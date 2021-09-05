import discord
from discord.ext import commands

from discord_slash import SlashCommand

import os

bot = commands.Bot(
    command_prefix="$", # Note: this shouldn't really be used as we won't be using any non-slash commands
    self_bot=False, #relatively useless, just a precaution,
    help_command=None, #we won't be using a help command as is
    owner_ids = [
        177766066728992768, #   Clincoin#6668
        393213862620430336, #   Taven#0001
        707643377621008447  #   Akins#1692
    ],
    case_insensitive=True,
    strip_after_whitespae=True,
    description="Automated debate server bot."
)

#intitialize slash commands
slash = SlashCommand(bot)

def main():
    extensions = [
        'plugins.core.error.on_command_error', # error handling
        'plugins.core.startup.on_ready' # login message
    ]
    for extension in extensions:
        bot.load_extension(extension)

    bot.run(os.getenv("TOKEN"))

if __name__ == "__main__":
    main()