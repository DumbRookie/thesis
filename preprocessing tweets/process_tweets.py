
import string
import emoji
from translation import google
import re
import enchant
from googletrans import Translator
import inflect

textify = inflect.engine()
translator = Translator()
dictionary = enchant.Dict("en_US")
exclude = set(string.punctuation)
english_letters = set(string.printable)

try:
    txt = open('/Users/teoflev/Desktop/thesis_code/tweets/no_dup_tweets.txt', 'r')

    #Read text line by line, break when the end of the document is reached.
    while True:
        line = txt.readline()
        if not line:
            break

    #make emojis into text ( text looks like --> :adjective_noun: )
        text_line = emoji.demojize(line)

    #remove URLs
        text_line = re.sub(r"http\S+", "\n", text_line)
    
    #add spaces between numbers and text.
        text_line = re.sub(r"([0-9]+(\.[0-9]+)?)",r" \1 ", text_line)
    
    #make numbers into English text
        for word in text_line:
            if word.isdigit():
                text_number = textify.number_to_words(word)
                text_line.replace(word, text_number)


    #add spaces between some punctuation, in this case ", . : _ !".
        text_line = re.sub(r'([a-zA-Z])([,.:_!])', r'\1 \2', text_line)

    
    #Strip each line of all punctuation.
        text_line = ''.join(ch for ch in text_line if ch not in exclude)


    #Divide each sentence into words & make them lowercase, returns a list of words. 
        tokens_of_line = text_line.split()
        tokens_of_line_lowercase = [word.lower() for word in tokens_of_line]
        
        
    
    #Remove words written with Latin alphabet, but aren't English words.
        for word in tokens_of_line_lowercase:
            if all(char in english_letters for char in word):
                if dictionary.check(word) == False:
                    tokens_of_line_lowercase.remove(word)

    #Translate English words, such as emoji descriptions and numbers, into Greek.
        for index, word in enumerate(tokens_of_line_lowercase):
            if dictionary.check(word):
                try:
                    gr_word = translator.translate(word, dest= 'el')
                    tokens_of_line_lowercase[index] = gr_word.text.lower()
                except:
                    pass

finally:
    txt.close()
    