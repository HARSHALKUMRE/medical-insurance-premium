from .configuration import TIMESTAMP
import logging
import os,sys

LOG_DIR = "insurance_logs"

LOG_FILE_NAME = f"log_{TIMESTAMP}.log"

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
                    filemode='w',
                    format='[%(asctime)s] \t%(levelname)s \t%(lineno)d \t%(filename)s \t%(funcName)s() \t%(message)s',
                    level=logging.INFO
                    #level=logging.DEBUG
                    )