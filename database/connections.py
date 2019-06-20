import sqlite3


def get_conection_sqlite3():
     return  sqlite3.connect("database/mydatabase.db")
