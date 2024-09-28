import pytest
from myapp import generate_number
from fractions import Fraction

def test_generate_integer():
    number = generate_number(10)
    assert isinstance(number, int)
    assert 1 <= number < 10

def test_generate_fraction():
    number = generate_number(10)
    if isinstance(number, Fraction):
        assert number < 1
        assert 1 <= number.numerator < 10
        assert 1 <= number.denominator < 10
        assert number.numerator < number.denominator

def test_boundary_value():
    number = generate_number(1)
    assert number == 1

def test_max_value():
    numbers = set()
    for _ in range(100):
        numbers.add(generate_number(100))
    assert all(1 <= n < 100 for n in numbers)

def test_fraction_less_than_one():
    numbers = set()
    for _ in range(100):
        number = generate_number(10)
        if isinstance(number, Fraction):
            numbers.add(number)
    assert all(n < 1 for n in numbers)

def test_integer_randomness():
    numbers = set()
    for _ in range(100):
        numbers.add(generate_number(10))
    assert len(numbers) > 1  # Check for randomness

def test_fraction_randomness():
    fractions = set()
    for _ in range(100):
        number = generate_number(10)
        if isinstance(number, Fraction):
            fractions.add((number.numerator, number.denominator))
    assert len(fractions) > 1  # Check for randomness

# Run the tests
if __name__ == "__main__":
    pytest.main()
