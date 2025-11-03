import json
import re


def getWords(docNames):
    docs = []
    for docName in docNames:
        with open(docName, encoding="utf-8") as file:
            text = file.read()
        words = re.findall(r"[A-Za-zÀ-ÿ]+(?:[-’'][A-Za-zÀ-ÿ]+)*", text.lower())
        words_with_index = [(w, i) for i, w in enumerate(words, 1)]
        docs.append({"name": docName, "words": words_with_index})
    return docs


def deleteStopWords(docs, stopWordsFile):
    with open(stopWordsFile, encoding="utf-8") as file:
        stopWords = [line.strip() for line in file if line.strip()]
    for doc in docs:
        doc["words"] = [w for w in doc["words"] if w[0] not in stopWords]
    return docs


def lematiceWords(docs, lemFile):
    with open(lemFile, encoding="utf-8") as file:
        lemat = json.load(file)
    for doc in docs:
        doc["words"] = [(lemat.get(w[0], w[0]), w[1]) for w in doc["words"]]
    return docs
