import logging
import os
import shutil
import time


class FileTools:

    def __init__(self):
        self.diretorio_arquivos = ''
        self.diretorio_arquivos_movidos = ''

    def escanear_diretorio(self, intervalo: float) -> list:
        time.sleep(intervalo)
        for _, _, arquivos in os.walk(self.diretorio_arquivos):
            return arquivos

    def mover_arquivo(self, nome_arquivo):
        shutil.move(f'{self.diretorio_arquivos}/{nome_arquivo}', f'{self.diretorio_arquivos_movidos}/{nome_arquivo}')
        logging.info(f'Arquivo {nome_arquivo} movido para {self.diretorio_arquivos_movidos}')
