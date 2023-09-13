import discord
from discord.ext import commands
import youtube_dl
import os
import asyncio
from corporalbot import pls_change_presence,reset_presence

i = 0
from discord.ext.commands.core import command
from discord.ext.commands import Bot
#from .constants import *
from corporalbot import get_path
#song_list={ 1 : "coco-pewdiepie.mp3"}

class node():
    def __init__(self,song_name,author):
        self.name = song_name
        self.author = author

class song_queue():
    def __init__(self):
        song_queue.lis = []

    def add(self,song : node,guild):
        song_queue[guild].append(song)
    
    def dequeue(self,guild):
        song_queue[guild].pop(0)
    
    def queue(self,guild):
        try:
            return len(song_queue[guild])
        except:
            return 0




que = asyncio.Queue()
que1= []
class vc(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases = ["s"])
    async def skip(self,ctx):
        voice = discord.utils.get(self.bot.voice_clients,guild = ctx.guild)
        
        if True:
            if que1 == []:
                await ctx.send("EMPTY QUEUE")
            else:
                
                voice.stop()
                
                def after_playing(err):

                    if len(que1) == 0:
                        asyncio.run(reset_presence())

                    elif len (que1) > 0:
                        nex = que1[0]
                        song_name = get_path() + "/songs/" + str(nex)
                        voice.play(source = discord.FFmpegPCMAudio(song_name),after= after_playing)
                        que1.pop(0)
                        nex = nex.strip(".mp3")
                        asyncio.run(pls_change_presence(nex))

                song_name = get_path() + "/songs/" + str(que1[0])
                
                voice.play(source = discord.FFmpegPCMAudio(song_name),after= after_playing)
                
                nex = que1.pop(0)
                nex = nex.strip(".mp3")
                await pls_change_presence(nex)

    @commands.command(aliases = ["c","C"])
    async def connect(self,ctx,channel = 'General'):
        def check1(m):
            return m.channel == ctx.channel and m.author != Bot.user
        
        VChannel = discord.utils.get(ctx.guild.voice_channels,name = channel)
        try:
            await VChannel.connect()
            await ctx.send("Connected to {}".format(channel))
        except:
            await ctx.send("Connection FAILED")




    @commands.command(aliases = ["p","play","P"])
    async def song(self,ctx,*,song_q= None):
        song_list=[]
        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                pass
                #os.remove("song.mp3")
        except PermissionError:
            await ctx.send("Wait for music to end")
        
        def check1(m):
            return m.channel == ctx.channel and m.author != Bot.user
        
        VChannel = discord.utils.get(ctx.guild.voice_channels,name = 'General')
        try:
            await VChannel.connect()
        except:
            pass
        voice = discord.utils.get(self.bot.voice_clients,guild = ctx.guild)
        #voice.stop()
        #try:
        #    await voice.disconnect()
        #except:
        #    await ctx.send("BOT is not connected to anything")
        wait = True
        #if voice.is_connected():
        #    await ctx.send("Already in use , use command .stop and retry")
        #    wait = False
        
        if song_q != None :
            numbas = song_q.split(" ")

        send_cache = "enter a number respective to the song :) \n\n "
        
        no_songs = 0
        i = 1
        no = 1
        if wait:
            for file in os.listdir(get_path()+ "\\songs"):
                if file.endswith(".mp3"):
                    #print(file)
                    #await ctx.send(f"{no} - {file}")
                    #send_cache += f"{no} - {file}" + "\n"
                    send_cache += str(no) + "-   " + str(file).strip(".mp3") + "\n"
                    no +=1
                    song_list.append(file)
                    #os.rename(file,"song.mp3")
        #print(song_list)

        
        if song_q == None:
            await ctx.send(send_cache)
            msg = None
            while wait:
                msg = await self.bot.wait_for("message",check = check1 )
                if msg != None:
                    print(msg.content)
                    numbas = msg.content
                    break
        
        
        for numba in numbas:
            numba = int(numba)
            if 0 < int(numba) < len(song_list)+1:
                choice = int(numba)
                def next_song():
                    global i
                    i +=1
                    song_name = get_path() +"/songs/" + str(i) + ".mp3"
                    voice.play(source = discord.FFmpegPCMAudio(song_name),after=next_song())

                song_name = get_path() + "/songs/" + str(song_list[choice-1])
                print(song_name)

                if voice.is_playing():
                    que1.append(song_list[choice-1])
                    await ctx.send("The song {} has been queued".format(str(song_list[choice-1]).strip(".mp3")))
                else:
                    def after_playing(err):
                        #print(len(que1))
                        if len(que1) == 0:
                            asyncio.run(reset_presence())

                        elif len (que1) > 0:
                            nex = que1[0]
                            nex = str(nex)
                            song_name = get_path() + "/songs/" + str(nex)

                            voice.play(source = discord.FFmpegPCMAudio(song_name),after= after_playing)

                            que1.pop(0)
                            nex = nex.strip(".mp3")
                            asyncio.run(pls_change_presence(nex))

                        print(err)
                    print(voice.__dict__)
                    voice.play(source = discord.FFmpegPCMAudio(song_name),after = after_playing)
                    songg = song_list[choice-1]
                    songg = str(songg)
                    songg= songg.strip(".mp3")
                    print(songg)
                    await pls_change_presence(songg)

            else:
                await ctx.send("ahhhh")

    @commands.command(aliases = ["q",'Q'])
    async def queue(self,ctx):
        send = ""
        if que1 == []:
            await ctx.send("Nothing IN Queue")
        else:
            send = "Queue:\n\n"
            for i in que1:
                send += str(i).strip(".mp3") + "\n"
            await ctx.send(send)

    @commands.command()
    async def connected(self,ctx):
        voice = discord.utils.get(self.bot.voice_clients,guild = ctx.guild)
        if voice.is_playing():
            return True

    @commands.command()
    async def clear(self,ctx):
        que1.clear()
        await ctx.send('Queue Cleared')

    
            
    @commands.command(aliases = ['L','l'])
    async def leave(self,ctx):
        voice = discord.utils.get(self.bot.voice_clients,guild = ctx.guild)
        try:
            await voice.disconnect()
            await reset_presence()
        except:
            await ctx.send("BOT is not connected to anything")

    @commands.command()
    async def pause(self,ctx):
        voice = discord.utils.get(self.bot.voice_clients,guild = ctx.guild)
        if voice.is_playing():
            voice.pause()
            #await reset_presence()
        else:
            await ctx.send("NO audio is playing")
    
    @commands.command()
    async def resume(self,ctx):
        voice = discord.utils.get(self.bot.voice_clients,guild = ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send("The audio is not paused.")
    
    @commands.command()
    async def stop(self,ctx):
        voice = discord.utils.get(self.bot.voice_clients,guild = ctx.guild)
        voice.stop()
        await reset_presence()

def setup(bot: commands.Bot):
    bot.add_cog(vc(bot))