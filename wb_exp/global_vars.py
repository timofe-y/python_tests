# coding=utf-8

import os
import configparser
import logging
from logging.handlers import RotatingFileHandler


main_logger =   None

WB_token =      None
WB_server =     None
Export_catalog = None

def read_configparser():
    global WB_token
    global WB_server
    global Export_catalog

    config = configparser.ConfigParser()
    config.read(os.path.abspath('settings.ini'))

    WB_token = config['WB']['token']
    WB_server = config['WB']['server']
    Export_catalog = config['Catalogs']['Export_catalog']


# Настройка логирования
def init_logging():
    log_format = '%(asctime)s [%(levelname)s] %(funcName)s (%(lineno)d) -> %(message)s'

    file_handler = RotatingFileHandler(os.path.abspath('wb.log'), maxBytes=10485760, backupCount=10)
    file_handler.setFormatter(logging.Formatter(log_format))
    file_handler.setLevel(logging.DEBUG)
    # file_handler.setLevel(logging.ERROR)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(logging.Formatter(log_format))

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger


def init():
    global main_logger
    main_logger = init_logging()
    read_configparser()

    main_logger.info('WB_token: ' + str(WB_token))
    main_logger.info('WB_server: ' + str(WB_server))
    main_logger.info('Export_catalog: ' + str(Export_catalog))
