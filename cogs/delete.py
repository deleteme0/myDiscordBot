import discord
from discord.ext import commands
import random
import time

from discord.ext.commands import Bot


def add(channel_name):
    with open("channels.text", "a") as f:
        f.write("\n" + str(channel_name))


def remove(channel):
    file = ""
    with open("../channel.txt", "r") as f:
        for i in f.readline():
            if str(channel) in i:
                continue
            file += str(i)

    with open("../channel.txt", "w") as f:
        f.write(file)


class delete(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def pmess(self, ctx, time):
        print(ctx.channel)
        add(str(ctx.channel))
        time.sleep(int(time))
        remove(str(ctx.channel))


def setup(bot: commands.Bot):
    bot.add_cog(delete(bot))
