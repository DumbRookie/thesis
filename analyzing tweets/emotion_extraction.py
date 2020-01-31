import pandas as pd
import string
import time
tweet_frame = pd.read_csv("/Users/teoflev/Desktop/thesis_code/thesis/tweets/polarized_tweet_frame.csv", encoding='utf-8-sig')
emotion_frame = pd.read_csv("/Users/teoflev/Desktop/thesis_code/thesis/resources/emotion.csv", encoding='utf-8-sig')
nrc = pd.read_csv("/Users/teoflev/Desktop/thesis_code/thesis/resources/nrc.csv", encoding='utf-8-sig')
progress_count = 0

def extract_emotion(text):
    global progress_count
    fear_count = 0
    anger_count = 0
    anticipation_count = 0
    disgust_count = 0
    joy_count = 0
    sadness_count = 0
    surprise_count = 0
    trust_count = 0

    emotions = ['θυμός', 'ανυπομονησία', 'αηδία', 'φόβος', 'χαρά', 'θλίψη', 'έκπληξη', 'εμπιστοσύνη']
    scores = []
    text_list = text.split(' ')
    for word in text_list:
        
        #Cleans word of punctuation
        wordtext = str(word)
        w = wordtext.translate(str.maketrans('', '', string.punctuation))
        for line in emotion_frame['Text']:
            #Cleans line of punctuation
            linetext = str(line)
            l = linetext.translate(str.maketrans('', '', string.punctuation))
            words_of_l = l.split(' ')
            for wort in words_of_l:
                worttext = str(wort)
                wl = worttext.translate(str.maketrans('', '', string.punctuation))

                if w == wl:
                    row_indices = emotion_frame.index[emotion_frame['Text'] == line].tolist()
                    for index in row_indices:
                        row = emotion_frame.iloc[index]
                        sentiment = row['Sentiment']
                        if sentiment == 'οργή':
                            anger_count += 1
                        if sentiment == 'ανυπομονησία':
                            anticipation_count += 1
                        if sentiment == 'αηδία':
                            disgust_count +=1
                        if sentiment == 'φόβος':
                            fear_count += 1
                        if sentiment == 'χαρά':
                            joy_count += 1
                        if sentiment == 'θλίψη':
                            sadness_count += 1
                        if sentiment == 'έκπληξη':
                            surprise_count += 1
                        if sentiment == 'εμπιστοσύνη':
                            trust_count += 1


        for linie in nrc['Text']:
            #Cleans line of punctuation
            linietext = str(linie)
            li = linietext.translate(str.maketrans('', '', string.punctuation))
            words_of_li = li.split(' ')
            for worter in words_of_li:
                wortertext = str(worter)
                wli = wortertext.translate(str.maketrans('', '', string.punctuation))

                if w == wli:
                    row_index = nrc.index[nrc['Text'] == linie].tolist()
                    for ind in row_index:
                        rowie = nrc.iloc[ind]
                        
                        sentiments = rowie['Emotion']

                        if 'anger' in sentiments:
                            anger_count += 1
                        if 'anticipation' in sentiments:
                            anticipation_count += 1
                        if 'disgust' in sentiments:
                            disgust_count += 1
                        if 'fear' in sentiments:
                            fear_count += 1
                        if 'joy' in sentiments:
                            joy_count += 1
                        if 'sadness' in sentiments:
                            sadness_count += 1
                        if 'surprise' in sentiments:
                            surprise_count += 1
                        if 'trust' in sentiments:
                            trust_count += 1
                        
                        
    scores.append(anger_count)
    scores.append(anticipation_count)
    scores.append(disgust_count)   
    scores.append(fear_count)
    scores.append(joy_count)   
    scores.append(sadness_count)     
    scores.append(surprise_count) 
    scores.append(trust_count)

    zipped = list(zip(emotions, scores))
    
    #Find max sentiment
    prevailing_emotion = sorted(zipped, key = lambda x : x[1], reverse = True)[:3]
    if prevailing_emotion[0][1] == 0 or prevailing_emotion[0][1] == 1:
        return 'ουδέτερο'
    
    progress_count += 1
    print(str(round(100 * float(progress_count)/1438, 2)) + "%")
    return prevailing_emotion[0][0]






tweet_frame['Emotion'] = [extract_emotion(tweet) for tweet in tweet_frame['Lemmatized_Tokens']]
print(tweet_frame)
tweet_frame.to_csv(r'/Users/teoflev/Desktop/thesis_code/thesis/tweets/training_set_tweets.csv', index = None)