INDENT_SIZE = 4


def stringify(value, depth):
    if value is None:
        return "null"

    if value is True:
        return "true"

    if value is False:
        return "false"

    if not isinstance(value, dict):
        return str(value)

    current_indent = " " * (depth * INDENT_SIZE)
    lines = ["{"]

    for key, val in value.items():
        lines.append(
            f"{current_indent}    {key}: "
            f"{stringify(val, depth + 1)}"
        )

    lines.append(f"{current_indent}}}")

    return "\n".join(lines)


def format_stylish(tree, depth=1):
    lines = ["{"]

    sign_indent = " " * (depth * INDENT_SIZE - 2)
    value_indent = " " * (depth * INDENT_SIZE)

    for node in tree:
        node_type = node["type"]
        key = node["key"]

        match node_type:
            case "added":
                lines.append(
                    f"{sign_indent}+ {key}: "
                    f"{stringify(node['value'], depth)}"
                )

            case "removed":
                lines.append(
                    f"{sign_indent}- {key}: "
                    f"{stringify(node['value'], depth)}"
                )

            case "unchanged":
                lines.append(
                    f"{value_indent}{key}: "
                    f"{stringify(node['value'], depth)}"
                )

            case "changed":
                lines.append(
                    f"{sign_indent}- {key}: "
                    f"{stringify(node['old_value'], depth)}"
                )

                lines.append(
                    f"{sign_indent}+ {key}: "
                    f"{stringify(node['new_value'], depth)}"
                )

            case "nested":
                children = format_stylish(
                    node["children"],
                    depth + 1,
                )

                lines.append(
                    f"{value_indent}{key}: {children}"
                )

    closing_indent = " " * ((depth - 1) * INDENT_SIZE)

    lines.append(f"{closing_indent}}}")

    return "\n".join(lines)