SELECT * FROM Maquina;
SELECT * FROM MaquinaComponente;
SELECT * FROM Componente;
SELECT * FROM Filial;
SELECT * FROM Supermercado;
SELECT * FROM Usuario;

SELECT fkidFilial FROM Usuario WHERE 'asdaw' = emailUsuario;
SELECT idMaquina FROM Maquina WHERE 'caixa 1' = descricaoMaquina;

DECLARE @A varchar(50)
SET @A = '1,2'
SELECT * FROM [dbo].[fnStringToArray] (@A, ',') 

SELECT nomeComponente FROM Componente WHERE idComponente IN (@A)

SELECT nomeComponente FROM Componente WHERE idComponente IN (
SELECT idComponente FROM [dbo].[fnStringToArray] (@A, ','))
SET @A = REPLACE(@A,'"','')
SET @A = REPLACE(@A,' ','')
SET @A = REPLACE(@A,',','')

SELECT @A;

-- function
CREATE FUNCTION [dbo].[fnStringToArray] (@String VARCHAR(1000), @Separador CHAR(1))
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








-- '"jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dEZ"
-- ENVIAR COMO MATRIZ
CREATE PROCEDURE sp_CadastroMaquina
@nomeMaquina varchar(50),
@emailUsuario varchar(50),
@hashmac varchar(260),
@componentes varchar(50),

AS
BEGIN

DECLARE @fkFilial INT, @fkMaquina INT, @vetorComp VARCHAR(50), @I INT, @comp INT

SET @fkFilial = (SELECT fkidFilial FROM Usuario WHERE @emailUsuario = emailUsuario)
SET @fkMaquina = (SELECT idMaquina FROM Maquina WHERE @nomeMaquina = descricaoMaquina)
-- RETIRAR OS ESPACOS E ASPAS E VIRGULAS
SET @vetorComp = REPLACE(@componentes,'"','')
SET @vetorComp = REPLACE(@vetorComp,' ','')
SET @vetorComp = REPLACE(@vetorComp,',','')



INSERT INTO Maquina(descricaoMaquina,fkFilial,hashmac)
    VALUES(@nomeMaquina,@fkFilial,@hashmac)

SET @I = 0
WHILE @I < LEN(@vetorComp)
BEGIN
    SET @I += 1;
    SET @comp = (SELECT idComponente FROM Componente WHERE @I = idComponente)

    INSERT INTO MaquinaComponente(fkMaquina,fkMaquina)
        VALUES(@fkMaquina,)
END

SELECT


END
GO

