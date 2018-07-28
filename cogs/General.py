import discord
import time
from discord.ext import commands

class General:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        """Gets the info about bot."""
        em=discord.Embed(
            title="The Window Bot",
            description="The Window Bot is a featured moderation bot which you can use to protect your server and to let your moderators use my commands for easier server protection.",
            colour=discord.Colour.green()
        )

        em.add_field(name="Add me to your discord", value="")

        await self.ctx.send(embed=em)


    @commands.command()
    async def ping(self, ctx):
        """Pong!"""
        msg = await self.ctx.send(':thinking: please wait... :thinking:')
        res = msg.created_at - self.ctx.message.created_at
        res = tdm(res)
        em=discord.Embed(title="Pong!", description=f"Latency: {res}ms")
        await msg.edit(embed=em)

def setup(bot):
    bot.add_cog(General(bot))
