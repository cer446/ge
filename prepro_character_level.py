# -*- coding: utf-8 -*-
"""
@Author: Viola

This module pre-processes the datasets before passed into the model.
It maps the de-en sentence pairs with tokenized words to sequences.

"""

import re
import random
import collections
import torch
import numpy as np
import nltk

#%%
    
PATH = './de-en/'

END = "<EOS>"
END_PADDING = "<PAD>"
UNKNOWN = "<UNK>"

def load_data(path):
    data = []
    with open(path) as f:
        for i, line in enumerate(f): 
            example = {}

            if line.startswith('<'):
                continue
            
            text = line.strip()
            example['text'] = text[:]

            data.append(example)

    random.seed(1)
    random.shuffle(data)
    return data

#%%
train_de = load_data(PATH + 'train.tags.de-en.de')
train_en = load_data(PATH + 'train.tags.de-en.en')

#%%
def build_corpus(dataset_from, dataset_to):

    corpus = []

    for tt_from, tt_to in zip(dataset_from, dataset_to):

        tokens_from = nltk.word_tokenize(tt_from['text']) + [END]
        tokens_to = nltk.word_tokenize(tt_to['text']) + [END]

        s_from = " ".join(tokens_from)
        s_to = " ".join(tokens_to)
        
        corpus.append(" ".join([s_from, s_to]))

    return " \n".join(corpus)


corpus_from_to = build_corpus(train_de, train_en)
with open("DATA_processed.txt", "w") as f:
    f.write(corpus_from_to)