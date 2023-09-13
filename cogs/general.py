import discord
from discord.ext import commands
import json

from discord.ext.commands.core import command

class general(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def check(self,ctx):
        await ctx.send("yessir")
        print("yessir")

    @commands.command()
    async def about(self,ctx):
        await ctx.send("Created by C , on 12/6/2020")
        #print(ctx.author)
        #print(ctx.__dict__)
        #author = ctx.author
        #print(author.__dict__)
        #for att in dir(ctx):
         #   print (att, getattr(ctx,att))
        #print(ctx.message.guild.__dict__)



def setup(bot: commands.Bot):
    bot.add_cog(general(bot))
