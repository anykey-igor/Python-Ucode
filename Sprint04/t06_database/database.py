import mysql.connector as mysql
import yaml
import sys


def read_yaml(*file_name):
    file_name = 'cfg.yaml'
    with open(file_name, 'r') as yaml_config:
        try:
            conf_mysql = yaml.safe_load(yaml_config)
        except yaml.YAMLError as exp:
            print(exp)
    return conf_mysql


f_arg = {
    'databases': "SHOW DATABASES;",
    'tables': "SHOW TABLES;",
    'create': "CREATE DATABASE {bd};",
    'drop': "DROP DATABASE {bd};"
}

arg_print = {
    'databases': "Database list:",
    'tables': "Table list:",
    'create': "Database '{bd}' is created.",
    'drop': "Database '{bd}' is dropped."
}

if __name__ == '__main__':
    cf_mysql = read_yaml()

    try:
        msq = mysql.MySQLConnection(
            host=cf_mysql.get('settings').get('host'),
            user=cf_mysql.get('settings').get('user'),
            password=cf_mysql.get('settings').get('password'),
            database=cf_mysql.get('settings').get('database')
        )
        with msq as connect:
            cur = connect.cursor()
            cur.execute("SELECT VERSION()")
            ls = cur.fetchall()

            print(
                f"Connected to MySQL server (version {ls[0][0]}), database {cf_mysql.get('settings').get('database')}.")
            if len(sys.argv) == 2:  # выводим базы данных и таблицы
                if sys.argv[1] in f_arg and sys.argv[1] in arg_print:
                    if sys.argv[1] == 'tables' and cf_mysql.get('settings').get('database') is None:
                        print("Error: not connected to a database.")
                        cur.close()
                        print("MySQL connection is closed.")
                        exit()
                    # sql_query = f_arg[sys.argv[1]]
                    # cur.execute(sql_query)

                    if not cur:
                        print("No tables")
                    else:
                        print(arg_print[sys.argv[1]])
                        for key in cur:
                            print(f'        - {key[0]}')

            elif len(sys.argv) == 3:  # Создаем базы данных и убаляем
                if sys.argv[1] in f_arg:
                    sql_query = f_arg[sys.argv[1]].format(bd=sys.argv[2])

                    cur.execute(sql_query)
                    print(arg_print[sys.argv[1]].format(bd=sys.argv[2]))

            else:
                print(f'Error: command-line arguments are invalid.')
            cur.close()
        print("MySQL connection is closed.")
    except mysql.Error as exp:
        print(exp)
