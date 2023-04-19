import discord, random, os, asyncio
from ossapi import Ossapi, UserLookupKey, GameMode, RankingType, Cursor

from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True # <-- Intents basicos
client = commands.Bot(command_prefix='+', intents=discord.Intents.all())




client_id = '21582'
client_secret = '8HgI7sfhYL4URYn2jqrXKj64RQ9zxRmQyPm0WW8U'
callback_url = 'http://localhost:727/'

api = Ossapi(client_id, client_secret, callback_url)


DISCORD_API_KEY = 'MTA5NTA5ODE3Mzc1MzY3NTg3OQ.GHmGIT.gA0A0PwpQGLC0nF_U8mJiCB8WEbHCEloV59hgY' # <-- Key do bot

@client.event
async def on_ready():
    await client.tree.sync()
    print(f'{client.user} está online!')
 

async def load():   
    for filename in os.listdir('D:/Estudos VSCODE/python/discordbot/cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')
            print(f'{filename} is ready!')


async def main():
    async with client:
        await load()
        await client.start(DISCORD_API_KEY)


asyncio.run(main()) 