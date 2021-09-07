import tweepy
import schedule
import time
import random

# Have to complete this with your own keys
consumer_key = '' 
consumer_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Have to complete this with your own keys
key = ''
secret = ''

auth.set_access_token(key, secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

simios = ['macaco', 'simio', 'primate', 'chimpancé', 'orangután', 'mono', 'unga unga', 'bonobo', 'gorila', 'babuino']

def read_last_id():
	file = open('last_id.txt', 'r')
	id = int(file.read().strip())
	file.close()
	return id

def store_last_id(id):
	file = open('last_id.txt', 'w')
	file.write(str(id))
	file.close()

def reply_simio(tweet):
	api.update_status(
		'@' + tweet.user.screen_name + ' Eres un tremendo ' + random.choice(simios),
		tweet.id
	)
	store_last_id(tweet.id)

def check_mentions():
	mentions = api.mentions_timeline(read_last_id(), tweet_mode = 'extended')
	for tweet in reversed(mentions):
		print(tweet.full_text)
		reply_simio(tweet)
        

def main():
	schedule.every(7).seconds.do(check_mentions)
	print('Iniciando')
	while True:
		try:
			schedule.run_pending()
			time.sleep(2)
		except tweepy.TweepError as e:
			raise e

if __name__ == "__main__":
	main()