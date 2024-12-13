create database CONSCESSIONARIA_BD;
use CONSCESSIONARIA_BD;
create table Cliente (
    codigo serial primary key,
    nome varchar(200) not null,
    idade integer not null,
    rg integer not null,
    cpf integer,
    telefone varchar(15),
    rua varchar(30),
    numero integer,
    cep integer default 79200000,
    cidade varchar(20) default 'Brasília',
    estado varchar(2) default 'DF'
);

create table Automovel (
    placa varchar(8) primary key,
    renavam integer,
    anofab integer,
    fabricante varchar(10),
    modelo varchar(25),
    codcliente integer references cliente(codigo) 
);

create table Ocorrencia (
	numero serial primary key,
    localidade varchar(50),
    descricao varchar(200),
    datas date,
    autoPlaca varchar(8) references automovel (placa)
);

