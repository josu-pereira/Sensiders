CREATE DATABASE `bdProjetoSensiders` ;

USE `bdProjetoSensiders`;

CREATE TABLE `Supermercado`(
	`idSupermercado` int AUTO_INCREMENT NOT NULL,
	`nome` varchar(30) NOT NULL,
PRIMARY KEY 
(
	`idSupermercado` ASC
)
)
;

CREATE TABLE `Filial`(
	`idFilial` int AUTO_INCREMENT NOT NULL,
	`fkSupermercado` int NOT NULL,
	`cep` varchar(8) NOT NULL,
	`numero` int NOT NULL,
PRIMARY KEY 
(
	`idFilial` ASC
),
foreign key (
	`fkSupermercado`
)
references `Supermercado`(
	`idSupermercado`
)
)
;

CREATE TABLE `Maquina`(
	`idMaquina` int AUTO_INCREMENT NOT NULL,
	`descricaoMaquina` varchar(30) NULL,
	`fkFilial` int NULL,
	`hashmac` varchar(300) NULL,
PRIMARY KEY 
(
	`idMaquina` ASC
),
foreign key 
(
	`fkFilial`
)
references `Filial`(`idFilial`)
)
;


CREATE TABLE `Componente`(
	`idComponente` int AUTO_INCREMENT NOT NULL,
	`nomeComponente` varchar(45) NULL,
	`totalComponente` varchar(50) NULL,
	`metricaComponente` varchar(30) NULL,
	`medidaAlertaComponente` int NULL,
PRIMARY KEY 
(
	`idComponente` ASC
)
)
;

CREATE TABLE `MaquinaComponente`(
	`idMaqComp` int AUTO_INCREMENT NOT NULL,
	`fkMaquina` int NULL,
	`fkComponente` int NULL,
PRIMARY KEY 
(
	`idMaqComp` ASC
),
foreign key (`fkMaquina`) references `Maquina`(`idMaquina`),
foreign key (`fkComponente`) references `Componente`(`idComponente`)
)
;

CREATE TABLE `Usuario`(
	`idUsuario` int AUTO_INCREMENT NOT NULL,
	`emailUsuario` varchar(70) NOT NULL,
	`senhaUsuario` varchar(45) NOT NULL,
	`nomeUsuario` varchar(45) NOT NULL,
	`fkIdFilial` int NOT NULL,
PRIMARY KEY 
(
	`idUsuario` ASC
),
foreign key(`fkIdFilial`) references`Filial`(`idFilial`),
UNIQUE NONCLUSTERED 
(
	`emailUsuario` ASC
)
)
;



CREATE TABLE `LeituraMaquina`(
	`idLeituraMaquina` int AUTO_INCREMENT NOT NULL,
	`leitura` varchar(5) NOT NULL,
	`dataHora` datetime NOT NULL,
	`fkMaqComp` int NULL,
PRIMARY KEY 
(
	`idLeituraMaquina` ASC
),
foreign key (`fkMaqComp`)references `MaquinaComponente`(`idMaqComp`)
)
;

CREATE TABLE `Setor`(
	`idSetor` int AUTO_INCREMENT NOT NULL,
	`nome` varchar(30) NOT NULL,
	`fkFilial` int NOT NULL,
	`qtdSensores` int NULL,
PRIMARY KEY 
(
	`idSetor` ASC
),
foreign key (`fkFilial`)references `Filial`(`idFilial`)
)
;

CREATE TABLE `dado`(
	`datahora` datetime NULL,
	`fkSetor` int NULL,
	`grauMov` decimal(4, 1) NULL,
    foreign key(`fkSetor`) references `Setor`(`idSetor`)
)
;


 -- funcao
DELIMITER $$
create function fc_returnCountComponente(p_maquina int)
returns int
deterministic
begin
declare v_num int; 
set v_num = (select count(idComponente) from Componente 
                inner join MaquinaComponente 
                on MaquinaComponente.fkComponente = Componente.idComponente 
                    inner join Maquina 
                    on Maquina.idMaquina = MaquinaComponente.fkMaquina
                        where Maquina.idMaquina = p_maquina );
return v_num;
end$$
DELIMITER ;

-- funcao
Delimiter $$
Create Function fc_returnLeitura(p_filial INT, p_componente INT, p_maquina INT)
returns VARCHAR(5)
deterministic
BEGIN

DECLARE v_leitura varchar(5);
SET v_leitura=(
    select DISTINCT leitura from LeituraMaquina 
    inner join MaquinaComponente 
    on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp
        inner join Componente
        on Componente.idComponente = MaquinaComponente.fkComponente
            inner join Maquina 
            on Maquina.idMaquina = MaquinaComponente.fkMaquina
                inner join Usuario 
                on Usuario.fkIdFilial = Maquina.fkFilial
                    where Usuario.fkIdFilial = p_filial AND Componente.idComponente = p_componente AND Maquina.idMaquina = p_maquina
                    AND LeituraMaquina.idLeituraMaquina = (select max(idLeituraMaquina) from LeituraMaquina 
                                                                inner join MaquinaComponente
                                                                on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp
                                                                    inner join Maquina 
                                                                    on Maquina.idMaquina = MaquinaComponente.fkMaquina
                                                                        inner join Componente
                                                                        on Componente.idComponente = MaquinaComponente.fkComponente
                                                                            where Maquina.idMaquina = p_maquina AND Componente.idComponente = p_componente)
);

RETURN v_leitura;
END$$
DELIMITER ;

-- view
create view `vwListaMaquinas` as 
    select idMaquina, descricaoMaquina, fkFilial as 'fkFilial', hashmac from Maquina
        inner join Filial 
        on Filial.idFilial = Maquina.fkFilial;

-- view
CREATE view `vwListaComponentes` as
    select distinct idComponente as idComponente, nomeComponente as nomeComponente,
     totalComponente as totalComponente, metricaComponente as metricaComponente, 
     medidaAlertaComponente as medidaAlertaComponente, Maquina.idMaquina as idMaquina from Componente 
        inner join MaquinaComponente
        on MaquinaComponente.fkComponente = Componente.idComponente
            inner join Maquina 
            on Maquina.idMaquina = MaquinaComponente.fkMaquina
                inner join Filial 
                on Filial.idFilial = Maquina.fkFilial
                    inner join Usuario 
                    on Usuario.fkIdFilial = Filial.idFilial;

-- view
create view `vw_returnLeitura` as
    select leitura as leitura, Componente.nomeComponente as nome_componente, Maquina.idMaquina as idMaquina from LeituraMaquina
        inner join MaquinaComponente 
        on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp
            inner join Maquina 
            on Maquina.idMaquina = MaquinaComponente.fkMaquina
                inner join Componente 
                on Componente.idComponente = MaquinaComponente.fkComponente;
-- ==========================================================
/*
Acredito que esta procedure nao sera mais necessaria para o mysql, como o felipe
fez ela pura no python.
no momento ela so esta funionando somente no mssql
vvvvvvvvvvvvvvvv procedure "traduzida" do mssql para o mysql vvvvvvvvvvvvvvvvv
ver nos arquivos a procedure original.
DELIMITER //
CREATE PROCEDURE `sp_CadastroMaquina`
(
	p_nomeMaquina varchar(50),
	p_emailUsuario varchar(50),
	p_hashmac varchar(260),
	p_componentes varchar(50)
)
BEGIN

DECLARE d_fkFilial INT;
DECLARE d_fkMaquina INT; 
DECLARE d_vetorComp VARCHAR(50);

	SET d_fkFilial = (SELECT fkidFilial FROM Usuario WHERE p_emailUsuario = emailUsuario);

	-- RETIRAR OS ESPACOS E ASPAS E VIRGULAS
	SET d_vetorComp = REPLACE(p_componentes,'"','');
	SET d_vetorComp = REPLACE(d_vetorComp,' ','');
	-- SET @vetorComp = REPLACE(@vetorComp,',','')

	INSERT INTO Maquina(descricaoMaquina,fkFilial,hashmac)
		VALUES(p_nomeMaquina,d_fkFilial,p_hashmac);

	SET d_fkMaquina = (SELECT idMaquina FROM Maquina WHERE p_nomeMaquina = descricaoMaquina);

	INSERT INTO MaquinaComponente(fkMaquina,fkComponente)
		SELECT d_fkMaquina, value FROM string_split(d_vetorComp, ',');

	SELECT d_fkMaquina as 'maq', p_nomeMaquina as 'nome da maquina', d_fkFilial as 'filial', p_componentes as 'MaqComps';

END;
//
DELIMITER ;
*/
-- =================PROCEDURES ===========================
DELIMITER //
CREATE PROCEDURE `sp_DadosUltimaDuasHora`(
p_Maquina INT,
p_Comp INT
)
BEGIN
    SELECT LeituraMaquina.leitura, Componente.nomeComponente, LeituraMaquina.dataHora
    FROM LeituraMaquina
        INNER JOIN MaquinaComponente
        on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp
        INNER JOIN Componente
        ON Componente.idComponente = MaquinaComponente.fkComponente
    WHERE dataHora >= DATEADD(HOUR, -5, GETDATE())
        AND Componente.idComponente = p_Comp
        AND MaquinaComponente.fkMaquina = p_Maquina;
END;
//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE `sp_DadosUltimaHora`(
p_Maquina INT,
p_Comp INT
)
BEGIN
    SELECT LeituraMaquina.leitura, Componente.nomeComponente, LeituraMaquina.dataHora
    FROM LeituraMaquina
        INNER JOIN MaquinaComponente
        on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp
        INNER JOIN Componente
        ON Componente.idComponente = MaquinaComponente.fkComponente
    WHERE dataHora >= DATEADD(HOUR, -4, GETDATE())
        AND Componente.idComponente = p_Comp
        AND MaquinaComponente.fkMaquina = p_Maquina;
END;
//
DELIMITER ;

-- ========================================================

DELIMITER //
CREATE PROCEDURE `sp_DadosUltimaSemana`(
p_Maquina INT,
p_Comp INT
)
BEGIN
    SELECT LeituraMaquina.leitura, Componente.nomeComponente, LeituraMaquina.dataHora
    FROM LeituraMaquina
        INNER JOIN MaquinaComponente
        on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp
        INNER JOIN Componente
        ON Componente.idComponente = MaquinaComponente.fkComponente
    WHERE dataHora >= DATEADD(WEEK, -1, GETDATE())
        AND Componente.idComponente = p_Comp
        AND MaquinaComponente.fkMaquina = p_Maquina;
END;
//
DELIMITER ;

-- =====================================================

DELIMITER //
CREATE PROCEDURE `sp_DadosUltimoDia`(
p_Maquina INT,
p_Comp INT
)
BEGIN
    SELECT LeituraMaquina.leitura, Componente.nomeComponente, LeituraMaquina.dataHora
    FROM LeituraMaquina
        INNER JOIN MaquinaComponente
        on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp
        INNER JOIN Componente
        ON Componente.idComponente = MaquinaComponente.fkComponente
    WHERE dataHora >= DATEADD(DAY, -1, GETDATE())
        AND Componente.idComponente = p_Comp
        AND MaquinaComponente.fkMaquina = p_Maquina;
END;
//
DELIMITER ;

-- =======================================================

DELIMITER //
CREATE PROCEDURE `sp_DadosUltimoDoisDias`(
p_Maquina INT,
p_Comp INT
)
BEGIN
    SELECT LeituraMaquina.leitura, Componente.nomeComponente, LeituraMaquina.dataHora
    FROM LeituraMaquina
        INNER JOIN MaquinaComponente
        on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp
        INNER JOIN Componente
        ON Componente.idComponente = MaquinaComponente.fkComponente
    WHERE dataHora >= DATEADD(DAY, -2, GETDATE())
        AND Componente.idComponente = p_Comp
        AND MaquinaComponente.fkMaquina = p_Maquina;
END;
//
DELIMITER ;

-- ==============================================

DELIMITER //
CREATE PROCEDURE `sp_DadosUltimoMes`(
p_Maquina INT,
p_Comp INT
)
BEGIN
    SELECT LeituraMaquina.leitura, Componente.nomeComponente, LeituraMaquina.dataHora
    FROM LeituraMaquina
        INNER JOIN MaquinaComponente
        on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp
        INNER JOIN Componente
        ON Componente.idComponente = MaquinaComponente.fkComponente
    WHERE dataHora >= DATEADD(MONTH, -1, GETDATE())
        AND Componente.idComponente = p_Comp
        AND MaquinaComponente.fkMaquina = p_Maquina;
END;
//
DELIMITER ;

-- ==================================================

DELIMITER //
CREATE PROCEDURE `sp_DadosUltimosQuacDias`(
p_Maquina INT,
p_Comp INT
)
BEGIN
    SELECT LeituraMaquina.leitura, Componente.nomeComponente, LeituraMaquina.dataHora
    FROM LeituraMaquina    
        INNER JOIN MaquinaComponente
        on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp
        INNER JOIN Componente
        ON Componente.idComponente = MaquinaComponente.fkComponente
    WHERE dataHora >= DATEADD(DAY, -14, GETDATE())
        AND Componente.idComponente = p_Comp
        AND MaquinaComponente.fkMaquina = p_Maquina;
END;
//
DELIMITER ;

-- ===============================================================

DELIMITER // 
CREATE PROCEDURE sp_NovoUsuario
(
p_nomeMercado varchar(50),
p_cep CHAR(8),
p_numero INT,
p_nome  VARCHAR(50),
p_email VARCHAR(50),
p_senha VARCHAR(50)
)
BEGIN
	DECLARE d_fkidmercado INT;
    DECLARE d_fkfilial INT;
	SET d_fkidmercado = (SELECT idSupermercado FROM Supermercado WHERE nome = p_nomeMercado);
	SET d_fkfilial = (SELECT idFilial FROM Filial ORDER BY idFilial DESC limit 1)+1;

		INSERT INTO Filial(fkSupermercado,cep,numero)
			VALUES(d_fkidmercado, p_cep, p_numero);
		INSERT INTO Usuario(emailUsuario, senhaUsuario, nomeUsuario, fkIdFilial)
			VALUES(p_email, p_senha, p_nome, d_fkfilial);

		SELECT p_cep as 'cep', p_numero as 'numero', p_nome as 'nomeUsuario', p_email as 'email';
END;
//
DELIMITER ;
