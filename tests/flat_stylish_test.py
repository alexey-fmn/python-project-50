from hexlet_code.flat_stylish import flat_stylish


def test_equal_values():
    content1 = {"host": "hexlet.io"}
    content2 = {"host": "hexlet.io"}

    expected = (
        "{\n"
        "    host: hexlet.io\n"
        "}"
    )

    assert flat_stylish(content1, content2) == expected


def test_added_key():
    content1 = {}
    content2 = {"timeout": 50}

    expected = (
        "{\n"
        "  + timeout: 50\n"
        "}"
    )

    assert flat_stylish(content1, content2) == expected


def test_removed_key():
    content1 = {"timeout": 50}
    content2 = {}

    expected = (
        "{\n"
        "  - timeout: 50\n"
        "}"
    )

    assert flat_stylish(content1, content2) == expected


def test_changed_value():
    content1 = {"timeout": 50}
    content2 = {"timeout": 20}

    expected = (
        "{\n"
        "  - timeout: 50\n"
        "  + timeout: 20\n"
        "}"
    )

    assert flat_stylish(content1, content2) == expected


def test_multiple_keys_sorted():
    content1 = {
        "host": "hexlet.io",
        "timeout": 50,
    }

    content2 = {
        "host": "hexlet.io",
        "proxy": "123.234.53.22",
    }

    expected = (
        "{\n"
        "    host: hexlet.io\n"
        "  + proxy: 123.234.53.22\n"
        "  - timeout: 50\n"
        "}"
    )

    assert flat_stylish(content1, content2) == expected