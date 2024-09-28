import pytest
from myapp import calculate_answer

def test_simple_addition():
    result = calculate_answer("2 + 3")
    assert result == 5

def test_addition_with_subtraction():
    result = calculate_answer("2 + 3 - 1")
    assert result == 4

def test_addition_with_multiplication():
    result = calculate_answer("2 + 3 * 2")
    assert result == 8

def test_addition_with_divison():
    result = calculate_answer("10 + 5 / 2")
    assert result == 12.5

def test_addition_commutative():
    result1 = calculate_answer("3 + 4")
    result2 = calculate_answer("4 + 3")
    assert result1 == result2 == 7

def test_addition_associative():
    result1 = calculate_answer("(1 + 2) + 3")
    result2 = calculate_answer("1 + (2 + 3)")
    assert result1 == result2 == 6

def test_addition_distributive():
    result1 = calculate_answer("2 * (3 + 4)")
    result2 = calculate_answer("2 * 3 + 2 * 4")
    assert result1 == result2 == 14

# Run the tests
if __name__ == "__main__":
    pytest.main()
