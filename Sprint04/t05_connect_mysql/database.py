import mysql.connector
import yaml

if __name__ == "__main__":
    with open("cfg.yaml", 'r') as yaml_config:
        try:
            cf_mysql = yaml.safe_load(yaml_config)
        except yaml.YAMLError as exp:
            print(exp)
    try:
        msq = mysql.connector.MySQLConnection(
            host=cf_mysql.get('settings').get('host'),
            user=cf_mysql.get('settings').get('user'),
            password=cf_mysql.get('settings').get('password'))
        #print(msq)
        with msq as connect:
            cur = connect.cursor()
            cur.execute("SELECT VERSION()")
            ls = cur.fetchall()
            print(f"Connected to MySQL server (version {ls[0][0]}).")
        print("MySQL connection is closed.")
    except mysql.connector.Error as exp:
        print(exp)
