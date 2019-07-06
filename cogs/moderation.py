import discord
import datetime
from discord.ext import commands

def check_perms(guild, author, member, role_perm):
    highest_role = None
    for role in author.roles:
        if role != guild.default_role and role.permissions == role_perm or role.permissions.manage_messages:
            highest_role = role
            break
        if ((highest_role != None and highest_role > member.top_role) or author == guild.owner) and author != member:
            return True
        else:
            return False



class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client
        
        
    @commands.command(aliases=['clear', 'purge'])
    @commands.has_permissions(manage_messages=True)
    async def prune(self, ctx, amount: int):
        deleted = await ctx.channel.purge(limit=amount)
        removed = await ctx.send(f'You have deleted `{len(deleted)}` messages')
        await removed.delete(delay=5)

    @prune.error
    async def prune_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please provide how many messages you\'d like to delete')
        if isinstance(error, commands.BadArgument):
            await ctx.send('You must supply a `number` of messages.')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You are lacking the `MANAGE_MESSAGES` permission.')

        
        
def setup(client):
    client.add_cog(Moderation(client))