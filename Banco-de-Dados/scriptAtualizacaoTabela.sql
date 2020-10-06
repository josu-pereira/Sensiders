create table MaquinaComponente(
    idMaqComp int primary key identity (1,1)
    , fkMaquina int foreign key references Maquina(idMaquina)
    , fkComponente int foreign key references Componente(idComponente)
)

create table LeituraMaquina(
    idLeituraMaquina int primary key identity (1,1)
    , leitura varchar(5) not null
    , dataHora datetime not null
    , fkMaqComp int foreign key references MaquinaComponente(idMaqComp)
)