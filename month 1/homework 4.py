data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []

for item in data_tuple:
    if type(item) == str:
        letters.append(item)
    else:
        numbers.append(item)

numbers.remove(6.13)
letters.append(numbers.pop(0))
numbers.insert(1, 2)
numbers.sort()
letters.reverse()
letters[1] = letters[1].upper()
letters[-2] = letters[-2].lower()
numbers = [number ** 2 for number in numbers]
letters = tuple(letters)
numbers = tuple(numbers)
print(letters)
print(numbers)