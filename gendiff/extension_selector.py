from pathlib import Path

from gendiff.diff_json import generate_diff_json
from gendiff.diff_yaml import generate_diff_yaml


def extension_selector(file1, file2):
    if Path(file1).suffix == '.json' and Path(file2).suffix == '.json':
        return generate_diff_json(file1, file2)
    elif Path(file1).suffix and Path(file2).suffix in ('.yml', '.yaml'):
        return generate_diff_yaml(file1, file2)
    else:
        raise ValueError('Invalid extension')
