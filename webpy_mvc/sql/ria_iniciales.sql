create database ria_iniciales;
use ria_iniciales;
create table clientes(
    id_clientes int(4) not null auto_increment primary key ,
    nombre_cliente varchar(20)not null,
    apellidos_cliente varchar(30) not null,
    tipo_cliente varchar (30) not null,
    calle_numero varchar(30) not null);

create table productos(
    id_producto int(4) not null auto_increment primary key,
    nombre_producto varchar(20) not null,
    contenido varchar(10) not null,
    marca varchar(20) not null,
    precio int(7) not null);

insert into clientes(nombre_cliente,apellidos_cliente,tipo_cliente,calle_numero)
values('Jose','Garcia Hernandez','preferencial','francisco Imadero n25'),
('Andrea','Resendiz Alvarado','general','allende n32'),
('Zuleyma','Garcia Resendiz','preferencial','heroes de nacozari n10');

insert into productos (nombre_producto,contenido,marca,precio)
values ('leche','1litro','alpura','15'),
('azucar','2kg','zuka','37'),
('crema','250ml','lala','12');

show tables;

select * from clientes;
describe clientes;

select * from productos;
describe productos;

create user 'egr'@'localhost' IDENTIFIED BY 'ria.2019';
Grant ALL PRIVILEGES ON ria_iniciales.* TO'egr'@'localhost';
FLUSH PRIVILEGES;
