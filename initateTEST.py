import sqlite3

       
connection = sqlite3.connect('resources/railway.db') 
database = connection.cursor()
database.execute(f"""CREATE TABLE IF NOT EXISTS Stations(
                         id_station INT PRIMARY KEY,
                         station_name STRING)""")
connection.commit()
with open('resourcesTEST/Stations.csv','r') as file:
    data = []
    for row in file:
        data.append(row.split(";"))
    data = data[1::]
    for row in data:
        database.execute(f"""
                INSERT INTO Stations
                VALUES (?, ?)
            """, row)
        
connection.commit()

database.execute(f"""CREATE TABLE IF NOT EXISTS Routes(
                         id_route INT PRIMARY KEY,
                         route_name_short CHAR(7),
                         route_name STRING)""")
connection.commit()
with open('resourcesTEST/Routes.csv','r') as file:
    data = []
    for row in file:
        data.append(row.split(";"))
    data = data[1::]
    for row in data:
        database.execute(f"""
                INSERT INTO Routes
                VALUES (?, ?, ?)
            """, row)
        
connection.commit()

database.execute(f"""CREATE TABLE IF NOT EXISTS Stops(
                         id_stop INT,
                         stop_number INT,
                         id_station STRING,
                         PRIMARY KEY(id_stop, stop_number))""")
connection.commit()
with open('resourcesTEST/Stops.csv','r') as file:
    data = []
    for row in file:
        data.append(row.split(";"))
    data = data[1::]
    for row in data:
        database.execute(f"""
                INSERT INTO Stops
                VALUES (?, ?, ?)
            """, row)
        
connection.commit()

database.execute(f"""CREATE TABLE IF NOT EXISTS Schedule(
                         id_route INT,
                         stop_number INT,
                         course_number INT,
                         arrival_time STRING,
                         PRIMARY KEY(id_route, stop_number, course_number))""")
connection.commit()
with open('resourcesTEST/Schedule.csv','r') as file:
    data = []
    for row in file:
        data.append(row.split(";"))
    data = data[1::]
    for row in data:
        database.execute(f"""
                INSERT INTO Schedule
                VALUES (?, ?, ?, ?)
            """, row)
        
connection.commit()

database.execute(f"""CREATE TABLE IF NOT EXISTS Positions(
                         id_position INT PRIMARY KEY,
                         position_name STRING,
                         salary FLOAT,
                         salary_allowance FLOAT)""")
connection.commit()
with open('resourcesTEST/Positions.csv','r') as file:
    data = []
    for row in file:
        data.append(row.split(";"))
    data = data[1::]
    for row in data:
        database.execute(f"""
                INSERT INTO Positions
                VALUES (?, ?, ?, ?)
            """, row)
        
connection.commit()

database.execute(f"""CREATE TABLE IF NOT EXISTS Employees(
                         id_employee INT PRIMARY KEY,
                         name STRING,
                         surname STRING,
                         gender CHAR,
                         date_of_birth STRING,
                         email STRING,
                         phone_number STRING,
                         id_position INT,
                         id_dcument INT,
                         id_train INT,
                         password STRING)""")
connection.commit()
with open('resourcesTEST/Employees.csv','r') as file:
    data = []
    for row in file:
        data.append(row.split(";"))
    data = data[1::]
    for row in data:
        database.execute(f"""
                INSERT INTO Employees
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, row)
        
connection.commit()

database.execute(f"""CREATE TABLE IF NOT EXISTS Tickets(
                         id_ticket INT PRIMARY KEY, 
                         id_passanger INTAGER,
                         document STRING,
                         start_station STRING,
                         end_station STING,
                         id_route INT,
                         travel_time STRING,
                         price FLOAT,
                         date_of_purchase STRING,
                         id_employeee INT
                )""")
connection.commit()
with open('resourcesTEST/Tickets.csv','r') as file:
    data = []
    for row in file:
        data.append(row.split(";"))
    data = data[1::]
    for row in data:
        database.execute(f"""
                INSERT INTO Tickets
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, row)
        
connection.commit()

database.execute(f"""CREATE TABLE IF NOT EXISTS Documents(
                         id_document INT PRIMARY KEY,
                         document_name STRING,
                         discount DECIMAL)""")
connection.commit()
with open('resourcesTEST/Documents.csv','r') as file:
    data = []
    for row in file:
        data.append(row.split(";"))
    data = data[1::]
    for row in data:
        database.execute(f"""
                INSERT INTO Documents
                VALUES (?, ?, ?)
            """, row)
        
connection.commit()

database.execute(f"""CREATE TABLE IF NOT EXISTS Passangers(
                         id_passanger INT PRIMARY KEY,
                         name STRING,
                         surname STRING,
                         sex CHAR,
                         date_of_birth STRING,
                         email STRING,
                         phone_number STRING,
                         id_document INT,
                         id_employeee INT,
                         password STRING)""")
connection.commit()
with open('resourcesTEST/Passangers.csv','r') as file:
    data = []
    for row in file:
        data.append(row.split(";"))
    data = data[1::]
    for row in data:
        database.execute(f"""
                INSERT INTO Passangers
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, row)
        
connection.commit()

database.execute(f"""CREATE TABLE IF NOT EXISTS Trains(
                         id_train INT PRIMARY KEY,
                         train_model STRING,
                         id_route INT,
                         number_of_seats INT)""")
connection.commit()
with open('resourcesTEST/Trains.csv','r') as file:
    data = []
    for row in file:
        data.append(row.split(";"))
    data = data[1::]
    for row in data:
        database.execute(f"""
                INSERT INTO Trains
                VALUES (?, ?, ?, ?)
            """, row)
        
connection.commit()
connection.close()
print("DATABASE_DEMO IS READY TO USE")