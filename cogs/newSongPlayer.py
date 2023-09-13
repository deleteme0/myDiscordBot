import discord
from discord.ext import commands

class newSongPlayer(commands.Cog):

    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def playSong(self,ctx,*,songq=[]):
        vclient = None
        VChannel = discord.utils.get(ctx.guild.voice_channels,name = 'General')
        try:
            vclient = await VChannel.connect()
        except:
            pass
            

        print(VChannel.__class__)
        print(vclient.__class__)
        vclient.play(source = discord.FFmpegPCMAudio("/songs/Unravel.mp3"),after= None)


def setup(bot: commands.Bot):
    bot.add_cog(newSongPlayer(bot))