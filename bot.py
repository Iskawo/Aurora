import discord
import os
import json
from discord import Game
from discord.ext import commands


config = {}
with open('config.json') as yes:
    config = json.load(yes)

client = commands.Bot(command_prefix = config['prefix'])

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_ready():
    print(client.user.name + " logged in and online!")
    await client.change_presence(activity=discord.Game(name="with new code >:3"))




client.run(config['token'])