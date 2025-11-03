import math
from collections import Counter


def compute_all_words(docs):
    total_words = set()
    for doc in docs:
        for word in doc["words"]:
            total_words.add(word)
    return total_words


def compute_tf(docs, word_set):
    tf_list = []
    for doc in docs:
        tf_dict = {w: 0.0 for w in word_set}
        counts = Counter(doc["words"])
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
        vector_lenght += freq**2
    return math.sqrt(vector_lenght)


def normalize_vector(tf_log):
    normalized_list = []
    for tf_dict in tf_log:
        lenght = calculate_vector_lenght(tf_dict)
        normalized_tf = {}
        for term, freq in tf_dict.items():
            normalized_tf[term] = freq / lenght
        normalized_list.append(normalized_tf)
    return normalized_list

def calculate_cosine(vec1, vec2):
    cosine = 0
    for word in vec1:
        if word in vec2:
            cosine += vec1[word] * vec2[word]
    long1 = math.sqrt(sum(value * value for value in vec1.values()))
    long2 = math.sqrt(sum(value * value for value in vec2.values()))
    if long1 == 0 or long2 == 0:
        return 0.0
    return cosine / (long1 * long2)

def compute_cosine(normalized_list):
    result = {}
    for i in range(len(normalized_list)):
        for j in range(i + 1, len(normalized_list)):
            key = f"{i} - {j}"
            result[key] = calculate_cosine(normalized_list[i], normalized_list[j])
    return result
    


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
