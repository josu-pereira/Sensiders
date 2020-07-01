SELECT * FROM Filial;
SELECT * FROM Supermercado;
SELECT * FROM Usuario;

INSERT INTO table4 ( name, age, sex, city, id, number, nationality)
SELECT name, age, sex, city, p.id, number, n.nationality
FROM table1 p
INNER JOIN table2 c ON c.Id = p.Id
INNER JOIN table3 n ON p.Id = n.Id

insert into Supermercado(nome, fkSupermercado, cep, numero, emailUsuario, senhaUsuario, nomeUsuario, fkFilial)
    select fkSupermercado, cep, numero, emailUsuario,
             senhaUsuario, nomeUsuario, fkFilial
        from Filial
        values('Dia','3','02235001','1231','ale@ale.com','q1w2e3r4','Gerente ale','5')
        inner join Filial on  Filial.fkSupermercado = Supermercado.idSupermercado
        inner join Usuario on Usuario.fkIdFilial = Filial.idFilial

SELECT TOP(1) idFilial FROM Filial ORDER BY idFilial DESC;
SELECT TOP(1) idSupermercado FROM Supermercado ORDER BY idSupermercado DESC;
SELECT idSupermercado FROM Supermercado WHERE nome = 'Sonda';

CREATE PROCEDURE sp_NovoUsuario
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
GO

drop PROCEDURE sp_NovoUsuario

sp_NovoUsuario 'Sonda', '876541320', 987, 'Gerente Ygor','igor@carlos.com','q1w2e3r4t5';

sp_help Setor;