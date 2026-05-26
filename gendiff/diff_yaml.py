import yaml


def read_yaml(filepath):
    with open(filepath, 'r') as file:
        return yaml.safe_load(file)


def generate_diff_yaml(file1, file2):
    content1 = read_yaml(file1)
    content2 = read_yaml(file2)

    all_lines = sorted(set(content1.keys()) | set(content2.keys()))

    lines = ['{']

    for key in all_lines:
        if key not in content2:
            lines.append(f"  - {key}: {content1[key]}")
        elif key not in content1:
            lines.append(f"  + {key}: {content2[key]}")
        elif content1[key] == content2[key]:
            lines.append(f"    {key}: {content1[key]}")
        else:
            lines.append(f"  - {key}: {content1[key]}")
            lines.append(f"  + {key}: {content2[key]}")

    lines.append('}')

    return '\n'.join(lines)