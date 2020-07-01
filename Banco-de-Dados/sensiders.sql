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
    foreign key(fkFilial) references Filial(idFilial)
);

create table Sensor (
	idSensor int primary key auto_increment,
    fkSetor int not null,
    foreign key(fkSetor) references Setor(idSetor)
);

create table dado (
	dataHora datetime not null,
    fkSensor int not null,
    foreign key(fkSensor) references Sensor(idSensor),
    primary key(dataHora, fkSensor),
    statusSensor char(1) not null,
    check (statusSensor = 's' or statusSensor = 'n')
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
(null, 'Padaria', 1),
(null, 'Padaria', 2),
(null, 'Açougue', 2),
(null, 'Açougue', 4),
(null, 'Eletrônicos', 3);

select * from setor;

insert into sensor values
(null, 1),
(null, 1),
(null, 1),
(null, 4),
(null, 4),
(null, 4),
(null, 2),
(null, 2),
(null, 2),
(null, 3),
(null, 3),
(null, 3),
(null, 5),
(null, 5),
(null, 5);

select * from sensor;

select * from setor, sensor where idSetor = fkSetor;
select * from supermercado, setor where idSupermercado = fkFilial and idSupermercado = 1;
select * from supermercado, setor, sensor where  idSupermercado = fkSetor and idSetor = fkSetor;

insert into dado values('2020-04-05 10:34:09', 1, 's'),
('2020-04-05 10:34:09', 2, 's'),
('2020-04-05 10:34:09', 3, 's'),
('2020-04-05 10:34:19', 1, 's'),
('2020-04-05 10:34:19', 2, 'n'),
('2020-04-05 10:34:19', 3, 's'),
('2020-04-05 10:34:29', 1, 's'),
('2020-04-05 10:34:29', 2, 'n'),
('2020-04-05 10:34:29', 3, 'n'),
('2020-04-05 10:34:39', 1, 'n'),
('2020-04-05 10:34:39', 2, 'n'),
('2020-04-05 10:34:39', 3, 'n');

select * from dado;

select * from dado where dataHora = '2020-04-05 10:34:19';