def calculator(*args, **kwargs):
    result = 0
    print(kwargs)

    operator = kwargs['operator']

    first_division_number = 0

    for i in args:
        if operator == '*':
            if result == 0:
                result = 1 * i
            else:
                result = result * i
        elif operator == '-':
            result -= i

        elif operator == '+':
            result += i

        elif operator == '/':
            result /= i

            if result == 0:
                result = i
            else:
                result = result/i

    return result