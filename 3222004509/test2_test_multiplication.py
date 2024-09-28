import pytest
from myapp import calculate_answer

def test_simple_multiplication():
    result = calculate_answer("2 * 3")
    assert result == 6

def test_multiplication_with_addition():
    result = calculate_answer("(2 * 3) + 4")
    assert result == 10

def test_multiplication_with_subtraction():
    result = calculate_answer("(5 - 2) * 3")
    assert result == 9

def test_multiplication_with_divison():
    result = calculate_answer("(10 / 2) * 3")
    assert result == 15

def test_multiplication_commutative():
    result1 = calculate_answer("3 * 4")
    result2 = calculate_answer("4 * 3")
    assert result1 == result2 == 12

def test_multiplication_associative():
    result1 = calculate_answer("(1 * 2) * 3")
    result2 = calculate_answer("1 * (2 * 3)")
    assert result1 == result2 == 6

def test_multiplication_distributive():
    result1 = calculate_answer("2 * (3 + 4)")
    result2 = calculate_answer("2 * 3 + 2 * 4")
    assert result1 == result2 == 14

# Run the tests
if __name__ == "__main__":
    pytest.main()
