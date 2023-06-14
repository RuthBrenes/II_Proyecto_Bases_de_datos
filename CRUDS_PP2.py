#Conexion a BD SQL

import pyodbc
import pandas as pd
import mysql.connector

try:
    conexion = mysql.connector.connect(host = "sql5.freemysqlhosting.net", user = "sql5625051", password = "XRy6s2AUyj", database = "sql5625051", port = "3306")
    cursor = conexion.cursor()
    cursor.execute("SELECT @@version")
    row=cursor.fetchone()
    #print(row)

    print("Conexion exitosa\n")

except:

    print("Error al intentar conectarse")

#Crear
def create(tabla, lista):
    cursorInsert = conexion.cursor()

    if(tabla == "producto"):

        ID_producto = lista[0]
        nombre = lista[1]
        descripcion = lista[2] 
        precio = lista[3] 
        categoria = lista[4] 

        consulta = "Insert into producto(ID_producto, nombre, descripcion, precio, categoria) values (%s, %s, %s, %s, %s)"
        valores = (ID_producto, nombre, descripcion, precio, categoria)
        cursorInsert.execute(consulta, valores)

    elif(tabla == "inventario"):
        
        ID_inventario = lista[0]
        ID_producto = lista[1]
        ID_proveedor = lista[2]
        existencias_actuales = lista[3]
        ventas_realizadas = lista[4]

        consulta = "Insert into inventario(ID_inventario, ID_producto, ID_proveedor, existencias_actuales, ventas_realizadas) values (%s, %s, %s, %s, %s)"
        valores = (ID_inventario, ID_producto, ID_proveedor, existencias_actuales, ventas_realizadas)
        cursorInsert.execute(consulta, valores)
    
    elif(tabla == "cliente"):

        cedula = lista[0]
        primer_nombre = lista[1]
        segundo_nombre = lista[2]
        primer_apellido = lista[3]
        segundo_apellido = lista[4]
        provincia = lista[5] 
        canton = lista[6] 
        distrito = lista[7]
        preferencias = lista[8]

        consulta = "Insert into cliente(cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, provincia, canton, distrito, preferencias) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, provincia, canton, distrito, preferencias)
        cursorInsert.execute(consulta, valores)

    elif(tabla == "telefono_cliente"):
        
        ID_telefono = lista[0]
        ID_cliente = lista[1]
        numeroTelefono = lista[2]

        consulta = "Insert into telefono_cliente(ID_telefono, ID_cliente, numeroTelefono) values (%s, %s, %s)"
        valores = (ID_telefono, ID_cliente, numeroTelefono)
        cursorInsert.execute(consulta, valores)

    elif(tabla == "correo_cliente"):

        ID_correo = lista[0]
        ID_cliente = lista[1]
        correo = lista[2]

        consulta = "Insert into correo_cliente(ID_correo, ID_cliente, correo) values (%s, %s, %s)"
        valores = (ID_correo, ID_cliente, correo)
        cursorInsert.execute(consulta, valores)

    elif(tabla == "compra_cliente"):
        
        ID_venta = lista[0]
        ID_cliente = lista[1]

        consulta = "Insert into compra_cliente(ID_venta, ID_cliente) values (%s, %s)"
        valores = (ID_venta, ID_cliente)
        cursorInsert.execute(consulta, valores)
    
    elif(tabla == "venta"):

        ID_venta = lista[0]
        fecha_hora = lista[1]
        metodo_pago = lista[2]
        ID_producto = lista[3]
        ID_empleado = lista[4]

        consulta = "Insert into venta(ID_venta, fecha_hora, metodo_pago, ID_producto, ID_empleado) values (%s, %s, %s, %s, %s)"
        valores = (ID_venta, fecha_hora, metodo_pago, ID_producto, ID_empleado)
        cursorInsert.execute(consulta, valores)

    elif(tabla == "empleado"):

        cedula = lista[0]
        primer_nombre = lista[1]
        segundo_nombre = lista[2]
        primer_apellido = lista[3]
        segundo_apellido = lista[4]
        rol = lista[5]
        dias_laborales = lista[6]
        hora_entrada = lista[7]
        hora_salida = lista[8]
        salario = lista[9]
        telefono = lista[10]
        area_trabajo = lista[11]

        consulta = "Insert into empleado(cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, rol, dias_laborales, hora_entrada, hora_salida, salario, telefono, area_trabajo) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, rol, dias_laborales, hora_entrada, hora_salida, salario, telefono, area_trabajo)
        cursorInsert.execute(consulta, valores)
    
    elif(tabla == "proveedor"):

        ID_proveedor = lista[0]
        telefono = lista[1]
        fecha_entrega = lista[2]

        consulta = "Insert into proveedor(ID_proveedor, telefono, fecha_entrega) values (%s, %s, %s)"
        valores = (ID_proveedor, telefono, fecha_entrega)
        cursorInsert.execute(consulta, valores)

    elif(tabla == "producto_proveedor"):

        ID_proveedor = lista[0]
        ID_producto = lista[1]
    
        consulta = "Insert into producto_proveedor(ID_proveedor, ID_producto) values (%s, %s)"
        valores = (ID_proveedor, ID_producto)
        cursorInsert.execute(consulta, valores)

    elif(tabla == "promocion_evento"):

        ID_promocion = lista[0]
        ID_producto = lista[1]
        fecha = lista[2]
        descuento= lista[3]
        
        consulta = "Insert into promocion_evento(ID_promocion, ID_producto, fecha, descuento) values (%s, %s, %s, %s)"
        valores = (ID_promocion, ID_producto, fecha, descuento)
        cursorInsert.execute(consulta, valores)

    conexion.commit()
    conexion.close()

    print("\nLa informacion se ha insertado exitosamente")


#Consulta a la base de datos

def read(tabla):
    cursor = conexion.cursor()

    if(tabla == "producto"):
        cursor.execute("Select * from producto;")
        producto = cursor.fetchall()

        for producto in producto:
            print(producto)
    
    elif(tabla == "inventario"):
        cursor.execute("Select * from inventario;")
        inventario = cursor.fetchall()

        for inventario in inventario:
            print(inventario)   

    elif(tabla == "cliente"):
        cedula = 123
        cursor.execute("Select * from cliente;")
        cliente = cursor.fetchall()

        for cliente in cliente:
            print(cliente)

    elif(tabla == "telefono_cliente"):
        cursor.execute("Select * from telefono_cliente;")
        telefono_cliente = cursor.fetchall()

        for telefono_cliente in telefono_cliente:
            print(telefono_cliente)

    elif(tabla == "correo_cliente"):
        cursor.execute("Select * from correo_cliente;")
        correo_cliente = cursor.fetchall()

        for correo_cliente in correo_cliente:
            print(correo_cliente)

    elif(tabla == "compra_cliente"):
        cursor.execute("Select * from compra_cliente;")
        compra_cliente = cursor.fetchall()

        for compra_cliente in compra_cliente:
            print(compra_cliente) 

    elif(tabla == "venta"):
        cursor.execute("Select * from venta;")
        venta = cursor.fetchall()

        for venta in venta:
            print(venta)  

    elif(tabla == "empleado"):
        cursor.execute("Select * from empleado")
        empleado = cursor.fetchall()

        for empleado in empleado:
            print(empleado)  

    elif(tabla == "proveedor"):
        cursor.execute("Select * from proveedor;")
        proveedor = cursor.fetchall()

        for proveedor in proveedor:
            print(proveedor) 

    elif(tabla == "producto_proveedor"):
        cursor.execute("Select * from producto_proveedor;")
        producto_proveedor = cursor.fetchall()

        for producto_proveedor in producto_proveedor:
            print(producto_proveedor)    

    elif(tabla == "promocion_evento"):
        cursor.execute("Select * from promocion_evento;")
        promocion_evento = cursor.fetchall()

        for promocion_evento in promocion_evento:
            print(promocion_evento)    

    elif(tabla == "promocion_cliente"):
        cursor.execute("Select * from promocion_cliente;")
        promocion_cliente = cursor.fetchall()

        for promocion_cliente in promocion_cliente:
            print(promocion_cliente)   

    cursor.close()
    conexion.close()

#Actualizar informacion

def updateProducto(atributo, PK, nuevaInfo):

    cursorUpdate = conexion.cursor()

    if(atributo == "nombre"):

        consulta = "Update producto set nombre = %s where ID_producto = %s" 
    
    elif(atributo == "descripcion"):

        consulta = "Update producto set descripcion = %s where ID_producto = %s"

    elif(atributo == "precio"):

        consulta = "Update producto set precio = %s where ID_producto = %s"

    elif(atributo == "categoria"):

        consulta = "Update producto set categoria = %s where ID_producto = %s"

    cursorUpdate.execute(consulta, nuevaInfo, PK)

    cursorUpdate.commit()
    cursorUpdate.close()

    print("Actualizacion exitosa")

def updateInventario(atributo, PK, nuevaInfo):

    cursorUpdate = conexion.cursor()

    if(atributo == "ID_producto"):

        consulta = "Update inventario set ID_producto = %s where ID_inventario = %s" 

    elif(atributo == "ID_proveedor"):

        consulta = "Update inventario set ID_proveedor = %s where ID_inventario = %s" 

    elif(atributo == "existencias_actuales"):

        consulta = "Update inventario set existencias_actuales = %s where ID_inventario = %s" 
    
    elif(atributo == "ventas_realizadas"):

        consulta = "Update inventario set ventas_realizadas = %s where ID_inventario = %s"

    cursorUpdate.execute(consulta, nuevaInfo, PK)

    cursorUpdate.commit()
    cursorUpdate.close()

    print("Actualizacion exitosa")

def updateCliente(atributo, PK, nuevaInfo):

    cursorUpdate = conexion.cursor()

    if(atributo == "primer_nombre"):

        consulta = "Update cliente set primer_nombre = %s where cedula = %s" 
    
    elif(atributo == "segundo_nombre"):

        consulta = "Update cliente set segundo_nombre = %s where cedula = %s"

    elif(atributo == "primer_apellido"):

        consulta = "Update cliente set primer_apellido = %s where cedula = %s"

    elif(atributo == "segundo_apellido"):

        consulta = "Update cliente set segundo_apellido = %s where cedula = %s"

    elif(atributo == "provincia"):

        consulta = "Update cliente set provincia = %s where cedula = %s"

    elif(atributo == "canton"):

        consulta = "Update cliente set canton = %s where cedula = %s"

    elif(atributo == "distrito"):

        consulta = "Update cliente set distrito = %s where cedula = %s"

    elif(atributo == "preferencias"):

        consulta = "Update cliente set preferencias = %s where cedula = %s"

    cursorUpdate.execute(consulta, nuevaInfo, PK)

    cursorUpdate.commit()
    cursorUpdate.close()

    print("Actualizacion exitosa")

def updateTelefonoC(atributo, PK, nuevaInfo):

    cursorUpdate = conexion.cursor()

    if(atributo == "ID_cliente"):

        consulta = "Update venta set ID_cliente = %s where ID_telefono = %s" 
    
    elif(atributo == "numero_telefono"):

        consulta = "Update venta set numero_telefono = %s where ID_telefono = %s"

    cursorUpdate.execute(consulta, nuevaInfo, PK)

    cursorUpdate.commit()
    cursorUpdate.close()

    print("Actualizacion exitosa")

def updateCorreoC(atributo, PK, nuevaInfo):

    cursorUpdate = conexion.cursor()

    if(atributo == "ID_cliente"):

        consulta = "Update venta set ID_cliente = %s where ID_correo = %s" 
    
    elif(atributo == "correo"):

        consulta = "Update venta set correo = %s where ID_correo = %s"

    cursorUpdate.execute(consulta, nuevaInfo, PK)

    cursorUpdate.commit()
    cursorUpdate.close()

    print("Actualizacion exitosa")

def updateVenta(atributo, PK, nuevaInfo):

    cursorUpdate = conexion.cursor()

    if(atributo == "fecha_hora"):

        consulta = "Update venta set fecha_hora = %s where ID_venta = %s" 

    elif(atributo == "metodo_pago"):

        consulta = "Update venta set metodo_pago = %s where ID_venta = %s"

    elif(atributo == "ID_producto"):

        consulta = "Update venta set ID_producto = %s where ID_venta = %s"
    
    elif(atributo == "ID_empleado"):

        consulta = "Update venta set ID_empleado = %s where ID_venta = %s"

    cursorUpdate.execute(consulta, nuevaInfo, PK)

    cursorUpdate.commit()
    cursorUpdate.close()

    print("Actualizacion exitosa")

def updateEmpleado(atributo, PK, nuevaInfo):

    cursorUpdate = conexion.cursor()

    if(atributo == "primer_nombre"):

        consulta = "Update empleado set primer_nombre = %s where cedula = %s" 

    elif(atributo == "segundo_nombre"):

        consulta = "Update empleado set segundo_nombre = %s where cedula = %s" 

    elif(atributo == "primer_apellido"):

        consulta = "Update empleado set primer_apellido = %s where cedula= %s" 

    elif(atributo == "segundo_apellido"):

        consulta = "Update empleado set segundo_apellido = %s where cedula = %s" 

    elif(atributo == "rol"):

        consulta = "Update empleado set rol = %s where cedula = %s" 

    elif(atributo == "dias_laborales"):

        consulta = "Update empleado set dias_laborales = %s where cedula = %s" 

    elif(atributo == "hora_entrada"):

        consulta = "Update "".empleado set hora_entrada = %s where cedula = %s" 

    elif(atributo == "hora_salida"):

        consulta = "Update "".empleado set hora_salida = %s where cedula = %s" 

    elif(atributo == "salario"):

        consulta = "Update .empleado set salario = %s where cedula = %s" 

    elif(atributo == "telefono"):

        consulta = "Update .empleado set telefono = %s where cedula = %s" 

    elif(atributo == "area_trabajo"):

        consulta = "Update empleado set area_trabajo = %s where cedula = %s" 
    
    cursorUpdate.execute(consulta, nuevaInfo, PK)

    cursorUpdate.commit()
    cursorUpdate.close()

    print("Actualizacion exitosa")

def updateProveedor(atributo, PK, nuevaInfo):

    cursorUpdate = conexion.cursor()

    if(atributo == "telefono"):

        consulta = "Update proveedor set telefono = %s where ID_proveedor = %s"

    elif(atributo == "correo"):

        consulta = "Update proveedor set correo = %s where ID_proveedor  = %s"

    elif(atributo == "fecha_entrega"):

        consulta = "Update proveedor set fecha_entrega = %s where ID_proveedor  = %s"

    cursorUpdate.execute(consulta, nuevaInfo, PK)

    cursorUpdate.commit()
    cursorUpdate.close()

    print("Actualizacion exitosa")

def updatePromocionEvento(atributo, PK, nuevaInfo):

    cursorUpdate = conexion.cursor()

    if(atributo == "ID_producto"):

        consulta = "Update promocion_evento set ID_producto = %s where ID_promocion = %s" 

    elif(atributo == "fecha"):

        consulta = "Update promocion_evento set fecha = %s where ID_promocion = %s" 
        
    elif(atributo == "descuento"):

        consulta = "Update promocion_evento set descuento = %s where ID_promocion = %s" 

    cursorUpdate.execute(consulta, nuevaInfo, PK)

    cursorUpdate.commit()
    cursorUpdate.close()

    print("Actualizacion exitosa")

#Eliminar datos

def delete(tabla, PK):
    
    cursorEliminar = conexion.cursor()

    if(tabla == "producto"):
        consulta = "delete from producto where ID_producto = %s"

    elif(tabla == "inventario"):
        consulta = "delete from inventario where ID_producto = %s"

    elif(tabla == "cliente"):
        consulta = "delete from cliente where cedula= %s"

    elif(tabla == "venta"):
        consulta = "delete from venta where ID_venta = %s"

    elif(tabla == "empleado"):
        consulta = "delete from empleado where cedula = %s"

    elif(tabla == "proveedor"):
        consulta = "delete from proveedor where ID_proveedor = %s"

    cursorEliminar.execute(consulta, PK)

    cursorEliminar.commit()
    cursorEliminar.close()
