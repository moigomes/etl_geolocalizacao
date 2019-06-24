import geocoder


class Transform:

    def __init__(self, key_google_maps: str):
        self.__key_google_maps = key_google_maps

    def get_endereco(self, latitude: float, longitude: float) -> dict:

        dados_retornados: geocoder = geocoder.google([latitude, longitude],
                                                     method='reverse',
                                                     key=self.__key_google_maps,
                                                     language='pt')

        if dados_retornados.status_code is 'Unknown':
            raise Exception('Verifique sua conexao com a internet!')

        if len(list(dados_retornados)) == 0:
            raise Exception(f'Erro de comunicação com a api, verifique sua KEY!')

        return {'latitude': latitude,
                'longitude': longitude,
                'rua': dados_retornados.street_long,
                'numero': dados_retornados.housenumber,
                'bairro': dados_retornados.sublocality,
                'cidade': dados_retornados.county,
                'cep': dados_retornados.postal,
                'uf': dados_retornados.state,
                'pais': dados_retornados.country_long}



