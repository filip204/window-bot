import discord
import os
from discord.ext import commands

bot=commands.Bot(command_prefix="w.", description="STILL IN DEVELOPMENT")

extensions=['cogs.General', 'cogs.Moderation']

for extension in extensions:
    bot.load_extension(extension)

bot.run(os.environ['TOKEN'])
