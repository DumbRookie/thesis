import pandas as pd
import spacy


emotion_frame = pd.read_csv("/Users/teoflev/Desktop/thesis_code/thesis/resources/emotion_lexicon.csv", encoding='utf-8-sig')


nlp = spacy.load("el_core_news_sm")

def lemmatize(text):
    return [token.lemma_ for token in nlp(text)]

emotion_frame['Text'] = [lemmatize(str(tweet)) for tweet in emotion_frame.Final_Content]

emotion_frame = emotion_frame.drop('Final_Content', axis = 1)

emotion_frame.to_csv(r'/Users/teoflev/Desktop/thesis_code/thesis/resources/emotion.csv', index = None)