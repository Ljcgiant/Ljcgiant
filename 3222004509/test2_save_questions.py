import pytest
from myapp import save_questions
from pathlib import Path

def test_save_empty_questions():
    save_questions([])
    assert not Path("Exercises.txt").exists()

def test_save_single_question():
    save_questions(["2 + 3"])
    assert Path("Exercises.txt").read_text() == "2 + 3 = \n"

def test_save_multiple_questions():
    save_questions(["2 + 3", "4 - 1", "6 * 2"])
    assert Path("Exercises.txt").read_text() == "2 + 3 = \n4 - 1 = \n6 * 2 = \n"

def test_file_naming():
    save_questions(["2 + 3"])
    assert Path("Exercises.txt").exists()

def test_custom_file_naming():
    save_questions(["2 + 3"], filename="CustomQuestions.txt")
    assert Path("CustomQuestions.txt").exists()

def test_file_content_format():
    save_questions(["2 + 3"])
    assert Path("Exercises.txt").read_text() == "2 + 3 = \n"

def test_file_write_permission():
    with pytest.raises(PermissionError):
        save_questions(["2 + 3"], filename="/path/without/permission.txt")

def test_file_override():
    save_questions(["2 + 3"])
    save_questions(["4 - 1"])
    assert Path("Exercises.txt").read_text() == "4 - 1 = \n"

# Run the tests
if __name__ == "__main__":
    pytest.main()
