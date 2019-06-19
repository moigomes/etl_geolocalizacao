import requests


class Transformacao():

    def __init__(self, key_google_maps='AIzaSyBhFuJK5JqixSDEaKPGjUmAoARcpntgU-c', url_base='https://maps.googleapis.com/maps/api/geocode/json?'):
        self.__url_base = url_base
        self.__key_google_maps = key_google_maps

        self.__address_components_type = {}

        self.__address_components_type['rua'] = 'route'
        self.__address_components_type['numero'] = 'street_number'
        self.__address_components_type['bairro'] = 'sublocality'
        self.__address_components_type['cidade'] = 'administrative_area_level_2'
        self.__address_components_type['cep'] = 'postal_code'
        self.__address_components_type['uf'] = 'administrative_area_level_1'
        self.__address_components_type['pais'] = 'country'

    def get_edereco(self, coordenadas: [[float, float]]) -> dict:

        endereco = {}

        url_completa = f'{self.__url_base}latlng={coordenadas[0]},{coordenadas[1]}&key={self.__key_google_maps}'

        response = requests.get(url_completa).json()

        for chave, component_type in self.__address_components_type.items():
            for component in response['results'][0]['address_components']:
                if component_type in component['types']:
                    endereco[chave] = component['short_name']

            #endereco[chave] = ''

        return endereco
