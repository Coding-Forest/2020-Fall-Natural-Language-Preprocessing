# -*- coding: utf-8 -*-
"""
# Topic modelling using LDA
How to Create an LDA Topic Model in Python with Gensim

**References**
SOURCE CODE FROM:

    Python Tutorials for Digital Humanities (2021)
    How to Create an LDA Topic Model in Python with Gensim (Topic Modeling for DH 03.03)
    https://www.youtube.com/watch?v=TKjjlp5_r7o&ab_channel=PythonTutorialsforDigitalHumanities

"""

# SETUP
import nltk
nltk.download('stopwords')

import numpy as np
import json
import glob # NEW

# Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

# spacy
import spacy
from nltk.corpus import stopwords

# vis
# !pip install pyLDAvis # (working as of Nov 2021)
import pyLDAvis
import pyLDAvis.gensim_models

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

#-------------------------------------------------------
# PRE-PROCESSING

def load_json(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return (data)

def write_json(file, data):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

stopwords = stopwords.words('english')



# Get data:
# !wget O ushmm_dn.json https://raw.githubusercontent.com/wjbmattingly/topic_modeling_textbook/main/data/ushmm_dn.json

data = load_json("/content/ushmm_dn.json")['texts']



# Lemmatisation: reduction of words to their root forms
# lemmatising function using spacy
def lemmatise(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    # Create spacy object
    # disable: computationally expensive but not necessary features. This allows the script to run a bit more quickly. 
    nlp = spacy.load("en_core_web_sm", disable=['parser', 'enr'])
    texts_out = []

    for text in texts:
        doc = nlp(text)
        new_text = []   # create a metadata object

        for token in doc:
            if token.pos_ in allowed_postags: # if the part of speech is in each token of the pos tags,
                new_text.append(token.lemma_)
        final = " ".join(new_text)
        texts_out.append(final)
    
    return (texts_out)


def gen_words(texts):
    final = []

    for text in texts:
        # get lemmatised words 
        new = gensim.utils.simple_preprocess(text, deacc=True) # deaccent: to remove the accent or stress from (a syllable)
        final.append(new)
    
    return (final)


lemmatised_texts = lemmatise(data)
data_words = gen_words(lemmatised_texts)

# Get word frequencies in tuple
id2word = corpora.Dictionary(data_words)

corpus = []
for text in data_words:
    new = id2word.doc2bow(text)
    corpus.append(new)

# example - Grab first tuple
word = id2word[[0][:1][0]] # word = able



# Create LDA topic model - all the words so far was preps for this step!
lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                            id2word=id2word,
                                            num_topics=30,    # this is a lot of topics for analysis. 
                                            random_state=100,
                                            update_every=1,   # update after each iteration
                                            chunksize=100,
                                            passes=10,        # pass over data 10 times 
                                            alpha='auto')

# Visualise data
pyLDAvis.enable_notebook()
vis = pyLDAvis.gensim_models.prepare(lda_model, corpus, id2word, mds='mmds', R=30)
vis

