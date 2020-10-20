from sqlAzure import Sql
#from services.dataGenerator import getData
from HashingMacAddress import readHashMAC
import analiseHardware
import time

#Inserir user, password, port , database, server
sql = Sql('adminlocal','#Gfgrupo11c', '1433', 'bdProjetoSensiders', 'serversensiders.database.windows.net')

sql.connect() # realiza conexão com o BD

""" (TODO: fazer integração com criptografia do endereço MAC?) ->>> """
maquina = readHashMAC()
maquina = 3 # define ID da máquina para realizar select dos componentes em uso
componentes = sql.selectComp(maquina) # realiza select dos componentes em uso da maquina
analiseHardware.enviarMensagemSlack("Iniciando leituras na Máquina: " + str(maquina))

while True:
    dados = analiseHardware.inserirComponentes(componentes, maquina) # com estes componentes, monitora-os pegando seus valores e inserindo-os no banco
    for dado in dados: # loop sequencial dos componentes
        sql.newInsert(dado) # insere os valores dos componentes no banco de dados

    time.sleep(1) # espera 1 segundo para a proxima linha ser executada
