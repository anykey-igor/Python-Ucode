def validator(num1_operator_num2):
    my_list = num1_operator_num2.split()
    operators = ['>', '<', '>=', '<=', '==']
    try:
        num1 = my_list[0]
        operator = my_list[1]
        num2 = my_list[2]
        float(num1)
        float(num2)
        1 / operators.count(operator)
    except ArithmeticError:
        return print(f'False')
    except LookupError:
        return print(f'False')
    except ValueError:
        return print(f'False')

    valid_opera = []
    y = 0
    while y < len(operators):
        if len(operators[y]) == len(operator):
            valid_opera.append(operators[y])
        y += 1

    if len(operator) == 1:
        if eval(str(float(num1)) + '==' + str(float(num2))):
            print('False')
        elif eval(str(float(num1)) + operator + str(float(num2))):
            print(f'True')
        else:
            a = 0
            while not eval(str(float(num1)) + valid_opera[a] + str(float(num2))):
                a += 1
            else:
                print(f'{str(float(num1))} {valid_opera[a]} {str(float(num2))}')
    else:
        if eval(str(float(num1)) + operator + str(float(num2))) and operator != '==':
            print(f'{str(float(num1))} == {str(float(num2))}')
        elif eval(str(float(num1)) + operator + str(float(num2))) and operator == '==':
            print(f'{eval(str(float(num1)) + operator + str(float(num2)))}')
        else:
            a = 0
            while not eval(str(float(num1)) + valid_opera[a] + str(float(num2))):
                a += 1
            else:
                print(f'{str(float(num1))} {valid_opera[a]} {str(float(num2))}')

