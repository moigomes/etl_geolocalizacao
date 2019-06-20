from database import connections
from database import queries


class Load:

    def __init__(self, destination='sqlite3'):
        if destination == 'sqlite3':
            self.__connection = connections.get_conection_sqlite3()
            self.__connection.cursor().execute(queries.create_table_results())
            self.__connection.commit()



    def save(self, adress):
        self.__connection.cursor().execute(queries.insert_results(adress))
        self.__connection.commit()
