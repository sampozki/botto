# import commands as commands

import praw
import asyncio
import configparser
import random

class Reddit():
    def __init__(self):

        cfg = configparser.ConfigParser()
        cfg.read('reddit.cfg')

        self.__reddit = praw.Reddit(client_id=cfg['REDDIT']['id'], 
                                    client_secret=cfg['REDDIT']['secret'], 
                                    user_agent='FuzuBot',
                                    check_for_async=False)

        print('Read only Reddit: ', self.__reddit.read_only)


    async def messageHandler(self, message, client):
        splitted = message.content.split(" ")

        if len(splitted) > 1:
            await self.getPost(message, client, splitted[1])
        else:
            await self.getPost(message, client, 'floppa')


    async def getPost(self, message, client, subreddit):

        posti = []
        postia = []

        try:
            for submission in self.__reddit.subreddit(subreddit).new(limit=6):
                posti.append(submission.url)
                postia.append(submission.title)

            for submission in self.__reddit.subreddit(subreddit).hot(limit=6):
                posti.append(submission.url)
                postia.append(submission.title)

            a = random.randint(0, len(posti) - 1)
            postiaa = postia[a]
            postii = posti[a]

            # await commands.sendMsg(str(postiaa), message)
            await message.channel.send(str(postiaa))

            # await commands.sendMsg(str(postii), message)
            await message.channel.send(str(postii))
            

        except Exception as E:
            print(E)
            # await commands.sendMsg('Im sorry, something went wrong ,-,', message)
            await message.channel.send('Im sorry, something went wrong ,-,')
