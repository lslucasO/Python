import discord, key, random, os, asyncio
from ossapi import Ossapi, UserLookupKey, GameMode, RankingType

from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True # <-- Intents basicos
client = commands.Bot(command_prefix='+', intents=discord.Intents.all())


DISCORD_API_KEY = key.token # <-- Key do bot

@client.event
async def on_ready():
    await client.tree.sync()
    print(f'{client.user} está online!')



async def load():
    for filename in os.listdir('discordbot/cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')
            print(f'{filename} is ready!')


async def main():
    async with client:
        await load()
        await client.start(DISCORD_API_KEY)


asyncio.run(main())


