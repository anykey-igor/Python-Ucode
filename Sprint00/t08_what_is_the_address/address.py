a = 1000
b = a 
c = 999

print(f'first_var = {a}, address is {id(a)}')
print(f'second_var = {b}, address is {id(b)}')
print(f'third_var = {c}, address is {id(c)}')
print(f'{a} is {b} = {a is b}')
print(f'{a} is {c} = {b is c}')