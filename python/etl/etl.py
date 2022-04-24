def transform(legacy_data):
    data = {}
    for keys, values in legacy_data.items():
        for letter in values:
            data[letter.lower()] = keys
    return data
