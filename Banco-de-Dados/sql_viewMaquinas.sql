create view vwListaMaquinas as 
    select idMaquina, descricaoMaquina, fkFilial as 'fkFilial', hashmac from Maquina
        inner join Filial 
        on Filial.idFilial = Maquina.fkFilial
        