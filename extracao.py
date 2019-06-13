class Extracao():

    def __init__(self, arquivo):
        self.__arq = open(f'resources/{arquivo}', 'r')


    def get_dados(self):
        dados = self.__arq.readlines()
        self.__arq.close()
        return dados