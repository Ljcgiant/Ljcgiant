import pytest
from myapp import generate_expression
from fractions import Fraction
import re

# 正则表达式匹配整数或分数
number_pattern = re.compile(r'\d+/\d+|\d+')

def test_expression_generation():
    expression = generate_expression(10)
    assert isinstance(expression, str)
    assert any(op in expression for op in ['+', '-', '*', '/'])

def test_expression_validity():
    expression = generate_expression(10)
    nums = number_pattern.findall(expression)
    operators = [op for op in expression if op in '+-*/']
    for i, num in enumerate(nums):
        if i == 0:
            continue
        op = operators[i-1]
        if op == '-':
            left, right = int(nums[i-1]), int(nums[i]) if '/' not in nums[i] else Fraction(nums[i])
            result = left - right
            assert result >= 0, f"减法表达式不应有负数结果: {expression}"
        if op == '/':
            left, right = Fraction(nums[i-1]), Fraction(nums[i])
            result = left / right
            assert left <= right, f"除法表达式的除数不应小于被除数: {expression}"
            assert result == Fraction(eval(nums[i-1] + op + nums[i])), f"除法结果不正确: {expression}"

# ... 其他测试用例 ...

# Run the tests
if __name__ == "__main__":
    pytest.main()
