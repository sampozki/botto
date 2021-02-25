import discord
import urllib3
import asyncio
import json
import random

async def sendface(message, urll):

    response = urllib3.PoolManager().request( "GET", "https://" + urll + ".com/api/random")
    data = json.loads(response.data.decode("utf-8"))

    url = "https://" + urll + ".com/img/" + data['Frame']['Episode'] + "/" + str(data['Frame']['Timestamp']) + ".jpg"
    await message.channel.send(url)


async def sendtagface(message, urll, tag):

    response = urllib3.PoolManager().request( "GET", "https://" + urll + ".com/api/search?q=" + tag)
    data = json.loads(response.data.decode("utf-8"))
    maxindex = len(data)
    randomimage = random.randint(0,maxindex-1)
    url = "https://" + urll + ".com/img/" + data[randomimage]['Episode'] + "/" + str(data[randomimage]['Timestamp']) + ".jpg"
    await message.channel.send(url)
