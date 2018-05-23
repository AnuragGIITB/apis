# lets try python one more time

import tweepy
ckey = 'PnaT9qfLBz6HbfRVaV1L4K6oi'
csec = 'GEkTBMH2YpzEtKq3K1ApwhodFfjA7QWpqLDaermv250nxTxjOH'
akey = '768483161894375425-yFeHaSVW390RuFRn4JCcgFkSHwgXW1C'
asec = 'nsrXhFVV2BgN5xs0DpLWalUw7VHDA5IpcGAHKciEaq04H'

auth = tweepy.OAuthHandler(ckey, csec)
auth.set_access_token(akey, asec)

api = tweepy.API(auth)
public_tweets = api.home_timeline()
for tweet in public_tweets:
	print(tweet.text)
	
a = ['Anurag Gupta', 'Anurag Gupta Mumbai']
for i in range(1):
	print('here \n\n\n')
	user = api.get_user('Yash')
	print(user.screen_name, user.id, user.followers_count, user.description.encode('utf-8'))
	print('\n\n\n\n\n\n')
	
