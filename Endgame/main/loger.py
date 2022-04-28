import logging
import sys


def logger_start(choose):
    logging_level = (lambda x: logging.DEBUG if x == 'DEBUG' else logging.ERROR if x == 'ERROR'\
        else logging.INFO)(choose)
    log = logging.getLogger(':::::END_GAME:::::')
    log.setLevel(logging_level)
    SH = logging.StreamHandler(stream=sys.stdout)
    FH = logging.FileHandler('logs.txt')
    formatter = logging.Formatter('%(name)s %(asctime)s - %(levelname)s - %(message)s')
    SH.setFormatter(formatter)
    FH.setFormatter(formatter)
    log.addHandler(SH)
    log.addHandler(FH)
