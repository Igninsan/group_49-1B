# Функции: виды параметров, возвращение данных, виды аргументов.

"""схема функции"""
# определение наименование(параметры):
#     (тело функции)
#     возвращение данных
#
# вызов функции
# наименование(аргументы)

# def name_function(surname, name='user'):   #required positional parameter
#     print(f'surname: {surname} name: {name}'.title())
#
#
# name_function(name='chyngyz', surname='aitmatov') #keyword arguments --> когда указываешь какие аргументы к чему относятся

# name_function()
# name_function('ildar')

# name_function('jack')  #required positional argument
# name_function('bruce')
# name_function(input('введите имя'))

# def get_square(length: int, width: int) -> int:
#     """Принимает ширину и длину, возвращает площадь."""
#     return length * width
#
# square_2 = get_square(5, 4)
# square_victory = get_square(250, 120)
#
# print(square_2)
# print(square_victory)
#
# print(help(get_square))
# print(get_square.__doc__)

# length = 5
# width = 4
# square_2 = length * width
# print(square_2)
#
# length = 250
# width = 120
# square_victory = length * width
# print(square_victory)


# *args, **kwargs

# def plus(*args): #arguments -> аргументы
#     return sum(args)
#
# print(plus(3, 4, 1, 6, 9))
# print(plus(31, 42, 10, 60, 91, 42, 75, 354))

# def menu(**kwargs): #keyword arguments -> ключевые аргументы
#     return kwargs
#
# monday = menu(drink='cola', eat='pizza', rtg=456, da='net', wer=345)
# print(monday)

