from unittest.mock import patch

import pytest

from gendiff.generate_diff import generate_diff


@patch(
    'gendiff.generate_diff.format_stylish',
    return_value='stylish result',
)
@patch(
    'gendiff.generate_diff.build_diff',
    return_value='tree',
)
@patch(
    'gendiff.generate_diff.parse',
    side_effect=lambda filename: {'file': filename},
)
def test_generate_diff_stylish(
    mock_parse,
    mock_build_diff,
    mock_format_stylish,
):
    result = generate_diff('file1.json', 'file2.json')

    assert result == 'stylish result'


@patch(
    'gendiff.generate_diff.format_plain',
    return_value='plain result',
)
@patch(
    'gendiff.generate_diff.build_diff',
    return_value='tree',
)
@patch(
    'gendiff.generate_diff.parse',
    side_effect=lambda filename: {'file': filename},
)
def test_generate_diff_plain(
    mock_parse,
    mock_build_diff,
    mock_format_plain,
):
    result = generate_diff(
        'file1.json',
        'file2.json',
        format_name='plain',
    )

    assert result == 'plain result'


def test_generate_diff_unknown_format():
    with pytest.raises(ValueError, match='Unknown format: uml'):
        generate_diff(
            'file1.json',
            'file2.json',
            format_name='uml',
        )