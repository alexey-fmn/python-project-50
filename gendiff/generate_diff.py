from gendiff.diff_builder import build_diff
from gendiff.formatters import format_plain
from gendiff.formatters.json import format_json
from gendiff.formatters.stylish import format_stylish
from gendiff.parsers.parse import parse


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