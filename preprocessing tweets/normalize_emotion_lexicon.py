import pandas as pd

emolex = pd.read_csv("/Users/teoflev/Desktop/thesis_code/thesis/resources/emotion.csv", encoding='utf-8-sig')

surprise = emolex[emolex['Sentiment'] == 'έκπληξη'].head(1140)
disgust = emolex[emolex['Sentiment'] == 'αηδία'].head(1140)
sadness = emolex[emolex['Sentiment'] == 'θλίψη'].head(1140)
anger = emolex[emolex['Sentiment'] == 'οργή'].head(1140)
fear = emolex[emolex['Sentiment'] == 'φόβος'].head(1140)
joy = emolex[emolex['Sentiment'] == 'χαρά'].head(1140)



em = emolex.groupby('Sentiment').agg(['count'])
dataframes = [surprise, disgust, sadness, anger, fear, joy]
emlex = pd.concat(dataframes)
eml = emlex.groupby('Sentiment').agg(['count'])

print(em)
print(eml)

emlex.to_csv(r'/Users/teoflev/Desktop/thesis_code/thesis/resources/6emotions.csv', index= None)