import pytest

from gendiff.generate_diff import generate_diff


def test_generate_diff_stylish(monkeypatch):
    monkeypatch.setattr(
        'gendiff.generate_diff.parse',
        lambda filename: {'file': filename},
    )

    monkeypatch.setattr(
        'gendiff.generate_diff.build_diff',
        lambda data1, data2: 'tree',
    )

    monkeypatch.setattr(
        'gendiff.generate_diff.format_stylish',
        lambda tree: 'stylish result',
    )

    result = generate_diff('file1.json', 'file2.json')

    assert result == 'stylish result'


def test_generate_diff_plain(monkeypatch):
    monkeypatch.setattr(
        'gendiff.generate_diff.parse',
        lambda filename: {'file': filename},
    )

    monkeypatch.setattr(
        'gendiff.generate_diff.build_diff',
        lambda data1, data2: 'tree',
    )

    monkeypatch.setattr(
        'gendiff.generate_diff.format_plain',
        lambda tree: 'plain result',
    )

    result = generate_diff(
        'file1.json',
        'file2.json',
        format_name='plain',
    )

    assert result == 'plain result'


def test_generate_diff_unknown_format():
    with pytest.raises(ValueError, match='Unknown format: json'):
        generate_diff(
            'file1.json',
            'file2.json',
            format_name='json',
        )