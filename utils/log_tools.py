import logging


def ajustar_log():
    logging.basicConfig(datefmt='%d-%m-%Y %H:%M:%S',
                        level=logging.INFO,
                        format='[%(levelname)-5.5s] %(asctime)s [%(filename)-15.15s / %(funcName)-20.22s / %(lineno)-5.5s] %(message)s')