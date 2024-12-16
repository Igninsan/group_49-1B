from random import randint

def game(money_amount, guess_range: list, attempts):
    while input('Хотите начать игру? Если нет, то введите "выход": ') != 'выход':
        print(f'Ваше количество денег: {money_amount}')
        guess_number = randint(int(guess_range[0]), int(guess_range[-1]))
        bet_money = int(input('Сколько вы хотите поставить? '))

        if bet_money > money_amount:
            print('У вас нет столько денег.')
            continue

        money_amount -= bet_money

        for i in range(attempts):
            print(f'Угадайте число от {guess_range[0]} до {guess_range[-1]}. Количество попыток: {attempts - i}.')

            if int(input('Выберите число: ')) == guess_number:
                money_amount += bet_money * 2
                print('Вы угадали число!')
                break
            elif i != attempts - 1:
                print('Вы не угадали число. Попробуйте ещё.')
            else:
                print('Вы не угадали число. У вас закончились попытки.')

        if money_amount == 0:
            print('У вас закончились деньги.')
            break

    print(f'Ваш итоговый баланс: {money_amount}')

