import discord, random, os, asyncio
from ossapi import Ossapi, Scope, UserLookupKey, GameMode, RankingType, Cursor
import requests, json, random


from discord import app_commands
from discord.ext import commands


client_id = '21582' # <-- oAuth application authorization
client_secret = '8HgI7sfhYL4URYn2jqrXKj64RQ9zxRmQyPm0WW8U'
api = Ossapi(client_id, client_secret) # <-- Registering the API



class Getplayer(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    
    @app_commands.command(name='6digitos', description='Puxa os 6 digitos BR ativos no osu!')
    async def getplayer(self, interaction: discord.Interaction, quantos_players:int):
        
        self.page = random.randint(80, 140)
        self.cursor = Cursor(page=self.page) # <-- Select the page of Users
        self.top = api.ranking(GameMode.OSU, RankingType.PERFORMANCE)
        self.top = api.ranking('osu', 'performance', country='br', cursor=self.cursor) # <-- Filtering by country, performance and page
        
        self.quantos_players = quantos_players
        
        self.index = 0
        self.player_list = [[], [], []]
        self.lista_convidados = []
        

        for self.index in range(len(self.top.ranking)): # <-- Get country page players
            
            self.base = self.top.ranking[self.index]

            if self.base.global_rank >= 100000:
                self.player_list[0].append(self.base.user.username)
                self.player_list[1].append(self.base.global_rank)
                self.player_list[2].append(f'https://osu.ppy.sh/community/chat?sendto={self.base.user.id}')
                
                self.lista_convidados.append(self.player_list[0][self.index])
                self.index += 1
           
            if self.index == self.quantos_players:
                await interaction.response.send_message(f'{self.quantos_players} jogadores foram encontrados!')
                break

        self.index = 0

        for self.player in self.player_list[0]: # <- Showing players
            await interaction.followup.send(f'-> ``{self.player}`` - **#{self.player_list[1][self.index]}** -> {self.player_list[2][self.index]}')
            self.index += 1
        
        

        self.player_list[0].clear
        self.player_list[1].clear
        self.player_list[2].clear


            
    

async def setup(client):
    await client.add_cog(Getplayer(client))




