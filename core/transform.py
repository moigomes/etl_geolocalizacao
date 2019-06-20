import requests


class Transform:

    def __init__(self, key_google_maps,
                 url_base='https://maps.googleapis.com/maps/api/geocode/json?'):

        self.__url_base = url_base
        self.__key_google_maps = key_google_maps

        self.__address_components_type = {'rua': 'route',
                                          'numero': 'street_number',
                                          'bairro': 'sublocality',
                                          'cidade': 'administrative_area_level_2',
                                          'cep': 'postal_code',
                                          'uf': 'administrative_area_level_1',
                                          'pais': 'country'}

    def get_adress(self, pair_of_coordinates):
        response = requests.get(self.__get_ful_url(pair_of_coordinates)).json()
        return self.__mount_dict_with_address(pair_of_coordinates, response)

    def __get_ful_url(self, pair_of_coordinates):
        return f'{self.__url_base}latlng={pair_of_coordinates[0]},{pair_of_coordinates[1]}&key={self.__key_google_maps}'

    @staticmethod
    def __get_response_address_components(response):
        return response['results'][0]['address_components']


    def __mount_dict_with_address(self, pair_of_coordinates, response):
        adress_dict = {'latitude': pair_of_coordinates[0], 'longitude': pair_of_coordinates[1]}
        for component_type in self.__address_components_type.items():
            adress_dict[component_type[0]] = ''
            for component in self.__get_response_address_components(response):
                if component_type[1] in component['types']:
                    adress_dict[component_type[0]] = component['short_name']
                    break

        return adress_dict

