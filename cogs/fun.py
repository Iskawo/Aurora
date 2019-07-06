import discord
import random
from discord.ext import commands
from discord import Game

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def pat(self, ctx, member: discord.Member = None):
        ''' - Pat someone :3'''
        if member == ctx.me:
            msg = f'Thank you for the pat, {ctx.author.mention}'
        elif member == ctx.author:
            msg = f'aww... ill pat you. {ctx.me} pats {ctx.author.mention}'
        elif member is not None:
            msg = f'{ctx.author.mention} gave {member.mention} a pat :3'
        else:
            msg = "Please mention user to pat!"
        
        await ctx.send(msg)


    @commands.command()
    async def love(self, ctx, member: discord.Member = None):
        '''
        - Loves someone :3
        '''
        if member == ctx.me:
            msg = f'Thank you for the love, {ctx.author.mention}'
        elif member == ctx.author:
            msg = f'aww... ill love you. {ctx.me} hugs {ctx.author.mention}'
        elif member is not None:
            msg = f'{ctx.author.mention} gave {member.mention} some love <3'
        else:
            msg = "Please mention user to love!"
        
        await ctx.send(msg)


    @commands.command()
    async def hug(self, ctx, member: discord.Member = None):
        ''' - Hugs someone :3'''
        if member == ctx.me:
            msg = f'Thank you for the hug, {ctx.author.mention}'
        elif member == ctx.author:
            msg = f'aww... ill hug you. {ctx.me} hugs {ctx.author.mention}'
        elif member is not None:
            msg = f'{ctx.author.mention} gave {member.mention} a hug :D'
        else:
            msg = "Please mention user to hug!"
        
        await ctx.send(msg)

    @commands.command()
    async def slap(self, ctx, member: discord.Member = None):
        ''' - Slap someone >:3'''
        if member == ctx.me:
            msg = f'{ctx.author.mention}, Nice try :LUL:'
        elif member == ctx.author:
            msg = f'Slapping yourself? :ok:...'
        elif member is not None:
            msg = f'{ctx.author.mention} gave {member.mention} a phat slap'
        else:
            msg = 'Please input a user to slap.'

        await ctx.send(msg)

    @commands.command()
    async def fight(self, ctx, member: discord.Member = None):
        ''' - Fight someone >:3'''
        randomnum = random.randint(1, 1100)
        randomnum2 = random.randint(1, 1100)
        if member == ctx.me:
            msg = f'{ctx.author.mention}, Nice try :LUL:'
        elif member == ctx.author:
            msg = f'Fighting yourself? :WhatTheFuck:...'
        elif member is not None:
            msg = f'{ctx.author.mention} fought {member.mention}.\n`{ctx.author.name}`\'s strength was: **{randomnum}**\n`{member.name}`\'s strength was: **{randomnum2}**'
        else:
            msg = 'Please input a user to slap.'

        await ctx.send(msg)


def setup(client):
    client.add_cog(Fun(client))