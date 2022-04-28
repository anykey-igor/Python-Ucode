import collections
import json


def summary(filename, summarize_by):
    try:
        with open(filename, "r+") as f:
            data = f.read()
            my_json = json.loads(data)
    except ValueError:
        return f'Error in decoding JSON.'
    else:
        counter = collections.Counter()
        for iterator in my_json:
            try:
                counter.update({iterator[summarize_by]})
            except KeyError:
                counter.update({None})
            except TypeError:
                counter.update({'unhashable'})
        result = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
        return result
