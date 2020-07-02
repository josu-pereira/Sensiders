create database sensiders;
use sensiders;

create table Supermercado(
	idSupermercado int primary key auto_increment,
    nome varchar(30) not null
);

create table Filial (
    idFilial int primary key auto_increment,
    fkSupermercado int not null,
    foreign key (fkSupermercado) references Supermercado(idSupermercado),
    cep char(8) not null,
    numero int not null
);

create table Usuario (
	idUsuario int primary key auto_increment,
    emailUsuario varchar(70) not null unique,
    senhaUsuario varchar(45) not null,
    nomeUsuario varchar(45) not null,
    fkIdFilial int not null,
    foreign key(fkIdFilial) references Filial(idFilial)
); 

create table Setor (
	idSetor int primary key auto_increment,
    nome varchar(30) not null,
    fkFilial int not null,
    foreign key(fkFilial) references Filial(idFilial),
	qtdSensor int
);

create table dado (
	dataHora datetime not null,
    fkSetor int not null,
    foreign key(fkSetor) references Setor(idSetor),
    primary key(dataHora, fkSetor),
    grauMov decimal(4,1) not null
);

insert into Supermercado values
(null, 'Sonda'),
(null, 'Dias');
select * from Supermercado;

insert into Filial values
-- id    idmarket     nome      email   senha     cep    numero
(null, 1, 02235001, 1214),
(null, 1, 02236005, 9242),
(null, 2, 06624009, 343),
(null, 2, 07724001, 151);

select * from filial;

-- id   email    senha   nome   fkfilial
insert into Usuario values
(null,'joao@outlook.com', 'q1w2e3r4','Gerente Joao', 1),
(null, 'paulo@outlook.com', 'a1s2d3f4','Administrador',2),
(null, 'carlinha@htomail.com', 'z1x2c3v4b5','Gerente Carla',3),
(null, 'carlinhos@htomail.com', 'z1x2c3w1e2','Gerente Carlos',4);

insert into Setor values
(null, 'Padaria', 1,10),
(null, 'Padaria', 2,10),
(null, 'Açougue', 2,10),
(null, 'Açougue', 4,10),
(null, 'Eletrônicos', 3,10);

select * from setor;
select * from supermercado, setor where idSupermercado = fkFilial and idSupermercado = 1;

insert into dado values('2020-04-05 10:34:09', 1, 30),
('2020-04-05 10:34:09', 2, 20),
('2020-04-05 10:34:09', 3, 10),
('2020-04-05 10:34:19', 1, 90),
('2020-04-05 10:34:19', 2, 80),
('2020-04-05 10:34:19', 3, 30),
('2020-04-05 10:34:29', 1, 50),
('2020-04-05 10:34:29', 2, 40),
('2020-04-05 10:34:29', 3, 60),
('2020-04-05 10:34:39', 1, 60),
('2020-04-05 10:34:39', 2, 50),
('2020-04-05 10:34:39', 3, 20);

select * from dado;

select * from dado where dataHora = '2020-04-05 10:34:19';
