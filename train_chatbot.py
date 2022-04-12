"""
train_chatbot.py
    ... build the model and train our chatbot
"""

# importing necessary packages
# nltk
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

import json  # json
import pickle  # pickle

import numpy as np  # numpy

# keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random

# tokenizing data
# tokenizing... the process of converting a word into its
# lemma form and then creating a pickle file to store the
# Python objects which we will use while predicting.

def tokenize_data(json_file_name):
    """ tokenizing data (json format)
        ... converts a word into its lemma form and then creates a
            pickle file to store the Python objects (use for predicting)
    """
    # loading data
    data_file = open(json_file_name).read()
    intents = json.loads(data_file)

    words=[] # a list of unique lemmatized words
    classes = [] # a list of classes for tags
    documents = [] # combination between patterns and intents

    for intent in intents['intents']:
        for pattern in intent['patterns']:

            # tokenize each word
            word = nltk.word_tokenize(pattern)
            # extend words-list by appending word
            words.extend(word)
            # add documents in the corpus
            documents.append((word, intent['tag']))

            if intent['tag'] not in classes:
                classes.append(intent['tag'])

    # print(words) # (v1)

    ignore_words = ['?', '!', '@']
    # lemmatize, lower each word and remove duplicates
    words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]

    words = sorted(list(set(words))) # sort words
    classes = sorted(list(set(classes))) # sort classes

    # print(words) # (v2) 

    # creating a pickle file for words to store the Python objects
    pickle.dump(words,open('words.pkl','wb'))
    # creating a pickle file for classes to store the Python objects
    pickle.dump(classes,open('classes.pkl','wb'))

    return words, classes, documents

def print_data(words, classes, documents):
    # documents = combination between patterns and intents
    print(len(documents), "documents", documents)
    print()
    # print(documents) # (v3)
    # classes = intents
    print (len(classes), "classes", classes)
    print()
    # words = all words, vocabulary
    print (len(words), "unique lemmatized words", words)

""" 
Training and Testing Data
"""
def create_training(words, classes, documents):
    """creating training data
    """
    training = []
    # create an empty array for our output
    output_empty = [0] * len(classes)

    for doc in documents:
        # initialize our bag of words
        bag = []
        # list of tokenized words for the pattern
        pattern_words = doc[0]
        # lemmatize each word 
        # - create base word, in attempt to represent related words
        pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
        # print(f"pattern_words:{pattern_words}")
        # create our bag of words array with 1, if word match found in current pattern
        for w in words:
            bag.append(1) if w in pattern_words else bag.append(0)
        # print(f"bag: {bag}")
        # output is a '0' for each tag and '1' for current tag (for each pattern)
        output_row = list(output_empty)
        output_row[classes.index(doc[1])] = 1
        
        training.append([bag, output_row])

    return training

def train_data(training):
    """shuffle training data and split to train_X (patterns) 
       and train_y (intents (tags))
    """
    # print(training)
    # shuffle our features and turn into np.array
    random.shuffle(training)
    training = np.array(training)
    # create train and test lists.  
    train_X = list(training[:,0])  # X - patterns
    train_y = list(training[:,1])  # Y - intents

    print("Training data created")
    #print(f"x:{train_X}")
    #print(f"y:{train_y}")

    return train_X, train_y

""" 
#Building model... Keras sequential API
"""
def build_model(name, train_X, train_y):
    """build a chatbot model using Keras sequential API
    """
    # Create model 
    # - 3 layers. First layer 128 neurons, second layer 64 neurons and 
    # 3rd output layer contains number of neurons equal to number of 
    # intents to predict output intent with softmax
    model = Sequential()
    model.add(Dense(128, input_shape=(len(train_X[0]),), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(len(train_y[0]), activation='softmax'))

    # Compile model.
    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

    #fitting and saving the model 
    hist = model.fit(np.array(train_X), np.array(train_y), epochs=200, batch_size=5, verbose=1)
    model.save(name, hist)

    print("model created")

if True:
    json_file_name = 'intents.json'
    # 1. tokenizing data
    words, classes, documents = tokenize_data(json_file_name)

    #print_data(words, classes, documents)

    # 2. creating training data
    training_data = create_training(words, classes, documents)
    # shuffle and split to patterns and intents
    train_X, train_y = train_data(training_data)

    # 3. build a model
    build_model('Ren2021.h5', train_X, train_y)
