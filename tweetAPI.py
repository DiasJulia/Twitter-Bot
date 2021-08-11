import tweepy as tp

class tweetAPI:
    def __init__(self):
        self.consumer_key = "consumer_key"
        self.consumer_secret = ""

        self.access_token = ""

        self.access_token_secret = ""

        self.auth = tp.OAuthHandler(self.consumer_key, self.consumer_secret)

        self.auth.set_access_token(self.access_token, self.access_token_secret)

        self.api = tp.API(self.auth)

    def postTweet(self, text, pic=''):
        if pic == '':
            self.api.update_status(text)
        else:
            self.api.update_status(pic, text)