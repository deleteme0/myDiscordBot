import discord
from discord.ext import commands
import random
import time

from discord.ext.commands.bot import Bot


class tut(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def hello(self,ctx):
        def check1(m):
            return m.channel == ctx.channel and m.author != Bot.user
        
        msg = await self.bot.wait_for('message', check=check1)
        data = str(msg.content)
        await ctx.send(f"hello {data}")
    
        print(msg.author.mention)
        await ctx.send(msg.author.mention)
        print(type(msg))
    
    @commands.command()
    async def check2(self,ctx):

        await ctx.send(f"{dir(ctx)}")

def setup(Bot):
    Bot.add_cog(tut(Bot))
