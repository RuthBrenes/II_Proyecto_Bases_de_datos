import pyodbc
import tkinter as tk
from tkinter import *
from tkinter import ttk
import webbrowser
from flask import Flask, redirect, render_template, request, url_for
from string import Template
import mysql.connector
import json

#CRL + SHIFT + P

#Conexion a BD SQL
try:
    conexion = mysql.connector.connect(host = "sql5.freemysqlhosting.net", user = "sql5625051", password = "XRy6s2AUyj", database = "sql5625051", port = "3306")
    cursor = conexion.cursor()

    print("Conexion exitosa\n")

except:

    print("Error al intentar conectarse")

def abrirPaginaConsultas():
    webbrowser.open('http://localhost:5000')

app = Flask(__name__)

@app.route('/')
def mostrar_info_productos():
    cursor.execute("SELECT nombre, descripcion, precio, categoria FROM producto;")
    productos = cursor.fetchall()
    conexion.commit()
    print(productos)

    return render_template("index.html", productos = productos)

@app.route('/inventario')
def mostrar_info_inventarios():
    cursor.execute("SELECT producto.nombre, inventario.existencias_actuales, inventario.ventas_realizadas \
    FROM inventario INNER JOIN producto ON inventario.ID_producto = producto.ID_producto;")
    inventarios = cursor.fetchall()

    conexion.commit()
    print(inventarios)

    return render_template("inventario.html", inventarios = inventarios)

@app.route('/clientes')
def mostrar_info_clientes():
    cursor.execute("SELECT CONCAT(primer_nombre, ' ', primer_apellido), provincia, preferencias FROM cliente;")
    clientes = cursor.fetchall()
    conexion.commit()
    print(clientes)

    return render_template("clientes.html", clientes = clientes)

@app.route('/empleados')
def mostrar_historial_empleado():
    return render_template("empleados.html")

@app.route('/tabla_empleados', methods=['GET'])
def mostrar_tabla_empleados():
    cedula = request.args.get('cedula')
    data = obtener_historial_empleado(cedula)
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    print(response)
    return response
    
def obtener_historial_empleado(cedula):
    cedula = request.args.get('cedula')
    cursor.execute("SELECT CONCAT(empleado.primer_nombre, ' ', empleado.primer_apellido), CONCAT(cliente.primer_nombre, ' ' , cliente.primer_apellido) AS Nombre_cliente, producto.nombre, venta.metodo_pago \
    FROM empleado INNER JOIN venta ON empleado.cedula = venta.ID_empleado \
    INNER JOIN compra_cliente ON compra_cliente.ID_venta = venta.ID_venta \
    INNER JOIN cliente ON cliente.cedula = compra_cliente.ID_cliente \
    INNER JOIN producto ON venta.ID_producto = producto.ID_producto WHERE empleado.cedula = '"+str(cedula)+"' \
    GROUP BY empleado.primer_nombre, empleado.primer_apellido, cliente.primer_nombre, cliente.primer_apellido, producto.nombre, venta.metodo_pago;")
    empleados = cursor.fetchall()

    print("Los empleados son: ", empleados)

    conexion.commit()
    return empleados

#Historial de clientes

@app.route('/historial_clientes')
def mostrar_historial_cliente():
    return render_template("historial_clientes.html")

@app.route('/tabla_historial', methods=['GET'])
def mostrar_tabla_historial():
    cedula = request.args.get('cedula')
    data = obtener_historial_cliente(cedula)
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    print(response)
    return response

def obtener_historial_cliente(cedula):
    cursor.execute("SELECT CONCAT(cliente.primer_nombre, ' ' , cliente.primer_apellido) AS cliente, MIN(telefono_cliente.numero_telefono) AS telefono, correo_cliente.correo, venta.metodo_pago, producto.nombre, producto.precio \
    FROM producto INNER JOIN venta ON producto.ID_producto = venta.ID_producto \
    INNER JOIN compra_cliente ON compra_cliente.ID_venta = venta.ID_venta \
    INNER JOIN cliente ON compra_cliente.ID_cliente = cliente.cedula \
    INNER JOIN empleado ON venta.ID_empleado = empleado.cedula \
    INNER JOIN telefono_cliente ON telefono_cliente.ID_cliente = cliente.cedula \
    INNER JOIN correo_cliente ON correo_cliente.ID_cliente = cliente.cedula WHERE cliente.cedula = '"+str(cedula)+"' \
    GROUP BY cliente.primer_nombre, cliente.primer_apellido, correo_cliente.correo, venta.fecha_hora, venta.metodo_pago, producto.nombre, producto.precio;")
    clientes = cursor.fetchall()
        
    print("Los clientes son: ", clientes)

    conexion.commit()
    return clientes

@app.route('/call_python_function')

def call_python_function():
    param = request.args.get('param')
    return "Python function called! " + param




