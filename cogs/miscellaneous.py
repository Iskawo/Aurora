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
        embed = discord.Embed(
            color=0xafdfeb
            )
        embed.add_field(name = 'Aurora Ping', value = f':stopwatch: My ping is `{round(self.client.latency * 1000)}ms`')
        embed.set_footer(text = "Requested by: " + str(ctx.message.author))
        await ctx.send(embed = embed)


    @commands.command(aliases=['information'])
    async def info(self, ctx):
        ''' - Shows information about the bot.'''
        embed = discord.Embed(
            color=0xafdfeb,
            title = "Aurora Information",
            description = "Here you can find information about me."
            )
        embed.add_field(name = "Owner", value = "<@!286509757546758156> (286509757546758156)", inline = "false")
        embed.add_field(name = "Discord.py version", value = f'[{discord.__version__}](https://discordpy.readthedocs.io/en/latest/)', inline = "false")
        embed.add_field(name = "Python version", value = "[3.7.3 64-bit](https://www.python.org/downloads/release/python-373/)", inline = "false")
        embed.add_field(name = "IDE Used", value = "[Visual Studio Code](https://code.visualstudio.com/)", inline = "false")
        embed.add_field(name = "Message Response Time", value = f'{round(self.client.latency * 1000)}ms', inline=False)
        embed.add_field(name = "Support Server", value = "https://discord.gg/aDHmSk8", inline=False)
        embed.set_image(url="https://i.imgur.com/P1fharf.png")
        await ctx.send(embed = embed)

    
    @commands.command(aliases=["ui"])
    async def userinfo(self, ctx, member: discord.Member = None):
        ''' - Display information about a user.'''
        if member is None:
            return await ctx.send('Please provide a user to get information for.')
        roles = [role for role in member.roles]
        embed = discord.Embed(
            color=0xafdfeb,
            timestamp=ctx.message.created_at
            )
        embed.set_author(name=f"Userinfo - {member}")
        embed.set_thumbnail(url=f"{ctx.me.avatar_url}")
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Nickname:", value=member.nick)
        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Account Created:", value=member.created_at.strftime("%a, %#d %B %Y"))
        embed.add_field(name="Joined Server:", value=member.joined_at.strftime("%a, %#d %B %Y"))
        embed.add_field(name="Top Role:", value=member.top_role.mention)
        embed.add_field(name="Bot?", value=member.bot)
        embed.add_field(name=f'Roles ({len(roles)})', value=" ".join([role.mention for role in roles]))
        await ctx.send(embed = embed)

    
    @commands.command()
    async def help(self, ctx):
        ''' - Help message'''
        author = ctx.author
        embed = discord.Embed(
            color = 0xafdfeb,
            title = "Aurora Help",
            description = "Here you can get information on all available commands.",
            timestamp = ctx.message.created_at
        )
        embed.add_field(name="Prefix", value="My prefix is `-`", inline=False)
        embed.add_field(name="Fun", value="`Pat` - Give someone a pat **[-pat <user>]**\n`Love` - Give someone some love **[-love <user>]**\n`Hug` - Give someone a hug **[-hug <user>]**\n`Slap` - Slap someone **[-slap <user>]**\n`Fight` - Fight someone **[-fight <user>]**", inline=False)
        embed.add_field(name="Miscellaneous", value="`Ping` - Returns the message response time\n`Info` - Gives you information on Aurora\n`Help` - Shows this command\n`Userinfo` - Gives you information on a user **[-userinfo <user>]**", inline=False)
        embed.add_field(name="Moderation", value="`Purge` - Delete a specified amount of messages **[-purge <amount>]**\n`Kick` - Kick a user **[-kick <user>]**\n`Ban` - Ban a user **[-ban <user>]**\n`Unban` - Unban a user **[-unban <user#discrim>]**", inline=False)
        embed.add_field(name="Secret", value="`Eval` - Evaluate code  **[-eval <code>]**\n`Load` - Loads a cog **[-load <cog_name>]**\n`Unload` - Unloads a cog **[-unload <cog_name>]**\n`Reload` - Reloads a cog **[-reload <cog_name>]**", inline=False)
        embed.set_thumbnail(url=ctx.me.avatar_url)
        embed.set_footer(text=f"Requested by: {author}")
        embed.set_image(url="https://i.imgur.com/BkGe9Lj.png")
        await ctx.send(embed = embed)

        

        
def setup(client):
    client.add_cog(Miscellaneous(client))