from read_files.jsonreader import JsonReader


def generate_diff_json(file1, file2):
    content1 = JsonReader.read(file1)
    content2 = JsonReader.read(file2)

    all_lines = sorted(set(content1.keys()) | set(content2.keys()))

    lines = ['{']
    for key in all_lines:
        if key not in content2:
            lines.append(f"  - {key}: {(content1[key])}")
        elif key not in content1:
            lines.append(f"  + {key}: {(content2[key])}")
        elif content1[key] == content2[key]:
            lines.append(f"    {key}: {(content1[key])}")
        else:
            lines.append(f"  - {key}: {(content1[key])}")
            lines.append(f"  + {key}: {(content2[key])}")

    lines.append('}')

    lines = '\n'.join(lines)
    return lines
