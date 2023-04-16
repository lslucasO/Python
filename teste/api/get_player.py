from ossapi import Ossapi, Scope, UserLookupKey, GameMode, RankingType, Cursor
import requests, json, random

client_id = '21582'
client_secret = '8HgI7sfhYL4URYn2jqrXKj64RQ9zxRmQyPm0WW8U'
callback_url = 'http://localhost:727/'


api = Ossapi(client_id, client_secret, callback_url)

profile_name = 'Mestre'

user = api.user(profile_name, key=UserLookupKey.USERNAME)


page = random.randint(63, 120)

cursor = Cursor(page=page) # <-- Select the page of Users
top = api.ranking(GameMode.OSU, RankingType.PERFORMANCE)
top = api.ranking('osu', 'performance', country='br', cursor=cursor) # <-- Filtering by country, performance and page


index = 0
player_list = [[], [], []]
player_convidados = []

for key in range(len(top.ranking)): # <-- Get country page players

    base = top.ranking[index]
    if base.global_rank >= 100000: # <-- Collecting Users data
        player_list[0].append(f'{base.user.username}')
        player_list[1].append(f'#{base.global_rank}')
        player_list[2].append(f'https://osu.ppy.sh/users/{base.user.id}')
        index += 1

index = 0

for player in player_list[0]: # <-- Showing players
    
    print(f'-> {player} - #{player_list[1][index]} - {player_list[2][index]}')
    index += 1
    player_convidados.append(player)


player_list.clear







