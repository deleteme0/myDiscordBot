import discord
from discord.ext import commands
import random
import json
import kleann

def check(author):
    with open('money.json', 'r') as f:
        dict = json.load(f)
        if str(author) not in dict:
            dict[str(author)] = 0

            with open('money.json', 'w') as f:
                json.dump(dict, f, indent=2)


async def give_money(ctx, giver, reciever, amount):
    check(giver)
    check(reciever)
    if get_money(giver) > amount or get_money(giver) == amount:
        sub_money(giver, amount)
        add_money(reciever, amount)
        await ctx.send("success")
    else:
        await ctx.send("transaction failed")


def sub_money(author, amount):
    check(author)
    bal = get_money(author)
    rem_sub_amount = 0
    if bal > amount or bal == amount:
        rem_sub_amount = bal - amount
        change_money(author, rem_sub_amount)


def add_money(author, amount):
    check(author)
    bal = get_money(author)
    amount = bal + amount
    change_money(author, amount)


def change_money(author, amount):
    check(author)
    with open('money.json', 'r') as f:
        coin_to_add = json.load(f)

    coin_to_add[str(author)] = amount

    with open('money.json', 'w') as f:
        json.dump(coin_to_add, f, indent=2)


def get_money(author2):
    check(author2)
    with open('money.json', 'r') as f:
        money_table = json.load(f)

    return money_table[str(author2)]


class currency(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('money is ready.')
#
    #@commands.command(alias='gimme_money')  # @commands.cooldown(1,100)
    #async def work(self, ctx):
    #    print("hello")
    #    doer = ctx.author
    #    print(doer)
    #    money_given = int(random.randint(100, 200))
    #    add_money(doer, money_given)
    #    await ctx.send(f'u earned {money_given} coins')
#
    #@commands.command()
    #async def balance(self, ctx):
    #    requester = ctx.author
    #    bal = get_money(requester)
    #    await ctx.send(bal)
#
    #@commands.command()
    #async def give(self, ctx, member: discord.Member, money: int):
    #    giver = ctx.author
    #    reciever = member
    #    await give_money(ctx, giver, reciever, money)

    @commands.command()
    async def start(self,ctx):
        ctx.author = kleann.member()
        await ctx.send("you have joined")
    
    @commands.command()
    async def bal(self,ctx):
        ctx.author.balance()
        


def setup(bot: commands.Bot):
    bot.add_cog(currency(bot))
