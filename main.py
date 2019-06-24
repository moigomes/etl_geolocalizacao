import logging

from core.extract import Extract
from core.load import Load
from core.transform import Transform
from utils.file_tools import FileTools
from utils import log_tools

log_tools.ajustar_log()

transform = Transform(key_google_maps='AIzaSyBhFuJK5JqixSDEaKPGjUmAoARcpntgU-c')

load = Load()

file_tools = FileTools()
file_tools.diretorio_arquivos = 'resources'
file_tools.diretorio_arquivos_movidos = 'resources/arquivos_extraidos'

while True:

    logging.info(f'Escaneando diretório: ({file_tools.diretorio_arquivos})')
    arquivos = file_tools.escanear_diretorio(intervalo=0.5)

    if len(arquivos) > 1:
        logging.info(f'Arquivo txt encontrado: ({arquivos[1]})')

        lista_de_coordenadas = Extract('resources/' + arquivos[1]).get_lista_de_coordenadas()
        logging.info(f'Extraído conteúdo do arquivo: ({arquivos[1]})')

        for latitude, longitude in lista_de_coordenadas:
            endereco: dict = transform.get_endereco(latitude, longitude)
            load.salvar(endereco)

            print(endereco)
            print('-' * 150)

        logging.info(f'Conteúdo do arquivo: ({arquivos[1]}), Extraído, Transformado e carregado na base de dados!')
        file_tools.mover_arquivo(arquivos[1])

    else:
        logging.warning('Nenum arquivo txt encontrado!')




