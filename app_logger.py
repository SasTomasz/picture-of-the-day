import logging
import os
import sys
from logging.handlers import RotatingFileHandler


def set_new_logger(name):
    log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')
    logs_dir = "./app_logs"
    if not os.path.isdir(logs_dir):
        os.makedirs(logs_dir)
    log_file = "./app_logs/logs.log"

    my_handler = RotatingFileHandler(log_file, mode='a', maxBytes=5*1024*1024, backupCount=2, encoding='utf-8', delay=False)
    my_handler.setFormatter(log_formatter)
    my_handler.setLevel(logging.DEBUG)

    app_logger = logging.getLogger(name)
    app_logger.setLevel(logging.DEBUG)

    app_logger.addHandler(my_handler)

    # Show logs in standard output
    app_logger.addHandler(logging.StreamHandler(sys.stdout))
    return app_logger
