import discord

client = discord.Client():
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(seld, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('TOKEN HERE')