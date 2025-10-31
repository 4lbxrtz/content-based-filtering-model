from etl import deleteStopWords, getWords, lematiceWords
from statistics_functions import compute_tf, compute_idf, compute_tfidf, compute_log_tf,normalize_vector, compute_all_words


def build_word_table(docs, tf_list, tf_log, normalized, idf, tfidf_list):
    """
    Build one table per document:
    [{ "word": ..., "TF": ..., "IDF": ..., "TF-IDF": ... }, ...]
    """
    tables = []
    for i, doc in enumerate(docs):
        rows = []
        for word in tf_list[i]:
            rows.append(
                {
                    "word": word,
                    "TF": tf_list[i][word],
                    "TF(log)": tf_log[i][word],
                    "Normalized": normalized[i][word],
                    "IDF": idf.get(word, 0.0),
                    "TF-IDF": tfidf_list[i][word],
                    
                }
            )
        tables.append({"doc": doc["name"], "rows": rows})
    return tables


def buildTable(docNames, stopWordsFile, lemFile):
    # ETL
    docs = getWords(docNames)
    docs = deleteStopWords(docs, stopWordsFile)
    docs = lematiceWords(docs, lemFile)

    # Calculations
    word_set = compute_all_words(docs)
    tf_list = compute_tf(docs, word_set)
    tf_log = compute_log_tf(tf_list)
    normalized = normalize_vector(tf_log)
    idf = compute_idf(tf_list)
    tfidf_list = compute_tfidf(tf_list, idf)

    # Tables
    tables = build_word_table(docs, tf_list, tf_log, normalized, idf, tfidf_list)

    # Output
    for table in tables:
        print(f"\n📄 {table['doc']}")
        print(f"{'WORD':<15}{'TF':<10}{'TF(log)':<10}{'Normalized':<10}{'IDF':<10}{'TF-IDF':<10}")
        for row in table["rows"]:
            print(
                f"{row['word']:<15}{row['TF']:<10.4f}{row['TF(log)']:<10.4f}{row['Normalized']:<10.4f}{row['IDF']:<10.4f}{row['TF-IDF']:<10.4f}"
            )

    return tables
