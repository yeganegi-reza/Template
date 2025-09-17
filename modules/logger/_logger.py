import os
import logging

from datetime import datetime

LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE_NAME)
os.makedirs(log_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE_NAME)

msg_format = "[ %(asctime)s ]: %(levelname)s %(name)s %(module)s %(lineno)d:-> %(message)s"
logging.basicConfig(filename=LOG_FILE_PATH, format=msg_format, level=logging.INFO)
