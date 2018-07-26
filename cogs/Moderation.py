import discord
import time
import asyncio
from discord.ext import commands

class Moderation:
    def __init__(self, ctx, bot):
        self.ctx = ctx
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, member: discord.Member, reason):
        """Kicks a member from your discord."""
        try:
            if member is None or reason is None:
                raise InvalidArgument

            if ctx.message.author == member:
                await ctx.send("You can\'t kick yourself.")
                return

            await member.kick()
            await ctx.send("{} has been kicked. Reason: {}".format(ctx.member.mention, reason))

            em=discord.Embed(title="Attention!", description="You were kicked from one of the servers you were in. See the more details below.")
            em.add_field(name="Server", value=ctx.guild)
            em.add_field(name="Moderator", value=ctx.message.author.mention)
            em.add_field(name="Reason", value=reason)
            await member.send(embed=em)

        except InvalidArgument:
            await ctx.send("You must specify a member which you want to kick and a reason for a kick.")
        except Forbidden:
            await ctx.send("You don\'t have permission to use this command")
        except:
            await ctx.send("An unknown error occured.")


def setup(bot):
    bot.add_cog(Moderation(bot))