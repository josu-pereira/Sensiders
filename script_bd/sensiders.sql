create database sensiders;
use sensiders;

create table Supermercado(
	idSupermercado int primary key auto_increment,
    cep char(8) not null,
    numero int not null,
    email varchar(50) not null,
    senha varchar(20) not null,
    nome varchar(30) not null
);

create table Setor (
	idSetor int primary key auto_increment,
    nome varchar(30) not null,
    fkSupermercado int not null,
    foreign key(fkSupermercado) references Supermercado(idSupermercado)
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
(null, '05386330', 37, 'dia@dia.com', 'dia123', 'Dia'),
(null, '09240000', 399, 'extra@extra.com', 'extra123', 'Extra');

select * from Supermercado;

insert into Setor values
(null, 'Padaria', 1),
(null, 'Padaria', 2),
(null, 'Açougue', 2),
(null, 'Açougue', 1),
(null, 'Eletrônicos', 2);

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

select * from setor, sensor where idSetor = fkSetor;
select * from supermercado, setor where idSupermercado = fkSupermercado and idSupermercado = 1;
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

select * from dado where dataHora = '2020-04-05 10:34:19';