from services.sqlAzure import Sql
#from services.dataGenerator import getData
import analiseHardware
import time

#Inserir user, password, port, database, server
sql = Sql('USER','PASSWORD', '1433', 'DATABSE ', 'SERVEr')

sql.connect()

while True:
    valoresHW = analiseHardware.dadosHardware()
    Slack = analiseHardware.alertarSlack(valoresHW)
    print(Slack)
    sql.insert(valoresHW)
    time.sleep(1)