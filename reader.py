from twython import Twython
from twython import TwythonStreamer

# Register a Twitter Application and generate API keys & Access Tokens
API_KEY = ''
API_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''


twitter = Twython(API_KEY, API_SECRET,ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

def  twitter_oauth_login():
    twitter = Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return twitter


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            if 'halloween' in str(data['text'].encode('utf-8')):
                print(data['text'])
                # self.disconnect()

    def on_error(self, status_code, data):
        print(status_code)

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()

stream = MyStreamer(API_KEY, API_SECRET,
                    ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Filter stream to get halloween related twitter posts.
stream.statuses.filter(track='halloween')
