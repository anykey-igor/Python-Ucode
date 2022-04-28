def raise_error(err_key, message):
    dic_error = {
        'value': ValueError(message),
        'key': KeyError(message),
        'index': IndexError(message),
        'memory': MemoryError(message),
        'name': NameError(message),
        'eof': EOFError(message)
    }

    if err_key in dic_error:
        raise dic_error[err_key]
    else:
        raise ValueError('No error with such key.')