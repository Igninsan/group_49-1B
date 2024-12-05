# monday = float(input('Введите расход за понедельник: '))
# tuesday = float(input('Введите расход за вторник: '))
# wednesday = float(input('Введите расход за среду: '))
# thursday = float(input('Введите расход за четверг: '))
# friday = float(input('Введите расход за пятницу: '))
# saturday = float(input('Введите расход за субботу: '))
# sunday = float(input('Введите расход за воскресенье: '))
#
# sum1 = monday + tuesday + wednesday + thursday + friday + saturday + sunday
# average_round = round(sum1 / 7, 1)
#
# print(f'Общая сумма расходов равна {sum1}')
# print(f'Средний расход в день составляет {average_round}')


expenses = []
for day in range(7):
    expenses.append(float(input(f'Введите расход за {day + 1} день: ')))

sum1 = sum(expenses)
average_round = round(sum1 / 7, 1)

print(f'Общая сумма расходов равна {sum1}')
print(f'Средний расход в день составляет {average_round}')