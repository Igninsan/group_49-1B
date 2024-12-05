day = int(input('Введите день рождения: '))
month = input('Введите месяц рождения: ')

if 21 <= day <= 31 and month == '03' or 1 <= day <= 20 and month == '04':
    print('Овен')
elif 21 <= day <= 30 and month == '04' or 1 <= day <= 21 and month == '05':
    print('Телец')
elif 22 <= day <= 31 and month == '05' or 1 <= day <= 21 and month == '06':
    print('Близнецы')
elif 22 <= day <= 30 and month == '06' or 1 <= day <= 22 and month == '07':
    print('Рак')
elif 23 <= day <= 31 and month == '07' or 1 <= day <= 21 and month == '08':
    print('Лев')
elif 22 <= day <= 31 and month == '08' or 1 <= day <= 23 and month == '09':
    print('Дева')
elif 24 <= day <= 30 and month == '09' or 1 <= day <= 23 and month == '10':
    print('Весы')
elif 24 <= day <= 31 and month == '10' or 1 <= day <= 22 and month == '11':
    print('Скорпион')
elif 23 <= day <= 30 and month == '11' or 1 <= day <= 22 and month == '12':
    print('Стрелец')
elif 23 <= day <= 31 and month == '12' or 1 <= day <= 20 and month == '01':
    print('Козерог')
elif 21 <= day <= 31 and month == '01' or 1 <= day <= 19 and month == '02':
    print('Водолей')
elif 20 <= day <= 29 and month == '02' or 1 <= day <= 20 and month == '03':
    print('Рыбы')
else:
    print('Дата введена неправильно, пример правильного ввода даты: 06.09')