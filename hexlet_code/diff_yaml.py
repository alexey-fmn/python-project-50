from hexlet_code.flat_stylish import flat_stylish
from hexlet_code.parsers.parse import parse


def generate_diff_yaml(file1, file2):
    content1 = parse(file1)
    content2 = parse(file2)

    return flat_stylish(content1, content2)