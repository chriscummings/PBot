'''Tranceiver-service Logging (to both stdout and file)
'''

import logging
import os


# Params
########
# TODO: Move to constants

FILENAME          = 'transceiver.log'
NAME              = os.path.basename(FILENAME)
FILE_LOG_LEVEL    = logging.NOTSET
CONSOLE_LOG_LEVEL = FILE_LOG_LEVEL
FILE_FORMAT       = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
CONSOLE_FORMAT    = '%(name)s - %(levelname)s - %(message)s'

# TODO: Refactor into function a la bot's logger.

logger = logging.getLogger(NAME)
logging.root.setLevel(logging.NOTSET)

# Handlers for Logger
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler(os.path.join('./', FILENAME))

# Log Levels
c_handler.setLevel(CONSOLE_LOG_LEVEL)
f_handler.setLevel(FILE_LOG_LEVEL)

# Formatters
c_format = logging.Formatter(CONSOLE_FORMAT)
f_format = logging.Formatter(FILE_FORMAT)
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)
logger.addHandler(c_handler)
logger.addHandler(f_handler)
