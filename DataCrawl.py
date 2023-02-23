import facebook as fb
import pandas as pd
import requests 
token = 'EAAIiQjDErnwBAPmwu3raOZAFZCNY2ZCZCa7CCf8hkAzNjBy9qaDmC0ZCbigKrOdvmCQk0VlEVeiYzxUmhZC5NGqGqxAb4ZBAzIKAimUs42ZAtclZCnyio8HkpwEqwZBtMabRo4PPWJFxj2xgTPZCh2qmSL2d4WZCegUNqDSSZAkmi8YJPfZAzmJUbFGHb9XGhvv0NCkBOl6xzOZA2IsTfxAcuDKhvmxHkyN7i2h4rw20LOUJPQUexyAYllB5LsR' # your token
graph = fb.GraphAPI(access_token=token, version = 2.9)

def getLikes(data):
    for post in data['data']: #data['posts']['data'] is a list of posts
        print(post)
        if 'name' not in post:
            tmp = ' '
        else:
            tmp = post['name']
        refined_data = {
                        'id': post['id'],\
                        'time': post['created_time'],\
                        'name': tmp
                        }
        data_list.append(refined_data)
    
data = graph.get_object('me', fields='likes', limit=1000) #fields = 'posts' means that we only want to get the posts
data_list = []
dataa = data['likes']

while (True):
    getLikes(dataa)
    dataa = requests.get(dataa['paging']['next']).json()
    if 'next' not in dataa['paging']:
        getLikes(dataa)
        break

df = pd.DataFrame(data_list)
print(df)
df.to_csv('data.csv')

