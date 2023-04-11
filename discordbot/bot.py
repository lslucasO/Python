import discord, key
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

DISCORD_API_KEY = key.token


@client.event
async def on_ready():
    print(f'{client.user} esta online!')



client.run(DISCORD_API_KEY)