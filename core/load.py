import logging

from database import conexoes
from database import queries


class Load:

    def __init__(self, destino='sqlite3'):
        try:
            if destino == 'sqlite3':
                self.__conexao = conexoes.get_conexao_sqlite3()
                self.__conexao.cursor().execute(queries.criar_tabela_resultados())
                self.__conexao.commit()

        except Exception as erro:
            logging.error(f'Erro ao criar tabela resultados! - {erro}')
            exit()

    def salvar(self, endereco: dict):
        try:
            self.__conexao.cursor().execute(queries.insert_resultados(endereco))
            self.__conexao.commit()

        except Exception as erro:
            logging.error(f'Erro ao inserir endereço no banco de dados! - {erro}')
            raise







