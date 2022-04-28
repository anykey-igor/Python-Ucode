def patoi(value):
    try:
        int(value)
    except ValueError:
        return False
    return int(value)
