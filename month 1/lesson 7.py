# Lambda функции. Обработка исключений.
#
# def up_first_letter(word: str) -> str:
#     """Принимает слово и возвращает его с большой буквы."""
#     return word.title()
#
# def show_words(func, objects):
#     for obj in objects:
#         print(func(obj))

# show_words(lambda word: word.title(), ['kant', 'talas', 'balykchy'])
# show_words(len, ['tokyo', 'london', 'paris'])
# show_words(up_first_letter, ['tokmok', 'bishkek', 'karakol'])


# lambda_func = lambda a, b: a + b
# print(lambda_func(2, 3))
# print(type(lambda_func))

# def plus(a, b):
#     return a + b

# print(plus(2, 3))
# print(type(plus))

words = ['berlin', 'abu-dhabi', 'paris', 'rome', 'istanbul', 'moscow']
# print(words)

# words_sorted = sorted(words, key = lambda word: word[-1])
# print(words_sorted)

words_filtered = list(filter(lambda word: 'i' not in word, words))
print(words_filtered)
#
words_mapped = list(map(lambda word: word.upper(), words))
print(words_mapped)


# try:
#     print(2 * 'ty')
# except:
#     print('есть ошибка')
# else:
#     print('нет ошибки')
# finally:
#     print('проверка завершена')


# students_count = tuple(range(1, 23))
# counter = 1
# data = {}
#
# while counter != len(students_count):
#     try:
#         exist = int(input(f'#{counter} ? '))
#     except:
#         print('неверный ввод, повторите попытку!')
#     else:
#         if exist:
#             data[input(f'enter name #{counter}: ')] = counter
#             counter += 1
#         print(data)
#
# print(len(data), students_count)