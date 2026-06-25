def flat_stylish(content1=None, content2=None):

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