import tweepy
#inport your config file
import config_hhn as conf

print("Don't go alone...")

# Initialization
auth = tweepy.OAuth1UserHandler(conf.consumer_key, conf.consumer_secret, conf.access_token, conf.access_token_secret)

api = tweepy.API(auth) 

# Getting Bot ID, must be an int. Change for bot
bot_id = 339317066

def run_into_the_fog(twt):    
    print("Tweet Found!")
        #twt.author.screen_name, etc, are taken from Twitter docs LINK HERE
    print(f"TWEET: {twt.author.screen_name} - {twt.text}")
    if ((twt.author.id == bot_id) and not (hasattr(twt, "quoted_status")) and not (hasattr(twt, "retweeted_status"))):
        try:
            print("Attempting RT")
            api.retweet(twt.id)
            print("RT SUCCESSFUL")
        except Exception as err:
            print(err)
    else:
        print("Better luck next time...")

class MyStreamListener(tweepy.Stream):
#on_status is what happens when a status ("tweet") comes into the stream
    def on_status(self, twts):
        run_into_the_fog(twts)

    def on_closed(self, response):
        print(self.response)

#create instance
stream = MyStreamListener(conf.consumer_key, conf.consumer_secret, conf.access_token, conf.access_token_secret)

#use "follow" for RT a specific account, "track" for tweets that contain the word follow must be string
stream.filter(follow =["339317066"])
