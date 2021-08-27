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


Go;

Select idMaqComp,
Substring(fkComponente, 9999, CHARINDEX(',', fkComponente + ',', 9999)-9999) As Comp
from  A Join dbo.Numeracao N
        On N.Numero <= DATALENGTH(A.Elementos) + 1
        And SUBSTRING(‘,’ + A.Elementos, Numero, 1) = ‘,’

BEGIN TRANSACTION;
Create Table Numeracao
(Numero Int Not Null Primary Key) ;
Go
Declare @ValorMaximo Int,
@Contador Int;
Set @ValorMaximo=100;
Set @Contador=1;
Insert Into dbo.Numeracao Values(1)
While @Contador * 2 <= @ValorMaximo
 Begin
   Insert Into dbo.Numeracao
   Select Numero+@Contador from dbo.Numeracao;
   Set @Contador *= 2;       
 End
 select * from Numeracao;

DECLARE @A varchar(50)
SET @A = (select idComponente from Componente where '2' = idComponente)
Select A.fkMaquina,
Substring(@A, N.Numero, CHARINDEX(',', @A + ',', N.Numero)- N.Numero) As Comp
from MaquinaComponente A Join Numeracao N
        On N.Numero <= DATALENGTH(@A) + 1
        And SUBSTRING(',' + @A, Numero, 1) = ','
        WHERE A.fkMaquina = '2'
        
DECLARE @A varchar(50), @B int
SET @A = '1,2,3'
Insert Into MaquinaComponente(fkMaquina,fkComponente)
Select A.fkMaquina,
Substring(@A, N.Numero, CHARINDEX(',', @A + ',', N.Numero)- N.Numero) As Comp
from MaquinaComponente A Join Numeracao N
        On N.Numero <= DATALENGTH(@A) + 1
        And SUBSTRING(',' + @A, Numero, 1) = ','

DECLARE @A varchar(50), @B INT
SET @A = '1,2,3,4'
SET @B = '2'
INSERT INTO MaquinaComponente(fkMaquina, fkComponente)
SELECT [value] FROM STRING_SPLIT(@A, ',');

CREATE PROCEDURE sp_TesteCad
@FKMID int,
@COMP VARCHAR(MAX)=NULL

AS
BEGIN

 INSERT INTO MaquinaComponente(fkMaquina,fkComponente)
    SELECT @FKMID, value FROM string_split(@COMP, ',')
 
END
GO

sp_TesteCad 2, '7,8'
SELECT * FROM MaquinaComponente
ROLLBACK;






-- '"jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dEZ"
-- ENVIAR COMO MATRIZ

CREATE PROCEDURE sp_CadastroMaquina
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
GO

drop PROCEDURE sp_CadastroMaquina

-- como enviar?
-- para os componentes envie: '1','1','1','1','1'
-- tanto faz se tiver aspas duplas ou espaços, o procedimento tira
-- mas envie como matriz
Exec sp_CadastroMaquina 'maquina caixa','patrick@outlook.com','hashmachere','7,8,9'
