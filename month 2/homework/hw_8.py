import sqlite3

db_name = 'hw_8.db'


def find_info(db_file):
    print('Вы можете отобразить список учеников по выбранному id города из перечня городов ниже,'
          'для выхода из программы введите 0: ')

    sql = '''SELECT id, title FROM cities;'''
    try:
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(f'{row[0]}. {row[1]}')
    except sqlite3.Error as e:
        print(e)
    find_id = int(input())
    if find_id != 0:
        sql = f''' SELECT s.first_name, s.last_name, co.title as country, c.title as city, c.area 
FROM students AS s
INNER JOIN
cities AS c ON s.city_id = {find_id}
INNER JOIN 
countries as co ON {find_id} = c.id AND c.country_id = co.id
    '''
        try:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(e)

find_info(db_name)