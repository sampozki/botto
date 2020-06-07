# -*- coding: utf-8 -*-
# Copyright: sampozki 2020

import discord
import asyncio
import random

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event  
async def on_message(message):
    if message.author == client.user:
        return
    
    if "hakemus" in message.content.lower():
        if random.randint(0,10) == 8:
            await message.channel.send("hyy-vä")
        else:
            await message.channel.send("tapan sut")


client.run(open("env.cfg", "r").read())