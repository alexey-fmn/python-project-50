import pytest
import yaml

from gendiff.diff_yaml import generate_diff_yaml, read_yaml


@pytest.fixture
def yaml_file(tmp_path):
    def _create_file(filename, content):
        file_path = tmp_path / filename

        with open(file_path, "w") as file:
            yaml.dump(content, file)

        return file_path

    return _create_file


def test_read_yaml(yaml_file):
    data = {"host": "localhost", "port": 80}
    filepath = yaml_file("test.yaml", data)

    result = read_yaml(filepath)

    assert result == data


def test_generate_diff_yaml_added_key(yaml_file):
    file1 = yaml_file("file1.yaml", {"host": "localhost"})
    file2 = yaml_file("file2.yaml", {
        "host": "localhost",
        "timeout": 20,
    })

    result = generate_diff_yaml(file1, file2)

    expected = (
        "{\n"
        "    host: localhost\n"
        "  + timeout: 20\n"
        "}"
    )

    assert result == expected


def test_generate_diff_yaml_removed_key(yaml_file):
    file1 = yaml_file("file1.yaml", {
        "host": "localhost",
        "timeout": 20,
    })
    file2 = yaml_file("file2.yaml", {"host": "localhost"})

    result = generate_diff_yaml(file1, file2)

    expected = (
        "{\n"
        "    host: localhost\n"
        "  - timeout: 20\n"
        "}"
    )

    assert result == expected


def test_generate_diff_yaml_changed_value(yaml_file):
    file1 = yaml_file("file1.yaml", {"timeout": 20})
    file2 = yaml_file("file2.yaml", {"timeout": 50})

    result = generate_diff_yaml(file1, file2)

    expected = (
        "{\n"
        "  - timeout: 20\n"
        "  + timeout: 50\n"
        "}"
    )

    assert result == expected


def test_generate_diff_yaml_unchanged_value(yaml_file):
    file1 = yaml_file("file1.yaml", {"host": "localhost"})
    file2 = yaml_file("file2.yaml", {"host": "localhost"})

    result = generate_diff_yaml(file1, file2)

    expected = (
        "{\n"
        "    host: localhost\n"
        "}"
    )

    assert result == expected


def test_generate_diff_yaml_complex_case(yaml_file):
    file1 = yaml_file("file1.yaml", {
        "host": "localhost",
        "timeout": 20,
        "verbose": True,
    })

    file2 = yaml_file("file2.yaml", {
        "host": "localhost",
        "timeout": 50,
        "follow": False,
    })

    result = generate_diff_yaml(file1, file2)

    expected = (
        "{\n"
        "  + follow: False\n"
        "    host: localhost\n"
        "  - timeout: 20\n"
        "  + timeout: 50\n"
        "  - verbose: True\n"
        "}"
    )

    assert result == expected