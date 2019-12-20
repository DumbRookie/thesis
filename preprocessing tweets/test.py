import pandas as pd
from multiprocessing import Pool
from googletrans import Translator
import string
import enchant
from num2words import num2words
import re
from pandarallel import pandarallel

pandarallel.initialize()

dictionary = enchant.Dict("en_UK")
translator = Translator()
english_letters = set(string.ascii_letters)
punct = set(string.punctuation)


def replace_punctuation(item):
    item = re.sub(r'([a-zA-Z])([,.:_!])', r'\1 \2', item)
    item = ''.join(ch if ch not in punct else ' ' for ch in item )
    return item

def translate_words(item):
    lemmas = replace_punctuation(str(item))
    lemma_list = lemmas.split(' ')
    lemma_list = list(filter(None, lemma_list))
    for word in lemma_list:
        if word.isdigit():
            lemma_list.append(replace_punctuation(num2words(word)))
            lemma_list.remove(word)

        else:
            try:
                new_word = translator.translate(word, dest='el', src='en').text
                lemma_list.remove(word)
                lemma_list.append(new_word)
            except:
                lemma_list.remove(word)
    print(lemma_list)
    return (lemma_list)

def translate_sentence(item):
    sentence = replace_punctuation(str(item))
    gr_line = translator.translate(sentence, dest='el', src='en').text
    for ch in gr_line:
        if ch in english_letters:
            gr_line = gr_line.replace(ch, "")
    return gr_line

frame = pd.read_csv('/Users/teoflev/Desktop/thesis_code/thesis/resources/lexiconframe.csv')

smol = frame.head(10)

smol['New'] = [translate_sentence(entry) for entry in smol.Content]

print (smol.New)
    
#workers = Pool()
#lexicon_frame['Gr_Contnent'] = workers.map(translate_words,lexicon_frame.Content)
#workers.close()
#workers.join()

#lexicon_frame['Gr_Content'] = lexicon_frame['Content'].parallel_apply(lambda item : translate_words(item) )
#lexicon_frame['Gr_Content'] = lexicon_frame['Content'].swifter.apply(lambda item : translate_words(item) )