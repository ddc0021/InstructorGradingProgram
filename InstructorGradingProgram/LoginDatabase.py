import sqlite3
from sqlite3 import Error
class Database:
    def create_connection(self, db_file):
        #Create a database connection to a SQLite database
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)
        return conn

    def create_table(self, conn, create_table_sql):
        print("Create table function")