import discord
import asyncio
import json
import urllib3
import re

async def mau(message):
    response= urllib3.PoolManager().request("GET","http://aws.random.cat/meow")
    data = json.loads(response.data.decode("utf-8"))
    await message.channel.send(str(data["file"]).replace(" ", "%20"))

async def mau2(message):
    response= urllib3.PoolManager().request("GET","https://api.thecatapi.com/v1/images/search")
    data = json.loads(response.data.decode("utf-8"))
    await message.channel.send(str(data[0]["url"]).replace(" ", "%20"))

async def mau3(message):
    await message.channel.send("https://thiscatdoesnotexist.com/")

