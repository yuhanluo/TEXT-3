import nltk
from nltk.stem.lancaster import LancasterStemmer
from nltk.tokenize import sent_tokenize
from nltk.corpus import brown
import os
from os.path import join
import numpy as np
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import functions as f
from gensim.models.word2vec import Word2Vec

#model = "hello"
model = Word2Vec.load_word2vec_format("/Users/luo/desktop/GoogleNews-vectors-negative300.bin.gz", binary = True)


def simplify(s):
    news_text = brown.words()
    emma = nltk.corpus.gutenberg.words()
    r = nltk.corpus.reuters.words()
    corpus = emma + news_text
    corpus += r
    fdist = nltk.FreqDist(w.lower() for w in corpus)

    res = ''
    st = LancasterStemmer()

    text = nltk.word_tokenize(s)
    tags = nltk.pos_tag(text)

    for tag in tags:
        word = tag[0]
        if f.checkPos(tag[1]):
                if word in model:
                    word_stem = st.stem(word)
                    top_words = model.most_similar(positive=[word], topn = 20)
                    candidate_list = [w[0] for w in top_words]
                    freq_list = [fdist[w] for w in candidate_list]
                    c_f_list = zip(candidate_list, freq_list)
                    ordered_list = sorted(c_f_list, key=lambda c_f_list:c_f_list[1], reverse=True)
                    word_freq = fdist[word]
                    #			synonmys = f.getSynonmys(word)  ## get synonmys from wordnet
                    # print synonmys
                    for w in ordered_list:
                        if not f.freq_diff(word_freq, w[1]):  ## break for loop if candidate word frequency does not exceed the word frequency by a threshold
                            break
                            if st.stem(w[0]) != word_stem and f.samePos(word, w[0]): ##exclude morphological derivations and same pos
                                word = w[0]  ### do not use wordnet

        res = res + word + ' '
    return res