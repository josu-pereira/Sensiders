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

maquina = readHashMAC() # lê o o hashmac da máquina que rodar o programa
#maquina = 3 # define ID da máquina para realizar select dos componentes em uso
componentes = sql.selectComp(maquina) # realiza select dos componentes em uso da maquina
# componentes_mysql = mysql.selectComp(maquina)
analiseHardware.enviarMensagemSlack("Iniciando leituras na Máquina: " + str(maquina))

while True:
    dados = analiseHardware.inserirComponentes(componentes, maquina) # com estes componentes, monitora-os pegando seus valores e inserindo-os no banco
    for dado in dados: # loop sequencial dos componentes
        sql.newInsert(dado) # insere os valores dos componentes no banco de dados
        # mysql.newInsert(dado)

    time.sleep(1) # espera 1 segundo para a proxima linha ser executada
