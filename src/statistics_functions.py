import math
from collections import Counter


def compute_tf(docs):
    tf_list = []
    for doc in docs:
        counts = Counter(doc["words"])
        total = len(doc["words"])
        tf = {w: counts[w] / total for w in counts}
        tf_list.append(tf)
    return tf_list


def compute_idf(tf_list):
    N = len(tf_list)
    all_words = {w for tf in tf_list for w in tf.keys()}
    idf = {}
    for word in all_words:
        df = sum(1 for tf in tf_list if word in tf)
        idf[word] = math.log(N / (1 + df))
    return idf


def compute_tfidf(tf_list, idf):
    tfidf_list = []
    for tf in tf_list:
        tfidf = {w: tf[w] * idf[w] for w in tf}
        tfidf_list.append(tfidf)
    return tfidf_list
