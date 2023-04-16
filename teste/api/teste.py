from ossapi import Ossapi, Scope, UserLookupKey, GameMode, RankingType, RankingFilter
import requests, json

client_id = '21582'
client_secret = '8HgI7sfhYL4URYn2jqrXKj64RQ9zxRmQyPm0WW8U'
callback_url = 'http://localhost:727/'

profile_name = 'Mestre'

api = Ossapi(client_id, client_secret, callback_url)
user = api.user(profile_name, key=UserLookupKey.USERNAME)


get_user = api.user(mode='osu', key='id', user=f'{user.id}')
lista = []
lista.append(f'{user.username} , https://osu.ppy.sh/users/{get_user.id}, {get_user.country_code}')

