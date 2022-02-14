import sqlite3
from sqlite3 import Error

############################Conexion a base de datos####################################################################

def sql_connection():

    try:

        con = sqlite3.connect('log_pokemon.db')

        return con

    except Error:

        print(Error)

def sql_table():
    con = sqlite3.connect('log_pokemon.db')
    cursorObj = con.cursor()

    cursorObj.execute("CREATE TABLE IF NOT EXISTS log_requests(log_id integer PRIMARY KEY AUTOINCREMENT, ip_origin text, request_date numeric,  method text, api_name text)")

    con.commit()

con = sql_connection()

sql_table()