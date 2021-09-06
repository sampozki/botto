import discord
import asyncio
import json
import urllib3
import re

async def mau(message):
    try:
        response= urllib3.PoolManager().request('GET','http://aws.random.cat/meow')
        data = json.loads(response.data.decode('utf-8'))

        

        await message.channel.send(str(data['file']).replace(' ', '%20'))
    except Exception as e:
        print(e)
        await mau2(message)

async def mau2(message):
    response= urllib3.PoolManager().request("GET","https://api.thecatapi.com/v1/images/search")
    data = json.loads(response.data.decode("utf-8"))

    responseUrl = str(data[0]["url"]).replace(" ", "%20")
    if responseUrl == "https://cdn2.thecatapi.com/images/sqb5Hk8Ck.jpg":
        responseUrl = 'Pahan mielen grumpy cat'
        await message.channel.send(responseUrl)
        await mau2(message)
        return
    await message.channel.send(responseUrl)

async def mau3(message):
    await message.channel.send("https://thiscatdoesnotexist.com/")

