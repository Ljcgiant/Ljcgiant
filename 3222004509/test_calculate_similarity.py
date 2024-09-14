import unittest
from main import calculate_similarity

class TestCalculateSimilarity(unittest.TestCase):
    def test_identical_strings(self):
        self.assertEqual(calculate_similarity("hello", "hello"), 1.0)

    def test_different_strings(self):
        self.assertEqual(calculate_similarity("hello", "world"), 0.0)

    def test_one_string_longer(self):
        self.assertLess(calculate_similarity("hello", "helloooo"), 1.0)

    def test_empty_strings(self):
        self.assertEqual(calculate_similarity("", ""), 1.0)

    def test_one_empty_string(self):
        self.assertEqual(calculate_similarity("hello", ""), 0.0)

    def test_strings_with_punctuation(self):
        self.assertEqual(calculate_similarity("hello!", "hello"), 0.0)  # 取决于预处理

    def test_strings_with_numbers(self):
        self.assertEqual(calculate_similarity("hello2", "hello3"), 0.0)  # 取决于预处理

    def test_strings_with_whitespace(self):
        self.assertEqual(calculate_similarity("hello world", "hello world"), 1.0)

    def test_strings_with_case_difference(self):
        self.assertEqual(calculate_similarity("Hello", "hello"), 1.0)  # 取决于预处理

if __name__ == '__main__':
    unittest.main()
