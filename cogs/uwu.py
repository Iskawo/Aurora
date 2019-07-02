import discord
from discord.ext import commands
from discord import Game

class UwU(commands.Cog):

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


def setup(client):
    client.add_cog(UwU(client))