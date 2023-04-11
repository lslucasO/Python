import discord, key
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True # <-- Intents basicos
 
DISCORD_API_KEI = key.token # <-- Key do bot


class MyClient(discord.Client):  # <-- Class principal do bot

    async def on_ready(self): 
        print(f'{self.user} esta online!')   

    
    async def on_message(self, message):
        if message.content.startswith('!oi'):
            print(f'oi cara')

        print(f'Message from {message.author}: {message.content} ')

        

client = MyClient(intents=intents)
client.run(DISCORD_API_KEI)