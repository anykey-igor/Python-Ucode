def make_unique(dict_uniq):
    for key in dict_uniq:
        dict_uniq[key] = sorted(set(dict_uniq[key]))
    return dict_uniq
