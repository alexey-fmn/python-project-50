import pytest

from hexlet_code.generate_diff import generate_diff


def test_changed_and_added_keys_json(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"

    file1.write_text(
        """
{
  "host": "hexlet.io",
  "timeout": 50
}
"""
    )

    file2.write_text(
        """
{
  "host": "hexlet.io",
  "timeout": 20,
  "proxy": "123.234.53.22"
}
"""
    )

    expected = (
        "{\n"
        "    host: hexlet.io\n"
        "  + proxy: 123.234.53.22\n"
        "  - timeout: 50\n"
        "  + timeout: 20\n"
        "}"
    )

    assert generate_diff(file1, file2) == expected


def test_removed_key_json(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"

    file1.write_text(
        """
{
  "timeout": 50,
  "verbose": true
}
"""
    )

    file2.write_text(
        """
{
  "verbose": true
}
"""
    )

    expected = (
        "{\n"
        "  - timeout: 50\n"
        "    verbose: true\n"
        "}"
    )

    assert generate_diff(file1, file2) == expected


def test_equal_files_json(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"

    content = """
{
  "host": "hexlet.io",
  "timeout": 50
}
"""

    file1.write_text(content)
    file2.write_text(content)

    expected = (
        "{\n"
        "    host: hexlet.io\n"
        "    timeout: 50\n"
        "}"
    )

    assert generate_diff(file1, file2) == expected


def test_empty_files_json(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"

    file1.write_text("{}")
    file2.write_text("{}")

    expected = "{\n}"

    assert generate_diff(file1, file2) == expected


def test_one_empty_file_json(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"

    file1.write_text(
        """
{
  "host": "hexlet.io",
  "timeout": 50
}
"""
    )

    file2.write_text("{}")

    expected = (
        "{\n"
        "  - host: hexlet.io\n"
        "  - timeout: 50\n"
        "}"
    )

    assert generate_diff(file1, file2) == expected


@pytest.mark.parametrize(
    "content1, content2, expected",
    [
        (
            '{"enabled": true}',
            '{"enabled": false}',
            (
                "{\n"
                "  - enabled: true\n"
                "  + enabled: false\n"
                "}"
            ),
        ),
        (
            '{"count": 1}',
            '{"count": 2}',
            (
                "{\n"
                "  - count: 1\n"
                "  + count: 2\n"
                "}"
            ),
        ),
    ],
)
def test_different_values_json(tmp_path, content1, content2, expected):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"

    file1.write_text(content1)
    file2.write_text(content2)

    assert generate_diff(file1, file2) == expected