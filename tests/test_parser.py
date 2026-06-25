from hexlet_code.parsers.parse import parse


def test_parse_json():
    result = parse('tests/test_data/two_line.json')

    assert result == {
        'host': 'hexlet.io',
        'timeout': 50,
    }


def test_parse_yaml():
    result = parse('tests/test_data/two_line.yaml')
    assert result == {
        'host': 'hexlet.io',
        'timeout': 50,
        'proxy': {
            'ip': '123.45.67.89',
        },
    }