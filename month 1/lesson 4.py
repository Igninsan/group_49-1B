# Списки - list, кортежи - tuple. Индексы и срезы. Встроенные функции к наборам элементов.
# Списковое включение List comprehension.


# a = (23) # не tuple (int)
# b = (23,) # tuple



"""Списковое включение List comprehension."""
# students = ['abdykalyk', 'aisuluu', 'mirbek', 'ademi', 'diana']
# students2 = [student.upper() for student in students if student.startswith('a')]
# print(students)
# print(students2)


"""add"""
# students.append('islam') # добавляет 1 объект в конец списка
# students.insert(2, 'aidar')  # добавляет 1 объект в выбранный индекс (остальные сдвигаются вправо)
# students.extend(['petr', 'iskender'])  # то же что и += (добавляет в конец списка несколько элементов из другого списка)
# students += ['karim', 'nurmuhammed']  # то же что и extend

"""edit"""
# students[-1], students[0] = students[0], students[-1]
# students.sort()
# students.reverse()
# students[0] = 'sardor'
# students[-2:] = ['aslan', 'timur']

"""delete"""
# print(students)
# students.remove('mirbek') #удаление по названию
# students.pop(0) #удаление по индексу (сохраняет в себе объект который удалил)
# # deleted = students.pop(0) #вот так можно сохранить объект
# del students[:2] #удаление по срезу (типо несколько)
# students.clear() #полное очищение (удаление всего)
#
# # print(deleted)
# print(students)


'''Индексы и срезы [start:stop:step]'''

# print(students[-2][3:])
# print(students[-1][2])
# print(students[0])
# print(students[1])
# print(students[-1])
#
# print(students[1:3])
# print(students[-2:])
# print(students[:2])
# print(students[::-1])
# print(students[::2])


"""Встроенные функции к наборам элементов."""
# numbers = [1, 2, 3, 0, 5]
# print(len(numbers)) #длина
# print(sum(numbers)) #сумма всех
# print(min(numbers)) #минимальное
# print(max(numbers)) #максимальное
# print(all(numbers)) #если хотя бы 1 объект имеет булевое значение = False --> возвращает False, иначе --> True
# print(any(numbers)) #если ВСЕ объекты имеют булевое значение = False --> возвращаeт False, иначе ---> True


