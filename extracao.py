class Extracao():

    def __init__(self, arquivo: str):
        self.__arquivo = open(f'resources/{arquivo}', 'r')
        self.__coordenadas:[float, float] = []


    def get_coordenadas(self) -> list:
        lista_temporaria:[float, float] = []

        for linha in self.__arquivo:
            linha_lista: list = linha.split(' ')
            if linha_lista[0] == 'Latitude:' or linha_lista[0] == 'Longitude:':
                lista_temporaria.append(float(linha_lista[4].replace('\n', '')))

            if len(lista_temporaria) == 2:
                self.__coordenadas.append(lista_temporaria.copy())
                lista_temporaria.clear()

        self.__arquivo.close()
        return self.__coordenadas
