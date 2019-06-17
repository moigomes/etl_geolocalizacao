import time


from extracao import Extracao
from transformacao import Transformacao


coordenadas: list = Extracao('data_points_20180101.txt').get_coordenadas()


transformacao = Transformacao()

for par_coordenadas in coordenadas:
    teste = transformacao.get_edereco(par_coordenadas)

    print(teste)

    break
