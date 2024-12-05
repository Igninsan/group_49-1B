vowels = 'aeiouyаеёиоуыэюя'
consonants = 'bcdfghjklmnpqrstvwxzбвгджзйклмнпрстфхцчшщ'

while True:
    word = input("Напишите слово для разбора. Если хотите выйти, напишите 'exit' или 'выход': ").lower()
    if word == 'exit' or word == 'выход':
        break
    letters_count = 0
    vowels_quantities = 0
    consonants_quantities = 0
    for letter in word:
        letters_count += 1
        if letter in consonants:
            consonants_quantities += 1
        elif letter in vowels:
            vowels_quantities += 1
    percent_vowels = round(vowels_quantities * 100 / letters_count, 2)
    percent_consonants = round(consonants_quantities * 100/ letters_count, 2)

    print(f'Количество букв: {letters_count}')
    print(f'Согласных букв: {consonants_quantities}')
    print(f'Гласных букв: {vowels_quantities}')
    print(f'Гласные/Согласные: {percent_vowels}% / {percent_consonants}%')
