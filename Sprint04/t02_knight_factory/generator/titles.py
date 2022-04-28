import random
import logging

module_logger = logging.getLogger("..::Knight Generator::..")


def titles(list_title: list):
    logger = logging.getLogger("..::Knight Generator::..")

    title = 'the ' + random.choice(list_title)

    logger.info("[Title chosen.]")
    return title
