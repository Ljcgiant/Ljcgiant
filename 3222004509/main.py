import sys
from collections import Counter


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def preprocess(text):
    # 去除标点符号并转换为小写
    text = ''.join([char.lower() for char in text if char.isalnum() or char.isspace()])
    return text


def calculate_similarity(orig_text, copy_text):
    # 使用余弦相似度计算方法
    orig_words = orig_text.split()
    copy_words = copy_text.split()

    orig_counter = Counter(orig_words)
    copy_counter = Counter(copy_words)

    intersection = orig_counter & copy_counter
    union = orig_counter | copy_counter

    if union == Counter():  # 避免除以零
        return 0
    similarity = sum(intersection.values()) / sum(union.values())
    return similarity


def main(orig_path, copy_path, output_path):
    orig_text = read_file(orig_path)
    copy_text = read_file(copy_path)

    orig_text = preprocess(orig_text)
    copy_text = preprocess(copy_text)

    similarity = calculate_similarity(orig_text, copy_text)
    duplication_rate = similarity * 100

    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(f"{duplication_rate:.2f}%")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python main.py [原文文件] [抄袭版论文的文件] [答案文件]")
        print()
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
