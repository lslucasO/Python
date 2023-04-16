from ossapi import Ossapi, Scope, UserLookupKey
import requests, json

client_id = '21582'
client_secret = '8HgI7sfhYL4URYn2jqrXKj64RQ9zxRmQyPm0WW8U'
callback_url = 'http://localhost:727/'


api = Ossapi(client_id, client_secret)

profile_name = 'Arimaki'

user = api.user(profile_name, key=UserLookupKey.USERNAME)



#perfomance = api.beatmap_user_score(beatmap_id=499343, user_id=user.id, mode='osu') # <- get best user score in the map

#print(f'\n player: {profile_name} \n top-score: {perfomance.score.pp:.1f} pp \n beatmap-id: {perfomance.score.beatmap.id} \n beatmap-url: {perfomance.score.beatmap.url} ')

ranks = api.ranking(mode='osu', country='BR', type='performance')



