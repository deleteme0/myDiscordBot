
import discord
import asyncio


client = discord.Client()

async def main():



    async with client:
        await client.start("NzIwNTU2MDk2NjY5ODc2Mjc3.Xxf8sA.RC1kDn3q8dRFEt4yKaxMZHO4koU")

asyncio.run(main())