import re


def validator(info, em_patt, name_patt):
    if 'email' not in info or 'name' not in info:
        return False
    if list(info.keys()).count('name') and list(info.keys()).count('email'):
        if re.search(name_patt, info['name']) and re.search(em_patt, info['email']):
            return info
        else:
            return False
    else:
        return False


def email_add(container, info):
    key = info.pop('email')
    print(f'Info Conteiner - {info}')

    print(f'Conteiner - before - {container}')
    container.update({key: info})
    print(f'Conteiner - after - {container}')
    return True


def email_update(container, info):
    key = info.pop('email')
    if key in container:
        container.update({key: {**container.get(key), **info}})
        return True
    else:
        return False


def email_delete(container, info):
    key = info.pop('email')
    if key in container:
        container.pop(key)
        print(container)
        return True
    else:
        return False


def contacts(container, info, operation):
    email_patt = r'^[^@]+@[^@]+[.][^@]+$'
    name_patt = r'^[\w+\s+]*$'

    command_dic = {
        'add': email_add,
        'delete': email_delete,
        'update': email_update
    }

    info_cont = validator(info, email_patt, name_patt)
    if not info_cont:
        return False
    else:
        if operation in command_dic:
            f = command_dic[operation]
            return f(container, info_cont)
        else:
            return False

    return True