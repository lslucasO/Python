import discord, key, random, os, asyncio
from ossapi import Ossapi, UserLookupKey, GameMode, RankingType

from discord import app_commands
from discord.ext import commands


client_id = '21582' # <-- oAuth application authorization
client_secret = '8HgI7sfhYL4URYn2jqrXKj64RQ9zxRmQyPm0WW8U'
api = Ossapi(client_id, client_secret) # <-- Registering the API


class Osuid(commands.Cog):
    def __init__(self, client):
        self.client = client

    

    @app_commands.command(name='osuprofile', description='send your osu stats')
    async def osuid(self, interaction: discord.Interaction, profile_name: str):

        user = api.user(profile_name, key=UserLookupKey.USERNAME) # <-- Osu player data

        embed_message = discord.Embed(title=f'Loading status for ``{profile_name}``', description='Osu! stats', color=discord.Color.green())
        embed_message.set_thumbnail(url=user.avatar_url)
        embed_message.add_field(name='osu! Standard', value=f'\n ▸ **Profile ID:** {user.id} \n ▸ **Followers:** {user.follower_count} \n ▸ **Country:** {user.country_code} \n ▸ **join-date:** {user.join_date}', inline=False)


        await interaction.response.send_message(embed=embed_message)
        


async def setup(client):
    await client.add_cog(Osuid(client))
