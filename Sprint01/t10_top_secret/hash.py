import hashlib


def md5_hash(st_sec):
    my = hashlib.md5(str.encode(str(st_sec)))
    return print(f'Original string: {st_sec} \nmd5 hash generated is\n{my.hexdigest()}')


def sha1_hash(st_sec):
    my = hashlib.sha1(str.encode(str(st_sec)))
    return print(f'Original string: {st_sec} \nsha1 hash generated is\n{my.hexdigest()}')
