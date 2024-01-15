# -*- coding: utf-8 -*-
# Copyright: sampozki 2020

import discord
import asyncio
import random
import json
import urllib3
import re
import string

import simpsonface
import mau
import hau

client = discord.Client()

banList = ["neekeri", "homo"]

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

    if "neekeri" in message.content.lower():
        await message.channel.send(random.choice(["KUKA HUUS TON?", "KUKA SE OLI?", "KUKA SANO TON ÄSKEN?"]))
        await asyncio.sleep(2)
        await message.delete()
        print(message.content.lower().split(" "))

    elif "hakemus" in message.content.lower():
        if random.randint(0,10) == 8:
            await message.channel.send("hyy-vä")
            await client.change_presence(activity=discord.Game("hyy-vä"))
        else:
            await message.channel.send("tapan sut")
            await client.change_presence(activity=discord.Game("tapan sut"))

    elif "pelaako andy final fantasyä" in message.content.lower():
        await message.channel.send("Pelaa")
    
    elif re.match(r'.*sotd|rotd|fotd.*', message.content.lower()):

        site = ''
        if 'sotd' in message.content.lower():
            site = 'frinkiac'
        elif 'fotd' in message.content.lower():
            site = 'morbotron'
        elif 'rotd' in message.content.lower():
            site = 'masterofallscience'

        if len(message.content) > 5:
            await simpsonface.sendTagFace(message, site, message.content[5:])
        else:
            await simpsonface.sendFace(message, site)

    elif "hyvä botti" in message.content.lower():
        await message.channel.send("Kiitos :3")

    elif "paska botti" in message.content.lower():
        await message.channel.send("Haista vittu!")

    elif re.match(r'^((m+|n+)a+u)|(m+i+u)|(m+(?:ä+|ö+)y)|(m+ä+y)', message.content.lower()):
        if re.match(r'^(((m+|n+)a+u)|(m+i+u)|(m+(?:ä+|ö+)y)|(m+ä+y))2', message.content.lower()):
            await mau.mau2(message)
        else:
            await mau.mau2(message)
        await setstatus(random.choice(["mau","maumau","määäyyyyy","mäymäymäymäyyy"]))
        print("maumau   " + str(message.author.id))

    elif re.match(r'^(?:h+)(?:a+)(?:u+).*', message.content.lower()):
        await hau.hau(message)
        await setstatus(random.choice(["hau","hauhau",]))
        print("hauhau   " + str(message.author.id))

    elif "syawn" in message.content.lower():
        await message.channel.send("https://sampozki.fi/syawn.png")

    elif "yawn" in message.content.lower():
        await message.channel.send("https://sampozki.fi/yawn.png")

    elif "yhteiskun" in message.content.lower():
        await message.channel.send("https://sampozki.fi/yhteiskunta.png")

    elif "swöö" in message.content.lower():
        if "otso" not in str(message.author.roles):
            await message.channel.send("https://sampozki.fi/swöö.png")

    elif "wöö" in message.content.lower():
        if "otso" not in str(message.author.roles):
            await message.channel.send("https://sampozki.fi/soyjak.jpg")

    elif "babbit" in message.content.lower():
        await message.channel.send("https://sampozki.fi/babbit.gif")

    elif "huutispic" in message.content.lower():
        link = "https://prnt.sc/"+random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)
        for a in range(0,4):
            link += str(random.randint(0,9))
        await message.channel.send(link)


client.run(open("env.cfg", "r").read())
