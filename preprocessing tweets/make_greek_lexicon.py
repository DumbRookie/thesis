import pandas as pd
from googletrans import Translator
import string
import re
from PyDictionary import PyDictionary
import six

dictionary=PyDictionary()

translator = Translator()
english_letters = set(string.ascii_letters)
punct = set(string.punctuation)
emotions = ('οργή', 'ανυπομονησία', 'αηδία', 'φόβος', 'χαρά', 'θλίψη', 'έκπληξη', 'εμπιστοσύνη')


def replace_punctuation(item):
    item = re.sub(r'([a-zA-Z])([,.:_!])', r'\1 \2', item)
    item = ''.join(ch for ch in item if ch not in punct)
    return item

def translate_text(text):

    from google.cloud import translate_v2 as translate
    translate_client = translate.Client.from_service_account_json('/Users/teoflev/Desktop/thesis_code/transKey.json')

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')
    teee = replace_punctuation(str(text))
    result = translate_client.translate(
        teee, target_language='el')
    

    return(result['translatedText'])



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

lexicon_frame = pd.read_csv('/Users/teoflev/Desktop/thesis_code/thesis/resources/sentences.csv')
print(lexicon_frame)
lexicon_frame['Gr_Content'] = [translate_text(entry) for entry in lexicon_frame.Content]
lexicon_frame = lexicon_frame.drop('Content', axis = 1)
lexicon_frame['Gr_Sentiment'] = [replace_sentiment(str(entry)) for entry in lexicon_frame.sentiment]
lexicon_frame = lexicon_frame.drop('sentiment', axis = 1)
print(lexicon_frame)

lexicon_frame.to_csv(r'/Users/teoflev/Desktop/thesis_code/thesis/resources/gr_sentences.csv', index = None)




