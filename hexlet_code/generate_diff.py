from hexlet_code.diff_builder import build_diff
from hexlet_code.formatters import format_plain
from hexlet_code.formatters.json import format_json
from hexlet_code.formatters.stylish import format_stylish
from hexlet_code.parsers.parse import parse


def generate_diff(file1, file2, format_name='stylish'):
    data1 = parse(file1)
    data2 = parse(file2)

    tree = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_stylish(tree)
    if format_name == 'plain':
        return format_plain(tree)
    if format_name == 'json':
        return format_json(tree)

    raise ValueError(f'Unknown format: {format_name}')