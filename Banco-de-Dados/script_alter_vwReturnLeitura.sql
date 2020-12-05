alter view vw_returnLeitura as
    select idLeituraMaquina as id, leitura as leitura, Componente.nomeComponente as nome_componente, Maquina.idMaquina as idMaquina from LeituraMaquina
        inner join MaquinaComponente 
        on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp
            inner join Maquina 
            on Maquina.idMaquina = MaquinaComponente.fkMaquina
                inner join Componente 
                on Componente.idComponente = MaquinaComponente.fkComponente