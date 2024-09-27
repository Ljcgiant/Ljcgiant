import argparse
import random
from fractions import Fraction
from sympy import sympify

def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate arithmetic questions and validate answers.")
    parser.add_argument("-n", type=int, help="Number of questions to generate")
    parser.add_argument("-r", type=int, required=True, help="Range of numbers")
    parser.add_argument("-e", type=str, help="Exercise file to validate")
    parser.add_argument("-a", type=str, help="Answer file to validate")
    return parser.parse_args()

def generate_number(max_range):
    if random.random() < 0.5:
        return random.randint(1, max_range)
    else:
        numerator = random.randint(1, max_range)
        denominator = random.randint(1, max_range)
        while numerator % 2 == 0 and denominator % 2 == 0:
            numerator = random.randint(1, max_range)
            denominator = random.randint(1, max_range)
        return Fraction(numerator, denominator)

def generate_expression(max_range):
    num1 = generate_number(max_range)
    num2 = generate_number(max_range)
    operators = ['+', '-', '*', '/']
    operator = random.choice(operators)
    if operator == '+':
        return f"{num1} {operator} {num2}"
    elif operator == '-':
        if num1 >= num2:
            return f"{num1} {operator} {num2}"
        else:
            return f"{num2} {operator} {num1}"
    elif operator == '*':
        return f"{num1} {operator} {num2}"
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
            if result <= 1 and result != int(result):
                return f"{num1} {operator} {num2}"
            else:
                return f"{num2} {operator} {num1}"

def generate_question(max_range):
    question = ""
    num_operators = random.randint(1, 3)
    expressions = []
    for _ in range(num_operators):
        expressions.append(generate_expression(max_range))
    question = " ".join(expressions)
    return question

def generate_questions(num_questions, max_range):
    questions = set()
    while len(questions) < num_questions:
        question = generate_question(max_range)
        parsed_question = parse_question(question)
        if parsed_question not in questions:
            questions.add(parsed_question)
    return questions

def parse_question(question):
    return question.replace(" ", "")

def test_multiplication(self):
    result = calculate_answer("3 * 3")
    print(f"Test '3 * 3': expected 9, got {result}")
    if result is not None:
        self.assertEqual(int(result) if result.is_integer() else result, 9)
    else:
        self.fail("calculate_answer returned None")

def test_simple_addition(self):
    result = calculate_answer("1 + 2")
    print(f"Test '1 + 2': expected 3, got {result}")
    if result is not None:
        self.assertAlmostEqual(result, 3, places=5)
    else:
        self.fail("calculate_answer returned None")

def calculate_answer(expression):
    try:
        # 使用 sympy 计算表达式的值
        answer = sympify(expression)
        float_answer = float(answer.evalf())
        # 如果结果是一个整数，返回 int 类型，否则返回 float 类型
        return int(float_answer) if float_answer.is_integer() else float_answer
    except Exception as e:
        print(f"Error calculating answer: {e}")
        return e

def save_questions(questions, filename="Exercises.txt"):
    with open(filename, "w") as file:
        for idx, question in enumerate(questions, 1):
            file.write(f"四则运算题目{idx}\n{question} = \n")

def save_answers(answers, filename="Answers.txt"):
    with open(filename, "w") as file:
        for idx, answer in enumerate(answers, 1):
            # 只写入分数部分，不包含 "答案X"
            file.write(f"{answer}\n")

def validate_answers(exercise_file, answer_file):
    correct = []
    wrong = []
    question_number = 1  # 初始化题目编号
    with open(exercise_file, "r") as ex_file, open(answer_file, "r") as ans_file:
        for ex_line, ans_line in zip(ex_file, ans_file):
            exercise = ex_line.strip()  # 提取题目部分（现在只有表达式）
            try:
                answer = Fraction(ans_line.strip())  # 尝试将文本转换为 Fraction
                calculated_answer = calculate_answer(exercise)
                if calculated_answer is None:
                    raise ValueError(f"calculate_answer returned None for expression '{exercise}'")
                if calculated_answer == answer:
                    correct.append(f"四则运算题目{question_number}")
                else:
                    wrong.append(f"四则运算题目{question_number}")
                question_number += 1  # 增加题目编号
            except ValueError as e:
                print(f"{e} in line: {ans_line.strip()}")
                wrong.append(f"四则运算题目{question_number}")
                question_number += 1  # 即使出错也要增加编号
            except Exception as e:
                print(f"Error calculating answer for: {exercise}. Error: {e}")
                wrong.append(f"四则运算题目{question_number}")
                question_number += 1  # 即使出错也要增加编号
    return correct, wrong

def save_grades(correct, wrong, filename="Grade.txt"):
    with open(filename, "w") as file:
        correct_ids = [idx.split("题目")[1] for idx in correct]
        wrong_ids = [idx.split("题目")[1] for idx in wrong]
        file.write(f"Correct: {len(correct)} ({', '.join(correct_ids)})\n")
        file.write(f"Wrong: {len(wrong)} ({', '.join(wrong_ids)})\n")

def main():
    args = parse_arguments()
    if args.n:
        questions = generate_questions(args.n, args.r)
        answers = [calculate_answer(q) for q in questions]
        save_questions(questions)
        save_answers(answers)
    if args.e and args.a:
        print(f"Validating answers using exercise file: {args.e}")
        print(f"And answer file: {args.a}")
        correct, wrong = validate_answers(args.e, args.a)
        print(f"Correct answers: {correct}")
        print(f"Wrong answers: {wrong}")
        save_grades(correct, wrong)
        print("Grades have been saved.")

if __name__ == "__main__":
    main()
