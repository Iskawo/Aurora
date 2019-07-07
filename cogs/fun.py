import discord
import random
from discord.ext import commands
from discord import Game

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def pat(self, ctx, member: discord.Member):
        ''' - Pat someone :3'''
        if member == ctx.me:
            msg = f'Thank you for the pat, {ctx.author.mention}'
        elif member == ctx.author:
            msg = f'aww... ill pat you. {ctx.me} pats {ctx.author.mention}'
        else:
            msg = f'{ctx.author.mention} gave {member.mention} a pat :3'        
        await ctx.send(msg)


    @commands.command()
    async def love(self, ctx, member: discord.Member):
        '''
        - Loves someone :3
        '''
        if member == ctx.me:
            msg = f'Thank you for the love, {ctx.author.mention}'
        elif member == ctx.author:
            msg = f'aww... ill love you. {ctx.me} hugs {ctx.author.mention}'
        else:
            msg = f'{ctx.author.mention} gave {member.mention} some love <3'
        await ctx.send(msg)


    @commands.command()
    async def hug(self, ctx, member: discord.Member):
        ''' - Hugs someone :3'''
        if member == ctx.me:
            msg = f'Thank you for the hug, {ctx.author.mention}'
        elif member == ctx.author:
            msg = f'aww... ill hug you. {ctx.me} hugs {ctx.author.mention}'
        else:
            msg = f'{ctx.author.mention} gave {member.mention} a hug :D'
        await ctx.send(msg)

    @commands.command()
    async def slap(self, ctx, member: discord.Member):
        ''' - Slap someone >:3'''
        if member == ctx.me:
            msg = f'{ctx.author.mention}, Nice try :LUL:'
        elif member == ctx.author:
            msg = f'Slapping yourself? :ok:...'
        else:
            msg = f'{ctx.author.mention} gave {member.mention} a phat slap'
        await ctx.send(msg)

    @commands.command()
    async def fight(self, ctx, member: discord.Member):
        ''' - Fight someone >:3'''
        randomnum = random.randint(1, 1100)
        randomnum2 = random.randint(1, 1100)
        if member == ctx.me:
            msg = f'{ctx.author.mention}, Nice try :LUL:'
        elif member == ctx.author:
            msg = f'Fighting yourself? :WhatTheFuck:...'
        else:
            msg = f'{ctx.author.mention} fought {member.mention}.\n`{ctx.author.name}`\'s strength was: **{randomnum}**\n`{member.name}`\'s strength was: **{randomnum2}**'
        await ctx.send(msg)

    
    @pat.error
    async def pat_error(self, ctx, error):
        embed = discord.Embed(color=0xafdfeb, description="**The user you entered was not found**\n\n:information_source: *If the members username has a space, please place the name inside quotation marks;*\n`-pat \"floof person\"`")
        embed2 = discord.Embed(color=0xafdfeb, description="Please provide a user to pat")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed = embed2)
        if isinstance(error, commands.BadArgument):
            return await ctx.send(embed = embed)
    @love.error
    async def love_error(self, ctx, error):
        embed = discord.Embed(color=0xafdfeb, description="**The user you entered was not found**\n\n:information_source: *If the members username has a space, please place the name inside quotation marks;*\n`-love \"floof person\"`")
        embed2 = discord.Embed(color=0xafdfeb, description="Please provide a user to love")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed = embed2)
        if isinstance(error, commands.BadArgument):
            return await ctx.send(embed = embed)
    @hug.error
    async def hug_error(self, ctx, error):
        embed = discord.Embed(color=0xafdfeb, description="**The user you entered was not found**\n\n:information_source: *If the members username has a space, please place the name inside quotation marks;*\n`-hug \"floof person\"`")
        embed2 = discord.Embed(color=0xafdfeb, description="Please provide a user to hug")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed = embed2)
        if isinstance(error, commands.BadArgument):
            return await ctx.send(embed = embed)
    @slap.error
    async def slap_error(self, ctx, error):
        embed = discord.Embed(color=0xafdfeb, description="**The user you entered was not found**\n\n:information_source: *If the members username has a space, please place the name inside quotation marks;*\n`-slap \"floof person\"`")
        embed2 = discord.Embed(color=0xafdfeb, description="Please provide a user to slap")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed = embed2)
        if isinstance(error, commands.BadArgument):
            return await ctx.send(embed = embed)
    @fight.error
    async def fight_error(self, ctx, error):
        embed = discord.Embed(color=0xafdfeb, description="**The user you entered was not found**\n\n:information_source: *If the members username has a space, please place the name inside quotation marks;*\n`-fight \"floof person\"`")
        embed2 = discord.Embed(color=0xafdfeb, description="Please provide a user to fight")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed = embed2)
        if isinstance(error, commands.BadArgument):
            return await ctx.send(embed = embed)


def setup(client):
    client.add_cog(Fun(client))