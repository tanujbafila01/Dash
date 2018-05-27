'''In this tutorial, we use textblob and vadersentiment for sentiment analysis.
We test them against known data i.e. positive and negative movie reviews.'''

from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time
#import nltk
#nltk.download('punkt')
'''analysis = TextBlob("TextBlob sure looks like it has some interesting features")

print(dir(analysis))
print(analysis.translate(to='es'))
print(analysis.tags)
print(analysis.sentiment)
# sentiment has 2 scores: polarity(-1 to 1) and subjectivity[0(objective) to 1(subjective)]
'''

pos_count = 0
pos_correct = 0

with open('data//positive.txt','r') as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)
        if analysis.subjectivity<0.8:
            if analysis.sentiment.polarity>0:
                pos_correct+=1
            pos_count+=1

neg_count = 0
neg_correct = 0

with open('data//negative.txt','r') as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)
        if analysis.subjectivity<0.8:
            if analysis.sentiment.polarity<=0:
                neg_correct+=1
            neg_count+=1

print("TextBlob Positive accuracy = {}% via {} samples.".format(pos_correct/pos_count*100.0,pos_count))
print("TextBlob Negative accuracy = {}% via {} samples.".format(neg_correct/neg_count*100.0,neg_count))

# VaderSentiment:

analyzer = SentimentIntensityAnalyzer()
#vs = analyzer.polarity_scores("Vader sentiment looks interesting.I have hopes")
#print(vs)

pos_count_vdr = 0
pos_correct_vdr = 0
threshold = 0.5
with open("data//positive.txt","r") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)
        if vs['compound'] >= threshold or vs['compound'] <= -threshold:
            if vs['compound']>0:        #compound > 0, positive, <=0, negative
                pos_correct_vdr += 1
            pos_count_vdr +=1

neg_count_vdr = 0
neg_correct_vdr = 0

with open("data//negative.txt","r") as f:
    for line in f.read().split("\n"):
        vs = analyzer.polarity_scores(line)
        if vs['compound'] >= threshold or vs['compound'] <= -threshold:
            if vs['compound']<=0:
                neg_correct_vdr +=1
            neg_count_vdr +=1

print("VaderSentiment(compound) Positive accuracy = {}% via {} samples.".format(pos_correct_vdr/pos_count_vdr*100.0,pos_count_vdr))
print("VaderSentiment(compound) accuracy = {}% via {} samples.".format(neg_correct_vdr/neg_count_vdr*100.0,neg_count_vdr))

#if we have a requirement that we don't want any positive or negative sentiment
#ignoring compound and requiring more negative  than positive sentiments

analyzer = SentimentIntensityAnalyzer()

pos_count = 0
pos_correct = 0

with open("data//positive.txt","r") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)
        if not vs['neg'] > 0.1:
            #if vs['pos']-vs['neg'] >= 0:
            if vs['pos'] - vs['neg'] > 0:
                pos_correct += 1
            pos_count +=1


neg_count = 0
neg_correct = 0

with open("data//negative.txt","r") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)
        if not vs['pos'] > 0.1:
            if vs['pos']-vs['neg'] <= 0:
                neg_correct += 1
            neg_count +=1

print("Positive accuracy(no_compound) = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
print("Negative accuracy(no_compound) = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))