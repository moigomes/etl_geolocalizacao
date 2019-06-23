import sqlite3


def get_conexao_sqlite3():
     return sqlite3.connect("database/mydatabase.db")
