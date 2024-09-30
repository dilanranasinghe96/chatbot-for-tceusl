import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np
import json
import pickle

nltk.download('punkt')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

def load_intents(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def preprocess_data(intents):
    words = []
    classes = []
    documents = []
    ignore_words = ['?', '!']
    
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            word_list = nltk.word_tokenize(pattern)
            words.extend(word_list)
            documents.append((word_list, intent['tag']))
            if intent['tag'] not in classes:
                classes.append(intent['tag'])
    
    words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
    words = sorted(list(set(words)))

    classes = sorted(list(set(classes)))

    return words, classes, documents

def save_preprocessed_data(words, classes, file_name):
    with open(file_name, 'wb') as file:
        pickle.dump((words, classes), file)
