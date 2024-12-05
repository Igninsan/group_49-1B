def calculator(first: int or float, operation: str, second: int or float) -> int or float or str:

    """
    Принимает первое число, арифметический оператор и второе число.
    Возвращает результат действия данного оператора между первым и вторым числом.
    """

    if type(first) == str or type(second) == str:
        try:
            first, second = float(first), float(second)
        except:
            return 'Вы ввели не числа'

    try:
        if operation in ['+', '-', '*', '/']:
            if operation in ['+', '-']:
                if operation == '+':
                    return first + second
                elif operation == '-':
                    return first - second
            else:
                if operation == '*':
                    return first * second
                else:
                    return first / second
        else:
            if operation == '//':
                return first // second
            elif operation == '%':
                return first % second
            elif operation == '**':
                return first ** second
            else:
                return 'Вы ввели неверный оператор'
    except:
        return 'Вы попытались поделить на ноль.'

print(calculator('5', '/4', 9))
