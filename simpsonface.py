import discord
import urllib3
import asyncio
import json


async def sendface(message):
    response = urllib3.PoolManager().request( "GET", "https://frinkiac.com/api/random")
    data = json.loads(response.data.decode("utf-8"))

    url = "https://frinkiac.com/img/" + data['Frame']['Episode'] + "/" + str(data['Frame']['Timestamp']) + ".jpg"
    await message.channel.send(url)
