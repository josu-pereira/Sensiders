/****** Object:  Database `bdProjetoSensiders`    Script Date: 04/12/2020 14:04:32 ******/
CREATE DATABASE `bdProjetoSensiders`  (EDITION = 'Basic', SERVICE_OBJECTIVE = 'Basic', MAXSIZE = 2 GB) WITH CATALOG_COLLATION = SQL_Latin1_General_CP1_CI_AS;
;
ALTER DATABASE `bdProjetoSensiders` SET COMPATIBILITY_LEVEL = 150
;
ALTER DATABASE `bdProjetoSensiders` SET ANSI_NULL_DEFAULT OFF 
;
ALTER DATABASE `bdProjetoSensiders` 
ALTER DATABASE `bdProjetoSensiders` 
ALTER DATABASE `bdProjetoSensiders` SET ANSI_WARNINGS OFF 
;
ALTER DATABASE `bdProjetoSensiders` SET ARITHABORT OFF 
;
ALTER DATABASE `bdProjetoSensiders` SET AUTO_SHRINK OFF 
;
ALTER DATABASE `bdProjetoSensiders` SET AUTO_UPDATE_STATISTICS ON 
;
ALTER DATABASE `bdProjetoSensiders` SET CURSOR_CLOSE_ON_COMMIT OFF 
;
ALTER DATABASE `bdProjetoSensiders` SET CONCAT_NULL_YIELDS_NULL OFF 
;
ALTER DATABASE `bdProjetoSensiders` SET NUMERIC_ROUNDABORT OFF 
;
ALTER DATABASE `bdProjetoSensiders` 
ALTER DATABASE `bdProjetoSensiders` SET RECURSIVE_TRIGGERS OFF 
;
ALTER DATABASE `bdProjetoSensiders` SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
;
ALTER DATABASE `bdProjetoSensiders` SET ALLOW_SNAPSHOT_ISOLATION ON 
;
ALTER DATABASE `bdProjetoSensiders` SET PARAMETERIZATION SIMPLE 
;
ALTER DATABASE `bdProjetoSensiders` SET READ_COMMITTED_SNAPSHOT ON 
;
ALTER DATABASE `bdProjetoSensiders` SET  MULTI_USER 
;
ALTER DATABASE `bdProjetoSensiders` SET ENCRYPTION ON
;
ALTER DATABASE `bdProjetoSensiders` SET QUERY_STORE = ON
;
ALTER DATABASE `bdProjetoSensiders` SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 7), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 10, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
;
/****** Object:  UserDefinedFunction `fc_returnCountComponente`    Script Date: 04/12/2020 14:04:32 ******/


create function `fc_returnCountComponente`(@maquina int)
returns int
as
begin
declare @num int 
set @num = (select count(idComponente) from Componente 
                inner join MaquinaComponente 
                on MaquinaComponente.fkComponente = Componente.idComponente 
                    inner join Maquina 
                    on Maquina.idMaquina = MaquinaComponente.fkMaquina
                        where Maquina.idMaquina = @maquina )
return @num
end
;
/****** Object:  UserDefinedFunction `fc_returnLeitura`    Script Date: 04/12/2020 14:04:32 ******/


Create Function `fc_returnLeitura`(@filial INT, @componente INT, @maquina INT)
returns VARCHAR(5)
AS
BEGIN

DECLARE @leitura varchar(5)
SET @leitura=(
    select DISTINCT leitura from LeituraMaquina 
    inner join MaquinaComponente 
    on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp
        inner join Componente
        on Componente.idComponente = MaquinaComponente.fkComponente
            inner join Maquina 
            on Maquina.idMaquina = MaquinaComponente.fkMaquina
                inner join Usuario 
                on Usuario.fkIdFilial = Maquina.fkFilial
                    where Usuario.fkIdFilial = @filial AND Componente.idComponente = @componente AND Maquina.idMaquina = @maquina
                    AND LeituraMaquina.idLeituraMaquina = (select max(idLeituraMaquina) from LeituraMaquina 
                                                                inner join MaquinaComponente
                                                                on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp
                                                                    inner join Maquina 
                                                                    on Maquina.idMaquina = MaquinaComponente.fkMaquina
                                                                        inner join Componente
                                                                        on Componente.idComponente = MaquinaComponente.fkComponente
                                                                            where Maquina.idMaquina = @maquina AND Componente.idComponente = @componente)
)

RETURN @leitura
END
;
/****** Object:  UserDefinedFunction `fn_diagramobjects`    Script Date: 04/12/2020 14:04:32 ******/



	CREATE FUNCTION `fn_diagramobjects`() 
	RETURNS int
	WITH EXECUTE AS N'dbo'
	AS
	BEGIN
		declare @id_upgraddiagrams		int
		declare @id_sysdiagrams			int
		declare @id_helpdiagrams		int
		declare @id_helpdiagramdefinition	int
		declare @id_creatediagram	int
		declare @id_renamediagram	int
		declare @id_alterdiagram 	int 
		declare @id_dropdiagram		int
		declare @InstalledObjects	int

		select @InstalledObjects = 0

		select 	@id_upgraddiagrams = object_id(N'dbo.sp_upgraddiagrams'),
			@id_sysdiagrams = object_id(N'dbo.sysdiagrams'),
			@id_helpdiagrams = object_id(N'dbo.sp_helpdiagrams'),
			@id_helpdiagramdefinition = object_id(N'dbo.sp_helpdiagramdefinition'),
			@id_creatediagram = object_id(N'dbo.sp_creatediagram'),
			@id_renamediagram = object_id(N'dbo.sp_renamediagram'),
			@id_alterdiagram = object_id(N'dbo.sp_alterdiagram'), 
			@id_dropdiagram = object_id(N'dbo.sp_dropdiagram')

		if @id_upgraddiagrams is not null
			select @InstalledObjects = @InstalledObjects + 1
		if @id_sysdiagrams is not null
			select @InstalledObjects = @InstalledObjects + 2
		if @id_helpdiagrams is not null
			select @InstalledObjects = @InstalledObjects + 4
		if @id_helpdiagramdefinition is not null
			select @InstalledObjects = @InstalledObjects + 8
		if @id_creatediagram is not null
			select @InstalledObjects = @InstalledObjects + 16
		if @id_renamediagram is not null
			select @InstalledObjects = @InstalledObjects + 32
		if @id_alterdiagram  is not null
			select @InstalledObjects = @InstalledObjects + 64
		if @id_dropdiagram is not null
			select @InstalledObjects = @InstalledObjects + 128
		
		return @InstalledObjects 
	END
	
;
/****** Object:  UserDefinedFunction `fnStringToArray`    Script Date: 04/12/2020 14:04:32 ******/


CREATE FUNCTION `fnStringToArray` (@String VARCHAR(1000), @Separador CHAR(1))
RETURNS @Array TABLE (Valor VARCHAR(500))
AS
BEGIN
    IF PATINDEX('%' + @Separador + '%', @String) = 0
        INSERT INTO @Array VALUES (LTRIM(RTRIM(@String)))

    ELSE
    BEGIN
        WHILE PATINDEX('%' + @Separador + '%', @String) > 0
        BEGIN
            INSERT INTO @Array VALUES
            (SUBSTRING(LTRIM(RTRIM(@String)), 1, PATINDEX('%' + @Separador + '%', LTRIM(RTRIM(@String))) - 1))

            SET @String = SUBSTRING(@String, PATINDEX('%' + @Separador + '%', @String) + 1, LEN(@String))
        END
        INSERT INTO @Array VALUES (LTRIM(RTRIM(@String)))
    END

    RETURN
END 
;
/****** Object:  Table `Maquina`    Script Date: 04/12/2020 14:04:32 ******/


CREATE TABLE `Maquina`(
	`idMaquina` int AUTO_INCREMENT NOT NULL,
	`descricaoMaquina` varchar(30) NULL,
	`fkFilial` int NULL,
	`hashmac` varchar(300) NULL,
PRIMARY KEY 
(
	`idMaquina` ASC
)
)
;
/****** Object:  Table `Filial`    Script Date: 04/12/2020 14:04:32 ******/


CREATE TABLE `Filial`(
	`idFilial` int AUTO_INCREMENT NOT NULL,
	`fkSupermercado` int NOT NULL,
	`cep` varchar(8) NOT NULL,
	`numero` int NOT NULL,
PRIMARY KEY 
(
	`idFilial` ASC
)
)
;
/****** Object:  View `vwListaMaquinas`    Script Date: 04/12/2020 14:04:32 ******/


create view `vwListaMaquinas` as 
    select idMaquina, descricaoMaquina, fkFilial as 'fkFilial', hashmac from Maquina
        inner join Filial 
        on Filial.idFilial = Maquina.fkFilial
;
/****** Object:  Table `Componente`    Script Date: 04/12/2020 14:04:32 ******/


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
/****** Object:  Table `MaquinaComponente`    Script Date: 04/12/2020 14:04:32 ******/


CREATE TABLE `MaquinaComponente`(
	`idMaqComp` int AUTO_INCREMENT NOT NULL,
	`fkMaquina` int NULL,
	`fkComponente` int NULL,
PRIMARY KEY 
(
	`idMaqComp` ASC
)
)
;
/****** Object:  Table `Usuario`    Script Date: 04/12/2020 14:04:32 ******/


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
UNIQUE NONCLUSTERED 
(
	`emailUsuario` ASC
)
)
;
/****** Object:  View `vwListaComponentes`    Script Date: 04/12/2020 14:04:32 ******/


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
                    on Usuario.fkIdFilial = Filial.idFilial
;
/****** Object:  Table `LeituraMaquina`    Script Date: 04/12/2020 14:04:32 ******/


CREATE TABLE `LeituraMaquina`(
	`idLeituraMaquina` int AUTO_INCREMENT NOT NULL,
	`leitura` varchar(5) NOT NULL,
	`dataHora` datetime NOT NULL,
	`fkMaqComp` int NULL,
PRIMARY KEY 
(
	`idLeituraMaquina` ASC
)
)
;
/****** Object:  View `vw_returnLeitura`    Script Date: 04/12/2020 14:04:32 ******/


create view `vw_returnLeitura` as
    select leitura as leitura, Componente.nomeComponente as nome_componente, Maquina.idMaquina as idMaquina from LeituraMaquina
        inner join MaquinaComponente 
        on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp
            inner join Maquina 
            on Maquina.idMaquina = MaquinaComponente.fkMaquina
                inner join Componente 
                on Componente.idComponente = MaquinaComponente.fkComponente
;
/****** Object:  Table `dado`    Script Date: 04/12/2020 14:04:32 ******/


CREATE TABLE `dado`(
	`datahora` datetime NULL,
	`fkSetor` int NULL,
	`grauMov` decimal(4, 1) NULL
)
;
/****** Object:  Table `Setor`    Script Date: 04/12/2020 14:04:32 ******/


CREATE TABLE `Setor`(
	`idSetor` int AUTO_INCREMENT NOT NULL,
	`nome` varchar(30) NOT NULL,
	`fkFilial` int NOT NULL,
	`qtdSensores` int NULL,
PRIMARY KEY 
(
	`idSetor` ASC
)
)
;
/****** Object:  Table `Supermercado`    Script Date: 04/12/2020 14:04:32 ******/


CREATE TABLE `Supermercado`(
	`idSupermercado` int AUTO_INCREMENT NOT NULL,
	`nome` varchar(30) NOT NULL,
PRIMARY KEY 
(
	`idSupermercado` ASC
)
)
;
/****** Object:  Table `sysdiagrams`    Script Date: 04/12/2020 14:04:32 ******/


CREATE TABLE `sysdiagrams`(
	`name` `sysname` NOT NULL,
	`principal_id` int NOT NULL,
	`diagram_id` int AUTO_INCREMENT NOT NULL,
	`version` int NULL,
	`definition` `varbinary`(max) NULL,
PRIMARY KEY 
(
	`diagram_id` ASC
),
 CONSTRAINT `UK_principal_name` UNIQUE NONCLUSTERED 
(
	`principal_id` ASC,
	`name` ASC
)
)
;
ALTER TABLE `dado`  WITH CHECK ADD FOREIGN KEY(`fkSetor`)
REFERENCES `Setor` (`idSetor`)
;
ALTER TABLE `Filial`  WITH CHECK ADD FOREIGN KEY(`fkSupermercado`)
REFERENCES `Supermercado` (`idSupermercado`)
;
ALTER TABLE `LeituraMaquina`  WITH CHECK ADD FOREIGN KEY(`fkMaqComp`)
REFERENCES `MaquinaComponente` (`idMaqComp`)
;
ALTER TABLE `Maquina`  WITH CHECK ADD FOREIGN KEY(`fkFilial`)
REFERENCES `Filial` (`idFilial`)
;
ALTER TABLE `MaquinaComponente`  WITH CHECK ADD FOREIGN KEY(`fkComponente`)
REFERENCES `Componente` (`idComponente`)
;
ALTER TABLE `MaquinaComponente`  WITH CHECK ADD FOREIGN KEY(`fkMaquina`)
REFERENCES `Maquina` (`idMaquina`)
;
ALTER TABLE `Setor`  WITH CHECK ADD FOREIGN KEY(`fkFilial`)
REFERENCES `Filial` (`idFilial`)
;
ALTER TABLE `Usuario`  WITH CHECK ADD FOREIGN KEY(`fkIdFilial`)
REFERENCES `Filial` (`idFilial`)
;
/****** Object:  StoredProcedure `sp_alterdiagram`    Script Date: 04/12/2020 14:04:32 ******/



	CREATE PROCEDURE `sp_alterdiagram`
	(
		@diagramname 	sysname,
		@owner_id	int	= null,
		@version 	int,
		@definition 	varbinary(max)
	)
	WITH EXECUTE AS 'dbo'
	AS
	BEGIN
		set nocount on
	
		declare @theId 			int
		declare @retval 		int
		declare @IsDbo 			int
		
		declare @UIDFound 		int
		declare @DiagId			int
		declare @ShouldChangeUID	int
	
		if(@diagramname is null)
		begin
			RAISERROR ('Invalid ARG', 16, 1)
			return -1
		end
	
		execute as caller;
		select @theId = DATABASE_PRINCIPAL_ID();	 
		select @IsDbo = IS_MEMBER(N'db_owner'); 
		if(@owner_id is null)
			select @owner_id = @theId;
		revert;
	
		select @ShouldChangeUID = 0
		select @DiagId = diagram_id, @UIDFound = principal_id from dbo.sysdiagrams where principal_id = @owner_id and name = @diagramname 
		
		if(@DiagId IS NULL or (@IsDbo = 0 and @theId <> @UIDFound))
		begin
			RAISERROR ('Diagram does not exist or you do not have permission.', 16, 1);
			return -3
		end
	
		if(@IsDbo <> 0)
		begin
			if(@UIDFound is null or USER_NAME(@UIDFound) is null) -- invalid principal_id
			begin
				select @ShouldChangeUID = 1 ;
			end
		end

		-- update dds data			
		update dbo.sysdiagrams set definition = @definition where diagram_id = @DiagId ;

		-- change owner
		if(@ShouldChangeUID = 1)
			update dbo.sysdiagrams set principal_id = @theId where diagram_id = @DiagId ;

		-- update dds version
		if(@version is not null)
			update dbo.sysdiagrams set version = @version where diagram_id = @DiagId ;

		return 0
	END
	
;
/****** Object:  StoredProcedure `sp_CadastroMaquina`    Script Date: 04/12/2020 14:04:32 ******/


CREATE PROCEDURE `sp_CadastroMaquina`
@nomeMaquina varchar(50),
@emailUsuario varchar(50),
@hashmac varchar(260),
@componentes varchar(50)

AS
BEGIN

DECLARE @fkFilial INT, @fkMaquina INT, @vetorComp VARCHAR(50)

SET @fkFilial = (SELECT fkidFilial FROM Usuario WHERE @emailUsuario = emailUsuario)

-- RETIRAR OS ESPACOS E ASPAS E VIRGULAS
SET @vetorComp = REPLACE(@componentes,'"','')
SET @vetorComp = REPLACE(@vetorComp,' ','')
-- SET @vetorComp = REPLACE(@vetorComp,',','')

INSERT INTO Maquina(descricaoMaquina,fkFilial,hashmac)
    VALUES(@nomeMaquina,@fkFilial,@hashmac)

SET @fkMaquina = (SELECT idMaquina FROM Maquina WHERE @nomeMaquina = descricaoMaquina)

INSERT INTO MaquinaComponente(fkMaquina,fkComponente)
    SELECT @fkMaquina, value FROM string_split(@vetorComp, ',')
    

SELECT @fkMaquina as 'maq', @nomeMaquina as 'nome da maquina', @fkFilial as 'filial', @componentes as 'MaqComps'


END

;
/****** Object:  StoredProcedure `sp_creatediagram`    Script Date: 04/12/2020 14:04:32 ******/



	CREATE PROCEDURE `sp_creatediagram`
	(
		@diagramname 	sysname,
		@owner_id		int	= null, 	
		@version 		int,
		@definition 	varbinary(max)
	)
	WITH EXECUTE AS 'dbo'
	AS
	BEGIN
		set nocount on
	
		declare @theId int
		declare @retval int
		declare @IsDbo	int
		declare @userName sysname
		if(@version is null or @diagramname is null)
		begin
			RAISERROR (N'E_INVALIDARG', 16, 1);
			return -1
		end
	
		execute as caller;
		select @theId = DATABASE_PRINCIPAL_ID(); 
		select @IsDbo = IS_MEMBER(N'db_owner');
		revert; 
		
		if @owner_id is null
		begin
			select @owner_id = @theId;
		end
		else
		begin
			if @theId <> @owner_id
			begin
				if @IsDbo = 0
				begin
					RAISERROR (N'E_INVALIDARG', 16, 1);
					return -1
				end
				select @theId = @owner_id
			end
		end
		-- next 2 line only for test, will be removed after define name unique
		if EXISTS(select diagram_id from dbo.sysdiagrams where principal_id = @theId and name = @diagramname)
		begin
			RAISERROR ('The name is already used.', 16, 1);
			return -2
		end
	
		insert into dbo.sysdiagrams(name, principal_id , version, definition)
				VALUES(@diagramname, @theId, @version, @definition) ;
		
		select @retval = @@IDENTITY 
		return @retval
	END
	
;
/****** Object:  StoredProcedure `sp_DadosUltimaDuasHora`    Script Date: 04/12/2020 14:04:32 ******/


CREATE PROCEDURE `sp_DadosUltimaDuasHora`
@Maquina INT,
@Comp INT

AS
BEGIN
    SELECT LeituraMaquina.leitura, Componente.nomeComponente, LeituraMaquina.dataHora
    FROM LeituraMaquina
        INNER JOIN MaquinaComponente
        on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp
        INNER JOIN Componente
        ON Componente.idComponente = MaquinaComponente.fkComponente
    WHERE dataHora >= DATEADD(HOUR, -5, GETDATE())
        AND Componente.idComponente = @Comp
        AND MaquinaComponente.fkMaquina = @Maquina
END

;
/****** Object:  StoredProcedure `sp_DadosUltimaHora`    Script Date: 04/12/2020 14:04:32 ******/


CREATE PROCEDURE `sp_DadosUltimaHora`
@Maquina INT,
@Comp INT

AS
BEGIN
    SELECT LeituraMaquina.leitura, Componente.nomeComponente, LeituraMaquina.dataHora
    FROM LeituraMaquina
        INNER JOIN MaquinaComponente
        on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp
        INNER JOIN Componente
        ON Componente.idComponente = MaquinaComponente.fkComponente
    WHERE dataHora >= DATEADD(HOUR, -4, GETDATE())
        AND Componente.idComponente = @Comp
        AND MaquinaComponente.fkMaquina = @Maquina
END

;
/****** Object:  StoredProcedure `sp_DadosUltimaSemana`    Script Date: 04/12/2020 14:04:32 ******/


CREATE PROCEDURE `sp_DadosUltimaSemana`
@Maquina INT,
@Comp INT

AS
BEGIN
    SELECT LeituraMaquina.leitura, Componente.nomeComponente, LeituraMaquina.dataHora
    FROM LeituraMaquina
        INNER JOIN MaquinaComponente
        on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp
        INNER JOIN Componente
        ON Componente.idComponente = MaquinaComponente.fkComponente
    WHERE dataHora >= DATEADD(WEEK, -1, GETDATE())
        AND Componente.idComponente = @Comp
        AND MaquinaComponente.fkMaquina = @Maquina
END

;
/****** Object:  StoredProcedure `sp_DadosUltimoDia`    Script Date: 04/12/2020 14:04:32 ******/


CREATE PROCEDURE `sp_DadosUltimoDia`
@Maquina INT,
@Comp INT

AS
BEGIN
    SELECT LeituraMaquina.leitura, Componente.nomeComponente, LeituraMaquina.dataHora
    FROM LeituraMaquina
        INNER JOIN MaquinaComponente
        on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp
        INNER JOIN Componente
        ON Componente.idComponente = MaquinaComponente.fkComponente
    WHERE dataHora >= DATEADD(DAY, -1, GETDATE())
        AND Componente.idComponente = @Comp
        AND MaquinaComponente.fkMaquina = @Maquina
END

;
/****** Object:  StoredProcedure `sp_DadosUltimoDoisDias`    Script Date: 04/12/2020 14:04:32 ******/


CREATE PROCEDURE `sp_DadosUltimoDoisDias`
@Maquina INT,
@Comp INT

AS
BEGIN
    SELECT LeituraMaquina.leitura, Componente.nomeComponente, LeituraMaquina.dataHora
    FROM LeituraMaquina
        INNER JOIN MaquinaComponente
        on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp
        INNER JOIN Componente
        ON Componente.idComponente = MaquinaComponente.fkComponente
    WHERE dataHora >= DATEADD(DAY, -2, GETDATE())
        AND Componente.idComponente = @Comp
        AND MaquinaComponente.fkMaquina = @Maquina
END

;
/****** Object:  StoredProcedure `sp_DadosUltimoMes`    Script Date: 04/12/2020 14:04:32 ******/


CREATE PROCEDURE `sp_DadosUltimoMes`
@Maquina INT,
@Comp INT

AS
BEGIN
    SELECT LeituraMaquina.leitura, Componente.nomeComponente, LeituraMaquina.dataHora
    FROM LeituraMaquina
        INNER JOIN MaquinaComponente
        on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp
        INNER JOIN Componente
        ON Componente.idComponente = MaquinaComponente.fkComponente
    WHERE dataHora >= DATEADD(MONTH, -1, GETDATE())
        AND Componente.idComponente = @Comp
        AND MaquinaComponente.fkMaquina = @Maquina
END

;
/****** Object:  StoredProcedure `sp_DadosUltimosQuacDias`    Script Date: 04/12/2020 14:04:32 ******/


CREATE PROCEDURE `sp_DadosUltimosQuacDias`
@Maquina INT,
@Comp INT

AS
BEGIN
    SELECT LeituraMaquina.leitura, Componente.nomeComponente, LeituraMaquina.dataHora
    FROM LeituraMaquina
        INNER JOIN MaquinaComponente
        on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp
        INNER JOIN Componente
        ON Componente.idComponente = MaquinaComponente.fkComponente
    WHERE dataHora >= DATEADD(DAY, -14, GETDATE())
        AND Componente.idComponente = @Comp
        AND MaquinaComponente.fkMaquina = @Maquina
END

;
/****** Object:  StoredProcedure `sp_dropdiagram`    Script Date: 04/12/2020 14:04:32 ******/



	CREATE PROCEDURE `sp_dropdiagram`
	(
		@diagramname 	sysname,
		@owner_id	int	= null
	)
	WITH EXECUTE AS 'dbo'
	AS
	BEGIN
		set nocount on
		declare @theId 			int
		declare @IsDbo 			int
		
		declare @UIDFound 		int
		declare @DiagId			int
	
		if(@diagramname is null)
		begin
			RAISERROR ('Invalid value', 16, 1);
			return -1
		end
	
		EXECUTE AS CALLER;
		select @theId = DATABASE_PRINCIPAL_ID();
		select @IsDbo = IS_MEMBER(N'db_owner'); 
		if(@owner_id is null)
			select @owner_id = @theId;
		REVERT; 
		
		select @DiagId = diagram_id, @UIDFound = principal_id from dbo.sysdiagrams where principal_id = @owner_id and name = @diagramname 
		if(@DiagId IS NULL or (@IsDbo = 0 and @UIDFound <> @theId))
		begin
			RAISERROR ('Diagram does not exist or you do not have permission.', 16, 1)
			return -3
		end
	
		delete from dbo.sysdiagrams where diagram_id = @DiagId;
	
		return 0;
	END
	
;
/****** Object:  StoredProcedure `sp_helpdiagramdefinition`    Script Date: 04/12/2020 14:04:32 ******/



	CREATE PROCEDURE `sp_helpdiagramdefinition`
	(
		@diagramname 	sysname,
		@owner_id	int	= null 		
	)
	WITH EXECUTE AS N'dbo'
	AS
	BEGIN
		set nocount on

		declare @theId 		int
		declare @IsDbo 		int
		declare @DiagId		int
		declare @UIDFound	int
	
		if(@diagramname is null)
		begin
			RAISERROR (N'E_INVALIDARG', 16, 1);
			return -1
		end
	
		execute as caller;
		select @theId = DATABASE_PRINCIPAL_ID();
		select @IsDbo = IS_MEMBER(N'db_owner');
		if(@owner_id is null)
			select @owner_id = @theId;
		revert; 
	
		select @DiagId = diagram_id, @UIDFound = principal_id from dbo.sysdiagrams where principal_id = @owner_id and name = @diagramname;
		if(@DiagId IS NULL or (@IsDbo = 0 and @UIDFound <> @theId ))
		begin
			RAISERROR ('Diagram does not exist or you do not have permission.', 16, 1);
			return -3
		end

		select version, definition FROM dbo.sysdiagrams where diagram_id = @DiagId ; 
		return 0
	END
	
;
/****** Object:  StoredProcedure `sp_helpdiagrams`    Script Date: 04/12/2020 14:04:32 ******/



	CREATE PROCEDURE `sp_helpdiagrams`
	(
		@diagramname sysname = NULL,
		@owner_id int = NULL
	)
	WITH EXECUTE AS N'dbo'
	AS
	BEGIN
		DECLARE @user sysname
		DECLARE @dboLogin bit
		EXECUTE AS CALLER;
			SET @user = USER_NAME();
			SET @dboLogin = CONVERT(bit,IS_MEMBER('db_owner'));
		REVERT;
		SELECT
			`Database` = DB_NAME(),
			`Name` = name,
			`ID` = diagram_id,
			`Owner` = USER_NAME(principal_id),
			`OwnerID` = principal_id
		FROM
			sysdiagrams
		WHERE
			(@dboLogin = 1 OR USER_NAME(principal_id) = @user) AND
			(@diagramname IS NULL OR name = @diagramname) AND
			(@owner_id IS NULL OR principal_id = @owner_id)
		ORDER BY
			4, 5, 1
	END
	
;
/****** Object:  StoredProcedure `sp_NovoUsuario`    Script Date: 04/12/2020 14:04:32 ******/


CREATE PROCEDURE `sp_NovoUsuario`
@nomeMercado varchar(50),
@cep CHAR(8),
@numero INT,
@nome  VARCHAR(50),
@email VARCHAR(50),
@senha VARCHAR(50)

AS
BEGIN

DECLARE @fkidmercado int, @fkfilial int

SET @fkidmercado = (SELECT idSupermercado FROM Supermercado WHERE nome = @nomeMercado);

SET @fkfilial = (SELECT TOP(1) idFilial FROM Filial ORDER BY idFilial DESC)+1;

    INSERT INTO Filial(fkSupermercado,cep,numero)
        VALUES(@fkidmercado, @cep, @numero)
    INSERT INTO Usuario(emailUsuario, senhaUsuario, nomeUsuario, fkIdFilial)
        VALUES(@email, @senha, @nome, @fkfilial)

    SELECT @cep as 'cep', @numero as 'numero', @nome as 'nomeUSuario', @email as 'email'

END
;
/****** Object:  StoredProcedure `sp_renamediagram`    Script Date: 04/12/2020 14:04:32 ******/



	CREATE PROCEDURE `sp_renamediagram`
	(
		@diagramname 		sysname,
		@owner_id		int	= null,
		@new_diagramname	sysname
	
	)
	WITH EXECUTE AS 'dbo'
	AS
	BEGIN
		set nocount on
		declare @theId 			int
		declare @IsDbo 			int
		
		declare @UIDFound 		int
		declare @DiagId			int
		declare @DiagIdTarg		int
		declare @u_name			sysname
		if((@diagramname is null) or (@new_diagramname is null))
		begin
			RAISERROR ('Invalid value', 16, 1);
			return -1
		end
	
		EXECUTE AS CALLER;
		select @theId = DATABASE_PRINCIPAL_ID();
		select @IsDbo = IS_MEMBER(N'db_owner'); 
		if(@owner_id is null)
			select @owner_id = @theId;
		REVERT;
	
		select @u_name = USER_NAME(@owner_id)
	
		select @DiagId = diagram_id, @UIDFound = principal_id from dbo.sysdiagrams where principal_id = @owner_id and name = @diagramname 
		if(@DiagId IS NULL or (@IsDbo = 0 and @UIDFound <> @theId))
		begin
			RAISERROR ('Diagram does not exist or you do not have permission.', 16, 1)
			return -3
		end
	
		-- if((@u_name is not null) and (@new_diagramname = @diagramname))	-- nothing will change
		--	return 0;
	
		if(@u_name is null)
			select @DiagIdTarg = diagram_id from dbo.sysdiagrams where principal_id = @theId and name = @new_diagramname
		else
			select @DiagIdTarg = diagram_id from dbo.sysdiagrams where principal_id = @owner_id and name = @new_diagramname
	
		if((@DiagIdTarg is not null) and  @DiagId <> @DiagIdTarg)
		begin
			RAISERROR ('The name is already used.', 16, 1);
			return -2
		end		
	
		if(@u_name is null)
			update dbo.sysdiagrams set `name` = @new_diagramname, principal_id = @theId where diagram_id = @DiagId
		else
			update dbo.sysdiagrams set `name` = @new_diagramname where diagram_id = @DiagId
		return 0
	END
	
;
/****** Object:  StoredProcedure `sp_upgraddiagrams`    Script Date: 04/12/2020 14:04:32 ******/



	CREATE PROCEDURE `sp_upgraddiagrams`
	AS
	BEGIN
		IF OBJECT_ID(N'dbo.sysdiagrams') IS NOT NULL
			return 0;
	
		CREATE TABLE dbo.sysdiagrams
		(
			name sysname NOT NULL,
			principal_id int NOT NULL,	-- we may change it to varbinary(85)
			diagram_id int PRIMARY KEY IDENTITY,
			version int,
	
			definition varbinary(max)
			CONSTRAINT UK_principal_name UNIQUE
			(
				principal_id,
				name
			)
		);


		/* Add this if we need to have some form of extended properties for diagrams */
		/*
		IF OBJECT_ID(N'dbo.sysdiagram_properties') IS NULL
		BEGIN
			CREATE TABLE dbo.sysdiagram_properties
			(
				diagram_id int,
				name sysname,
				value varbinary(max) NOT NULL
			)
		END
		*/

		IF OBJECT_ID(N'dbo.dtproperties') IS NOT NULL
		begin
			insert into dbo.sysdiagrams
			(
				`name`,
				`principal_id`,
				`version`,
				`definition`
			)
			select	 
				convert(sysname, dgnm.`uvalue`),
				DATABASE_PRINCIPAL_ID(N'dbo'),			-- will change to the sid of sa
				0,							-- zero for old format, dgdef.`version`,
				dgdef.`lvalue`
			from dbo.`dtproperties` dgnm
				inner join dbo.`dtproperties` dggd on dggd.`property` = 'DtgSchemaGUID' and dggd.`objectid` = dgnm.`objectid`	
				inner join dbo.`dtproperties` dgdef on dgdef.`property` = 'DtgSchemaDATA' and dgdef.`objectid` = dgnm.`objectid`
				
			where dgnm.`property` = 'DtgSchemaNAME' and dggd.`uvalue` like N'_EA3E6268-D998-11CE-9454-00AA00A3F36E_' 
			return 2;
		end
		return 1;
	END
	
;
EXEC sys.sp_addextendedproperty @name=N'microsoft_database_tools_support', @value=1 , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'sysdiagrams'
;
ALTER DATABASE `bdProjetoSensiders` SET  READ_WRITE 
;
