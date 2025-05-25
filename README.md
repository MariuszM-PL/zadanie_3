# mylib

📦 **mylib** to prosta biblioteka Pythona zawierająca przydatne funkcje do przetwarzania danych, tekstów i obliczeń matematycznych.

## ✨ Główne funkcje

### `data_utils.py`
- `clean_missing_values(data)` – usuwa `None`, puste stringi, listy itp. z listy.
- `get_unique_elements(data)` – zwraca unikalne elementy zachowując kolejność.

### `math_tools.py`
- `is_prime(n)` – sprawdza, czy liczba jest pierwsza.
- `calculate_quadratic(a, b, c, x)` – oblicza wartość funkcji kwadratowej.
- `mean(data)` – oblicza średnią arytmetyczną.

### `text_processing.py`
- `count_words(text)` – liczy słowa w tekście.
- `remove_punctuation(text)` – usuwa znaki interpunkcyjne.

## 🚀 Instalacja

Po prostu sklonuj repozytorium lub pobierz projekt, a następnie importuj moduły bezpośrednio z plików Python:

```python
from data_utils import clean_missing_values
from math_tools import is_prime
from text_processing import count_words
```

## ✅ Testy

Uruchom wszystkie testy:
```bash
python -m unittest discover -s tests -p "test_*.py"
```

## 🧪 Przykłady użycia

```python
from data_utils import clean_missing_values
print(clean_missing_values([1, None, '', 2]))  # [1, 2]

from math_tools import is_prime
print(is_prime(7))  # True

from text_processing import count_words
print(count_words("To jest test."))  # 3
```

## 👤 Autor

Mariusz Mikołajczyk  
📧 Kontakt: mmikolajczyk93@hotmail.com

## 📄 Licencja

MIT License
