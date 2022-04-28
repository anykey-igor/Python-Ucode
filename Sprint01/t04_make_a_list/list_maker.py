def list_maker(my_list, my_delim):
    if my_delim == '':
        my_delim = ' '

    return my_list.split(my_delim)
