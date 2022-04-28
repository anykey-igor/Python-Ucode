import sqlite3
import re

list_db = []    # список открытых соединения с базами данных
db_conect = {}  # словарь содержащий имя базы к которой подключились и ссылки на объект

#pat_command = r'^\w+'
#pat_db = r'\w+.[d|D][b|D]'
pat_query = r'".*"$'
full_pat = r'\b\w+,?\.\w+|\w+|(?:".*"$)'

def f_exit(*args):
    if len(list_db) == 0:
        return False
    else:
        for key in db_conect:
            try:
                cur = db_conect[key]
                cur.close()
                print(f'Closed connection to database "{key}".')
            except sqlite3.Error as error:
                print(error)
        return False


def f_show(*args):
    if len(list_db) > 0:
        print(f'Connected to:\n{list_db}')
    else:
        print(f'No connections.')
    return True


def f_help(*args):
    del args
    command_help = {'help': '- help',
                    'connect': '- connect [database]',
                    'close': '- close [database]',
                    'execute': '- execute [database] "[SQL statement]"',
                    'show': '- show',
                    'exit': '- exit'
                    }
    print('Available commands:')
    for key in command_help:
        print(f'{command_help[key]}')
    return True


def f_connect(*db_name):
    if db_name[0] in list_db:
        print(f'Already connected to database "{db_name[0]}".')
        return True
    else:
        try:
            sqlite_connection = sqlite3.connect(db_name[0])
            list_db.append(db_name[0])                      # добавляем имя базы с которой успешно соединение
            db_conect[db_name[0]] = sqlite_connection       # добавляем в словарь имя базы и ссылку на объект
            print(f'Created connection to database "{db_name[0]}".')
            return True
        except sqlite3.Error as error:
            print(error)


def f_close(*db_name):
    if db_name[0] in list_db:
        if db_name[0] in db_conect:
            try:
                cur = db_conect[db_name[0]]
                cur.close()
                db_conect.pop(db_name[0])
                list_db.remove(db_name[0])
                print(f'Closed connection to database "{db_name[0]}".')
                return True
            except sqlite3.Error as error:
                print(error)
                return True
    else:
        print(f'Cannot close connection to "{db_name[0]}". Not connected.')
        return True


def f_execute(*db_name):
    if db_name[0] not in list_db:
        print(f'Cannot execute SQL statement. Not connected to "{db_name[0]}".')
        return True
    else:
        try:
            if db_name[0] in db_conect:
                sqlite_connection = db_conect[db_name[0]]
                #print(sqlite_connection)
                cur = sqlite_connection.cursor()
                cur.execute(db_name[1])
                sqlite_connection.commit()
            # sqlite_connection = sqlite3.connect(db_name[0]).cursor()
            # sqlite_connection.execute(db_name[1])
            # sqlite3.connect(db_name[0]).commit()
            print(f'Executed SQL statement.')
            return True
        except sqlite3.Error as error:
            print(error)
    return True


if __name__ == '__main__':

    start = True
    command_dict = {'help': {0: f_help},
                    'connect': {1: f_connect},
                    'close': {1: f_close},
                    'execute': {2: f_execute},
                    'show': {0: f_show},
                    'exit': {0: f_exit}
                    }
    while start:
        db_name = ''
        sql_query = ''
        input_command = str(input('Enter command: '))
        input_list = re.findall(full_pat, input_command) # При помощи создаем список содержащий команду и аргументы
        command = input_list[0]  # команду присваиваем переменной, она всегда первая в списке
        input_list.pop(0)  # удаляем из спика команду оставляя только аргументы
        qtty_arg = len(input_list) # Оставший список равен количеству введенных аргументов

        if command in command_dict:  # поиск комманды
            command_list = command_dict[command]
            if qtty_arg in command_list:
                #print(f'This function need: {qtty_arg} args; link to function: {command_list[qtty_arg]}')
                if qtty_arg == 0:
                    pass
                    # db_name = ''
                    # sql_query = ''
                elif qtty_arg == 1:
                    db_name = input_list[0]
                    #sql_query = ''
                elif qtty_arg == 2 and re.match(full_pat, input_list[1]):
                    db_name = input_list[0]
                    sql_query = re.search(pat_query, input_list[1]).group(0)[1:-1]
                start = command_list[qtty_arg](db_name, sql_query)
            else:
                print('Invalid command. Try "help" to see available commands.')
        else:
            print('Invalid command. Try "help" to see available commands.')
