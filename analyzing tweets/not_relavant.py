from polyglot.text import Text

text = Text(" Καλημέρα ", hint_language_code='el')

print("{:<16}{}".format("Word", "Polarity")+"\n"+"-"*30)
for w in text.words:
    print (w, w.polarity)