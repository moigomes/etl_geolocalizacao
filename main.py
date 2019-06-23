from pprint import pprint

from core.extract import Extract
from core.load import Load
from core.transform import Transform

lista_de_coordenadas = Extract('resources/data_points_20180101.txt').get_lista_de_coordenadas()
transform = Transform(key_google_maps='AIzaSyBhFuJK5JqixSDEaKPGjUmAoARcpntgU-c')
load = Load()

for latitude, longitude in lista_de_coordenadas:
    endereco: dict = transform.get_endereco(latitude, longitude)
    load.salvar(endereco)

    pprint(endereco)
    print('-' * 50)
