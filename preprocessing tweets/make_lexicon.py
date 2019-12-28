import nltk 
import pandas as pd
import re


emotions = ('anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust')


#----CROWDFLOWER 1---------------------------------
crowdflower1 = pd.read_csv('/Users/teoflev/Desktop/thesis_code/thesis/resources/crowdFlower/text_emotion.csv', sep=",")
crowdflower1 = crowdflower1.drop('tweet_id', axis = 1)
crowdflower1 = crowdflower1.drop('author', axis = 1)

# Remove Username
crowdflower1['Content'] = [re.sub('@[^\s]+','',str(entry)) for entry in crowdflower1.content]
crowdflower1 = crowdflower1.drop('content', axis = 1)
crowdflower1['Content'] = [(str(entry)) for entry in crowdflower1.Content]

# Drop unneccesary sentiment 
crowdflower1 = crowdflower1[crowdflower1['sentiment'].isin(emotions)]


crowdflower1.to_csv(r'/Users/teoflev/Desktop/thesis_code/thesis/resources/crowdflower1frame.csv', index = None)

#----CROWDFLOWER 2---------------------------------

crowdflower2 = pd.read_csv('/Users/teoflev/Desktop/thesis_code/thesis/resources/crowdFlower/text_emotion2.txt', sep="  ")

crowdflower2['Content'] = [(str(entry)) for entry in crowdflower2.content]
crowdflower2 = crowdflower2.drop('content', axis = 1)

# Drop unneccesary sentiment 
crowdflower2 = crowdflower2[crowdflower2['sentiment'].isin(emotions)]


crowdflower2.to_csv(r'/Users/teoflev/Desktop/thesis_code/thesis/resources/crowdflower2frame.csv', index = None)

#----ISEAR ---------------------------------

isear = pd.read_csv('/Users/teoflev/Desktop/thesis_code/thesis/resources/ISEAR/isear.csv', sep="---", error_bad_lines=False)

isear['Content'] = [(str(entry)) for entry in isear.content]
isear = isear.drop('content', axis = 1)

# Drop unneccesary sentiment 
isear = isear[isear['sentiment'].isin(emotions)]


isear.to_csv(r'/Users/teoflev/Desktop/thesis_code/thesis/resources/isearframe.csv', index = None)

#----NRC ---------------------------------

nrc = pd.read_csv('/Users/teoflev/Desktop/thesis_code/thesis/resources/NRC/NRC-Emotion-Lexicon-Wordlevel-v0.92.txt', sep= '--', error_bad_lines=False)

nrc['Content'] = [(str(entry)) for entry in nrc.content]
nrc = nrc.drop('content', axis = 1)
nrc = nrc.drop('irrelevant', axis = 1)
# Drop unneccesary sentiment 
nrc = nrc[nrc['sentiment'].isin(emotions)]

nrc.to_csv(r'/Users/teoflev/Desktop/thesis_code/thesis/resources/nrcframe.csv', index = None)

#----COMBINATION ---------------------------------

dataframes = [crowdflower1, crowdflower2, isear]
lexicon_frame = pd.concat(dataframes)

lexicon_frame.to_csv(r'/Users/teoflev/Desktop/thesis_code/thesis/resources/sentences.csv', index = None)
print(lexicon_frame)

