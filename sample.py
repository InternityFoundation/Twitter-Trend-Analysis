from twython import Twython
import pandas as pd

# Get credentials from Twitter Developer Account.
creds = {
    'consumerKey': '',
    'consumerSecret': ''
}

python_tweets = Twython(creds['consumerKey'], creds['consumerSecret'])

query = {
    'q': 'Kashmir',
    'result_type': 'popular',
    'count': 10,
    'lang': 'en'
}

# Search tweets. Can add more fields, see documentation.
dict_type = {
    'user': [],
    'date': [],
    'text': [],
    'favorite_count': []
}  

for status in python_tweets.search(**query)['statuses']:  
    dict_type['user'].append(status['user']['screen_name'])
    dict_type['date'].append(status['created_at'])
    dict_type['text'].append(status['text'])
    dict_type['favorite_count'].append(status['favorite_count'])

# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_type)

print(df.head(5))