import discord
import inspect
from discord.ext import commands

class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    # @commands.Cog.listener()
    # async def on_command_error(self, ctx, error):
    #     if isinstance(error, commands.CommandNotFound):
    #         return
    #     if isinstance(error, commands.MissingPermissions):
    #         return

    #     raise error


def setup(client):
    client.add_cog(Events(client))