# Словари - dict, множества - set
# {key: value}

# beshbarmak = {'мясо', 'тесто', 'лук'}
# plov = {'рис', 'мясо', 'морковь'}
#
# print(beshbarmak.intersection(plov))
# print(beshbarmak.difference(plov))
# print(beshbarmak.symmetric_difference(plov))
# print(beshbarmak.union(plov))




student = {
    'name': 'adilet',
    'age': 19,
    #1: 45,
    #2: False
}

# for key, value in student.items():
#     print(f'{key}: {value}')


# print(student['nam']) --> код не работает из-за ошибки
# print(student.get('nam', 'нет такого ключа')) --> при ошибки выводит то что после запятой(default=None)

"""add"""
# student['weight'] = 64.8
# student.update(surname='manasov', country='KG')
# student.update({'name': 'manasov', 'country':'KG'})
# student['hobby'] = ['football', 'checkers']
# print(student)

""""edit"""
# student['age'] = 20
# student['name'] = 'tilek'


"""delete"""
# student.pop(1)
# del student[2]


# print(student)
# print(student['name'])
# print(student['age'])