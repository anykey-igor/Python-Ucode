import mysql.connector as mysql
import yaml
import json
import sys


def check_mysql_column(show_column, cur, news_list):
    # Запрос в мускуль для получения всех колонок
    cur.execute(show_column)
    # парсим только названия колонок и создаем список из названий колонок
    ls = cur.fetchall()
    i = 0
    sql_col = list()
    while i < len(ls):
        sql_col.append(ls[i][0])
        i += 1
    # сравниваем полученный список после прохода по JSON файлу и список с названиями колонок
    res = [x for x in sql_col + news_list if x not in sql_col] #or x not in news_list]
    #убираем дублирующиеся названия колонок которые нужно добавить, используем конвертацию в множество
    #возвращаем список названий колонок которые необходимо создать перед вставкой данных в мускуль
    res = set(res)
    return res


def read_yaml(*file_name):
    file_name = 'cfg.yaml'
    with open(file_name, 'r') as yaml_config:
        try:
            conf_mysql = yaml.safe_load(yaml_config)
        except yaml.YAMLError as exp:
            print(exp)
    return conf_mysql


def insert_db(*mydata):
    cur = mydata[0]
    table_sql_exec = mydata[1]
    data = mydata[2]
    db = mydata[3]
    columns = ", ".join(data.keys())
    value = tuple(data.values())
    val_s = ", ".join(['%s' for i in range(len(data.keys()))])

    my_sql = """INSERT {table} ({columns}) VALUES ({val_s});""".format(table=table_sql_exec, columns=columns, val_s=val_s)

    try:
        cur.execute(my_sql, value)
        print(f"Inserted {list(data.values())[0]} {list(data.values())[1]} into table {table_sql_exec} of {db}.")
    except Exception as exc:
        print(f"Failed to process event: {data}. Error: {exc}")


def update_db(*mydata):
    cur = mydata[0]
    table_sql_exec = mydata[1]
    data = mydata[2]
    db = mydata[3]
    columns = ", ".join(data.keys())
    value = tuple(data.values())
    val_s = ", ".join(['%s' for i in range(len(data.keys()))])

    my_sql = """INSERT {table} ({columns}) VALUES ({val_s});""".format(table=table_sql_exec, columns=columns,
                                                                       val_s=val_s)

    try:
        cur.execute(my_sql, value)
        print(f"Inserted {list(data.values())[0]} {list(data.values())[1]} into table {table_sql_exec} of {db}.")
    except Exception as exc:
        print(f"Failed to process event: {data}. Error: {exc}")


def delete_db(*mydata):
    cur = mydata[0]
    table_sql_exec = mydata[1]
    data = mydata[2]
    db = mydata[3]
    columns = ", ".join(data.keys())
    value = tuple(data.values())
    val_s = ", ".join(['%s' for i in range(len(data.keys()))])

    my_sql = """INSERT {table} ({columns}) VALUES ({val_s});""".format(table=table_sql_exec, columns=columns,
                                                                       val_s=val_s)

    try:
        cur.execute(my_sql, value)
        print(f"Inserted {list(data.values())[0]} {list(data.values())[1]} into table {table_sql_exec} of {db}.")
    except Exception as exc:
        print(f"Failed to process event: {data}. Error: {exc}")


def move_in_db(*mydata):
    cur = mydata[0]
    table_sql_exec = mydata[1]
    data = mydata[2]
    db = mydata[3]
    columns = ", ".join(data.keys())
    value = tuple(data.values())
    val_s = ", ".join(['%s' for i in range(len(data.keys()))])

    my_sql = """INSERT {table} ({columns}) VALUES ({val_s});""".format(table=table_sql_exec, columns=columns,
                                                                       val_s=val_s)

    try:
        cur.execute(my_sql, value)
        print(f"Inserted {list(data.values())[0]} {list(data.values())[1]} into table {table_sql_exec} of {db}.")
    except Exception as exc:
        print(f"Failed to process event: {data}. Error: {exc}")


def move_out_db(*mydata):
    cur = mydata[0]
    table_sql_exec = mydata[1]
    data = mydata[2]
    db = mydata[3]
    columns = ", ".join(data.keys())
    value = tuple(data.values())
    val_s = ", ".join(['%s' for i in range(len(data.keys()))])

    my_sql = """INSERT {table} ({columns}) VALUES ({val_s});""".format(table=table_sql_exec, columns=columns,
                                                                       val_s=val_s)

    try:
        cur.execute(my_sql, value)
        print(f"Inserted {list(data.values())[0]} {list(data.values())[1]} into table {table_sql_exec} of {db}.")
    except Exception as exc:
        print(f"Failed to process event: {data}. Error: {exc}")


def update_zoo(**args: dict):
    #
    # f_arg = {
    #     'databases': "SHOW DATABASES;",
    #     'tables': "SHOW TABLES;",
    #     'create': "CREATE DATABASE {bd};",
    #     'drop': "DROP DATABASE {bd};"
    #
    # }
    #
    # arg_print = {
    #     'databases': "Database list:",
    #     'tables': "Table list:",
    #     'create': "Database '{bd}' is created.",
    #     'drop': "Database '{bd}' is dropped."
    # }

    mysql_command = {
        'born': insert_db,
        'birthday': update_db,
        'died': delete_db,
        'moved in': move_in_db,
        'moved out': move_out_db
    }

    key = 'data'

    my_data = args[key]
    # имя базы данных полученное из json файла
    name_db = my_data["database"]
    table_sql_exec = my_data["table"]  # имя таблицы базы данных с которой будем работать
    json_list = len(my_data["news"])  # длина списка в json

    mysql_create_DB = "CREATE DATABASE IF NOT EXISTS {db_name}".format(db_name=name_db)

    mysql_use_DB = "USE {db_name}".format(db_name=name_db)

    mysql_create_table = "CREATE TABLE IF NOT EXISTS {tab}(" \
                         "species VARCHAR(100) NOT NULL, " \
                         "name VARCHAR(100) NOT NULL, " \
                         "age TINYINT DEFAULT 0 CHECK(age >= 0 AND age <= 100), " \
                         "PRIMARY KEY ( species, name));".format(tab=table_sql_exec)

    show_column = "SHOW COLUMNS from {tab}".format(tab=table_sql_exec)


    mysql_data_type = {
                "<class 'int'>": "TINYINT",
                "<class 'bool'>": "BOOL",
                "<class 'str'>": "VARCHAR(300)"
    }

    cf_mysql = read_yaml()

    try:
        msq = mysql.MySQLConnection(
            host=cf_mysql.get('settings').get('host'),
            user=cf_mysql.get('settings').get('user'),
            password=cf_mysql.get('settings').get('password'),
        )
        with msq as connect:
            cur = connect.cursor()
            cur.execute("SELECT VERSION()")
            ls = cur.fetchall()
            print(f"Connected to MySQL server (version {ls[0][0]}).")

            cur.execute(mysql_create_DB)
            cur.execute(mysql_use_DB)
            cur.execute(mysql_create_table)
            connect.commit()
            print(f"Using Using database '{args['data'].get('database')}'")

            news_list = list()
            j = 0
            while j != json_list:
                news = my_data["news"][j]
                for key in news:
                    if key == "event":
                        pass
                    else:
                        news_list.append(key)
                j += 1

            res = check_mysql_column(show_column, cur, news_list)
            for col in res:
                k = 0
                while k != json_list:
                    news = my_data["news"][k]
                    if news.get(col) != None:
                        if str(type(news.get(col))) in mysql_data_type:
                            insert_mysql_col = "ALTER TABLE {tab} ADD COLUMN {col} {type_col};".format(
                                tab=table_sql_exec, col=col, type_col=mysql_data_type[str(type(news.get(col)))])
                            cur.execute(insert_mysql_col)
                        break
                    k +=1

            j = 0
            while j != json_list:
                news = my_data["news"][j]
                if news["event"] in mysql_command:
                    data_for_sql = {key: news[key] for key in news if key != "event"}
                    mysql_command[news["event"]](cur, table_sql_exec, data_for_sql, name_db)
                    connect.commit()
                j += 1

            cur.close()
            print("MySQL connection is closed.")
    except mysql.Error as exp:
        print(exp)
