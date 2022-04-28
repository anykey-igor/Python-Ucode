def print_str_analytics(string):
    print('|------------------------------------------------|') # '|'=2; '-'=48
    print(f'|{"String analytics".center(48," ")}|')
    print('|------------------------------------------------|')
    print(f'| \'{string}\'')
    print('|------------------------------------------------|')
    print(f'| Number of printable characters is: {sum(map(str.isprintable, string))}')
    print(f'| Number of alphanumeric characters is: {sum(map(str.isalnum, string))}')
    print(f'| Number of alphabetic characters is: {sum(map(str.isalpha, string))}')
    print(f'| Number of decimal characters is: {sum(map(str.isdecimal, string))}')
    print(f'| Number of lowercase letters is: {sum(map(str.islower, string))}')
    print(f'| Number of uppercase letters is: {sum(map(str.isupper, string))}')
    print(f'| Number of whitespace characters is: {sum(map(str.isspace, string))}')
    print(f'|------------------------------------------------|')
