def stringify(value):
    if isinstance(value, dict):
        return '[complex value]'

    if isinstance(value, str):
        return f"'{value}'"

    if value is None:
        return 'null'

    if isinstance(value, bool):
        return str(value).lower()

    return str(value)


def format_plain(diff):
    return '\n'.join(iter_nodes(diff))


def iter_nodes(nodes, path=''):
    lines = []

    for node in nodes:
        name = node['key']
        current_path = f'{path}.{name}' if path else name

        node_type = node['type']

        if node_type == 'nested':
            lines.extend(iter_nodes(node['children'], current_path))

        elif node_type == 'added':
            value = stringify(node['value'])
            lines.append(
                f"Property '{current_path}' was added with value: {value}"
            )

        elif node_type == 'removed':
            lines.append(
                f"Property '{current_path}' was removed"
            )

        elif node_type == 'changed':
            old_value = stringify(node['old_value'])
            new_value = stringify(node['new_value'])

            lines.append(
                f"Property '{current_path}' was updated. "
                f"From {old_value} to {new_value}"
            )

    return lines