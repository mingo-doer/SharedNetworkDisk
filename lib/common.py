import logging.config
from conf import settings
from core import admin
import os

def get_logger(name):
    logging.config.dictConfig(settings.LOGGING_DIC)
    return logging.getLogger(name)