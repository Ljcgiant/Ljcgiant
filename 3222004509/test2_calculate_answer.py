import unittest
from myapp import calculate_answer

class TestCalculateAnswer(unittest.TestCase):
    def test_simple_addition(self):
        result = calculate_answer("1 + 2")
        print(f"Test '1 + 2': expected 3, got {result}")
        self.assertEqual(result, 3)

    def test_multiplication(self):
        result = calculate_answer("3 * 3")
        print(f"Test '3 * 3': expected 9, got {result}")
        self.assertEqual(int(result) if result.is_integer() else result, 9)


if __name__ == '__main__':
    unittest.main()
