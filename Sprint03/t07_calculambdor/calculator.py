operations = {"add": (lambda x, y: x + y),
              "sub": (lambda x, y: x - y),
              "mul": (lambda x, y: x * y),
              "div": (lambda x, y: x / y),
              "pow": (lambda x, y: x ** y)
              }


def calculator(operator, num1, num2):
    global operations

    if operator not in operations:
        raise ValueError("Invalid operation. Available operations: add, sub, mul, div, pow.")
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Invalid numbers. Second and third arguments must be numerical.")
    else:
        return operations[operator](num1, num2)
