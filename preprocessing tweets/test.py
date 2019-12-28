import pandas as pd
import spacy
import string

nlp = spacy.load("el_core_news_sm")


english_letters = set(string.ascii_letters)

def remove_english(lemma):
    lemma_list = lemma.split(' ')
    for word in lemma_list:
        if all(char in english_letters for char in word):
            lemma_list.remove(word)

        lex = nlp.vocab[word]
        if lex.is_stop == True:
            lemma_list.remove(word)

    returned_lemma = ' '.join(lemma_list)
    return(returned_lemma)

lexicon = pd.read_csv("/Users/teoflev/Desktop/thesis_code/thesis/resources/full_lexiconframe.csv") 
lexicon['Final_Content'] = [remove_english(str(entry)) for entry in lexicon.Content]
lexicon = lexicon.drop('Content', axis = 1)

lexicon.to_csv(r'/Users/teoflev/Desktop/thesis_code/thesis/resources/emotion_lexicon.csv', index = None)
