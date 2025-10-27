"""Entry point for the application."""

from cli import parse_args
from output import buildTable


def main():
    args = parse_args()
    documents = args.documents
    stop_words = args.stopwords
    lemmatization = args.lemmatization
    buildTable(documents, stop_words, lemmatization)


if __name__ == "__main__":
    main()
