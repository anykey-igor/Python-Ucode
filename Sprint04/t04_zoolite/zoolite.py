import sqlite3
import json
import re

def insert_db(*mydata):
    cur = mydata[0]
    species = mydata[1]
    name = mydata[2]
    event = mydata[3]
    table_sql_exec = mydata[4]
    file_db = mydata[5]
    my_sql = """INSERT INTO {table} (species, name) VALUES(?,?)""".format(table=table_sql_exec)
    try:
        cur.execute(my_sql, (species, name))
        print(f"Inserted {species} {name} into table {table_sql_exec} of {file_db}.")
    except Exception as exc:
        print(f"Failed to process event: {event}. Error: {exc}")


def update_db(*mydata):
    cur = mydata[0]
    species = mydata[1]
    name = mydata[2]
    event = mydata[3]
    table_sql_exec = mydata[4]
    file_db = mydata[5]
    my_sql = """UPDATE {table} SET age=age+1 WHERE species=? AND name=?""".format(table=table_sql_exec)
    try:
        cur.execute(my_sql, (species, name))
        print(f"Updated {species} {name} in table {table_sql_exec} of {file_db}.")
    except Exception as exc:
        print(f"Failed to process event: {event}. Error: {exc} del")


def delete_db(*mydata):
    cur = mydata[0]
    species = mydata[1]
    name = mydata[2]
    event = mydata[3]
    table_sql_exec = mydata[4]
    file_db = mydata[5]
    my_sql = """DELETE FROM {table} WHERE species=? AND name=?""".format(table=table_sql_exec)
    try:
        cur.execute(my_sql, (species, name))
        print(f"Deleted {species} {name} from table {table_sql_exec} of {file_db}.")
    except Exception as exc:
        print(f"Failed to process event: {event}. Error: {exc}")


def update_zoo(**args: dict):
    sql_command = {
        'born': insert_db,
        'birthday': update_db,
        'died': delete_db
    }
    reg_p = r'\b\w+(?=\.)'
    key = 'data'
    my_data = args[key]
    json_data = json.dumps(my_data)  # упаковываем
    parsed_json = json.loads(json_data)  # распаковываем
    file_db = parsed_json["database"]  # имя базы данных полученное из json файла
    table_sql_exec = parsed_json["table"]  # имя таблицы базы данных с которой будем работать
    json_list = len(parsed_json["news"])  # длина списка в json

    sql_create_table = "CREATE TABLE IF NOT EXISTS {table} (" \
                       "species TEXT NOT NULL, " \
                       "name TEXT NOT NULL, " \
                       "age int DEFAULT 0, " \
                       "PRIMARY key(species, name));".format(table=table_sql_exec)
    try:
        sqlite_connection = sqlite3.connect(file_db)
        cur = sqlite_connection.cursor()
        cur.execute(sql_create_table)
        cur.execute("SELECT COUNT (*) FROM {table}".format(table=table_sql_exec))
        print(f"*** BEFORE: {cur.fetchone()[0]} animals in the zoo.")#'")#{re.findall(reg_p, file_db)[0]}.")
        j = 0
        while j != json_list:
            event = parsed_json["news"][j]["event"]
            species = parsed_json["news"][j]["species"]
            name = parsed_json["news"][j]["name"]
            if event in sql_command:
                sql_command[event](cur, species, name, parsed_json["news"][j], table_sql_exec, file_db)
                sqlite_connection.commit()
            j += 1
        cur.execute("SELECT COUNT (*) FROM {table}".format(table=table_sql_exec))
        print(f'*** AFTER: {cur.fetchone()[0]} animals in the zoo.')#{re.findall(reg_p, file_db)[0]}.')
        cur.close()
    except Exception as exc:
        print(exc)
