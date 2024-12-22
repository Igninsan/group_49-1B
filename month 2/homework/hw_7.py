import sqlite3

db_name = 'hw.db'

sql_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''

def create_table(db_file, create_table_sql):
    try:
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def insert_product(db_file, product):
    sql = '''INSERT INTO products
    (product_title, price, quantity)
    VALUES (?, ?, ?)'''
    try:
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def update_price_product(db_file, product):
    sql = '''UPDATE products SET price = ? WHERE id = ?'''
    try:
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def update_quantity_product(db_file, product):
    sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
    try:
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def delete_product(db_file, id):
    sql  = '''DELETE FROM products WHERE id = ?'''
    try:
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def select_all_products(db_file):
    sql = '''SELECT * FROM products'''
    try:
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

def select_products_by_price_and_quantity(db_file, price_limit, quantity_limit):
    sql = '''SELECT * FROM products WHERE price < ? and quantity > ?'''
    try:
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (price_limit, quantity_limit))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

def find_by_title(db_file):
    sql = '''SELECT * FROM products WHERE product_title LIKE '%сок%' '''
    try:
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


# insert_product(db_name, ('carrot', 51.5, 20))
# insert_product(db_name, ('Яблочный сок', 150.5, 40))
# insert_product(db_name, ('Клубничный йогурт', 55.0, 65))
# insert_product(db_name, ('Апельсиновый сок', 165.0, 38))
# insert_product(db_name, ('Шоколадные вафли', 235.5, 20))
# insert_product(db_name, ('Клубничный сок', 155.0, 45))
# insert_product(db_name, ('Мыло жидкое', 212, 30))
# insert_product(db_name, ('Яблоки красные', 95.8, 25))
# insert_product(db_name, ('Яблоки зелёные', 103.5, 25))
# insert_product(db_name, ('Хлеб белый', 26.7, 86))
# insert_product(db_name, ('Тетрадь 12 л.', 15.65, 68))
# insert_product(db_name, ('Сосиски в тесте', 31.4, 54))
# insert_product(db_name, ('Тетрадь общая 24 л.', 35.5, 47))
# insert_product(db_name, ('Ручка синяя', 20.0, 100))
# insert_product(db_name, ('Гранатовый сок', 180.5, 31))
# insert_product(db_name, ('Тетрадь общая 48 л.', 57.5, 38))

# update_price_product(db_name, (162.5, 2))
# update_quantity_product(db_name, (82, 12))
# delete_product(db_name, 1)
# select_all_products(db_name)
# select_products_by_price_and_quantity(db_name, 150.8, 30)
# find_by_title(db_name)
