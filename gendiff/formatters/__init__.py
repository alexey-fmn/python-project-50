from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish


def format_diff(diff, format_name):
    formatters = {
        'stylish': format_stylish,
        'plain': format_plain,
        'json': format_json
    }

    if format_name not in formatters:
        raise ValueError(f'Unknown format: {format_name}')

    return formatters[format_name](diff)