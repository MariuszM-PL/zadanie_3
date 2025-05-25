import unittest
from data_utils import clean_missing_values, get_unique_elements

class TestDataUtils(unittest.TestCase):

    def test_clean_missing_values(self):
        data = [1, None, 2, '', 3, [], {}, (), 4]
        result = clean_missing_values(data)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_clean_missing_values_empty(self):
        self.assertEqual(clean_missing_values([]), [])

    def test_get_unique_elements(self):
        data = [1, 2, 2, 3, 1, 4]
        result = get_unique_elements(data)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_get_unique_elements_empty(self):
        self.assertEqual(get_unique_elements([]), [])

if __name__ == '__main__':
    unittest.main()
