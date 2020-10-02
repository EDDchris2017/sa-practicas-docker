
from flask import Flask
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def conexionBD():
    connection = mysql.connector.connect(host='mysql',database='TIENDA',user='sapractica',password='sapractica')
    sql_select_Query = "select * from VIDEOJUEGOS"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    connection.close()
    return records

def generarTabla(records):
    cad = "<table>"
    cad += "<tr>"
    cad +="<th>ID</th>"
    cad +="<th>Nombre</th>"
    cad +="<th>Genero</th>"
    cad +="<th>Plataforma</th>"
    cad += "</tr>"
    for row in records:
        cad += "<tr>"
        cad += "<td>" + str(row[0]) + "</td>"
        cad += "<td>" + str(row[1]) + "</td>"
        cad += "<td>" + str(row[2]) + "</td>"
        cad += "<td>" + str(row[3]) + "</td>"
        cad += "</tr>"
    cad += "</table>"
    return cad

@app.route('/')
def servicio():
    res = conexionBD()
    tabla = generarTabla(res)
    return tabla