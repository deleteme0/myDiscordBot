import discord
from discord.ext import commands
import random


def addnote(message):
    f = open("feedback.txt", 'a')
    f.write(message + '\n')
    f.close()


async def retrive(ctx):
    f = open('feedback.txt', 'r')
    no = str("1")
    for i in f.readlines():
        no = str(no)
        await ctx.send(no + '.' + '  ' + i)
        no = int(no) + 1


class feedback(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def report(self, ctx, message):
        if message is None:
            await ctx.send('please enter a message')

        else:
            addnote(message)
            await ctx.send("thank you for reporting!")

    @commands.command(alias='retrieve')
    async def feedbacks(self, ctx):
        await retrive(ctx)


def setup(bot: commands.Bot):
    bot.add_cog(feedback(bot))
