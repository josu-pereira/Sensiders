create table Maquina(
    idMaquina int primary key identity (1,1)
    , descricaoMaquina varchar (30)
    , fkFilial int foreign key references Filial(idFilial)
)

create table Componente(
    idComponente int primary key identity (1,1)
    , nomeComponente varchar (45)
    , totalComponente float
)

create table DadosComponentes(
    idDadosComponentes int primary key identity (1,1)
    , fkComponente int foreign key references Componente (idComponente)
    , fkMaquina int foreign key references Maquina (idMaquina)
    , dadoGerado float
    , dataHora datetime
)
