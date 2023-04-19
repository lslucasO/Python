from discord import app_commands
from discord.ext import commands
from discord.ext import tasks
import discord



class Verinvites(commands.Cog):
    def __init__(self, client):
        self.client = client


    @app_commands.command(name='invites', description='Abre a lista de players já encontrados pelo bot')
    async def verinvites(self, interaction: discord.Interaction):

        
        filetext = open('invites.txt', 'r') # <-- Armazenando as mensagens de convite
        await interaction.response.send_message(f'**Players já convidados:**')
        await interaction.followup.send(f'```{filetext.read()}```')
            
            




async def setup(client):
    await client.add_cog(Verinvites(client))
