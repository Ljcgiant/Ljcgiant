import pytest
from myapp import generate_questions

def test_generate_questions_count():
    questions = generate_questions(5, 10)
    assert len(questions) == 5

def test_generate_questions_uniqueness():
    questions = generate_questions(5, 10)
    assert len(questions) == len(set(questions))

def test_boundary_value():
    questions = generate_questions(1, 1)
    assert len(questions) == 1
    assert questions[0] == "1 "

def test_max_value():
    questions = generate_questions(100, 100)
    assert len(questions) == 100

def test_question_diversity():
    questions_set = set()
    for _ in range(100):
        questions_set.update(generate_questions(10, 10))
    assert len(questions_set) > 1  # Check for diversity

# Run the tests
if __name__ == "__main__":
    pytest.main()
