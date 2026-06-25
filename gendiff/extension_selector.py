from pathlib import Path

from gendiff.generate_diff import generate_diff


def extension_selector(file1, file2, format_name='stylish'):
    ext1 = Path(file1).suffix
    ext2 = Path(file2).suffix

    if ext1 == '.json' and ext2 == '.json':
        return generate_diff(file1, file2, format_name)

    if ext1 in ('.yml', '.yaml') and ext2 in ('.yml', '.yaml'):
        return generate_diff(file1, file2, format_name)

    raise ValueError('Invalid extension')