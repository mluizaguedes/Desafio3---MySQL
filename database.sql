create database desafio3;
#drop database desafio3;

show databases;

use desafio3;

create table contatos
(
	email varchar(60) not null,
    assunto varchar(60) not null,
    descricao varchar(200) not null
);

select * from contatos;
