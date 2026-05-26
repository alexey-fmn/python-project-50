import pytest

from gendiff.extension_selector import extension_selector


def test_extension_selector_json(monkeypatch):
    def mock_generate_diff_json(file1, file2):
        return "json diff"

    monkeypatch.setattr(
        "gendiff.extension_selector.generate_diff_json",
        mock_generate_diff_json,
    )

    result = extension_selector("file1.json", "file2.json")

    assert result == "json diff"


@pytest.mark.parametrize("ext", [".yml", ".yaml"])
def test_extension_selector_yaml(monkeypatch, ext):
    def mock_generate_diff_yaml(file1, file2):
        return "yaml diff"

    monkeypatch.setattr(
        "gendiff.extension_selector.generate_diff_yaml",
        mock_generate_diff_yaml,
    )

    result = extension_selector(f"file1{ext}", f"file2{ext}")

    assert result == "yaml diff"


def test_extension_selector_invalid_extension():
    with pytest.raises(ValueError, match="Invalid extension"):
        extension_selector("file1.txt", "file2.txt")