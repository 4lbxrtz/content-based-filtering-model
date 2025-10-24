"""Entry point for the application."""

from cli import parse_args
from izan import buildTable

def main():
    args = parse_args()
    documents = args.documents
    stop_words = args.stopwords
    lemmatization = args.lemmatization
    buildTable(documents, stop_words, lemmatization)
    # for document in documents:
    #     print(f"Document name: {document}")

    # print(f"Stop Words: {stop_words}")
    # print(f"Lemmatization: {lemmatization}")


if __name__ == "__main__":
    main()
