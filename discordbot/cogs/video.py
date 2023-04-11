import discord
from discord.ext import commands
import random

class Video(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener() # <-- Events
    async def on_ready():
        print(f'Video.py is ready!')

    @commands.command()
    async def video(self, ctx):
        await ctx.send('https://youtu.be/rV5ynCW-kVw')
        print('ambatukammmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')
        



async def setup(client):
    await client.add_cog(Video(client))