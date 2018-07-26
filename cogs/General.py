import discord
import time
from discord.ext import commands

class General:
    def __init__(self, ctx, bot):
        self.ctx = ctx
        self.bot = bot

    @commands.command()
    async def info(ctx):
        """Gets the info about bot."""
        em=discord.Embed(
            title="The Window Bot",
            description="The Window Bot is a featured moderation bot which you can use to protect your server and to let your moderators use my commands for easier server protection.",
            colour=discord.Colour.green()
        )

        em.add_field(name="Add me to your discord", value="")
        em.add_field(name="Submit a bug report", value="")

        await ctx.send(embed=em)


    @commands.command()
    async def ping(ctx):
        """Pong!"""
        msg = await ctx.send(':thinking: please wait... :thinking:')
        res = msg.created_at - ctx.message.created_at
        res = tdm(res)
        em=discord.embed(title="Pong!", description="Latency: {}ms".format(res))
        await msg.edit(embed=em)

def setup(bot):
    bot.add_cog(General(bot))