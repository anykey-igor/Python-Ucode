from generator import *
import logging

module_logger = logging.getLogger("..::Knight Generator::..")


if __name__ == '__main__':

    logger = logging.getLogger("..::Knight Generator::..")

    name_list = ['Galahad', 'Lancelot', 'Gawain', 'Percivale', 'Lionell', 'Tristram de Lyones', 'Gareth',
                 'Bedivere', 'Bleoberis', 'Lacotemale Taile', 'Lucan', 'Palomedes', 'Lamorak',
                 'Bors de Ganis', 'Safer', 'Pelleas', 'Kay', 'Ector de Maris', 'Dagonet',
                 'Degore', 'Brunor le Noir', 'Lebius Desconneu', 'Alymere', 'Mordred']

    title_list = ['Tiny', 'Good-Enough', 'Thrice-Divorced', 'Not-so-Mighty', 'Hungry', 'Puzzled', 'Never-There', 'Tall-One']

    for i in range(5):
        name = names(name_list)
        title = titles(title_list)
        logger.info("%s %s" % (name, title))
