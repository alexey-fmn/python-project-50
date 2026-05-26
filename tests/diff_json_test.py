from pathlib import Path

from gendiff.diff_json import generate_diff_json


def test_generate_diff_same_content():
    current_dir = Path(__file__).parent
    file1 = current_dir / "test_data" / "two_line.json"
    file2 = current_dir / "test_data" / "two_line2.json"

    expected = (
        "{\n"
        "    host: hexlet.io\n"
        "    timeout: 50\n"
        "}"
    )

    assert generate_diff_json(file1, file2) == expected


def test_generate_diff_removed_key():
    current_dir = Path(__file__).parent
    file1 = current_dir / "test_data" / "two_line.json"
    file2 = current_dir / "test_data" / "one_word.json"

    expected = (
        "{\n"
        "    host: hexlet.io\n"
        "  - timeout: 50\n"
        "}"
    )

    assert generate_diff_json(file1, file2) == expected


def test_generate_diff_added_key():
    current_dir = Path(__file__).parent
    file1 = current_dir / "test_data" / "one_word.json"
    file2 = current_dir / "test_data" / "two_line.json"

    expected = (
        "{\n"
        "    host: hexlet.io\n"
        "  + timeout: 50\n"
        "}"
    )

    assert generate_diff_json(file1, file2) == expected


def test_generate_diff_changed_value():
    current_dir = Path(__file__).parent
    file1 = current_dir / "test_data" / "one_word_time_50.json"
    file2 = current_dir / "test_data" / "one_word_time_20.json"

    expected = (
        "{\n"
        "  - timeout: 50\n"
        "  + timeout: 20\n"
        "}"
    )

    assert generate_diff_json(file1, file2) == expected