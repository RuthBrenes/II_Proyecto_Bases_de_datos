CREATE DATABASE PP2
USE PP2

CREATE SCHEMA tienda;

CREATE TABLE tienda.producto(
	ID_producto int NOT NULL,
	nombre varchar(50) NOT NULL,
	descripcion varchar(100) NOT NULL,
	precio float NOT NULL,
	categoria varchar(30) NOT NULL
	);

ALTER TABLE tienda.producto ADD CONSTRAINT id_producto_PK PRIMARY KEY (ID_producto);

INSERT INTO tienda.producto (ID_producto, nombre, descripcion, precio, categoria)
VALUES (22, 'Camiseta', 'Camiseta Hogwarts Houses', 9735, 'Ropa')

CREATE TABLE tienda.inventario(
	ID_inventario int NOT NULL,
	ID_producto int NOT NULL,
	ID_proveedor int NOT NULL,
	existencias_actuales int NOT NULL,
	ventas_realizadas int NOT NULL,
	);

ALTER TABLE tienda.inventario ADD CONSTRAINT id_inventario_PK PRIMARY KEY (ID_inventario);
ALTER TABLE tienda.inventario ADD CONSTRAINT id_producto_inventario_FK FOREIGN KEY (ID_producto) REFERENCES tienda.producto(ID_producto);
ALTER TABLE tienda.inventario ADD CONSTRAINT id_proveedor_inventario_FK FOREIGN KEY (ID_proveedor) REFERENCES tienda.proveedor(ID_proveedor);

CREATE TABLE tienda.cliente(
	cedula int NOT NULL,
	primer_nombre varchar(30) NOT NULL,
	segundo_nombre varchar(30),
	primer_apellido varchar(30) NOT NULL,
	segundo_apellido varchar(30) NOT NULL,
	provincia varchar(30) NOT NULL,
	canton varchar(30) NOT NULL,
	distrito varchar(30) NOT NULL,
	preferencias varchar(50) NOT NULL
	);

ALTER TABLE tienda.cliente ADD CONSTRAINT id_cliente_PK PRIMARY KEY (cedula);

CREATE TABLE tienda.telefono_cliente(
	ID_telefono int NOT NULL,
	ID_cliente int NOT NULL,
	numero_telefono int NOT NULL
	);

ALTER TABLE tienda.telefono_cliente ADD CONSTRAINT id_telefonoC_PK PRIMARY KEY (ID_telefono);
ALTER TABLE tienda.telefono_cliente ADD CONSTRAINT id_cliente_telefono_FK FOREIGN KEY (ID_cliente) REFERENCES tienda.cliente(cedula);

INSERT INTO tienda.telefono_cliente(ID_telefono, ID_cliente, numero_telefono)
VALUES
	(1, 123, 88022456),
	(2, 123, 84729133)

INSERT INTO tienda.telefono_cliente(ID_telefono, ID_cliente, numero_telefono)
VALUES
	(3, 134, 85629128),
	(4, 134, 87359630)

CREATE TABLE tienda.correo_cliente(
	ID_correo int NOT NULL,
	ID_cliente int NOT NULL,
	correo varchar(30) NOT NULL
	);

ALTER TABLE tienda.correo_cliente ADD CONSTRAINT id_correoC_PK PRIMARY KEY (ID_correo);
ALTER TABLE tienda.correo_cliente ADD CONSTRAINT id_cliente_correo_FK FOREIGN KEY (ID_cliente) REFERENCES tienda.cliente(cedula);

INSERT INTO tienda.correo_cliente(ID_Correo, ID_cliente, correo)
VALUES
	(10, 123, 'victorloria23@gmail.com'),
	(20, 134, 'andreybrenes12@gmail.com')

CREATE TABLE tienda.compra_cliente(
	ID_venta int NOT NULL,
	ID_cliente int NOT NULL
	);

INSERT INTO tienda.compra_cliente(ID_venta, ID_cliente)
VALUES(1,123);

DELETE FROM tienda.compra_cliente;

ALTER TABLE tienda.compra_cliente ADD CONSTRAINT id_venta_compra_FK FOREIGN KEY (ID_venta) REFERENCES tienda.venta(ID_venta);
ALTER TABLE tienda.compra_cliente ADD CONSTRAINT id_cliente_compra_FK FOREIGN KEY (ID_cliente) REFERENCES tienda.cliente(cedula);

CREATE TABLE tienda.venta(
	ID_venta int NOT NULL,
	fecha_hora datetime NOT NULL,
	metodo_pago varchar(15) NOT NULL,
	ID_producto int NOT NULL,
	ID_empleado int NOT NULL
	);

ALTER TABLE tienda.venta ADD CONSTRAINT id_venta_PK PRIMARY KEY (ID_venta);
ALTER TABLE tienda.venta ADD CONSTRAINT id_producto_venta_FK FOREIGN KEY (ID_producto) REFERENCES tienda.producto(ID_producto);
ALTER TABLE tienda.venta ADD CONSTRAINT id_empleado_venta_FK FOREIGN KEY (ID_empleado) REFERENCES tienda.empleado(cedula);

CREATE TABLE tienda.empleado(
	cedula int NOT NULL,
	primer_nombre varchar(30) NOT NULL,
	segundo_nombre varchar(30),
	primer_apellido varchar(30) NOT NULL,
	segundo_apellido varchar(30) NOT NULL,
	rol varchar(20) NOT NULL,
	dias_laborales varchar(30) NOT NULL,
	hora_entrada time NOT NULL,
	hora_salida time NOT NULL,
	salario float NOT NULL,
	telefono int NOT NULL,
	area_trabajo varchar(30) NOT NULL
	);

ALTER TABLE tienda.empleado ADD CONSTRAINT id_empleado_PK PRIMARY KEY (cedula);

CREATE TABLE tienda.proveedor(
	ID_proveedor int NOT NULL,
	telefono int NOT NULL,
	fecha_entrega date NOT NULL
	);

ALTER TABLE tienda.proveedor ADD CONSTRAINT id_proveedor_PK PRIMARY KEY (ID_proveedor);

CREATE TABLE tienda.producto_proveedor(
	ID_proveedor int NOT NULL,
	ID_producto int NOT NULL
	);

ALTER TABLE tienda.producto_proveedor ADD CONSTRAINT id_proveedor_producto_FK FOREIGN KEY (ID_proveedor) REFERENCES tienda.proveedor(ID_proveedor);
ALTER TABLE tienda.producto_proveedor ADD CONSTRAINT id_producto_producto_FK FOREIGN KEY (ID_producto) REFERENCES tienda.producto(ID_producto);

CREATE TABLE tienda.promocion_evento(
	ID_promocion int NOT NULL,
	ID_producto int NOT NULL,
	fecha date NOT NULL,
	descuento int NOT NULL,
	);

ALTER TABLE tienda.promocion_evento ADD CONSTRAINT id_promocion_PK PRIMARY KEY (ID_promocion);
ALTER TABLE tienda.promocion_evento ADD CONSTRAINT id_producto_promocion_FK FOREIGN KEY (ID_producto) REFERENCES tienda.producto(ID_producto);

CREATE TABLE tienda.promocion_cliente(
	ID_promocion int NOT NULL,
	ID_telefono int NOT NULL,
	correo varchar(30)
	);

ALTER TABLE tienda.promocion_cliente ADD CONSTRAINT id_promocion_promocion_FK FOREIGN KEY (ID_promocion) REFERENCES tienda.promocion_evento(ID_promocion);
ALTER TABLE tienda.promocion_cliente ADD CONSTRAINT id_telefono_promocion_FK FOREIGN KEY (ID_telefono) REFERENCES tienda.telefono_cliente(ID_telefono);

SELECT * FROM tienda.producto;
SELECT * FROM tienda.cliente;
SELECT * FROM tienda.empleado;
SELECT * FROM tienda.venta;
SELECT * FROM tienda.compra_cliente;
SELECT * FROM tienda.inventario;
SELECT * FROM tienda.telefono_cliente;


SELECT count(venta.ID_venta) AS Ventas, producto.nombre AS Producto, cliente.primer_nombre + ' ' + cliente.primer_apellido AS Cliente, venta.metodo_pago AS Método_pago, empleado.primer_nombre +' '+ empleado.primer_apellido AS Empleado
FROM tienda.producto INNER JOIN tienda.venta ON producto.ID_producto = venta.ID_producto
INNER JOIN tienda.compra_cliente ON compra_cliente.ID_venta = venta.ID_venta 
INNER JOIN tienda.cliente ON compra_cliente.ID_cliente = cliente.cedula 
INNER JOIN tienda.empleado ON venta.ID_empleado = empleado.cedula
GROUP BY producto.nombre, cliente.primer_nombre, cliente.primer_apellido, venta.metodo_pago, empleado.primer_nombre, empleado.primer_apellido;

SELECT count(venta.ID_venta) AS Ventas
FROM tienda.producto INNER JOIN tienda.venta ON producto.ID_producto = venta.ID_producto
INNER JOIN tienda.compra_cliente ON compra_cliente.ID_venta = venta.ID_venta 
INNER JOIN tienda.cliente ON compra_cliente.ID_cliente = cliente.cedula 
INNER JOIN tienda.empleado ON venta.ID_empleado = empleado.cedula;

-- Historial de compra sin cliente frecuente
SELECT cliente.primer_nombre + ' ' + cliente.primer_apellido, MIN(telefono_cliente.numero_telefono), correo_cliente.correo, venta.fecha_hora, venta.metodo_pago, producto.nombre, producto.precio
FROM tienda.producto INNER JOIN tienda.venta ON producto.ID_producto = venta.ID_producto
INNER JOIN tienda.compra_cliente ON compra_cliente.ID_venta = venta.ID_venta 
INNER JOIN tienda.cliente ON compra_cliente.ID_cliente = cliente.cedula 
INNER JOIN tienda.empleado ON venta.ID_empleado = empleado.cedula
INNER JOIN tienda.telefono_cliente ON telefono_cliente.ID_cliente = cliente.cedula
INNER JOIN tienda.correo_cliente ON correo_cliente.ID_cliente = cliente.cedula
GROUP BY cliente.primer_nombre, cliente.primer_apellido, correo_cliente.correo, venta.fecha_hora, venta.metodo_pago, producto.nombre, producto.precio
--HAVING COUNT(venta.ID_venta) < AVG(venta.ID_venta)

--Historial de compra con cliente frecuente
SELECT cliente.primer_nombre, venta.fecha_hora, venta.metodo_pago, producto.nombre, producto.precio
FROM tienda.producto INNER JOIN tienda.venta ON producto.ID_producto = venta.ID_producto
INNER JOIN tienda.compra_cliente ON compra_cliente.ID_venta = venta.ID_venta 
INNER JOIN tienda.cliente ON compra_cliente.ID_cliente = cliente.cedula 
INNER JOIN tienda.empleado ON venta.ID_empleado = empleado.cedula
GROUP BY cliente.primer_nombre, venta.fecha_hora, venta.metodo_pago, producto.nombre, producto.precio
HAVING COUNT(compra_cliente.ID_cliente) >= AVG(compra_cliente.ID_cliente)

SELECT producto.nombre, cliente.primer_nombre
FROM tienda.producto INNER JOIN tienda.venta ON tienda.producto.ID_producto = venta.ID_producto
INNER JOIN tienda.compra_cliente ON compra_cliente.ID_venta = venta.ID_venta 
INNER JOIN tienda.cliente ON compra_cliente.ID_cliente = cliente.cedula;

SELECT c.primer_nombre, v.fecha_hora, v.metodo_pago
FROM tienda.cliente c INNER JOIN tienda.compra_cliente p ON c.cedula = p.ID_cliente
INNER JOIN tienda.venta v ON p.ID_venta = v.ID_venta

SELECT compra_cliente.ID_cliente
FROM tienda.compra_cliente
GROUP BY compra_cliente.ID_cliente
HAVING COUNT(compra_cliente.ID_cliente) > (SELECT AVG(contador) AS promedio FROM (SELECT COUNT(*) AS contador FROM tienda.compra_cliente GROUP BY compra_cliente.ID_cliente)AS c)

Select nombre, descripcion, precio, categoria from tienda.producto

SELECT empleado.primer_nombre, empleado.segundo_nombre, producto.nombre, venta.fecha_hora, venta.metodo_pago
FROM tienda.empleado INNER JOIN tienda.venta ON empleado.cedula = venta.ID_empleado
INNER JOIN tienda.producto ON venta.ID_producto = producto.ID_producto WHERE empleado.cedula = 321
GROUP BY empleado.primer_nombre, empleado.segundo_nombre, producto.nombre, venta.fecha_hora, venta.metodo_pago;