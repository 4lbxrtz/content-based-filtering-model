import json
import re

from airam import compute_tf_idf


def getWords(docNames):
    docs = []
    for docName in docNames:
        with open(docName, encoding="utf-8") as file:
            text = file.read()
        words = re.findall(r"\b\w+\b", text.lower())
        docs.append({"name": docName, "words": words})
    return docs


def deleteStopWords(docs, stopWordsFile):
    with open(stopWordsFile, encoding="utf-8") as file:
        stopWords = [line.strip() for line in file if line.strip()]
    for doc in docs:
        doc["words"] = [w for w in doc["words"] if w not in stopWords]
    return docs


def lematiceWords(docs, lemFile):
    with open(lemFile, encoding="utf-8") as file:
        lemat = json.load(file)
    for doc in docs:
        doc["words"] = [lemat.get(w, w) for w in doc["words"]]
    return docs


def buildTable(docNames, stopWordsFile, lemFile):
    docs = getWords(docNames)
    docs = deleteStopWords(docs, stopWordsFile)
    docs = lematiceWords(docs, lemFile)

    tfidf_list, idf = compute_tf_idf(docs)

    # Example output
    for i, doc in enumerate(docs):
        print(f"\n📄 {doc['name']}")
        print(
            f"Top TF-IDF words: {sorted(tfidf_list[i].items(), key=lambda x: x[1], reverse=True)[:5]}"
        )

    return docs, tfidf_list, idf
