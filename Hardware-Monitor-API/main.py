from sqlAzure import Sql
#from services.dataGenerator import getData
import analiseHardware
import time

#Inserir user, password, port , database, server
sql = Sql('adminlocal','#Gfgrupo11c', '1433', 'bdProjetoSensiders', 'serversensiders.database.windows.net')

sql.connect() # realiza conexão com o BD

maquina = 2 # define ID da máquina para realizar select dos componentes em uso (TODO: fazer integração com criptografia do endereço MAC?)
componentes = sql.selectComp(maquina) # realiza select dos componentes em uso da maquina
analiseHardware.enviarMensagemSlack("Iniciando leituras na Máquina: " + str(maquina))

while True:
    dados = analiseHardware.inserirComponentes(componentes, maquina) # com estes componentes, monitora-os pegando seus valores e inserindo-os no banco
    for dado in dados: # loop sequencial dos componentes
        sql.newInsert(dado) # insere os valores dos componentes no banco de dados
    
    """valoresHW = analiseHardware.dadosHardware()
    Slack = analiseHardware.alertarSlack(valoresHW[1])
    print(Slack)"""
    time.sleep(1) # espera 1 segundo para a proxima linha ser executada