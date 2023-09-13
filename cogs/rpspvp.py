import discord
from discord.ext import commands
import random

NUM = [1,2,3]

def rnd_gen():
    random.shuffle(NUM)
    return NUM

async def dms(ctx , num_list ,user):
    await user.send(f"{num_list[0]} - rock \n {num_list[1]} - paper \n {num_list[2]} - scissor" )

def rps_answer(num_list , number: int):
    no = 0
    if number == int(num_list[0]):
        no = 1
    elif number == int(num_list[1]):
        no = 2
    elif number == int(num_list[2]):
        no = 3
    return no

async def winner(ctx,p1,p2,p1c,p2c):
    a = p1c
    b = p2c

    if b == 1 and a == 3:
        await ctx.send(f"{p1.mention} won")
    elif b == 2 and a == 1:
        await ctx.send(f"{p1.mention} won")
    elif b == 3 and a == 2:
        await ctx.send(f"{p1.mention} won")
    else:
        await ctx.send(f"{p2.mention} won")
    
class rpspvp(commands.Cog):
    def _init_(self, Bot):
        self.Bot = Bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('rpspvp is ready')

    @commands.command()
    async def rps(self, ctx):
        await ctx.send("enter join to join the game!")
        wait = True
        author = ctx.author
        opponent = None
        def check(m):
            return m.channel == ctx.channel
        
        def check1(m):
            return m.channel == ctx.channel and (m.author in remain)

        while wait:
            msg = await self.Bot.wait_for('message', check=check)
            if msg.content in ["accept", 'join']:
                wait = False
                opponent = msg.author
        author_num=rnd_gen()
        opp_num=rnd_gen()
            
        remain = [author,opponent]

        await dms(ctx,author_num,author)
        await dms(ctx,opp_num,opponent)

        auth_choice = opp_choice = None

        wait_for_action = True
        while wait_for_action:
            choice =  await self.Bot.wait_for('message', check=check1)
            if choice.author == author:
                auth_choice = choice.content()
            elif choice.author == opponent:
                opp_choice = choice.content()
            remain.remove(choice.author)
            if remain == []:
                wait_for_action = False
        auth_main = rps_answer(author_num,auth_choice)
        opp_main = rps_answer(opp_num,opp_choice)

        await winner(ctx,author,opponent,auth_main,opp_main)


def setup(Bot):
    Bot.add_cog(rpspvp(Bot))
