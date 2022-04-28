import yaml
import copy
import re
from main.loger import *

"""Находим все параметры которые были приняты как список и преобразовуем в словарь"""
log = logging.getLogger(':::::END_GAME:::::')


def names_list_to_dict(**kwargs):
    for key in kwargs:
        if isinstance(kwargs[key], list) and key != 'auth':
            kwargs[key] = dict(kwargs[key])
        else:
            if key == 'auth' and kwargs[key] is not None:
                # print(kwargs[key])
                kwargs[key] = tuple(kwargs[key])
            else:
                pass
    return kwargs


"""Загрузить переменные из файла"""


def get_variables(filename):
    with open(filename, 'r') as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as exp:
            return {}


def get_var(my_var, var):
    for key in my_var:
        if var == key:
            return my_var[key]
    return None


def extract_variable(filename, **kwargs):
    extra_args = copy.deepcopy(kwargs)
    my_var = get_variables(filename)
    if my_var is None:
        print(f'No available variables! Pls create variable in variable.yaml and try again')
        exit()
    # print(my_var)
    for key in kwargs:
        if isinstance(kwargs[key], tuple):
            i = 0
            new_auth = []
            while i < len(kwargs[key]):
                if re.match(r".*{@.+}.*", kwargs[key][i]):
                    new_auth.append(get_var(my_var, kwargs[key][i][2:-1]))
                i += 1
            extra_args[key] = tuple(new_auth)
        elif isinstance(kwargs[key], dict):
            for k in kwargs[key]:
                k_key = k
                val_k = kwargs[key][k]
                if re.match(r".*{@.+}.*", k):
                    k_key = get_var(my_var, k[2:-1])
                if re.match(r".*{@.+}.*", kwargs[key][k]):
                    val_k = get_var(my_var, kwargs[key][k][2:-1])
                extra_args[key].pop(k)
                extra_args[key].update({k_key: val_k})
        else:
            kas = copy.deepcopy(kwargs[key])
            if re.match(r".*{@.+}.*", str(kas)):
                extra_args[key] = get_var(my_var, kwargs[key][2:-1])
    return extra_args
