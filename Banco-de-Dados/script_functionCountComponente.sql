create function fc_returnCountComponente(@maquina int)
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

