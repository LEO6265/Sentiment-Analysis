import re
import os
import pickle
from sklearn.feature_extraction.text import HashingVectorizer


curr_dir = os.path.dirname(__file__)
stop = pickle.load(open(os.path.join(curr_dir, 'pkl_objects', 'stopwords.pkl'), 'rb'))


def tokenizer(text):

    text = re.sub('<[^>]*>', '', text)
    emoticons = re.findall(r'(?::|;|=)(?:-)?(?:\)|\(|D|P)',
    text.lower())
    text = re.sub(r'[\W]+', ' ', text.lower()) \
    + ' '.join(emoticons).replace('-', '')
    tokenized = [w for w in text.split() if w not in stop]
    
    return tokenized


vect = HashingVectorizer(decode_error='ignore',
                         n_features = 2**21,
                         preprocessor=None,
                         tokenizer=tokenizer)