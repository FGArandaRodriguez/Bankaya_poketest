from flask import Flask, request, jsonify
import requests
import json
import sqlite3
from datetime import datetime
from Connection_db import sql_connection,sql_table

#Creamos las tablas de bases de datos
conexion = sql_connection
create_tables = sql_table()

class Exceptions(Exception):
    def __init__(self,message):
        super().__init__(message)

def insert_in_table(id,ip_origin,request_date, method,api_name):
    try:
        sqliteConnection = sqlite3.connect('log_pokemon.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO log_requests
                          (ip_origin, request_date, method, api_name) 
                          VALUES ( ?, ?, ?, ?);"""

        data_tuple = (ip_origin,request_date, method,api_name)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


def obtener_datos(url_api, nombre_pokemon):
    url_pokemon = url_api + nombre_pokemon
    try:
        result = requests.get(url_pokemon)
        if result.status_code != 200:
            message = str("Sorry Pokemon " + nombre_pokemon +' ' + result.text)
            raise Exceptions(message)
    except Exceptions:
        message = str("Sorry Pokemon " + nombre_pokemon +' ' + "Not found")
        return jsonify({"error": 404, "menssage": message,}),404

    result_json=json.loads(result.text)

    return result_json

#Este método 
def obtener_locacion_area(url_api):

    try:
        result = requests.get(url_api)
        if result.status_code != 200:
            message = str("Sorry"+' ' + result.text)
            raise Exceptions(message)
    except Exceptions:
        message = str("Sorry" +' ' + "Not found")
        return jsonify({"error": 404, "menssage": message,}),404

    result_json=json.loads(result.text)

    return result_json


app=Flask(__name__)

#Este servicio da la bienvenida a la API
@app.route('/', methods=['GET'])
def welcome():
    
    ip_origin = request.environ['REMOTE_ADDR']
    request_date = datetime.now()
    method = request.environ['REQUEST_METHOD']
    api = request.environ['PATH_INFO']

    insert_in_table(1,ip_origin,request_date,method, api)
    return 'Bienvenidos a la Pokedex By Bankaya!'

#Este servicio consulta los datos en la base de datos
@app.route('/api/bankaya/database/show-data', methods=['GET'])
def show_datas():
    ip_origin = request.environ['REMOTE_ADDR']
    request_date = datetime.now()
    method = request.environ['REQUEST_METHOD']
    api = request.environ['PATH_INFO']

    insert_in_table(1,ip_origin,request_date,method,api)

    con = sqlite3.connect('log_pokemon.db')
    sql_table()
    cur = con.cursor()

    datas = []
    for row in cur.execute('select * from log_requests;'):
            #datas.append(row)
            datas.append({
                'ip_origin':row[1],
                'request_date': row[2],
                'method': row[3],
                'origin_request': row[4]
                })
    con.close()
    
    response = {'log_data':datas}

    return response


#Este servicio obtiene los datos que se requieren en el challenge
@app.route('/api/bankaya/pokemon/<string:name>', methods=['GET'])
def obtener_datos_test_pokemon(name):
    datos_pokemon = obtener_datos_pokemon(name)

    if 404 in datos_pokemon:
        return datos_pokemon
     
    abilities = []
    for ability in datos_pokemon['abilities']:
        abilities.append(ability['ability']['name'])
    
    held_items = []
    for item in datos_pokemon['held_items']:
        held_items.append(
            {
                "name": item['item']['name'],
                "version_details": item['version_details']

            })
    resp_locacion = obtener_locacion_area(datos_pokemon['location_area_encounters'])

    locaciones = []
    for locacion in resp_locacion:
        locaciones.append(locacion['location_area'].pop("name"))
    
    response = {
        "pokemon_name": datos_pokemon['forms'][0]['name'],
        "abilities": abilities,
        "base_experience": datos_pokemon['base_experience'],
        "held_items": held_items,
        "id": datos_pokemon['id'],
        "location_area_encounters" : locaciones
    }
    ip_origin = request.environ['REMOTE_ADDR']
    request_date = datetime.now()
    method = request.environ['REQUEST_METHOD']
    api = request.environ['PATH_INFO']

    insert_in_table(1,ip_origin,request_date,method,api)

    return response

#Este servicio obtiene todos los datos del pokemon
#@app.route('/api/bankaya/pokemon/datos/<string:name>', methods=['GET'])
def obtener_datos_pokemon(name):
    url_api = 'https://pokeapi.co/api/v2/pokemon/'
    datos_pokemon = obtener_datos(url_api, name)
    if 404 in datos_pokemon:
        return datos_pokemon
    response = datos_pokemon

    return response

#Este servicio obtiene las habilidades del pokemon
@app.route('/api/bankaya/pokemon/<string:name>/abilities', methods=['GET'])
def obtener_habilidades(name):    
    datos_pokemon = obtener_datos_pokemon(name)

    if 404 in datos_pokemon:
        return datos_pokemon
     
    abilities = []
    for ability in datos_pokemon['abilities']:
        abilities.append(ability['ability']['name'])
    
    response = {
        "pokemon": datos_pokemon['forms'][0]['name'],
        "abilities": abilities
    }

    ip_origin = request.environ['REMOTE_ADDR']
    request_date = datetime.now()
    method = request.environ['REQUEST_METHOD']
    api = request.environ['PATH_INFO']

    insert_in_table(1,ip_origin,request_date,method,api)

    return response

#Este servicio obtiene el nivel de experiencia del pokemon
@app.route('/api/bankaya/pokemon/<string:name>/experience', methods=['GET'])
def obtener_experiencia(name):    
    datos_pokemon = obtener_datos_pokemon(name)

    if 404 in datos_pokemon:
        return datos_pokemon

    response = {
        "pokemon": datos_pokemon['forms'][0]['name'],
        "base_experience": datos_pokemon['base_experience']
    }

    ip_origin = request.environ['REMOTE_ADDR']
    request_date = datetime.now()
    method = request.environ['REQUEST_METHOD']
    api = request.environ['PATH_INFO']

    insert_in_table(1,ip_origin,request_date,method,api)

    return response

#Este servicio obtiene los held items del pokemon
@app.route('/api/bankaya/pokemon/<string:name>/held-items', methods=['GET'])
def obtener_held_items(name):    
    datos_pokemon = obtener_datos_pokemon(name)

    if 404 in datos_pokemon:
        return datos_pokemon
    
    held_items = []
    for item in datos_pokemon['held_items']:
        held_items.append(
            {
                "name": item['item']['name'],
                "version_details": item['version_details']

            })

    response = {
        "pokemon": datos_pokemon['forms'][0]['name'],
        "held_items": held_items
    }

    ip_origin = request.environ['REMOTE_ADDR']
    request_date = datetime.now()
    method = request.environ['REQUEST_METHOD']
    api = request.environ['PATH_INFO']

    insert_in_table(1,ip_origin,request_date,method,api)

    return response

#Este servicio obtiene el id del pokemon
@app.route('/api/bankaya/pokemon/<string:name>/id', methods=['GET'])
def obtener_id(name):    
    datos_pokemon = obtener_datos_pokemon(name)

    if 404 in datos_pokemon:
        return datos_pokemon

    response = {
        "id": datos_pokemon['id'],
        "pokemon": datos_pokemon['forms'][0]['name']
    }

    ip_origin = request.environ['REMOTE_ADDR']
    request_date = datetime.now()
    method = request.environ['REQUEST_METHOD']
    api = request.environ['PATH_INFO']

    insert_in_table(1,ip_origin,request_date,method,api)

    return response

#Este servicio obtiene el nombre del pokemon
@app.route('/api/bankaya/pokemon/<string:name>/name', methods=['GET'])
def obtener_nombre(name):    
    datos_pokemon = obtener_datos_pokemon(name)

    if 404 in datos_pokemon:
        return datos_pokemon

    response = {
        "pokemon_name": datos_pokemon['forms'][0]['name']
    }

    ip_origin = request.environ['REMOTE_ADDR']
    request_date = datetime.now()
    method = request.environ['REQUEST_METHOD']
    api = request.environ['PATH_INFO']

    insert_in_table(1,ip_origin,request_date,method,api)

    return response

#Este servicio obtiene las locaciones de los pokemon
@app.route('/api/bankaya/pokemon/<string:name>/location-area', methods=['GET'])
def obtener_datos_locacion(name):
    datos_pokemon = obtener_datos_pokemon(name)

    if 404 in datos_pokemon:
        return datos_pokemon
    
    resp_locacion = obtener_locacion_area(datos_pokemon['location_area_encounters'])

    locaciones = []
    for locacion in resp_locacion:
        locaciones.append(locacion['location_area'].pop("name"))


    response = {
        "pokemon": datos_pokemon['forms'][0]['name'],
        "location_area_encounters" : locaciones
    }

    ip_origin = request.environ['REMOTE_ADDR']
    request_date = datetime.now()
    method = request.environ['REQUEST_METHOD']
    api = request.environ['PATH_INFO']

    insert_in_table(1,ip_origin,request_date,method,api)

    return response

################Función de POW ##############################
def function_potencia(base,exponente):
    if (exponente > 0):
        return function_producto(base,function_potencia(base, exponente - 1))
    else:
        return 1

def function_producto(a,b):
    if (b>0):
        return (a + function_producto(a,b -1))
    else:
         return 0

#Este servicio calcula la función de POW()
@app.route('/POW/<int:base>/<int:exponente>', methods=['GET'])
def POW(base,exponente):

    print(function_potencia(base,exponente))
    response = {'resultado': function_potencia(base,exponente)}
    ip_origin = request.environ['REMOTE_ADDR']
    request_date = datetime.now()
    method = request.environ['REQUEST_METHOD']
    api = request.environ['PATH_INFO']

    insert_in_table(1,ip_origin,request_date,method, api)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='9000',debug=True)
