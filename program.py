import discord
from discord.ext import commands

import time
import asyncio
import aiohttp
import traceback
import urllib
import json
import io
import os
import string

client = commands.Bot(command_prefix="w.", description="")
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f'with {len(client.guilds)} discords'))

@client.command()
async def help(ctx):
    await ctx.send(':no_entry: **[THE HELP COMMAND IS CURRENTLY UNDER CONSTRUCTION]**')

@client.command(aliases=['pingtime'])
async def ping(ctx):
    '''Call the bot'''
    message = await ctx.send(':time: **Recognizing the ping time, please wait...**')
    res = message.created_at - ctx.message.created_at
    res = tdm(res)
    await message.edit(content=f':heavy_check_mark: __**Pingtime:__**`{res}ms`')
    
@client.command(aliases=['wiki'])
    async def wikipedia(ctx, *, anything):
            '''Search for something on wikipedia.'''
            wew=urllib.request.pathname2url(anything)
            f=await getjson(f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&indexpageids=1&redirects=1&explaintext=1&exsectionformat=plain&titles={wew}")
            query=f['query']
            pageids=query['pageids']
            title=list(query['pages'].values())[0]['title']
            extract=list(query['pages'].values())[0]['extract']
            await ctx.send(embed=discord.Embed(title=title,description=extract[:max(list(filter(lambda x:x<1980,find(". ",extract))))],colour=ctx.author.colour))

@client.command(name='eval')
    async def _eval(self, ctx, *, body: str):
        '''Execute some code with pytrhon [BOT OWNER / ADMIN ONLY]'''
        if ctx.author.id != 361948178573950985:
            return
        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'server': ctx.guild,
            'message': ctx.message,
            '_': self._last_result,
        }
        env.update(globals())
        body = self.cleanup_code(body)
        stdout = io.StringIO()
        to_compile = 'async def func():\n%s' % textwrap.indent(body, '  ')
        try:
            exec(to_compile, env)
        except SyntaxError as e:
            return await ctx.send(self.get_syntax_error(e))
        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            await ctx.message.add_reaction('\u274C')
            value = stdout.getvalue()
            await ctx.send('
py\n{}{}\n
'.format(value, traceback.format_exc()))
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction('\u2705')
            except:
                pass
            sendable=""
            if ret is None:
                if value:
                    sendable=value
            else:
                self._last_result = ret
                sendable=str(value)+str(ret)
            for i in range(len(sendable)//1900):
                await ctx.send('
py\n'+sendable[i1990:(i+1)1990]+'\n
')
            await ctx.send('
py\n'''+sendable[len(sendable)//1990:]+'\n
')
