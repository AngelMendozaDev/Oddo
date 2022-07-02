/***************************
* Base de datos de Oddo
* Realizo: Luis Angel Mendoza Garcia
* creado: 20-06-2022
*****************************/

create database oddo;

use oddo;

create table cards(
	id_card int auto_increment not null,
    org_contact varchar(45),
    oportunity varchar(45),
    mail varchar(60),
    phone varchar(10),
    ingreso decimal(7,2),
    calif int,
    estado int,
    primary key(id_card)
);

create view getAllCards as SELECT * FROM cards;

DELIMITER $$
create procedure newRegister(
	in contact varchar(45),
    in op varchar(45),
    in tomail varchar(60),
    in tel varchar(10),
    in cash decimal(7,2))
    begin
		INSERT INTO cards (org_contact, oportunity, mail, phone, ingreso, calif, estado) VALUES (contact,op, tomail, tel, cash, '0', 1);
    end