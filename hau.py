import discord
import asyncio
import json
import urllib3
import re

async def hau(message):
    response= urllib3.PoolManager().request("GET","https://random.dog/woof.json")
    data = json.loads(response.data.decode("utf-8"))
    await message.channel.send(data["url"])

