import pandas as pd

df10 = pd.read_csv("NYT2010SentScores.csv")
df11 = pd.read_csv("NYT2011SentScores.csv")
df12 = pd.read_csv("NYT2012SentScores.csv")
df13 = pd.read_csv("NYT2013SentScores.csv")
df14 = pd.read_csv("NYT2014SentScores.csv")
df15 = pd.read_csv("NYT2015SentScores.csv")
df16 = pd.read_csv("NYT2016SentScores.csv")
df17 = pd.read_csv("NYT2017SentScores.csv")
df18 = pd.read_csv("NYT2018SentScores.csv")
df19 = pd.read_csv("NYT2019SentScores.csv")
df20 = pd.read_csv("NYT2020SentScores.csv")
df21 = pd.read_csv("NYT2021SentScores.csv")

dataframes = [df10, df11, df12, df13, df14, df15, df16, df17, df18, df19, df20, df21]

df = pd.concat(dataframes)

topic = input("Type your topic: ")

print("Searching now for Topic - ", topic)

df2= df.query('headline.str.contains(@topic)', engine='python')

allList = []
avg = 0

for index, row in df2.iterrows():
    allList.append([row['headline'], row['Positive'], row['Neutral'], row['Negative'], row['Compound'],
                    len(row['headline'].split())])

for i in allList:
    avg = avg + i[5]

avg = round(avg / len(df2))
print("Average word length: ", avg)
newList = []

for i in allList:
    if(i[5] == avg or i[5] == avg-1 or i[5] == avg+1):
        newList.append(i)

allList = newList

print("What would you like to sort by?")
print("Positive = 1")
print("Neutral = 2")
print("Negative = 3")
print("Compound = 4")
print("Composite = 5")
selection = int(input("Type Selection Now: "))

if(selection == 5):
    allList.sort(key = lambda x: x[1], reverse=True)
    print('\n Most Positive:')
    print(allList[0][0], ' : ', allList[0][1])

    print('\n Two Neutral: ')
    allList.sort(key = lambda x: x[2], reverse=True)
    #High Compound
    print(allList[0][0], ' : ', allList[0][2])
    print(allList[1][0], ' : ', allList[1][2])

    print('\n Most Negative: ')
    allList.sort(key = lambda x: x[3], reverse=True)
    print(allList[0][0], ' : ', allList[0][3])
    print('\n Highest Compound Score: ')
    allList.sort(key = lambda x: x[4], reverse=True)
    print(allList[0][0], ' : ', allList[0][4])

elif(selection == 2):
    allList.sort(key=lambda x: x[2], reverse=True)
    print('Most Neutral: ')
    print(allList[0][0] + ' : ' + str(allList[0][2]) + ' : ' + str(allList[0][4]))
    print(allList[1][0] + ' : ' + str(allList[1][2]) + ' : ' + str(allList[1][4]))
    print(allList[2][0] + ' : ' + str(allList[2][2]) + ' : ' + str(allList[2][4]))
    max = ''
    neutral = 0.75
    maxval = 0.0
    print('High Neutral High Compound: ')
    for i in allList:
        if(i[2] >= neutral and i[4] > maxval):
            max = i[0]
            neutral = i[2]
            maxval=i[4]
    print(max + ' : ' + str(neutral) + ' : ' + str(maxval))

else:
    allList.sort(key = lambda x: x[selection])
    for i in allList:
        print(i[0] + ' : ' + str(i[selection]) + ' : ' + str(i[4]))


