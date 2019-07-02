import discord
import datetime
import os
import json
import random
import ast
from discord.ext import commands
from discord import Game

class Miscellaneous(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def ping(self, ctx):
        ''' - Return the bots message response time.'''
        embed = discord.Embed()
        embed.add_field(name = 'Aurora Ping', value = f':stopwatch: My ping is `{round(self.client.latency * 1000)}ms`')
        embed.set_footer(text = "Requested by: " + str(ctx.message.author))
        await ctx.send(embed = embed)


    @commands.command(aliases=['information'])
    async def info(self, ctx):
        ''' - Shows information about the bot.'''
        embed = discord.Embed(title = "Aurora Information", description = "Here you can find information about me.")
        embed.add_field(name = "Owner", value = "<@!286509757546758156> (286509757546758156)", inline = "false")
        embed.add_field(name = "Discord.py Version", value = f'{discord.__version__}', inline = "false")
        embed.add_field(name = "Python Version", value = "3.7.3", inline = "false")
        await ctx.send(embed = embed)
    

        
def setup(client):
    client.add_cog(Miscellaneous(client))