def convert_to_bytes(f, s, t):

    try:
        int(f)
        if str(s) == 'True':
            pass
        else:
            s = ''
        bool(s)
        str(t)
    except ValueError:
        return print(f'False')
    encode = 'utf-8'

    print(f'-- The int value is "{int(f)}"')
    print(f'bytes: "{bytes(int(f))}"')
    print(f'-- The bool value is "{bool(s)}"')
    print(f'bytes: "{bytes(bool(s))}"')
    print(f'- The string value is "{str(t)}"')
    print(f'bytes: "{bytes(str(t), encode)}"')
