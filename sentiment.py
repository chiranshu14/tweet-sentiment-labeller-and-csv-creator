from textblob import TextBlob
import tweepy
import csv

#twitter credentials!
consumer_key = "TLnzReJKRu8xYUvQM4q4GKRv2"
consumer_secret = "kclBizOjeXt2IaOB3tZALu94ieIGcVPDtn7UYxwdEu8A6C27Ym"

access_token = "710527168-4gVBwbhdG0C8Meq08v1oNIP8ULeCupianqE6G7VE"
access_token_secret = "sPyLdi9oflE4pKpd3hxNjs8NL9PQvTGqC2PbqthCvNUqy"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('@sirajraval')

# for tweet in public_tweets:
# 	print tweet.text
# 	analysis = TextBlob(tweet.text)
# 	print (analysis.sentiment)
# 	print "\n\n"

		# analysis = TextBlob(tweet.text)
		# print (analysis.sentiment)
		# print "\n\n"

#
with open('sentiment.csv', 'w') as csvfile:
    fieldnames = ['tweet', 'sentiment']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for t in public_tweets:
    	ttext = t.text
    	#cleanedtext = ' '.join([word for word in text.split(' ') if len(word) > 0 and word[0] != '@' and word[0] = '.' and word[0] != '#' and 'http' not in word and word != 'RT'])
    	cleanedtext = ' '.join([word for word in ttext.split(' ') if len(word) > 0 and word[0] != '@' and word[0] == '.' and word[0] != '#' and 'http' not in word and word != 'RT'])
    	
    	sen = TextBlob(t.text)
    	sen = sen.sentiment
    	writer.writerow({'tweet': cleanedtext, 'sentiment':sen})





