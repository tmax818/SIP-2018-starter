'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
# from wordcloud import WordCloud

# def avg(lst):
#     return sum(lst)/len(lst)


#Get the JSON data
tweetFile = open("TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below! 
tweettext = []
tweetstring = ""
for tweet in tweetData:
    tweetstring += tweet['text']
    # blob = TextBlob(tweet['text'])
    #tweettext.append(blob)

#print(tweetstring)

tweetBlob = TextBlob(tweetstring)

print(tweetBlob.translate(to='es'))

blob_polarity = []
for blob in tweettext:
    blob_polarity.append(blob.polarity)

blob_subjectivity = []
for blob in tweettext:
    blob_subjectivity.append(blob.subjectivity)

word_dict = {}

for word in tweetBlob.words:
    word_dict[word.lower()] = tweetBlob.word_counts[word.lower()]

print(word_dict) 

# avgPol = avg(blob_polarity)
# avgSub = avg(blob_subjectivity)

# print(avgPol, avgSub)


# Textblob sample:
# tb = TextBlob("You are a horrible computer scientist.")
# words = tb.words
#print(tb.sentiment)
# print(TextBlob("bad").sentiment)

# for word in words:
#     print(TextBlob(word).sentiment)

