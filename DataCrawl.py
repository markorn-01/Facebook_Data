import facebook as fb
import pandas as pd

token = '' # your token
graph = fb.GraphAPI(access_token=token, version = 2.9)
data = graph.get_object('me', fields='posts', limit=1000) #fields = 'posts' means that we only want to get the posts
data_list = []
for post in data['posts']['data']: #data['posts']['data'] is a list of posts
    print(post)
    if 'message' not in post:
        tmp = ' '
    else:
        tmp = post['message']
    refined_data = {
                    'time': post["created_time"],\
                    'post': tmp
                    }
    data_list.append(refined_data)
df = pd.DataFrame(data_list)
print(df)
df.to_csv('data.csv')
    