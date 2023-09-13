import discord
from discord.ext import commands 
import random

class embed_test(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('embed test is ready.')

    @commands.command()
    async def embed(self,ctx):
        
        await ctx.send(file=discord.File("tenor.gif")) 
        await ctx.send("get rekt")
    
    @commands.command()
    async def mute(self,ctx):
        voice_client = ctx.guild.voice_client #get bot's current voice connection in this guild
        if not voice_client:  #if no connection...
            return  #probably should add some kind of message for the users to know why nothing is happening here, like ctx.send("I'm not in any voice channel...")
        channel = voice_client.channel #get the voice channel of the voice connection
        people = channel.members #get the members in the channel
        for person in people: #loop over those members
            if person == bot.user: #if the person being checked is the bot...
                continue #skip this iteration, to avoid muting the bot
            await person.edit(mute=True, reason="{} told me to mute everyone in this channel".format(ctx.author))



def setup(bot: commands.Bot):
    bot.add_cog(embed_test(bot))
