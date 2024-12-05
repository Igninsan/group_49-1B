def safety_check(password:str):
    if len(password) >= 6:
        letter_check = 0
        digit_check = 0
        alphabet = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщьъыэюя'
        digit = '1234567890'
        for letter in password:
            if letter.lower() in alphabet:
                letter_check = 1
            if letter in digit:
                digit_check = 1
            if letter_check == 1 and digit_check == 1:
                return True
    return False

print(safety_check(input('Введите пароль: ')))