import pytest
from myapp import calculate_answer
from fractions import Fraction

def test_simple_addition():
    result = calculate_answer("2 + 3")
    assert result == 5

def test_simple_subtraction():
    result = calculate_answer("5 - 2")
    assert result == 3

def test_simple_multiplication():
    result = calculate_answer("3 * 4")
    assert result == 12

def test_simple_divison():
    result = calculate_answer("8 / 2")
    assert result == 4

def test_expression_with_parentheses():
    result = calculate_answer("(3 + 2) * 2")
    assert result == 10

def test_expression_with_negative_numbers():
    result = calculate_answer("-2 + 3")
    assert result == 1

def test_expression_with_decimals():
    result = calculate_answer("3 * 0.5")
    assert result == 1.5

def test_expression_with_floats():
    result = calculate_answer("2.5 + 3.5")
    assert result == 6.0

def test_expression_with_fractions():
    result = calculate_answer("1/2 + 1/3")
    assert result == Fraction(5, 6)

def test_expression_with_large_integers():
    result = calculate_answer("1234567890 + 987654321")
    assert result == 2147483211

# Run the tests
if __name__ == "__main__":
    pytest.main()
