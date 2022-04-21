import tweepy
from tweepy import OAuthHandler

import pandas as pd
import numpy as np
import re
from nltk.stem.porter import *

from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Part 1: Tweet Scraping

"""
To be able to download tweets using Python, we have to set up a twitter API 
using the following steps:

1. Log in or make a Twitter account at https://apps.twitter.com/
2. Create a new app (top right button)
3. Fill in application creation page
4. Once project has been created, click on 'Keys and Access Tokens'. You 
should see your consumer secret and consumer key. Copy these.
5. Scroll down and request the access tokens. You should now have an access 
token and access token secret. Copy these.

"""

# adding our authentication information
consumer_key = ()
consumer_secret = ()
access_token = ()
access_secret = ()

# creating our API object
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

"""
There are different ways to retrieve tweets in Python. We are using the 
'tweepy' package to scrape tweets in two different ways:

1. We are going to retrieve tweets from a specific user, 'Donald Trump'
2. We are going to retrieve tweets from a specific keyword, 'Trump
"""

# getting tweets from a specific user
name = 
tweet_count = 
language = 

user_tweets = []
for tweet in tweepy.Cursor(api.user_timeline, id=name, lang=language, count=tweet_count, tweet_mode='extended').items(1000):
    user_tweets.append(tweet.full_text)
    
print("User Tweet = " + user_tweets[0])

input('Step 5 completed. Press ENTER to continue')

# getting tweets about a specific key word
tweet_count = 1000

search_tweets = []
# we are collecting tweets without any retweets, and 'extended' mode takes the full longer 280 character tweets
for tweet in tweepy.Cursor(api.search, q='Trump -filter:retweets', count=tweet_count, tweet_mode='extended').items(1000):
    search_tweets.append(tweet.full_text)
    
print("Search Tweet = " + search_tweets[0])

"""
For our twitter sentiment analysis we are going to focus on the keyword tweets, 
500 tweets that contain the word 'Trump'.
"""

# creating a dataframe of the tweets
Tweets = pd.DataFrame({'Tweets':np.array(search_tweets)})

# writing the dataframe to a csv file
Tweets.to_csv('data/Tweets.csv')

input('Step 6 completed. Press ENTER to continue')

# Part 2: Sentiment Analysis


"""
After saving the tweets to a csv file, we manually labelled the sentiment 
(positive or negative) of the tweets in order to build a sentiment 
classification model using labelled training data.

To build a sentiment classification model involves two parts:

1. clean the text
2. training and testing the classification model
"""

# importing the labelled tweets as a dataframe
Labelled_Tweets = pd.read_csv('data/training_data/Labelled Sentiment.csv')
Labelled_Tweets.head()

"""
Here we clean the tweets by applying a function to the text that will remove 
links, @user mentions, and punctuation
"""

# cleaning the text
def clean_tweet(tweet):
    '''
    Utility function to clean the text in a tweet by removing 
    links and special characters using regex.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

Labelled_Tweets['Cleaned_Tweet'] = Labelled_Tweets['Tweets'].apply(clean_tweet)
Labelled_Tweets.head()

"""
We clean the tweets further using the following functions to remove short 
words, tokenizing the tweets, stemming the words, and rejoining the words 
together.
"""

# removing short words
def short_words(tweet):
    return ' '.join([w for w in tweet.split() if len(w)>3])

# tokenization
def tokenization(tweet):
    return tweet.split()

# stemming
stemmer = PorterStemmer()
def stemming(tweet):
    return [stemmer.stem(i) for i in tweet]

Labelled_Tweets['Cleaned_Tweet'] = Labelled_Tweets['Cleaned_Tweet'].apply(short_words)
Labelled_Tweets['Tokenized_Tweet'] = Labelled_Tweets['Cleaned_Tweet'].apply(tokenization)
Labelled_Tweets['Stemmed'] = Labelled_Tweets['Tokenized_Tweet'].apply(stemming)

# rejoining the words
Labelled_Tweets['Cleaned_Tweet_Final'] = Labelled_Tweets['Stemmed'].str.join(" ")
Labelled_Tweets.head()

input('Step 7 completed. Press ENTER to continue')

"""
Using word clouds to visualize the most common words used in tweets of each 
sentiment
"""

pos_tweets = Labelled_Tweets[Labelled_Tweets.Sentiment == 'pos']
neg_tweets = Labelled_Tweets[Labelled_Tweets.Sentiment == 'neg']

# creating wordcloud of tweets classed as positive
all_pos_words = ' '.join([text for text in pos_tweets['Cleaned_Tweet_Final']])
wordcloud = WordCloud().generate(all_pos_words)
plt.figure(figsize=(10,7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# creating wordcloud of tweets classed as negative
all_neg_words = ' '.join([text for text in neg_tweets['Cleaned_Tweet_Final']])
wordcloud = WordCloud().generate(all_neg_words)
plt.figure(figsize=(10,7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

input('Step 8 completed. Press ENTER to continue')

"""
We now need to extract features from cleaned tweets to analyse the cleaned 
tweets. The two techniques we will use are:

1. Bag-of-Words features: it is a method to represent text as numerical 
features. It involves looking at the D documents (tweets) with N unique tokens 
(each word) to create a D x N matrix, with each row containing the frequency of 
tokens in a document.
2. TF-IDF features: it is another method based on the frequency method, but it 
also takes into account the entire collection of tweets, not just the occurence 
of words. It penalises common words by assigning lower weights to more 
frequently occuring words.
"""

# 1. Bag-of-Words features
bow_vectorizer = CountVectorizer(max_df=0.90, min_df=2, max_features=1000, stop_words='english')
bow = bow_vectorizer.fit_transform(Labelled_Tweets['Cleaned_Tweet_Final'])

# 2. TF-IDF features
tfidf_vectorizer = TfidfVectorizer(max_df=0.9, min_df=2, max_features=1000, stop_words='english')
tfidf = tfidf_vectorizer.fit_transform(Labelled_Tweets['Cleaned_Tweet_Final'])

# Creating training and test data for our sentiment analysis classifier
x_train_bow, x_test_bow, y_train, y_test = train_test_split(bow, Labelled_Tweets['Sentiment'], random_state=1234, test_size=0.6)
x_train_tfidf, x_test_tfidf, y_train, y_test = train_test_split(tfidf, Labelled_Tweets['Sentiment'], random_state=1234, test_size=0.6)

"""
Now that we have our training and test data, we can build a classification 
model to predict the sentiment of tweets. There are many different classifiers 
we can use, here we will use two; logistic regression, and linear support 
vector classification. We will apply each of these models to both the 
bag-of-words features and the tf-idf features to compare the performance.
"""

# Building a Logistic Regression classifier using bag-of-words features
lreg = LogisticRegression()
lreg.fit(x_train_bow,y_train.astype(str))
predictions = lreg.predict(x_test_bow)

accuracy = accuracy_score(y_test,predictions)
print("Logistic_Regression " + str(accuracy))

# Building a Logistic Regression classifier using tf-idf features
lreg = LogisticRegression()
lreg.fit(x_train_tfidf,y_train.astype(str))
predictions = lreg.predict(x_test_tfidf)

accuracy = accuracy_score(y_test,predictions)
print("LogisticRegression_tfidf "+ str(accuracy))

# Building a linear support vector classificaiton using bag-of words features
nb = LinearSVC()
nb.fit(x_train_bow,y_train.astype(str))
predictions = nb.predict(x_test_bow)

accuracy = accuracy_score(y_test,predictions)
print("LinearSVC "+ str(accuracy))

# Building a linear support vector classificaiton using tf-idf features
nb = LinearSVC()
nb.fit(x_train_tfidf,y_train.astype(str))
predictions = nb.predict(x_test_tfidf)

accuracy = accuracy_score(y_test,predictions)
print("LinearSVC_tfidf "+ str(accuracy))

input('Step 9 completed. Press ENTER to continue')

# cleaning the new tweets
Labelled_Tweets = pd.read_csv('data/Tweets.csv')
Labelled_Tweets['Cleaned_Tweet'] = Labelled_Tweets['Tweets'].apply(clean_tweet)

# removing short words
# tokenization
# stemming
Labelled_Tweets['Cleaned_Tweet'] = Labelled_Tweets['Cleaned_Tweet'].apply(short_words)
Labelled_Tweets['Tokenized_Tweet'] = Labelled_Tweets['Cleaned_Tweet'].apply(tokenization)
Labelled_Tweets['Stemmed'] = Labelled_Tweets['Tokenized_Tweet'].apply(stemming)

# rejoining the words
Labelled_Tweets['Cleaned_Tweet_Final'] = Labelled_Tweets['Stemmed'].str.join(" ")

# 2. TF-IDF features
tfidf = tfidf_vectorizer.fit_transform(Labelled_Tweets['Cleaned_Tweet_Final'])

# Creating test data for our sentiment analysis classifier
x_train_tfidf, x_test_tfidf, y_train, y_test = train_test_split(tfidf, Labelled_Tweets, random_state=1234, test_size=0.999)

# Classifying the new tweets
predictions = nb.predict(x_test_tfidf)

# Pie chart to highlight the distribution
slices_hours = [list(predictions).count("neg"), list(predictions).count("pos")]
activities = ['Negative', 'Positive']
colors = ['b', 'g']
plt.pie(slices_hours, labels=activities, colors=colors, startangle=90, autopct='%.1f%%')
plt.show()

print('Step 10 completed.')
