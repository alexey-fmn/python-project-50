from gendiff.diff_yaml import generate_diff_yaml


def test_generate_diff_yaml(tmp_path):
    file1 = tmp_path / "file1.yml"
    file2 = tmp_path / "file2.yml"

    file1.write_text(
        """
host: hexlet.io
timeout: 50
"""
    )

    file2.write_text(
        """
host: hexlet.io
timeout: 20
proxy: 123.234.53.22
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

    assert generate_diff_yaml(file1, file2) == expected