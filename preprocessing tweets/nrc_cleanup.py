import pandas as pd
import time

nrc = pd.read_csv("/Users/teoflev/Desktop/thesis_code/thesis/resources/nrc_csv.csv", sep=';')

def findit(row):
    feelings = []
    for column in nrc:
        if str(nrc.iloc[row][column]) == '1':
            feelings.append(str(column).lower())

    return(feelings)

nrc['Emotion'] = [findit(row) for row in nrc['Text'].index]

nrc = nrc[nrc.astype(str)['Emotion'] != '[]']
nrc.to_csv(r'/Users/teoflev/Desktop/thesis_code/thesis/resources/nrc_el.csv', index = None)