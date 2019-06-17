from pygeocoder import Geocoder


class Transformacao():

    def __init__(self, key_google_maps='AIzaSyBhFuJK5JqixSDEaKPGjUmAoARcpntgU-c'):
        self.__geocoder = Geocoder(api_key=key_google_maps)



    def get_edereco(self, coordenadas: [[float, float]]) -> dict:
        teste = self.__geocoder.reverse_geocode(coordenadas[0], coordenadas[1])
        print(type(teste))
        return teste

