import sqlite3



class DBHandler:

       
    def create_table_stations():
        connection = sqlite3.connect('C:/Users/Szymon/Desktop/TMS/railway.db')
        database = connection.cursor()
        database.execute(f"""CREATE TABLE IF NOT EXISTS Stations(
                         ID INTAGER PRIMARY KEY,
                         station_name VARCHAR)""")
        connection.commit()

DBHandler.create_table_stations()
