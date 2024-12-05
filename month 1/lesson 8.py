# Контекстный менеджер "with", работа с файлами
# w - write (запись, перезапись)
# a - add (дозапись)
# x -  (проверяет есть ли такой же файл)

# file = open('file_name.txt', 'w', encoding='utf8')
# file.write('строка на кириллице!')
# file.close()
#
# with open('file_name.txt', 'a', encoding='utf8') as file:
#     file.write('new data')

# with open('file2.txt', 'x', encoding='utf8') as new_file:
#     new_file.write('111')


# from time import sleep
#
# with open('file_name1.txt', 'r') as file:
#     for i in file.read():
#         sleep(0.1)
#         print(i, end='')