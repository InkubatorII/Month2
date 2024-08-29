import sqlite3
with sqlite3.connect('person.db') as connection:
    cursor = connection.cursor()

    # cursor.execute('DROP TABLE IF EXISTS Departments')
    # cursor.execute('DROP TABLE IF EXISTS Employees')
    #
    # cursor.execute('''CREATE TABLE IF NOT EXISTS Departments(
    #     DepartmentID INTEGER PRIMARY KEY,
    #     DepartmentName TEXT NOT NULL
    # )''')
    # cursor.execute('''CREATE TABLE IF NOT EXISTS Employees(
    #     EmployeeID INTEGER PRIMARY KEY,
    #     FirstName TEXT NOT NULL,
    #     LastName TEXT NOT NULL,
    #     DepartmentID INTEGER
    #
    # )''')

    # cursor.execute('''INSERT INTO Departments (DepartmentID, DepartmentName) VALUES (101, 'HR') ''')
    # cursor.execute('''INSERT INTO Departments (DepartmentID, DepartmentName) VALUES (102, 'IT') ''')
    # cursor.execute('''INSERT INTO Departments (DepartmentID, DepartmentName) VALUES (103, 'Sales') ''')
    #
    # cursor.execute('''INSERT INTO Employees (EmployeeID, FirstName, LastName, DepartmentID)
    # VALUES (1, 'Tair', 'Akimov', 101)''')
    # cursor.execute('''INSERT INTO Employees (EmployeeID, FirstName, LastName, DepartmentID)
    # VALUES (2, 'Aibek', 'Djamalbekov', 101)''')
    # cursor.execute('''INSERT INTO Employees (EmployeeID, FirstName, LastName, DepartmentID)
    # VALUES (3, 'Firuza', 'Khasanova', 102)''')
    # cursor.execute('''INSERT INTO Employees (EmployeeID, FirstName, LastName, DepartmentID)
    # VALUES (4, 'Dastan', 'Erkibaev', 102)''')
    # cursor.execute('''INSERT INTO Employees (EmployeeID, FirstName, LastName, DepartmentID)
    # VALUES (5, 'Timur', 'Tahirovich', 103)''')
    # cursor.execute('''INSERT INTO Employees (EmployeeID, FirstName, LastName, DepartmentID)
    # VALUES (6, 'Nastya', 'Li', 103)''')

    cursor.execute('''SELECT Employees.EmployeeID, Employees.FirstName, Employees.LastName, Departments.DepartmentName
    FROM Employees
    JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID
    ''')

    cursor.execute('''SELECT Employees.EmployeeID, Employees.FirstName, Employees.LastName, Departments.DepartmentName
    FROM Employees
    JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID
    WHERE Departments.DepartmentName = 'IT'
    ''')


    employees_in_it = cursor.fetchall()
    for employee in employees_in_it:
        print(f"ID: {employee[0]}, Имя: {employee[1]}, Фамилия: {employee[2]}, Отдел: {employee[3]}")
