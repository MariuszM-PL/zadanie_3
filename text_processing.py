import string

def count_words(text):
    """
    Liczy liczbę słów w tekście.

    Args:
        text (str): Tekst wejściowy.

    Returns:
        int: Liczba słów.
    """
    words = text.split()
    return len(words)


def remove_punctuation(text):
    """
    Usuwa znaki interpunkcyjne z tekstu.

    Args:
        text (str): Tekst wejściowy.

    Returns:
        str: Tekst bez znaków interpunkcyjnych.
    """
    return text.translate(str.maketrans('', '', string.punctuation))
