import emoji
import pandas as pd 
import spacy
import re
import string
from num2words import num2words
from googletrans import Translator
import enchant

punct = set(string.punctuation)
punct.add('«')
punct.add('»')

dictionary = enchant.Dict("en_US")

translator = Translator()

english_letters = set(string.ascii_letters)

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
    item = re.sub(r'([a-zA-Z])([^a-zA-Z])', r'\1 \2', item)
    item = re.sub(r"([0-9]+(\.[0-9]+)?)",r" \1 ", item)
    return item

def translate_words(item):
    lemmas = replace_punctuation(item)
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
tweet_frame['Translated_Tweet'] = [translate_words(str(entry)) for entry in tweet_frame.new_No_Punctuation]

# Remove any English Remnant words and also remove stopwords
tweet_frame['Greek_Tweet'] = [remove_english(str(entry)) for entry in tweet_frame.Translated_Tweet]

# Remove word that are one or two-character long
tweet_frame['Greek_Words'] =[remove_small_words(str(lemma)) for lemma in tweet_frame.Greek_Tweet]

# Tokenize tweets
tweet_frame['Token'] = [nlp(str(text)) for text in tweet_frame.Greek_Words]

# Lemmatization
tweet_frame['Lemmatized_Tokens'] = [lemmatize(str(tweet)) for tweet in tweet_frame.Token]

#-------------------------------------------------------------------------------------------------------------------------
tweet_frame = tweet_frame.drop('Token', axis = 1)
tweet_frame = tweet_frame.drop('No_Emoji_Tweet', axis = 1)
tweet_frame = tweet_frame.drop('Greek_Tweet', axis = 1)
tweet_frame = tweet_frame.drop('new_No_Punctuation', axis = 1)
tweet_frame = tweet_frame.drop('Translated_Tweet', axis = 1)
tweet_frame = tweet_frame.drop('No_Punctuation', axis = 1)
tweet_frame = tweet_frame.drop('Greek_Words', axis = 1)

for row in tweet_frame.Lemmatized_Tokens:
    if str(row) == '[]':
        tweet_frame.drop(row, axis = 0)

print (tweet_frame)
tweet_frame.to_csv(r'/Users/teoflev/Desktop/thesis_code/thesis/tweets/preprocessed_tweet_frame.csv', index = None)



