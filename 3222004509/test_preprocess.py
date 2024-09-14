import unittest
from main import preprocess

class TestPreprocess(unittest.TestCase):
    def test_preprocess(self):
        # 测试去除标点符号并转换为小写
        self.assertEqual(preprocess('Hello, World!'), 'hello world')
        self.assertEqual(preprocess('Foo-Bar;'), 'foo bar')
        self.assertEqual(preprocess('123'), '123')  # 测试数字字符串
        self.assertEqual(preprocess(''), '')  # 测试空字符串

if __name__ == '__main__':
    unittest.main()
