from sqlAzure import Sql as Azure
from mysqlConnection import Sql as Mysql
from HashingMacAddress import readHashMAC
import analiseHardware
import time

#Inserir user, password, port , database, server
sql = Azure('adminlocal','#Gfgrupo11c', '1433', 'bdProjetoSensiders', 'serversensiders.database.windows.net')
mysql = Mysql('root','urubu100', 'bdProjetoSensiders', '3.93.53.111')

sql.connect() # realiza conexão com o BD
mysql.connect()

maquina_hash = readHashMAC() # lê o o hashmac da máquina que rodar o programa
componentes = sql.selectComp(maquina_hash) # realiza select dos componentes em uso da maquina
componentes_mysql = mysql.selectComp(maquina_hash)
maquina = sql.select_machine_name(maquina_hash)[0][0]
maquina_mysql = mysql.select_machine_name(maquina_hash)[0][0]

assert maquina == maquina_mysql, "Nomes das máquinas diferentes entre os bancos Azure e MySQL."
assert len(componentes) == len(componentes_mysql), "Componentes diferentes entre os bancos Azure e MySQL."

print("\nIniciando leituras na Máquina:", maquina)
time.sleep(0.5)
msg = ""
for i in componentes:
    msg += str(i[0]) + ", "
msg = msg[:-2]
print("Componentes em Uso:", msg)

time.sleep(1)
analiseHardware.enviarMensagemSlack("Iniciando leituras na Máquina: " + str(maquina))

while True:
    dados = analiseHardware.inserirComponentes(componentes, maquina) # com estes componentes, monitora-os pegando seus valores e inserindo-os no banco
    sql.multi_insert(dados) # insere os valores dos componentes no Azure
    mysql.multi_insert(dados) # insere os valores dos componentes no MySQL

    time.sleep(1) # espera 1 segundo para a proxima linha ser executada
