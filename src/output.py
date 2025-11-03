from etl import deleteStopWords, getWords, lematiceWords
from statistics_functions import (
    compute_cosine,
    compute_tf,
    compute_idf,
    compute_tfidf,
    compute_log_tf,
    normalize_vector,
    compute_all_words,
)
from tabulate import tabulate


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
                    "first_index": next((w[1] for w in doc["words"] if w[0] == word), None),
                    "TF": tf_list[i][word],
                    "TF(log)": tf_log[i][word],
                    "Normalized": normalized[i][word],
                    "IDF": idf.get(word, 0.0),
                    "TF-IDF": tfidf_list[i][word],
                }
            )
        tables.append({"doc": doc["name"], "rows": rows})
    return tables


def display_cosine_table(docs, normalized_list):
    cosine_results = compute_cosine(normalized_list)
    headers = ["Par de Documentos", "Similitud Coseno"]
    data = [
        [
            f"{docs[int(pair.split(' - ')[0])]['name']} ↔ {docs[int(pair.split(' - ')[1])]['name']}",
            f"{value:.4f}",
        ]
        for pair, value in cosine_results.items()
    ]

    print("\n📊 Similitud Coseno entre Documentos")
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))


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

    # Output with tabulate
    for table in tables:
        print(f"\n📄 {table['doc']}")
        headers = ["WORD","FIRST INDEX","TF", "TF(log)", "Normalized", "IDF", "TF-IDF"]
        data = [
            [
                row["word"],
                f"{row['first_index']}",
                f"{row['TF']:.4f}",
                f"{row['TF(log)']:.4f}",
                f"{row['Normalized']:.4f}",
                f"{row['IDF']:.4f}",
                f"{row['TF-IDF']:.4f}",
            ]
            for row in table["rows"]
        ]
        print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

    if len(docs) > 1:
        display_cosine_table(docs, normalized)

    return tables
