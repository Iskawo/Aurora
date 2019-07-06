import discord
import os
import json
import asyncio
import random
from discord import Game
from discord.ext import commands


config = {}
with open('config.json') as yes:
    config = json.load(yes)

client = commands.Bot(command_prefix = config['prefix'])
client.remove_command('help')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


async def chng_pr():
    await client.wait_until_ready()
    statuses = ["-help", 'with cute little bunnies', 'with new code >:3']
    while not client.is_closed():
        status = random.choice(statuses)
        await client.change_presence(activity=discord.Game(status))
        await asyncio.sleep(15)


@client.event
async def on_ready():
    print(client.user.name + " logged in and online!")
    #await client.change_presence(activity=discord.Game(name="with cute little bunnies"))


client.loop.create_task(chng_pr())
client.run(config['token'])