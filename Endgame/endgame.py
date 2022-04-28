import argparse
import yaml, json
from main import *


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='About our API software.',
        prog='endgame',
        usage='%(prog)s [options]',
        epilog='It is my API tester - %(prog)s')

    parser.add_argument('-m', '--method',
                        action='store',
                        choices=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
                        default='GET',
                        help='The argument must have the choices: GET, POST, PUT, PATCH, and DELETE')

    parser.add_argument('-g', '--gui',
                        action='store_true',
                        help='Start GUI')

    parser.add_argument('--history',
                        choices=['show', 'clear'],
                        help='Show 10 last requests or clear all')

    parser.add_argument('-a', '--auth',
                        nargs=2,
                        type=str,
                        help='Set username and password')

    parser.add_argument('-l', '--log',
                        default='INFO',
                        choices=['INFO', 'DEBUG', 'WARNING'],
                        type=logger_start(log),
                        help='Set logging level (Default INFO)')

    parser.add_argument('-e', '--endpoint',
                        type=str,
                        help='Set endpoint of request')

    parser.add_argument('-p', '--params',
                        nargs='+',
                        #action='append',
                        type=lambda kv: kv.split("=", 1) ,
                        #type=my_func,
                        help='Set params of request')

    parser.add_argument('--headers',
                        nargs='+',
                        #action='append',
                        type=lambda kv: kv.split("=", 1),
                        dest='headers',
                        help='Set headers of request')

    parser.add_argument('-b', '--body',
                        nargs='+',
                        #action='append',
                        type=lambda kv: kv.split("=", 1),
                        #type=str,
                        help='Set body of request')

    parser.add_argument('--tree',
                        action='store_true',
                        help='Set Tree view mode')

    parser.add_argument('-r', '--raw',
                        action='store_true',
                        help='Set Raw view mode')

    parser.add_argument('--pretty',
                        action='store_true',
                        help='Set Pretty JSON view mode')

    parser.add_argument('-y', '--yaml',
                        action='store_true',
                        help='Set Yaml view mode')

    """Нужно принять имя файла переменных и имя файла аргументов запроса"""

    args = parser.parse_args()

    """Все полученные аргументы преобразовываем в словарь"""
    #print(args)
    all_args = names_list_to_dict(**vars(args))
    # my_var = get_variables('variable.yaml')
    # if my_var == None:
    complite = extract_variable('variable.yaml', **all_args)
    #print(complite)

    if args.gui:
        print('RUN Gui turned ON\n')
        mainwindow(all_args)

    else:
        print(f'---->>>> с CLI версией - выполняем запросы')
        web_surfer(complite)