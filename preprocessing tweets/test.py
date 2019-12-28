import pandas as pd

lexicon_frame1 = pd.read_csv('/Users/teoflev/Desktop/thesis_code/thesis/resources/greek_nrc.csv')
lexicon_frame2 = pd.read_csv('/Users/teoflev/Desktop/thesis_code/thesis/resources/gr_sentences.csv')

dataframes = [lexicon_frame1, lexicon_frame2]
lexicon_frame = pd.concat(dataframes)

lexicon_frame.to_csv(r'/Users/teoflev/Desktop/thesis_code/thesis/resources/full_lexicon.csv', index = None)