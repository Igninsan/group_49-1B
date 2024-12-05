

while True:
    color = input('Введите цвет светофора или "выход": ').lower()
    if color == 'выход':
        break
    elif color == 'зеленый':
        print('Можешь идти!')
    elif color == 'желтый':
        print('Подожди!')
    elif color == 'красный':
        print('Стой!')
    else:
        print('Вы ввели неверный цвет, правильными цветами являются: "красный", "желтый", "зеленый" ')