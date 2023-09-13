import discord
from discord.ext import commands
import random
import os
import time
import json
import kleann
import sys
bot = commands.Bot(command_prefix='.')

def get_path():
    #return "D:/calvin/corporal_bot_1"
    return os.path.dirname(__file__)

def __init__(self, bot: commands.Bot):
    self.bot = bot

def find(channel):
    with open("channel.txt","r") as f:
        for i in f.readlines():
            if str(channel) in str(i):
                return True
    return False

@bot.event
async def on_ready():
    print('bot is ready.')
    game = discord.Game("with mr.C")
    await bot.change_presence(status=discord.Status.online, activity=game)

async def change_presence(wut : str):
    gamer = discord.Streaming(name = wut,url ="https://www.youtube.com/watch?v=dQw4w9WgXcQ", twitch_name ="BILL DIPPERLY",game ="FORTNITE")
    await bot.change_presence(status=discord.Status.online, activity= gamer)

async def reset_presence():
    game = discord.Game("with mr.C")
    await bot.change_presence(status=discord.Status.online, activity=game)

# @bot.event
# async def on_command_error(ctx, error):
#    if isinstance(error, commands.CommandOnCooldown):
#        await ctx.send(f'This command is on cooldown. Please wait {error.retry_after:.2f}s')
#
#    else:
#        await ctx.send("The command that you used does not exist!")
#@bot.event
#async def on_message(ctx):
#    if find(str(ctx.channel)):
#        await ctx.channel.purge(limit=1)

@bot.command()
async def shut(ctx):
    print(ctx.author.id)
    if ctx.author.id == 528476369152376832 :
        await ctx.send("Yes")
        sys.exit()
    else:
        await ctx.send("No")
@bot.command()
async def tell(ctx,*,q):
    choice = ['yes','no']
    await ctx.send(f"q:{q}\n answer: {random.choice(choice)}")

str = get_path()

for filename in os.listdir(get_path() +"\\cogs"):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('Token')
