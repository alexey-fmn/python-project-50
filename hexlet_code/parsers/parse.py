import json
from pathlib import Path

import yaml


def parse(filepath):
    path = Path(filepath)

    extension = path.suffix

    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    if extension == '.json':
        return json.loads(content)

    if extension in ('.yml', '.yaml'):
        return yaml.safe_load(content)

    raise ValueError(f'Unsupported file format: {extension}')