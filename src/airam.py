import math
from collections import Counter  

with open("./data/stop-words/stop-words-en.txt", "r", encoding="utf-8") as file:
    stops = file.read()
with open("./data/examples-documents/document-01.txt", "r", encoding="utf-8") as file:
    content = file.read()

docs = []   # Set of files
docs.append(content)  # Simulate the real document collection
tf_list = []

# Calculate the TF
for doc in docs:
    words = doc.lower().split()
    total = len(words)
    counts = Counter(words)
    tf = {w: counts[w] / total for w in counts}
    tf_list.append(tf)

# Calculate the IDF
N = len(docs)
all_words = set()
for tf in tf_list:
    for word in tf.keys():
        all_words.add(word)

idf = {}

for word in all_words:
    df = 0
    for tf in tf_list:
        if word in tf:
            df += 1
    idf[word] = math.log(N /1 + df)
print (idf)

# Calculate TF-IDF

    

