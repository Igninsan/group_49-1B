"Задание №1"

# def nearest_number(closest_list: list or tuple, target: int) -> tuple:
#     """
#     Принимает список или кортеж, состоящие из чисел, целевое число.
#     Возвращает кортеж состоящий из целевого числа и отсортированного списка.
#     числа списка стоят в порядке их приближенности к целевому числу (Начиная с самого близкого числа)
#     """
#
#     sorted_tuple = (target, sorted(closest_list, key = lambda number: abs(number - target)))
#     return sorted_tuple
#
# print(nearest_number([5, 20.18, 103, 4], 27))

"Задание №2"
# numbers = range(1, 101)
#
# not_divide_3 = list(filter(lambda number: number % 3 != 0, numbers))
# """оставляет только числа, которые не делятся на 3 без остатка"""
# print(not_divide_3)
#
#
# words = 'abcdefghijklmnopqrstuvwxyz'
#
# words_mapped = list(map(lambda word: word.upper() + word, words))
# """создает список из английского алфавита, в каждом индексе которого - заглавная и прописная буква алфавита"""
# print(words_mapped)
#
#
"Задание №3"
#
# def find_with_index(object=[1, 2, 3, 4, 5]):
#     """
#     Может принимать итерируемый объект. Запускает бесконечный цикл.
#     При вводе индекса, выводит элемент под данным индексом в итерируемом объекте.
#     Для выхода введите 'exit', 'выход' или 'break'
#     """
#
#     while True:
#         print('Вашим объектом является:', object)
#         index = input('Введите индекс: ')
#         if index.lower() in ['exit', 'выход', 'break']:
#             break
#         try:
#             print((object[int(index)]))
#         except:
#             print(f'Вы указали неверный индекс. Верными индексами являются: {list(range(len(object)))}')
#
# print(find_with_index())