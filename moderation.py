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
        if amount < 1:
            return await ctx.send('You can\'t delete less than 1 message.')
        elif amount == 1:
            deleted = await ctx.channel.purge(limit=amount)
            removed = await ctx.send(f'You have deleted `{len(deleted)}` message')
            return await removed.delete(delay=5)
        else:
            deleted = await ctx.channel.purge(limit=amount)
            removed = await ctx.send(f'You have deleted `{len(deleted)}` messages')
            return await removed.delete(delay=5)


    @commands.command(aliases=['yeet'])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f':white_check_mark: `{member} ({member.id})` has been kicked.')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f':white_check_mark: `{member} ({member.id})` has been banned.')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f':white_check_mark: `{user} ({user.id})` has been unbanned.')
                return


    @prune.error
    async def prune_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send('Please provide how many messages you\'d like to delete')
        if isinstance(error, commands.BadArgument):
            return await ctx.send('You must supply a `number` of messages.')
        if isinstance(error, commands.MissingPermissions):
            return await ctx.send('You are lacking the `MANAGE_MESSAGES` permission.')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send('Please provide a user to kick.')
        if isinstance(error, commands.MissingPermissions):
            return await ctx.send('You are lacking the `KICK_MEMBERS` permission.')
        if isinstance(error, commands.CommandInvokeError):
            return await ctx.send('You are unable to kick this user.')
        if isinstance(error, commands.BadArgument):
            return await ctx.send('The member you entered is invalid.')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send('Please provide a user to ban.')
        if isinstance(error, commands.MissingPermissions):
            return await ctx.send('You are lacking the `BAN_MEMBERS` permission.')
        if isinstance(error, commands.CommandInvokeError):
            return await ctx.send('You are unable to ban this user.')
        if isinstance(error, commands.BadArgument):
            return await ctx.send('The member you entered is invalid.')

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send('Please provide a user to unban.')
        if isinstance(error, commands.MissingPermissions):
            return await ctx.send('You are lacking the `BAN_MEMBERS` permission.')
        if isinstance(error, commands.CommandInvokeError):
            return await ctx.send('You must supply the user in the format: `username#discriminator`')
        if isinstance(error, commands.BadArgument):
            return await ctx.send('The member you entered is invalid.')


        
        
def setup(client):
    client.add_cog(Moderation(client))