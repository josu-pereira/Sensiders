Create Function fc_returnLeitura(@filial INT, @componente INT, @maquina INT)
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
                    
