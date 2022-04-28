from functools import reduce


def multiplier(num_list):
    if all([isinstance(x, (float, int)) for x in num_list]):
        return reduce(lambda x, y: x*y, num_list)
    else:
        raise ValueError('The given data is invalid.')
