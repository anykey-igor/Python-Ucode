import itertools as it
import copy


def group(input_dict, list_keys):
    dict_to_group = copy.deepcopy(input_dict)
    result_dict = dict()
    temp_dict = dict()
    dict_to_group = sorted(dict_to_group, key=lambda x: x[list_keys[0]])
    for key, gr in it.groupby(dict_to_group, lambda x: x.pop(list_keys[0], None)):
        if key:
            new_key = list(gr)
            if len(list_keys) > 1:
                temp_dict = {**temp_dict, key: group(new_key, list_keys[1:])}
            else:
                temp_dict = {**temp_dict, key: new_key}
    result_dict = {**result_dict, **temp_dict}
    return result_dict
