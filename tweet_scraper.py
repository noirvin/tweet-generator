import GetOldTweets3 as got

username = 'kasubasushi'
count = 2000
# Creation of query object
tweetCriteria = got.manager.TweetCriteria().setUsername(username)\
                                        .setMaxTweets(count)
# Creation of list that contains all tweets
tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# Creating list of chosen tweet data
user_tweets = [[tweet.date, tweet.text] for tweet in tweets]

count = 0

while count != 10:

    print(user_tweets[count][1])
    count+=1
