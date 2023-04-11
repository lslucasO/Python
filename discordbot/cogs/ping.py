import discord
from discord.ext import commands
import random

class Ping(commands.Cog): # <- Comando que ira ser executado
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener() # <-- Events
    async def on_ready():
        print(f'Ping.py is ready!')


    @commands.command() # <_- Commands
    async def ping(self, ctx, question):
        list_secrets = ['a podridão esta com voce', 'gui é calvo', 'mala noticia mi gente', 'cavalos, cavalos e mais cavalos', '"Mestre, esse cara é o naru"', 'Vou hackear todos vocês']

        message = random.choice(list_secrets)
        await ctx.author.send(message)


async def setup(client):
    await client.add_cog(Ping(client))