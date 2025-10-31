import math
from collections import Counter

def compute_all_words(docs):
    total_words = set()
    for doc in docs:
        for word in doc['words']:
            total_words.add(word)
    return total_words

def compute_tf(docs, word_set):
    tf_list = []
    for doc in docs:
        tf_dict = {w: 0.0 for w in word_set}
        counts = Counter(doc['words'])
        for word in counts:
            tf_dict[word] = counts[word]
        tf_list.append(tf_dict)
    return tf_list  

def compute_log_tf(tf_list):
    log_tf_list = []
    for tf_dict in tf_list:
        log_tf = {}
        for term, freq in tf_dict.items():
            if freq == 0:
                log_tf[term] = 0
            else:
                log_tf[term] = 1 + math.log10(freq)
        log_tf_list.append(log_tf)
    return log_tf_list

def calculate_vector_lenght(tf_log):
    vector_lenght = 0
    for term, freq in tf_log.items():
            vector_lenght += freq ** 2
    return (math.sqrt(vector_lenght))

def normalize_vector(tf_log):
    normalized_list = []
    for tf_dict in tf_log:
        lenght = calculate_vector_lenght(tf_dict)
        normalized_tf = {}
        for term, freq in tf_dict.items():
            normalized_tf[term] = freq / lenght
        normalized_list.append(normalized_tf)
    return normalized_list
        


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


    


# print(calculate_vector_lenght([2.322, 2.38, 0, 1.3, 1.3]))
# print(compute_log_tf([21, 24, 0, 2, 2]))
# print(normalize_vector(compute_log_tf([21, 24, 0, 2, 2]), calculate_vector_lenght(compute_log_tf([21, 24, 0, 2, 2]))))