# thesis
Twitter Sentiment Analysis for Greek Tweets regarding Immigration

This repository is used for showing code I personally created regarding my thesis. The Thesis has the title "Targeted Sentiment 
Analysis on Immigration in Greek Society" and is being carried out under the supervision of K.G. Margaritis, a professor at 
the University of Macedonia.

The code is organized into folders, each with a name explaining its use. Each file is a Python script with part of the functionality
necessary.

All the .txt data are versions of the data that will be used for this analysis.

To recreate the results found on this thesis, run the files in the following order:

1) clean_data.py
2) preprocess_dataframe.py
3) polarity.py
4) emotion_extraction.py

To create the neural network, open the file cnn.py. This network uses embeddings created using word2vec found on the vectorize.py file. Both are in the directory called neural.
