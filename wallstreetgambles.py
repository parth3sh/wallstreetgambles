import discord
import os
import wsbscraper as wsb

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(wsb.run(1, "wallstreetbets", 5))
        

client.run("ODE1ODY1MjU1MzUxMTU2Nzg3.YDynug.AITkYpPTTHS9ygY8P0vLdiDkhXs")