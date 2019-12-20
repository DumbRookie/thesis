import pandas as pd
from googletrans import Translator
import string
import re


translator = Translator()
english_letters = set(string.ascii_letters)
punct = set(string.punctuation)


def replace_punctuation(item):
    item = re.sub(r'([a-zA-Z])([,.:_!])', r'\1 \2', item)
    item = ''.join(ch for ch in item if ch not in punct)
    return item

def translate_sentence(item):
    sentence = replace_punctuation(str(item))
    gr_line = translator.translate(sentence, dest='el', src='en').text
    print(gr_line)
    return gr_line

def replace_sentiment(feeling):

    if feeling == 'anger':
        return 'οργή'
    elif feeling == 'anticipation':
        return 'ανυπομονησία'
    elif feeling == 'disgust':
        return 'αηδία'
    elif feeling == 'fear':
        return 'φόβος'
    elif feeling == 'joy':
        return 'χαρά'
    elif feeling == 'sadness':
        return 'θλίψη'
    elif feeling == 'surprise':
        return 'έκπληξη'
    else:
        return 'εμπιστοσύνη'
 

lexicon_frame = pd.read_csv('/Users/teoflev/Desktop/thesis_code/thesis/resources/lexiconframe.csv')

lexicon_frame['Sentiment'] = [replace_sentiment(str(entry)) for entry in lexicon_frame.sentiment]
lexicon_frame = lexicon_frame.drop('sentiment', axis = 1)
lexicon_frame['Gr_Content'] = [translate_sentence(entry) for entry in lexicon_frame.Content]

print(lexicon_frame)

lexicon_frame.to_csv(r'/Users/teoflev/Desktop/thesis_code/thesis/resources/half_lexiconframe.csv', index = None)
  


