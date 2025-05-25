import unittest
from text_processing import count_words, remove_punctuation

class TestTextProcessing(unittest.TestCase):

    def test_count_words(self):
        text = "To jest przykładowe zdanie."
        self.assertEqual(count_words(text), 4)

    def test_count_words_empty(self):
        self.assertEqual(count_words(""), 0)

    def test_remove_punctuation(self):
        text = "Cześć! Jak się masz?"
        result = remove_punctuation(text)
        self.assertEqual(result, "Cześć Jak się masz")

    def test_remove_punctuation_only_punct(self):
        self.assertEqual(remove_punctuation("!?.,"), "")

if __name__ == '__main__':
    unittest.main()
