import pandas as pd
import snscrape.modules.twitter as sntwitter
from flask import Flask, request, jsonify, send_from_directory
import time

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/scrape_tweets', methods=['POST'])
def scrape_tweets():
    tweet_count = int(request.json.get('tweet_count'))
    text_query = request.json.get('text_query')
    since_date = request.json.get('since_date')
    until_date = request.json.get('until_date')

    tweets = []
    for attempt in range(100):  # Retry up to 5 times
        try:
            for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{text_query} since:{since_date} until:{until_date}').get_items()):
                if i >= tweet_count:
                    break
                tweets.append({
                    'date': tweet.date,
                    'content': tweet.content,
                    'username': tweet.username,
                    'url': tweet.url
                })
            break  # If successful, break out of the retry loop
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            time.sleep(10)  # Wait before retrying
            if attempt == 4:  # On the last attempt, return an error
                return jsonify({'error': 'Failed to retrieve tweets after multiple attempts.'}), 500

    tweets_df = pd.DataFrame(tweets)
    tweets_df.to_csv('text-query-tweets.csv', sep=',', index=False)

    return jsonify(tweets_df.head().to_dict(orient='records'))

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
