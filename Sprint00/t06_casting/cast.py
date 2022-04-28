a = 3
b = 10
c = -14.8
d = True

print('Available variables:')
print(f'a = {a}\nb = {b}\nc = {c}\nd = {d}\n')

result= float(a + b)
print(f'{a} + {b} = {result}')

result= int(c - b)
print(f'{c} - {b} = {result}')

result= str(c) + str(b)
print(f'{c} + {b} = {result}')

result= bool(a - a)
print(f'{a} - {a} = {result}')