n = int(input('n: '))
a = int(input('a: '))
b = int(input('b: '))

# Only edit the following line
result = lambda x, y, z : True if x % y == 0 and x % z == 0 else False

print(result(n, a, b))
