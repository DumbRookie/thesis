import pandas as pd
from multiprocessing import Pool
from dask import delayed
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

workers = Pool()
"""
lexicon_frame = pd.read_csv('/Users/teoflev/Desktop/thesis_code/thesis/resources/lexiconframe.csv')

lexicon_frame['Sentiment'] = [replace_sentiment(str(entry)) for entry in lexicon_frame.sentiment]
lexicon_frame = lexicon_frame.drop('sentiment', axis = 1)
print (lexicon_frame)
#lexicon_frame['gr_sentiment'] = lexicon_frame['sentiment'].apply(translator.translate,src='en',dest='el').apply(getattr, args=('text',))

lexicon_frame.to_csv(r'/Users/teoflev/Desktop/thesis_code/thesis/resources/half_lexiconframe.csv', index = None)

"""
if __name__ == '__main__':
   
    lexicon_frame = pd.read_csv('/Users/teoflev/Desktop/thesis_code/thesis/resources/half_lexiconframe.csv')
   

    lexicon_frame['Gr_Contnent'] = workers.map(translate_words,lexicon_frame.Content)
    workers.close()
    workers.join()

    lexicon_frame = lexicon_frame.drop('Content', axis = 1)

    print(lexicon_frame)

    lexicon_frame.to_csv(r'/Users/teoflev/Desktop/thesis_code/thesis/resources/full_lexiconframe.csv', index = None)

