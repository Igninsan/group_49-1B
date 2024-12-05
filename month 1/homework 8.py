print('Загадайте число от 1 до 100')
min_number = 1
max_number = 100
answer_count = 0
answer_list = []
while True:
    point = round((max_number - min_number) / 2)
    if point < min_number:
        point += min_number
    print(f'Ваше число {point}?')
    answer = input().lower()
    if answer not in ["да", "больше", "меньше"]:
        print('Введен неправильный ответ. Правильными ответами являются: "да", "больше", "меньше"')
        continue
    answer_list.append(point)
    if answer == 'да':
        with open('game_results.txt', 'w', encoding='utf8') as file:
            file.write(f'Количество попыток: {answer_count + 1} \nСписок попыток:{answer_list} \nЗагаданным числом было: {point}')
            break
    elif answer == 'больше':
        min_number = point
    elif answer == 'меньше':
        max_number = point

    answer_count += 1