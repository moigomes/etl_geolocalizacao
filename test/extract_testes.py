import unittest
from core.extract import Extract


class EstractTestes(unittest.TestCase):

    def setUp(self):
        self.__extracao = Extract('../test/resources/arquivo_txt_de_coordenadas_para_testes.txt')

        self.__linhas = ['Latitude: 30°02′59″S   -30.04982864',
                         'Longitude: 51°12′05″W   -51.20150245',
                         'Distance: 2.2959 km  Bearing: 137.352°']

    def test_get_lista_de_coordenadas(self):
        self.assertEqual([[-30.04982864, -51.20150245]], self.__extracao.get_lista_de_coordenadas())

    def test_get_valor_coordenada(self):
        self.assertEqual(-30.04982864, Extract.get_valor_coordenada(self.__linhas[0]))


if __name__ == '__main__':
    unittest.main()
