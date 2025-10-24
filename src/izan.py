def term_index():
  pass


def term():
  pass

def tf(word, document):
  pass

def openDoc(documentName):
  try:
    dfile = open(documentName)
    return 1

  except Exception:
    exit(NameError)

import re
def getWords(docName):
  with open(docName, "r", encoding="utf-8") as file:
    text = file.read()
  return re.findall(r'\b\w+\b', text.lower())

def deleteStopWords(words, docName):
  with open(docName, "r", encoding="utf-8") as file:
    stopWords = [line.strip() for line in file if line.strip()]
  return [word for word in words if word not in stopWords]

import json
def lematiceWords(words, docName):
  with open(docName, "r", encoding="utf-8") as file:
    lemat = json.load(file)
  return [lemat.get(word, word) for word in words]


def buildTable(docName, stopWordsDocName, lemDocName):
  words = getWords(docName)
  words = deleteStopWords(words, stopWordsDocName)
  words = lematiceWords(words, lemDocName)
  


  

