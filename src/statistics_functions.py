import math
from collections import Counter


def compute_tf(docs):
    tf_list = []
    for doc in docs:
        counts = Counter(doc["words"])
<<<<<<< Updated upstream
        total = len(doc["words"])
        tf = {w: counts[w] / total for w in counts}
=======
        tf = {w: counts[w] for w in counts}
>>>>>>> Stashed changes
        tf_list.append(tf)
    return tf_list

def calculate_vector_lenght(list):
    vector_lenght = 0
    for element in list:
        vector_lenght += element ** 2
    return math.sqrt(vector_lenght)
        
    

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

def normalize_vector(non_normalized_vector, lenght):
    return [w/lenght for w in non_normalized_vector]
    


# print(calculate_vector_lenght([2.322, 2.38, 0, 1.3, 1.3]))
# print(compute_log_tf([21, 24, 0, 2, 2]))
# print(normalize_vector(compute_log_tf([21, 24, 0, 2, 2]), calculate_vector_lenght(compute_log_tf([21, 24, 0, 2, 2]))))