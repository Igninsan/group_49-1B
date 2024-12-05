def find_closest(numbers: list, find=0):
    closest = min(numbers)
    for number in numbers:
        if abs(number-find) < abs(closest-find):
            closest = number
    return closest

numbers_list = [int(num) for num in input('Введите список чисел: ').split()]
if input('Хотите ли вы ввести целевое число? ').lower() in ['да', 'yes']:
    target = float(input('Введите целевое число: '))
    print(find_closest(numbers_list, find=target))
else:
    print(find_closest(numbers_list))


