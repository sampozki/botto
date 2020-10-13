import discord
import urllib3
import asyncio
import json


async def sendface(message, urll):
    
    response = urllib3.PoolManager().request( "GET", "https://" + urll + ".com/api/random")
    data = json.loads(response.data.decode("utf-8"))

    url = "https://" + urll + ".com/img/" + data['Frame']['Episode'] + "/" + str(data['Frame']['Timestamp']) + ".jpg"
    await message.channel.send(url)
