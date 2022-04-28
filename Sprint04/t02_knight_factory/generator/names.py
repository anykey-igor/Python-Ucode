import random
import logging

module_logger = logging.getLogger("..::Knight Generator::..")


def names(list_name: list):
    logger = logging.getLogger("..::Knight Generator::..")

    name = 'Sir ' + random.choice(list_name)

    logger.info("[Name chosen.]")
    return name
