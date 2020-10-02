
from flask import Flask
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def conexionBD():
    connection = mysql.connector.connect(host='mysql',
                                        database='TIENDA',
                                        user='sapractica',
                                        password='sapractica')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Conectando a la BD ... ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select * from VIDEOJUEGOS")
        record = cursor.fetchone()
        print("Lista de videjuegos: ", record)
    cursor.close()
    connection.close()
    print("MySQL connection is closed")

@app.route('/')
def servicio():
    conexionBD()
    return 'Servidor Flask Practica 8 Activo **201504100**'