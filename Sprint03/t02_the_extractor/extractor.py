def extractor(diction, data=str):
    return dict((key, value) for key, value in diction.items() if isinstance(value, data))
