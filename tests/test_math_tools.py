import unittest
from math_tools import is_prime, calculate_quadratic, mean

class TestMathTools(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(1))

    def test_is_prime_edge_cases(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(-5))

    def test_calculate_quadratic(self):
        result = calculate_quadratic(2, 3, 1, 2)  # 2*4 + 3*2 + 1 = 15
        self.assertEqual(result, 15)

    def test_mean(self):
        self.assertEqual(mean([1, 2, 3]), 2)
        self.assertAlmostEqual(mean([1.0, 2.0, 3.0]), 2.0)

    def test_mean_empty_list(self):
        with self.assertRaises(ValueError):
            mean([])

    def test_mean_single_element(self):
        self.assertEqual(mean([42]), 42)

if __name__ == '__main__':
    unittest.main()
