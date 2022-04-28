def fib(num):
    square = fib_generator(num+1)
    return square[num]

def fib_generator(num):
    squares = []
    start = True
    for i in range(num):
        if start == True:
            squares.append(i)
            if len(squares) < 2:
                pass
            else:
                start = False
        else:
            squares.append(squares[i-2]+squares[i-1])
    return squares
