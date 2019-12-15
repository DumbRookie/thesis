import pandas as pd
from googletrans import Translator
import string
import enchant
from num2words import num2words
import re
import nltk 

dictionary = enchant.Dict("en_UK")
translator = Translator()
english_letters = set(string.ascii_letters)
punct = set(string.punctuation)


def replace_punctuation(item):
    item = re.sub(r'([a-zA-Z])([,.:_!])', r'\1 \2', item)
    item = ''.join(ch for ch in item if ch not in punct)
    return item

def translate_words(item):
    lemmas = replace_punctuation(str(item))
    lemma_list = lemmas.split(' ')
    lemma_list = list(filter(None, lemma_list))
    for word in lemma_list:
        if word.isdigit():
            lemma_list.append(num2words(word))
            lemma_list.remove(word)

    for word in lemma_list:
            if not word.isdigit():
                if all(char in english_letters for char in word):
                    if dictionary.check(word) is True:
                        try:
                            new_word = translator.translate(word, dest= 'el').text
                            gr_word = str(new_word)
                            lemma_list.remove(word)
                            lemma_list.append(gr_word)
                        except:
                            lemma_list.remove(word)
                    else:
                        lemma_list.remove(word)

    returned_lemma = ' '.join(lemma_list)
    return nltk.word_tokenize(returned_lemma)

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

nrc_frame = pd.read_csv('/Users/teoflev/Desktop/thesis_code/thesis/resources/nrcframe.csv')

nrc_frame['Sentiment'] = [replace_sentiment(str(entry)) for entry in nrc_frame.sentiment]
nrc_frame['Gr_Content'] = [translate_words(str(entry)) for entry in nrc_frame.Content]

print (nrc_frame)
nrc_frame.to_csv(r'/Users/teoflev/Desktop/thesis_code/thesis/resources/gr_nrc.csv', index = None)
