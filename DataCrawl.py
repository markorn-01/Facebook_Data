import facebook as fb
import pandas as pd
import requests 

token = '' # your token
graph = fb.GraphAPI(access_token=token, version = 2.9)

def getLikes(data):
    for post in data['data']: 
        refined_data = {
                        'Year': post['created_time'].split('-')[0],\
                        'Name': post['name'] 
                        }
        data_list.append(refined_data)
    
data = graph.get_object('me', fields='likes', limit=1000) 
data_list = []
dataa = data['likes']

while (True):
    getLikes(dataa)
    dataa = requests.get(dataa['paging']['next']).json()
    if 'next' not in dataa['paging']:
        getLikes(dataa)
        break

df = pd.DataFrame(data_list)
num = df.groupby('Year').count()
num_page = pd.DataFrame(columns=['Year', 'Number of Pages'])
num_page['Year'] = num.index
num_page['Number of Pages'] = num.values

df.to_csv('page_liked.csv', index=False)
num_page.to_csv('num_page.csv', index=False)

