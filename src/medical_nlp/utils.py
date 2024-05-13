from collections import Counter
import pandas as pd
import numpy as np


def get_vectors(sentence: str, nlp) -> np.ndarray:
    """Get Vectors from text using Spacy.

    Vectors are obtained after stopwords removal.
    A simple vector avg. is calculated for a given sentence.

    Args:
        sentence (str): sentence to process and get vectors from.
        nlp: Spacy's language Model.
    Returns:
        np.ndarray: mean of the vector representation of the sentence.
    """
    doc = nlp(sentence)
    cleaned_txt = " ".join(
        [token.lemma_ for token in doc if not token.is_stop]
    )

    return nlp(cleaned_txt).vector


def process_keywords(row: pd.Series) -> list:
    """Cleans and process the keywords column.

    Creates a list of keywords from the `keywords` column.
    in the mtsamples.csv dataset.

    Args:
        row (pd.Series): Row of keywords

    Returns:
        list: List of processed keywords.
    """
    res: list[str] = []
    if pd.notna(row):
        res = [str_.strip().lower() for str_ in row.split(",")]
    return res


def format_embeddings_for_clustering(vectors_series: pd.Series) -> np.ndarray:
    """Formats the embeddings from the `get_vectors` function.

    Allows the vectors to pass through a SKlearn fitting pipeline

    Args:
        vectors_series (pd.Series): Vectors as obtained by the
        get_vectors function.

    Returns:
        np.ndarray: Array of vectors formatted.
    """
    return np.array([v for v in vectors_series])


def get_most_common(
        list_: list,
        top_n: int = 10,
        exclude: list[str] = []
):
    counts = Counter(
        x for sublist in list_
        for x in sublist
        if x not in exclude
    ).most_common(top_n)
    return counts
