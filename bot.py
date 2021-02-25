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
import hau

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
        if len(message.content) > 5:
            await simpsonface.sendtagface(message, "frinkiac", message.content[5:])
        else:
            await simpsonface.sendface(message, "frinkiac")

    elif "fotd" in message.content.lower():
        if len(message.content) > 5:
            await simpsonface.sendtagface(message, "morbotron", message.content[5:])
        else:
            await simpsonface.sendface(message, "morbotron")

    elif "rotd" in message.content.lower():
        if len(message.content) > 5:
            await simpsonface.sendtagface(message, "masterofallscience", message.content[5:])
        else:
            await simpsonface.sendface(message, "masterofallscience")

    elif "hyvä botti" in message.content.lower():
        await message.channel.send("Kiitos :3")

    elif "paska botti" in message.content.lower():
        await message.channel.send("Haista vittu!")

    elif re.match(r'.*(?:m+|n+)(?:a+|ä+|i+|ö+)(?:u+|y+|a+)2.*', message.content.lower()):
        await mau.mau2(message)
        await setstatus(random.choice(["mau","maumau","määäyyyyy","mäymäymäymäyyy"]))
        print("maumau   " + str(message.author.id))

    elif re.match(r'.*(?:m+|n+)(?:a+|ä+|i+|ö+)(?:u+|y+|a+).*', message.content.lower()):
        await mau.mau(message)
        await setstatus(random.choice(["mau","maumau","määäyyyyy","mäymäymäymäyyy"]))
        print("maumau   " + str(message.author.id))

    elif re.match(r'.*(?:h+)(?:a+)(?:u+).*', message.content.lower()):
        await hau.hau(message)
        await setstatus(random.choice(["hau","hauhau",]))
        print("hauhau   " + str(message.author.id))

    elif "syawn" in message.content.lower():
        await message.channel.send("https://sampozki.fi/syawn.png")

    elif "yawn" in message.content.lower():
        await message.channel.send("https://sampozki.fi/yawn.png")

    elif "yhteiskun" in message.content.lower():
        await message.channel.send("https://sampozki.fi/yhteiskunta.png")

    elif "wöö" in message.content.lower():
        await message.channel.send("https://sampozki.fi/soyjak.jpg")

    elif "babbit" in message.content.lower():
        await message.channel.send("https://sampozki.fi/babbit.gif")

    # await client.change_presence(activity=discord.Game("Hyvää joulua!"))

client.run(open("env.cfg", "r").read())
