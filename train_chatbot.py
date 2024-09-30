import json
import pickle
import numpy as np
import random
import nltk

from nltk.stem import WordNetLemmatizer
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Load intents file
data_file = open('data/intents.json').read()
intents = json.loads(data_file)

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Lists for words, classes, and documents
words = []
classes = []
documents = []
ignore_words = ['?', '!', '.', ',']

# Preprocess the intents data
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # Tokenize each word in the sentence
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        # Add to documents
        documents.append((word_list, intent['tag']))
        # Add to classes if not already there
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Lemmatize, lower each word, and remove duplicates
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

# Sort classes
classes = sorted(list(set(classes)))

# Create training data
training = []
output_empty = [0] * len(classes)

for doc in documents:
    # Initialize bag of words
    bag = []
    # List of tokenized words for the pattern
    pattern_words = doc[0]
    # Lemmatize each word
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    # Create bag of words array
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)
    
    # Output is '0' for each tag and '1' for current tag
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    # Debugging prints
    if len(bag) != len(words) or len(output_row) != len(classes):
        print(f"Mismatch in lengths: bag length {len(bag)}, output_row length {len(output_row)}")
    
    training.append([bag, output_row])

# Convert to numpy array safely
try:
    training = np.array(training, dtype=object)
except Exception as e:
    print(f"Error converting to numpy array: {e}")

# Split the data into features (X) and labels (y)
train_x = list(training[:, 0])
train_y = list(training[:, 1])

# Define the model
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compile the model
sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Train the model
model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)

# Save the model and data structures
model.save('models/chatbot_model.h5')
pickle.dump({'words': words, 'classes': classes, 'train_x': train_x, 'train_y': train_y}, open('training_data.pkl', 'wb'))

print("Model training complete.")
