create database RPG
default character set utf8
default collate utf8_general_ci;

use RPG;

create table armas(
	id int not null auto_increment,
	nome varchar(30) not null,
    custo decimal(8,2) not null,
    dano decimal(8,2) not null,
    peso decimal(5,2) not null,
    propriedade text,
    primary key(id)
) default charset = utf8;

insert into armas
(nome, custo, dano, peso, propriedade)
values
('Espada', '10.00', '20.00', '15.30', 'Duas mãos'),
('Adaga', '5.00', '7.5', '5.0', 'Uma mão'),
('Arco', '20.75', '10.00', '10.0', 'Duas mãos');