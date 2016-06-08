# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Variables that contains the user credentials to access Twitter API
access_token = "3996253032-S05T2eGVuah9Gc0sRbcJqwN0l7m1GwvD5QU6wmx"
access_token_secret = "CipJfOLM946CAdVGCNJ19QeOTVFddlRA7I48trDo899Nj"
consumer_key = "ImsAPmcMBYhxIqaeEDroA0BDM"
consumer_secret = "lo6qcNP6upm8PFSRh0HJURULA8BumlhgS9TCbgvspw6lwvkbMj"



# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
