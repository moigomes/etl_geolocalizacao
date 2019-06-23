import logging


class Extract:

    def __init__(self, nome_arquivo_txt: str):
        self.__nome_do_arquivo_txt = nome_arquivo_txt

    def get_lista_de_coordenadas(self) -> list:
        lista_de_cordenadas = []
        arquivo_de_texto = self.abrir_arquivo_de_texto()
        linhas: list = arquivo_de_texto.readlines()
        arquivo_de_texto.close()

        for linha in linhas:
            if 'Latitude:' in linha:
                lista_de_cordenadas.append([Extract.get_valor_coordenada(linha)])
            if 'Longitude:' in linha:
                lista_de_cordenadas[-1].append(Extract.get_valor_coordenada(linha))

        return lista_de_cordenadas

    def abrir_arquivo_de_texto(self):
        try:
            return open(self.__nome_do_arquivo_txt, 'r')

        except FileNotFoundError as erro:
            logging.error(f'Não foi possivel ler o arquivo! - {erro}')
            exit()

    @staticmethod
    def get_valor_coordenada(linha: str) -> float:
        return float(linha.split(' ')[4].replace('\n', ''))
