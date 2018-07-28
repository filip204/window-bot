import discord
import time
import asyncio
from discord.ext import commands

class Moderation:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason):
        """Kicks a member from your discord."""
        if ctx.message.author == member:
            await self.ctx.send(f"{self.ctx.message.author.mention}, you can\'t kick yourself.")
            return
        try:

            await member.kick()
            await self.ctx.send("{} has been kicked. Reason: {}".format(ctx.member.mention, reason))

            em=discord.Embed(title="Attention!", description="You were kicked from one of the servers you were in. See the more details below.")
            em.add_field(name="Server", value=self.ctx.guild)
            em.add_field(name="Moderator", value=self.ctx.message.author.mention)
            em.add_field(name="Reason", value=reason)
            await member.send(embed=em)

        except InvalidArgument:
            await self.ctx.send("You must specify a member which you want to kick and a reason for a kick.")
        except Forbidden:
            await self.ctx.send("You don\'t have permission to use this command")
        except:
            await self.ctx.send("An unknown error occured.")


def setup(bot):
    bot.add_cog(Moderation(bot))
