import json
import pandas as pd

# Path to tweets.js
tweets_file = 'path_to_your_archive/data/tweets.js'

# Read tweets.js
with open(tweets_file, 'r', encoding='utf-8') as file:
    tweets_data = json.loads(file.read()[25:])

# Extract to Only Media Tweets
media_tweets = []
for tweet in tweets_data:
    if 'media' in tweet['entities']:
        media_tweets.append({
            'datetime': tweet['created_at'],
            'text': tweet['full_text'],
            'media': [media['media_url_https'] for media in tweet['entities']['media']]
        })

# Convert to DataFrame and Save to CSV
media_tweets_df = pd.DataFrame(media_tweets)
media_tweets_df.to_csv('media_tweets.csv', index=False)

#This software is released under the MIT License, see LICENSE.