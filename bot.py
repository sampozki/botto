# -*- coding: utf-8 -*-
# Copyright: sampozki 2020 - 2025

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

banList = ["neekeri"]

garglList = ["gargl", "_gargl_", "GARGL", "GARGLL............", "Gargl 💀", "come on parti lets go gargli"]

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

    elif "gargl" in message.content.lower():
        if random.randint(0,50) == 3:
            await message.channel.send(random.choice(garglList))
            await client.change_presence(activity=discord.Game("Gargling away"))

    elif "hakemus" in message.content.lower():
        if random.randint(0,10) == 8:
            await message.channel.send("hyy-vä")
            await client.change_presence(activity=discord.Game("hyy-vä"))
        else:
            await message.channel.send("tapan sut")
            await client.change_presence(activity=discord.Game("tapan sut"))
    
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

    elif re.match(r'^motd', message.content.lower()):
        await message.channel.send("https://www.placemonkeys.com/500?random=1")

    elif re.match(r'smotd', message.content.lower()):
        await message.channel.send("https://www.placemonkeys.com/500?spooky&random=1")

    elif "hyvä botti" in message.content.lower():
        await message.channel.send("Kiitos :3")

    elif "paska botti" in message.content.lower():
        await message.channel.send("Haista vittu!")

    elif re.match(r'^(m+(a+u|i+u|ä+y|ö+y|i+a+u|j+ä+y))$', message.content.lower()):
        await mau.mau2(message)
        await setstatus(random.choice(["mau","maumau","määäyyyyy","mäymäymäymäyyy"]))
        print("maumau   " + str(message.author.id))

    elif re.match(r'^(?:h+)(?:a+)(?:u+)$', message.content.lower()):
        await hau.hau(message)
        await setstatus(random.choice(["hau","hauhau",]))
        print("hauhau   " + str(message.author.id))

    elif "yawn" in message.content.lower():
        await message.channel.send("https://sampozki.fi/yawn.png")

    elif "bark" in message.content.lower():
        await message.channel.send("https://sampozki.fi/barkmanul.gif")

    elif "huutispic" in message.content.lower():
        link = "https://prnt.sc/"+random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)
        for a in range(0,4):
            link += str(random.randint(0,9))
        await message.channel.send(link)

    elif re.match(r'^(t+u+(l+i+n|l+e+n|u+n|l+i|u+t|l+e+e|l+e))$', message.content.lower()):
        await message.channel.send("tirsk")


client.run(open("env.cfg", "r").read())
