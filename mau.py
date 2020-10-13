import discord
import asyncio
import json
import urllib3
import re

async def mau(message):
    response= urllib3.PoolManager().request("GET","http://aws.random.cat/meow")
    data = json.loads(response.data.decode("utf-8"))
    await message.channel.send(str(data["file"]))

