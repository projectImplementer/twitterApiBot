import tweepy
import time

auth = tweepy.OAuthHandler('cqRavqyH4wyVb5CSQTx4n7281', 'WKwhMFKlsxwEPW62PDvfSlmU6ZsI5XL1Ht9KsuJZQsAFe8LHOk')
auth.set_access_token('275018543-QfTFWUbX0iP2iy9nDz0cVci0d6uRIZwHqdHK1GOz',
                      'K9z169k2VTSEczOkVIz1Y0VfgbHZya7nLj78gQmrNNgtY')

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


search_string = 'python'
numbersOfTweets = 3

# will click like on the posts that contain python

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


# # Generous bot will follow if name we search for belongs to someone that follows us
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == 'technedigitus':
#         print('found!')
#         follower.follow()
#         break
