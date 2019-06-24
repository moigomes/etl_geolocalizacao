import logging
import geocoder


class Transform:

    def __init__(self, key_google_maps: str):
        self.__key_google_maps = key_google_maps

    def get_endereco(self, latitude: float, longitude: float) -> dict:
        try:
            dados_retornados: geocoder = geocoder.google([latitude, longitude],
                                                         method='reverse',
                                                         key=self.__key_google_maps,
                                                         language='pt')
            return {'latitude': latitude,
                    'longitude': longitude,
                    'rua': dados_retornados.street_long,
                    'numero': dados_retornados.housenumber,
                    'bairro': dados_retornados.sublocality,
                    'cidade': dados_retornados.county,
                    'cep': dados_retornados.postal,
                    'uf': dados_retornados.state,
                    'pais': dados_retornados.country_long}

        except Exception as erro:
            logging.error(f'Erro ao realizar requisição usando geocoder.google! - {erro}')
            exit()
