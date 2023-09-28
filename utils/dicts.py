def get_val(collection, key, default='git'):
    value = collection.get(key)
    if value is None:
        value = default
    return value
