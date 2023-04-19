from discord import app_commands
from discord.ext import commands
from discord.ext import tasks

import discord, random, os, asyncio
from ossapi import Ossapi, Scope, UserLookupKey, GameMode, RankingType, Cursor
import requests, json, random


client_id = '21582' # <-- oAuth application authorization
client_secret = '8HgI7sfhYL4URYn2jqrXKj64RQ9zxRmQyPm0WW8U'
api = Ossapi(client_id, client_secret) # <-- Registering the API



class Getplayer(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    
    @app_commands.command(name='6digitos', description='Puxa os 6 digitos BR ativos no osu!')
    async def invite(self, interaction: discord.Interaction, quantos_players:int):

        await interaction.response.defer(ephemeral=True)

        self.page = random.randint(65, 140)
        self.cursor = Cursor(page=self.page) # <-- Select the page of Users
        self.top = api.ranking(GameMode.OSU, RankingType.PERFORMANCE)
        self.top = api.ranking('osu', 'performance', country='br', cursor=self.cursor) # <-- Filtering by country, performance and page
        
        self.quantos_players = quantos_players
        
        self.index = self.contador = 0
        self.player_list = [[], [], []]
        self.lista_convidados = []
        self.player_passado = []
    
       
        with open('invites.txt', 'r') as arquivo:
            for nome in arquivo:
                self.lista_convidados.append(nome[:-1])
        
        

        while self.contador != self.quantos_players: # <-- Get country page players
            
            self.base = self.top.ranking[self.index]

            if self.base.user.is_online == True and self.base.user.is_active == True and self.base.global_rank >= 100000 and self.base.user.username not in self.lista_convidados and self.base.user.username not in self.player_passado:
                
                
                self.player_list[0].append(self.base.user.username)
                self.player_list[1].append(self.base.global_rank)
                self.player_list[2].append(f'https://osu.ppy.sh/community/chat?sendto={self.base.user.id}')
                self.player_passado.append(self.base.user.username)
                self.contador += 1
            
                
            if self.index == 49:
                self.page = random.randint(65, 140)
                self.index = 0
                self.cursor = Cursor(page=self.page) # <-- Select the page of Users
                self.top = api.ranking(GameMode.OSU, RankingType.PERFORMANCE)
                self.top = api.ranking('osu', 'performance', country='br', cursor=self.cursor) 


            self.index += 1
        
    
        self.index = 0

        with open('invites_message.txt', 'w') as arquivo: # <-- Armazenando as mensagens de convite
            for player in self.player_list[0]:
                arquivo.write(f'> ``{player}`` - **#{self.player_list[1][self.index]}** - {self.player_list[2][self.index]}\n')
                self.index += 1
            

        await interaction.followup.send(f'{self.quantos_players} jogadores estão online e foram encontrados')

        textfile = open('invites_message.txt', 'r') # <-- Reading the file of invites message
        await interaction.followup.send(textfile.read())
                            
        with open('invites.txt', 'a') as arquivo: # <-- manda o nome dos jogadores convidados
            for nome in self.player_list[0]:
                arquivo.write(str(nome) + '\n')

        


async def setup(client):
    await client.add_cog(Getplayer(client))



