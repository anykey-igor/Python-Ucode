from generator.names import *
from generator.titles import *
import logging
import logging.config
import random

dictLogConfig = {
    "version": 1,
    "handlers": {
        # "fileHandler": {
        #     "class": "logging.FileHandler",
        #     "formatter": "myFormatter",
        #     "filename": "config.log"
        # },
        "consoleHandler": {
            "class": "logging.StreamHandler",
            "formatter": "myFormatter",
            "stream": "ext://sys.stdout"
        }
    },
    "loggers": {
        "..::Knight Generator::..": {
            "handlers": ["consoleHandler"],
            "level": "INFO",
        }
    },
    "formatters": {
        "myFormatter": {
            "format": "%(name)s 8672-%(levelname)s-%(message)s"
        }
    }
}

logging.config.dictConfig(dictLogConfig)
logger = logging.getLogger("..::Knight Generator::..")
logger.info("Package __init__ executed.")
