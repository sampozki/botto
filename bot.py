# -*- coding: utf-8 -*-
# Copyright: sampozki 2020

import discord
import asyncio
import random

import simpsonface

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
            await client.change_presence(activity=discord.Game("hyy-vä"))
        else:
            await message.channel.send("tapan sut")
            await client.change_presence(activity=discord.Game("tapan sut"))

    elif "pelaako andy final fantasyä" in message.content.lower():
        await message.channel.send("Pelaa")

    elif "pakkaako andy" in message.content.lower():
        await message.channel.send(random.choice(["Joo", "Kyllä", "Ikävä kyllä"]))

    elif "sotd" in message.content.lower():
        await simpsonface.sendface(message, "frinkiac")
    
    elif "fotd" in message.content.lower():
        await simpsonface.sendface(message, "morbotron")


client.run(open("env.cfg", "r").read())
