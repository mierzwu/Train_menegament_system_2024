import sqlite3

connection = sqlite3.connect('resources/railway.db') 
database = connection.cursor()

database.execute(f"""SELECT *
                FROM Employees, Positions""")
connection.commit()
data = database.fetchall()
for row in data:
    print(row)
connection.close()
#test