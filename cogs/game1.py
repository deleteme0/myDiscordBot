import discord
from discord.ext import commands
import random


async def rps_answer(ctx, number):
    no = ' '
    if number == 1:
        no = 'rock'
    elif number == 2:
        no = 'paper'
    elif number == 3:
        no = 'scissor'
    await ctx.send(f'DEFEAT , bot chose {no}')


class game1(commands.Cog):
    def _init_(self, Bot):
        self.Bot = Bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('rps is ready')

    @commands.command()
    async def rps_bot(self, ctx, arg):
        a = random.randint(1, 3)
        b = 0
        if arg == 'r' or arg == 'rock':
            b = 1
        elif arg == 'p' or arg == 'paper':
            b = 2
        elif arg == 's' or arg == 'scissor':
            b = 3
        else:
            await ctx.send("u typed wrong uwu")
            return
        if b != 0:
            if b == 1 and a == 3:
                await ctx.send("bot chose scissors, YOU WIN!!")
            elif b == 2 and a == 1:
                await ctx.send("bot chose rock, YOU WIN!!")
            elif b == 3 and a == 2:
                await ctx.send("bot chose paper, YOU WIN!!")
            else:
                await rps_answer(ctx, a)



def setup(Bot):
    Bot.add_cog(game1(Bot))
