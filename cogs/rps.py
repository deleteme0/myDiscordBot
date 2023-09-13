import discord
from discord.ext import commands
from discord.ext.commands.bot import Bot
import random

from discord.ext.commands.core import check


class rps(commands.Cog):

    def  __init__(self,client:commands.Bot):
        self.client=client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online.") 
   
    @commands.command()
    async def start_rps(self,ctx,name):
        await ctx.send(f"Hello, {name} ,Lets play ROCK,PAPER,SCISSORS!!\nIam your opponent for today's match\nThe rules are simple:\nType 1 for rock\nType 2 for paper\nType 3 for scissors\nType 4 to view score\nType 5 to exit\nThat's it")
        await ctx.send(f'Type ?ch to enter ur choice')
    
    @commands.command()
    async def ch(self,ctx,number: int):
        a=("rock","paper","scissors")
        i=random.choice(a)
        p1=p2=0
        def check1(m):
            return m.author == ctx.author
        while True:
            msg = await self.client.wait_for("message",check=check1)
            number = int(msg.content)
            i=random.choice(a)
            if number ==1:
                if i=='rock':
                    await ctx.send("The opponent chose rock")
                    await ctx.send("It's a draw")
                elif i=='paper':
                    await ctx.send("The opponent chose paper")
                    await ctx.send("The opponent won")
                    p2+=1
                elif i=='scissors':
                    await ctx.send("The opponent chose scissors")
                    await ctx.send("You won")
                    p1+=1
            elif number ==2:
                if i=='rock':
                    await ctx.send("The opponent chose rock")
                    await ctx.send("You won")
                    p1+=1
                elif i=='paper':
                    await ctx.send("The opponent chose paper")
                    await ctx.send("It's a draw")
                elif i=='scissors':
                    await ctx.send("The opponent chose scissors")
                    await ctx.send("The opponent won")
                    p2+=1
            elif number ==3:
                if i=='rock':
                    await ctx.send("The opponent chose rock")
                    await ctx.send("The opponent won")
                    p2+=1
                elif i=='paper':
                    await ctx.send("The opponent chose paper")
                    await ctx.send("You won")
                    p1+=1   
                elif i=='scissors':
                    await ctx.send("The opponent chose scissors")
                    await ctx.send("It's a draw") 
            elif number ==4:
                    await ctx.send(f"Your score= {p1}\nOpponent's score= {p2}")
            elif number ==5:
                    await ctx.send('bye bye')
                    break
            else:
                await('Wrong choice!!')


    async def hello(self,ctx):
        def check1(m):
            return True

        msg = await self.client.wait_for('message', check=check1)
        data = str(msg.content)
        await ctx.send(f'hello {data}')

        print(msg)
        print(type(msg))    

def setup(client):
    client.add_cog(rps(client))
