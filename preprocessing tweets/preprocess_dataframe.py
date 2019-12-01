import emoji
import pandas as pd 
import spacy
import matplotlib.pyplot as plt
import seaborn as sns
import re
import string
from num2words import num2words
from googletrans import Translator
import enchant

punct = set(string.punctuation)

dictionary = enchant.Dict("en_US")

translator = Translator()

english_letters = set(string.printable)

tweet_frame = pd.read_csv("/Users/teoflev/Desktop/thesis_code/thesis/tweets/tweet_frame.csv") 

nlp = spacy.load("el_core_news_sm")

tweet_frame = tweet_frame.drop_duplicates()

def lemmatize(text):
    return [token.lemma_ for token in nlp(text)]

def replace_punctuation(item):
    item = re.sub(r'([a-zA-Z])([,.:_!])', r'\1 \2', item)
    item = ''.join(ch for ch in item if ch not in punct)
    return item

def add_whitespace(item):
    item = re.sub(r'([a-zA-Z])([,.:_!])', r'\1 \2', item)
    item = re.sub(r"([0-9]+(\.[0-9]+)?)",r" \1 ", item)
    return item

def translate_words(lemma):
    lemmas = replace_punctuation(lemma)
    lemma_list = lemmas.split(' ')
    lemma_list = list(filter(None, lemma_list))
    for word in lemma_list:
            if not word.isdigit():
                if all(char in english_letters for char in word):
                    if dictionary.check(word) is True:
                        try:
                            new_word = translator.translate(word, dest= 'el')
                            gr_word = str(new_word)
                            lemma_list.remove(word)
                            lemma_list.append(gr_word)
                        except:
                            lemma_list.remove(word)
                    else:
                        lemma_list.remove(word)

    returned_lemma = ' '.join(lemma_list)
    return nlp(returned_lemma)

def remove_english(lemma):
    lemmas = replace_punctuation(lemma)
    lemma_list = lemmas.split(' ')
    
    for word in lemma_list:
        if all(char in english_letters for char in word):
            lemma_list.remove(word)

        lex = nlp.vocab[word]
        if lex.is_stop == True:
            lemma_list.remove(word)

    returned_lemma = ' '.join(lemma_list)
    return nlp(returned_lemma)

def remove_small_words(entry):
    lemmas = replace_punctuation(entry)
    lemma_list = lemmas.split(' ')
    lemma_list = list(filter(None, lemma_list))
    for word in lemma_list:
        if (len(word) == 1 or len (word) == 2) and not word.isdigit():
            lemma_list.remove(word)

    returned_lemma = ' '.join(lemma_list)
    return nlp(returned_lemma)
#-------------------------------------------------------------------------------------------------------------------------

# Removing Emojis
tweet_frame['No_Emoji_Tweet'] = [emoji.demojize(str(tweet)) for tweet in tweet_frame.Tweet]

# Replacing Punctuation with Whitespace
tweet_frame['No_Punctuation'] = [replace_punctuation(str(no_e_entry)) for no_e_entry in tweet_frame.No_Emoji_Tweet]

# Adding Whitespace between Numbers and Words
tweet_frame['new_No_Punctuation'] = [add_whitespace(str(entry)) for entry in tweet_frame.No_Punctuation]

# Translating English words, filtering out word that are written with English alphabet but aren't valid English words.
tweet_frame['Translated_Lemma'] = [translate_words(str(lemma)) for lemma in tweet_frame.new_No_Punctuation]

# Remove any English Remnant words and also remove stopwords
tweet_frame['Greek_Lemma'] = [remove_english(str(lemma)) for lemma in tweet_frame.Translated_Lemma]

#remove word that are one or two-character long
tweet_frame['Greek_Words'] =[remove_small_words(str(lemma)) for lemma in tweet_frame.Greek_Lemma]

# Tokenize tweets
tweet_frame['Token'] = [nlp(str(text)) for text in tweet_frame.Greek_Words]

# Lemmatization
tweet_frame['Lemmatized_Tokens'] = [lemmatize(str(tweet)) for tweet in tweet_frame.Token]

#-------------------------------------------------------------------------------------------------------------------------
tweet_frame = tweet_frame.drop('Token', axis = 1)
tweet_frame = tweet_frame.drop('No_Emoji_Tweet', axis = 1)
tweet_frame = tweet_frame.drop('Greek_Lemma', axis = 1)
tweet_frame = tweet_frame.drop('new_No_Punctuation', axis = 1)
tweet_frame = tweet_frame.drop('Translated_Lemma', axis = 1)
tweet_frame = tweet_frame.drop('No_Punctuation', axis = 1)
tweet_frame = tweer_frame.drop('Greek_Words', axis = 1)

print (tweet_frame)

tweet_frame.to_csv(r'/Users/teoflev/Desktop/thesis_code/thesis/tweets/tweet_frame_2.csv', index = None)

