# Операторы: принадлежности, назначения. Циклы.

"""for"""
# in_lesson = 0
# not_in_lesson = 0
# students = 20
#
# for number in range(1, 21):
#     answer = input(f'студент под номером №{number}: ')
#     if answer == '1':
#         in_lesson += 1
#     else:
#         not_in_lesson += 1
# print(f'кол-во студентов: {students}\n'
#       f'присутствует: {in_lesson}\n'
#       f'отсутствует: {not_in_lesson}')

# word = 'KYRGYZSTAN'
# for letter in word:
#     if letter == 'S':
#         break
#     # if letter == 'R' or letter == 'Z':
#     if letter in 'RZ':
#         continue
#     print(letter)

"""while"""
# counter = 5
# while counter > 0:
#     print(f'попыток осталось: {counter}')
#     time = input('введите время суток: ').lower()
#     if time == 'stop':
#         break
#     if time == 'morning' or time == 'утро':
#         print('good morning')
#     elif time == 'day' or time == 'день':
#         print('good afternoon')
#     elif time == 'evening' or time == 'вечер':
#         print('good evening')
#     else:
#         print('hello')
#     counter -= 1

# rounds = 0
# while rounds < 100:
#     rounds += 1
#     if rounds == 50:
#         print('exit...')
#         break
#     if rounds % 2 == 0:
#         continue
#     print('Hello, world!', rounds)

"""Операторы: назначения"""
# number = 5
# print(number)
# # number = number + 4
# number += 4
# number /= 2
# number **= 2
# number -= 0.25
# number %= 2
# print(number)


"""Операторы: принадлежности"""
# numbers = range(1, 11)
# print(4 in numbers)
# print(24 in numbers)

# word = 'geeks'
# print('g' in word)
# print('o' in word)

# Кыргызстан
# GEEKS
# алиbek

