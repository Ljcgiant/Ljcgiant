import unittest
from main import read_file

class TestReadFile(unittest.TestCase):
    def test_normal_text_file(self):
        # 测试正常文本文件
        test_file_path = r'D:\UThird\软工\output.txt'
        expected_content = 'Hello, world!'
        with open(test_file_path, 'w', encoding='utf-8') as file:
            file.write(expected_content)
        self.assertEqual(read_file(test_file_path), expected_content)

    def test_nonexistent_file(self):
        # 测试文件不存在的情况
        nonexistent_file_path = r'D:\UThird\软工\input.txt'
        with self.assertRaises(FileNotFoundError):
            read_file(nonexistent_file_path)

    def test_non_text_file(self):
        # 测试非文本文件
        non_text_file_path = r'D:\UThird\zhouyv.jpg'
        # 假设这是一个二进制文件
        with open(non_text_file_path, 'rb') as file:
            content = file.read()
        self.assertEqual(read_file(non_text_file_path), content)

if __name__ == '__main__':
    unittest.main()
