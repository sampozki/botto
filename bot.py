# -*- coding: utf-8 -*-
# Copyright: sampozki 2020

import discord
import asyncio
import random
import json
import urllib3
import re

import simpsonface
import mau

client = discord.Client()



async def setstatus(status):
    await client.change_presence(activity=discord.Game(str(status)))


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event  
async def on_message(message):
    if message.author == client.user:
        return
    
    if "Horny Jail" in str(message.author.roles):
        await message.channel.send("BONK!")
        return

    elif "hakemus" in message.content.lower():
        if random.randint(0,10) == 8:
            await message.channel.send("hyy-vä")
            await client.change_presence(activity=discord.Game("hyy-vä"))
        else:
            await message.channel.send("tapan sut")
            await client.change_presence(activity=discord.Game("tapan sut"))

    elif "pelaako andy final fantasyä" in message.content.lower():
        await message.channel.send("Pelaa")
    
    elif "sotd" in message.content.lower():
        await simpsonface.sendface(message, "frinkiac")
    
    elif "fotd" in message.content.lower():
        await simpsonface.sendface(message, "morbotron")
        
    elif "rotd" in message.content.lower():
        await simpsonface.sendface(message, "masterofallscience")

    elif "hyvä botti" in message.content.lower():
        await message.channel.send("Kiitos :3")

    elif "paska botti" in message.content.lower():
        await message.channel.send("Haista vittu!")
    
    elif re.match(r'.*m+(?:a+|ä+|i+|ö+)(?:u+|y+)2.*', message.content.lower()):
        await mau.mau2(message)
        await setstatus(random.choice(["mau","maumau","määäyyyyy","mäymäymäymäyyy"]))
        print("maumau   " + str(message.author.id))

    elif re.match(r'.*m+(?:a+|ä+|i+|ö+)(?:u+|y+).*', message.content.lower()):
        await mau.mau(message)
        await setstatus(random.choice(["mau","maumau","määäyyyyy","mäymäymäymäyyy"]))
        print("maumau   " + str(message.author.id))
   
    elif "syawn" in message.content.lower():
        await message.channel.send("https://sampozki.fi/syawn.png")

    elif "yawn" in message.content.lower():
        await message.channel.send("https://sampozki.fi/yawn.png")
    
    elif "yhteiskun" in message.content.lower():
        await message.channel.send("https://sampozki.fi/yhteiskunta.png")

    # await client.change_presence(activity=discord.Game("Hyvää joulua!"))

client.run(open("env.cfg", "r").read())
