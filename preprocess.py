import nltk
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import difflib

import pandas as pd

#Function to get rid of punctuations, stop words and converting to lower case
def word_extractor(sentence):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens =tokenizer.tokenize(sentence)
    tokens=[token.lower() for token in tokens]
    tokens = [token for token in tokens if not token in stopwords.words()]
    return tokens

#Function to match the output from word_extractor() with our vocabulary of symptoms
def symptoms(symptoms):
    final_symptoms = []
    final_symptoms_flat = []
    df_train = pd.read_csv('dataset/training_data.csv', delimiter=',')
    vocab = df_train.columns.tolist()
    
    for symptom in symptoms:
        final_symptoms.append(difflib.get_close_matches(symptom, vocab, cutoff=0.6))
    for sublist in final_symptoms:
        for item in sublist:
            final_symptoms_flat.append(item)
            
    return set(final_symptoms_flat)