# database
# SQL - язык - Работа с таблицами как в эксель
# noSQL - не табличный, это ввиде графика и каких то других рисунков
# (СУБД) - система управления баз данных
# Oracle(СУБД Microsoft), SQlite, PosgreSQL, mongoDB, MySQL
# CRUD - create, read, update, delete

# SQLite 3.0

import sqlite3 as sql3
# db = sql3.connect('user.db')
# # sql3.connect().cursor() - так не надо прописывать
# cursor = db.cursor()
# db.commit()
# db.close()

with sql3.connect('user.db') as connection:
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS students(
    fullname TEXT NOT NULL,
    pol INT DEFAULT 0,
    bdate DATE
    ) ''')
    # # CREATE
    # cursor.execute('''INSERT INTO students (fullname, pol, bdate)
    # VALUES ('BEKA', 1, '2020-01-01'), ('DASTAN', 2, '2014-12-28')
    #
    # ''')

    # cursor.execute('''SELECT rowid,* FROM students''')
    # # for row in cursor.fetchall():
    # #     print(row)
    # print(cursor.fetchmany(4))
