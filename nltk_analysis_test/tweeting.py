#Tutorial URL: https://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/

import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):
    """
    Generic twitter class for sentiment analysis
    """
    
    def __init__(self):
        """
        constructor
        """
        #keys and tokens from tweeter dev console
        consumer_key = input("Consumer Key: ")
        consumer_secret = input("Consumer Secret: ")
        access_token = input("Access Token: ")
        access_token_secret = input("Access Token Secret: ")

        #Authentication
        try:
            #OAuthgandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            #set tokens
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy object, fetch some tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Authentication failed, mate :c")

    def clean_tweet(self,tweet):
        """
        Cleans text, removes links, special chars using regex.
        """
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        """
        classifies sentiment of tweet using tesxtblob's sentiment method
        """
        # create TExtBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return "positive"
        elif analysis.sentiment.polarity == 0:
            return "neutral"
        else:
            return "negative"

    def get_tweets(self, query, count = 10):
        """
        Main function to fetch tweets and parse them.
        """
        #List for tweets
        tweets = []

        try:
            #call twitter api
            fetched_tweets = self.api.search(q = query, count = count)

            #parse tweets on by one
            for tweet in fetched_tweets:
                #store params of a tweet
                parsed_tweet = {}

                #text of tweet
                parsed_tweet["text"] = tweet.text
                #sentiment of tweet
                parsed_tweet["sentiment"] = self.get_tweet_sentiment(tweet.text)

                # append to list
                if tweet.retweet_count > 0:
                    #if has retweets, append only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
            return tweets

        except tweepy.TweepError as e:
            # print.error
            print("Error: "+ str(e))


def main():
    api = TwitterClient()
    tweets = api.get_tweets(query = 'Donal Trump', count = 200)

    #Pos tweets
    ptweets = [tweet for tweet in tweets if tweet["sentiment"] == "positive"]
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))

    #Neg tweets
    ntweets = [tweet for tweet in tweets if tweet["sentiment"] == "negative"]
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))

    #Neutreal tweets
    netweets = [tweet for tweet in tweets if tweet["sentiment"] == "neutral"]
    print("Neutral tweets percentage: {} % \ ".format(100*len(netweets)/len(tweets)))
    
    #print tweets
    print("Positive:")
    print(ptweets[:10])

    print("Negative:")
    print(ntweets[:10])

if __name__ == "__main__":
    main()