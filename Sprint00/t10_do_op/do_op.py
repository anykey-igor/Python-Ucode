print('---- Simple calculator ----')
print('Let\'s add some numbers')

first = input('Input your first value: ')
operator = input('Input your operator: ')

first = int(first)

if operator == '+' :
    second = input('Input your second value: ')
    second = int(second)
    print(f'{first} {operator} {second} = {first + second}')
    print('---- Simple calculator ----')
elif operator == '-' :
    second = input('Input your second value: ')
    second = int(second)
    print(f'{first} {operator} {second} = {first - second}')
    print('---- Simple calculator ----')
elif operator == '*' :
    second = input('Input your second value: ')
    second = int(second)
    print(f'{first} {operator} {second} = {first * second}')
    print('---- Simple calculator ----')
elif operator == '/' :
    second = input('Input your second value: ')
    second = int(second)
    print(f'{first} {operator} {second} = {first / second}')
    print('---- Simple calculator ----')
else : print('usage: the operator must be\'*\' or \'+\' or \'-\' or \'/\'\n---- Simple calculator ----')
