tweets = [
    {"username": "user1", "timestamp": "2023-05-01 12:30", "likes": 12, "retweets": 4, "text": "I love this game!!! #GameBrand"},
    {"username": "user2", "timestamp": "2023-05-01 13:15", "likes": 45, "retweets": 5, "text": "I can't believe how bad this game is... #GameBrand #Disappointed"},
    {"username": "user3", "timestamp": "2023-05-01 13:47", "likes": 23, "retweets": 2, "text": "What a great game! #GameBrand #Fun"},
    {"username": "user4", "timestamp": "2023-05-01 14:05", "likes": 78, "retweets": 7, "text": "This game is too difficult. #GameBrand #Frustrated"},
    {"username": "user5", "timestamp": "2023-05-01 14:23", "likes": 45, "retweets": 5, "text": "I can't stop playing this game! #GameBrand #Addicted"},
    {"username": "user6", "timestamp": "2023-05-01 15:00", "likes": 67, "retweets": 6, "text": "The graphics in this game are amazing. #GameBrand #Impressed"},
    {"username": "user7", "timestamp": "2023-05-01 15:30", "likes": 34, "retweets": 3, "text": "I wish this game had better controls. #GameBrand #Frustrated"},
    {"username": "user8", "timestamp": "2023-05-01 16:00", "likes": 23, "retweets": 2, "text": "This game is a waste of money. #GameBrand #Disappointed"},
    {"username": "user9", "timestamp": "2023-05-01 16:45", "likes": 56, "retweets": 5, "text": "I can't wait for the sequel! #GameBrand #Excited"},
    {"username": "user10", "timestamp": "2023-05-01 17:00", "likes": 78, "retweets": 7, "text": "This game has too many bugs. #GameBrand #Frustrated"}
]

# print(tweets)

import string

#Task - clean up the text
for tweet in tweets:
    text = tweet['text'].lower().strip()
    for punctuation in string.punctuation:
        text = text.replace(punctuation,'')
    tweet['text'] = text



#Extract hashtag

for tweet in tweets:
    words = tweet['text'].split()
    hashtags = [word for word in words if word.startswith('#')]
    tweet['hashtags'] = hashtags

    

# Create a dictionary of users and their sentiments

tweets = [
    {'username': 'user1', 'hashtags': ['#excited', '#happy']},
    {'username': 'user2', 'hashtags': ['#disappointed', '#frustrated', '#excited']},
    {'username': 'user1', 'hashtags': ['#impressed']},
    {'username': 'user3', 'hashtags': ['#happy', '#excited']},
    {'username': 'user2', 'hashtags': ['#excited']},
    {'username': 'user3', 'hashtags': ['#happy']},
]
sentiments={}
for tweet in tweets:
    user = tweet['username']
    if user not in sentiments:
        sentiments[user] = {'positive': 0, 'negative': 0}

positive_hashtags = ['#excited', '#impressed']
negative_hashtags = ['#disappointed', '#frustrated']

for tweet in tweets:
    user = tweet['username']
    for hashtag in tweet['hashtags']:
        if hashtag in positive_hashtags:
            sentiments[user]['positive'] += 1
        elif hashtag in negative_hashtags:
            sentiments[user]['negative'] += 1

print(sentiments)
