import re


def clear_words(some_text):
    reg = r'[?!.:;,-]'
    list_of_some_text = some_text.split(' ')
    return list(map((lambda x: re.sub(reg, '', x)), list_of_some_text))
