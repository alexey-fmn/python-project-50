def build_diff(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))

    result = []

    for key in keys:
        if key not in data1:
            result.append({
                "type": "added",
                "key": key,
                "value": data2[key],
            })

        elif key not in data2:
            result.append({
                "type": "removed",
                "key": key,
                "value": data1[key],
            })

        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result.append({
                "type": "nested",
                "key": key,
                "children": build_diff(data1[key], data2[key]),
            })

        elif data1[key] == data2[key]:
            result.append({
                "type": "unchanged",
                "key": key,
                "value": data1[key],
            })

        else:
            result.append({
                "type": "changed",
                "key": key,
                "old_value": data1[key],
                "new_value": data2[key],
            })

    return result