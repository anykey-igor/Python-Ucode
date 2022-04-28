import json
import math

def quad(a, b, c):
    if a != 0 and isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
        a_str = str(a)
        b_str = str(b)
        c_str = str(c)

        d = ((b ** 2) - (4 * a * c))

        if d < 0:
            all_x = None
        elif d == 0:
            if b == 0:
                all_x = float(0)
            else:
                all_x = (-b / (2 * a))
        elif d > 0:
            x1 = float(round((-b - math.sqrt(d)) / (2 * a), 3))
            x2 = float(round((-b + math.sqrt(d)) / (2 * a), 3))

            all_x = [x1, x2]
            all_x.sort()

        if a > 1 or a < -1 :
            part1 = a_str+'x^2'
        elif a == 1:
            part1 = 'x^2'
        elif a == -1:
            part1 = '-x^2'

        if b == 0:
            part2 = ''
        elif b > 0 and b < 1 or b > 1:
            part2 = '+' + b_str + 'x'
        elif b == 1:
            part2 = '+' + b_str + 'x'
        elif b < 0 and b > -1 or b < -1:
            part2 = b_str + 'x'
        elif b == -1:
            part2 = '-x'

        if c == 0:
            part3 = ''
        elif c > 0 :
            part3 = '+' + c_str
        elif c < 0:
            part3 = c_str

        pat_str = part1 + part2 + part3 +'=0'

        result = {'equation': pat_str, 'solution': {'discriminant': round(float(d), 3), 'x': all_x}}
        return json.dumps(result, indent=3)
    else:
        return f'Cannot generate a quadratic equation.'
