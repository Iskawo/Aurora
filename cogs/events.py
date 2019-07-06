import discord
import inspect
from discord.ext import commands

class Events(commands.Cog):

    def __init__(self, client):
        self.client = client


    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f'You don\'t have permission to do that!')
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("The command entered is invalid.")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You are missing permissions.')

        raise error


def setup(client):
    client.add_cog(Events(client))