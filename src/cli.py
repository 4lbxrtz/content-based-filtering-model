"""Parser module."""

import argparse


def parse_args():
    """
    Parse command-line arguments for the content-based recommendation system.

    Arguments:
      -d, --documents (str, required): Directorio o lista de ficheros de texto plano (.txt).
      -s, --stopwords (str, required): Fichero con palabras de parada a descartar.
      -l, --lemmatization (str, required): Fichero con las reglas o equivalencias de lematización.

    Returns
    -------
      argparse.Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Sistema de recomendación basado en contenido"
    )

    parser.add_argument(
        "-d",
        "--documents",
        required=True,
        nargs="+",
        help=(
            "Conjunto de ficheros de texto plano (.txt) o un directorio que los contenga."
            "Ejemplo: ./examples-documents/*.txt"
        ),
    )

    parser.add_argument(
        "-s",
        "--stopwords",
        required=True,
        help="Fichero con palabras de parada a descartar (stop words) durante el proceso de recomendación.",
    )

    parser.add_argument(
        "-l",
        "--lemmatization",
        required=True,
        help="Fichero con reglas de lematización de términos.",
    )

    return parser.parse_args()
