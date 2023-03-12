from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
from nltk import pos_tag, word_tokenize

df = pd.read_csv("NYT2012SentScores.csv")

text = " ".join(i for i in df.headline)

Nonly = ""

for i in df.headline:
    speech = nltk.pos_tag(word_tokenize(i))
    #print(speech)
    for j in speech:
        if(j[1] == 'NNP' or j[1] == 'NNS' or j[1] == 'NN'):
            Nonly += j[0] + ' '


STOPWORDS = list(STOPWORDS)
STOPWORDS.append('Romney')
STOPWORDS.append('Obama')
STOPWORDS.append('China')
STOPWORDS.append('U.S.')
STOPWORDS.append('New')
STOPWORDS.append('Day')
STOPWORDS.append('Say')
STOPWORDS.append('Plan')
STOPWORDS.append('S')
STOPWORDS.append('US')
STOPWORDS.append('U')
STOPWORDS.append('Will')
STOPWORDS.append('Time')
STOPWORDS.append('Says')
STOPWORDS.append('One')
STOPWORDS.append('Back')
STOPWORDS.append('Take')
STOPWORDS.append('Make')
STOPWORDS.append('May')
STOPWORDS.append('Big')
STOPWORDS.append('City')
STOPWORDS.append('York')
STOPWORDS.append('Win')
STOPWORDS.append('Year')
STOPWORDS.append('Home')
STOPWORDS.append('Look')
STOPWORDS.append('Game')
STOPWORDS.append('Deal')
STOPWORDS.append('Case')
STOPWORDS.append('India')
STOPWORDS.append('First')
STOPWORDS.append('Two')
STOPWORDS.append('Test')
STOPWORDS.append('Week')
STOPWORDS.append('End')
STOPWORDS.append('Show')
STOPWORDS.append('Face')
STOPWORDS.append('Else')
STOPWORDS.append('Women')
STOPWORDS.append('Talk')
STOPWORDS.append('Help')
STOPWORDS.append('Return')
stopwords = set(STOPWORDS)

words = Nonly.split()
print(words)

positiveList = []
neutralList = []
negativeList = []

for i in words:
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(i)
    if(sentiment_dict['pos'] > sentiment_dict['neg']):
        positiveList.append(i)
    elif(sentiment_dict['neg'] > sentiment_dict['pos']):
        negativeList.append(i)
    elif(sentiment_dict['neg'] == sentiment_dict['pos']):
        neutralList.append(i)
    else:
        neutralList.append(i)


neuwordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(' '.join(neutralList))
plt.figure( figsize=(15,10))
plt.imshow(neuwordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

poswordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(' '.join(positiveList))
plt.figure( figsize=(15,10))
plt.imshow(poswordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()