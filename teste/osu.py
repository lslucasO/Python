from ossapi import Ossapi, Scope

client_id = '21582'
client_secret = '8HgI7sfhYL4URYn2jqrXKj64RQ9zxRmQyPm0WW8U'
callback_url = 'http://localhost:727/'
scopes = [Scope.PUBLIC, Scope.FRIENDS_READ]
api = Ossapi(client_id, client_secret, callback_url, scopes=scopes)
print(api.friends())