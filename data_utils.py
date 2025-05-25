def clean_missing_values(data):
    """
    Usuwa wartości None, puste stringi i inne "puste" elementy z listy.

    Args:
        data (list): Lista danych (dowolnych typów).

    Returns:
        list: Lista bez pustych wartości.
    """
    return [item for item in data if item not in (None, '', [], {}, ())]


def get_unique_elements(data):
    """
    Zwraca listę unikalnych elementów w kolejności ich pierwszego wystąpienia.

    Args:
        data (list): Lista danych.

    Returns:
        list: Lista unikalnych elementów.
    """
    seen = set()
    unique = []
    for item in data:
        if item not in seen:
            unique.append(item)
            seen.add(item)
    return unique
