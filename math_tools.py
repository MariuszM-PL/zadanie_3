def is_prime(n):
    """
    Sprawdza, czy podana liczba jest liczbą pierwszą.

    Args:
        n (int): Liczba całkowita do sprawdzenia.

    Returns:
        bool: True jeśli liczba jest pierwsza, False w przeciwnym razie.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def calculate_quadratic(a, b, c, x):
    """
    Oblicza wartość funkcji kwadratowej ax^2 + bx + c.

    Args:
        a (float): Współczynnik a.
        b (float): Współczynnik b.
        c (float): Współczynnik c.
        x (float): Wartość zmiennej x.

    Returns:
        float: Wynik działania funkcji kwadratowej.
    """
    return a * x ** 2 + b * x + c


def mean(data):
    """
    Oblicza średnią arytmetyczną z listy liczb.

    Args:
        data (list of float): Lista liczb.

    Returns:
        float: Średnia arytmetyczna.

    Raises:
        ValueError: Jeśli lista jest pusta.
    """
    if not data:
        raise ValueError("Lista nie może być pusta")
    return sum(data) / len(data)
