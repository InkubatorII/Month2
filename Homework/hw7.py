import sqlite3 as sql3

with sql3.connect('users.db') as connection:
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    salary READ NOT NULL
    ) ''')

    # cursor.execute('''INSERT INTO employees (name, salary)
    # VALUES ('Исак', 50000), ('Олег', 55000), ('Исак', 60000), ('Анита', 65000), ('Иван', 70000), ('Айбек', 75000), ('Влад', 80000),
    # ('Олеся', 85000), ('Евгений', 90000), ('Тилек', 95000)

    # ''')

    cursor.execute('''SELECT rowid, * FROM employees''')

    for row in cursor.fetchall():
        print(row)

