def contains(my_string, list_substring):
    check_list = list()
    for key in list_substring:
        try:
            my_string.lower().index(key.lower())
            check_list.append(key)
        except ValueError:
            pass
    return check_list
