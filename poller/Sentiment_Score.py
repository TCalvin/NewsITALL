from __future__ import print_function
import nltk, re
from nltk.corpus import stopwords
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalMaxPooling1D
from keras.datasets import imdb
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences


# set parameters:


class Sentiment_Analysis:
    def __init__(self):
        self.tk = Tokenizer()

        # set parameters:
        max_features = 20000
        maxlen = 400
        batch_size = 32
        embedding_dims = 50
        filters = 250
        kernel_size = 3
        hidden_dims = 250
        epochs = 2

        (x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)

        x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
        x_test = sequence.pad_sequences(x_test, maxlen=maxlen)

        model = Sequential()

        # we start off with an efficient embedding layer which maps
        # our vocab indices into embedding_dims dimensions
        model.add(Embedding(max_features,
                            embedding_dims,
                            input_length=maxlen))
        model.add(Dropout(0.2))

        # we add a Convolution1D, which will learn filters
        # word group filters of size filter_length:
        model.add(Conv1D(filters,
                         kernel_size,
                         padding='valid',
                         activation='relu',
                         strides=1))
        # we use max pooling:
        model.add(GlobalMaxPooling1D())

        # We add a vanilla hidden layer:
        model.add(Dense(hidden_dims))
        model.add(Dropout(0.2))
        model.add(Activation('relu'))

        # We project onto a single unit output layer, and squash it with a sigmoid:
        model.add(Dense(1))
        model.add(Activation('sigmoid'))

        model.compile(loss='binary_crossentropy',
                      optimizer='adam',
                      metrics=['accuracy'])
        model.fit(x_train, y_train,
                  batch_size=batch_size,
                  epochs=epochs,
                  validation_data=(x_test, y_test))

        self.model = model

    def clean_text(self, text, remove_stopwords=True):
        '''Clean the text, with the option to remove stopwords'''

        # Convert words to lower case and split them
        text = text.lower().split()

        # Optionally, remove stop words
        if remove_stopwords:
            stops = set(stopwords.words("english"))
            text = [w for w in text if not w in stops]

        text = " ".join(text)

        # Clean the text
        text = re.sub(r"<br />", " ", text)
        text = re.sub(r"[^a-z]", " ", text)
        text = re.sub(r"   ", " ", text)  # Remove any extra spaces
        text = re.sub(r"  ", " ", text)

        # Return a list of words
        return (text)

    def get_score(self, post):

        post = self.clean_text(str(post))
        dictionary_words = imdb.get_word_index()
        words = post.split()
        review = []
        for word in words:
            if word.lower() not in dictionary_words:
                review.append(2)
            elif dictionary_words[word.lower()] > 19997:
                review.append(2)
            else:
                review.append(dictionary_words[word.lower()] + 3)

        review = pad_sequences([review], truncating='pre', padding='pre', maxlen=400)
        return self.model.predict(review)[0][0]

# model = Sentiment_Analysis()

# model.get_score("Donald trump has been doing very bad things")
