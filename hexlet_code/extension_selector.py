from pathlib import Path

from hexlet_code.generate_diff import generate_diff


def extension_selector(file1, file2, format_name='stylish'):
    if Path(file1).suffix == '.json' and Path(file2).suffix == '.json':
        return generate_diff(file1, file2, format_name)
    elif Path(file1).suffix and Path(file2).suffix in ('.yml', '.yaml'):
        return generate_diff(file1, file2, format_name)
    else:
        raise ValueError('Invalid extension')
