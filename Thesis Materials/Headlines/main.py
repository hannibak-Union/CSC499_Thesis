from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

def sentiment_scores(sentence):
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)
    return sentiment_dict

df = pd.read_csv("nyt_articles_2021.csv")
#print(df)

df = df.drop('pub_date', axis=1)
df = df.drop('abstract', axis=1)
df = df.drop('lead_paragraph', axis=1)
df = df.drop('news_desk', axis=1)
df = df.drop('section_name', axis=1)
df = df.drop('word_count', axis=1)

df = df.dropna()

positiveValues = []
neutralValues = []
negativeValues = []
compoundValues = []

for index, row in df.iterrows():
    #print(row['headline'])
    current = sentiment_scores(row['headline'])

    positiveValues.append(current['pos'])
    neutralValues.append(current['neu'])
    negativeValues.append(current['neg'])
    compoundValues.append(current['compound'])

df.insert(1, "Positive", positiveValues, True)
df.insert(2, "Neutral", neutralValues, True)
df.insert(3, "Negative", negativeValues, True)
df.insert(4, "Compound", compoundValues, True)

print(df.head)

df.to_csv('NYT2021SentScores.csv', index=False)
