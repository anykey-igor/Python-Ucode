def cube(number):
    number = int(number)
    if number > 0:
        while number>0:
            yield number ** 3
            number -= 1
