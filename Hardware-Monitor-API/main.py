from services.mysql import Mysql
#from services.dataGenerator import getData
import analiseHardware
import time

#Inserir user, password, host, database
mysql = Mysql('marise','123mysql@', 'localhost', 'projeto')

mysql.connect()

while True:
    valoresHW = analiseHardware.dadosHardware()
    Slack = analiseHardware.alertarSlack(valoresHW)
    print(Slack)
    mysql.insert(valoresHW)
    time.sleep(1)