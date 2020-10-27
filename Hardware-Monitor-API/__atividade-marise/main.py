from services.mysqLocal import MySQL
#from services.dataGenerator import getData
import analiseHardware
import time

#Inserir user, password, host, database
mysql = MySQL('felipe', '123mysql@', 'localhost', 'projeto')

mysql.connect()

cont = 0
total_hw = []
while True:
    cont += 1
    print('segundo: ' + str(cont))
    valoresHW = analiseHardware.dadosHardware()
    if cont == 1:
        for val in range(len(valoresHW)):
            total_hw.append(valoresHW[val])
    else:
        for val in range(len(valoresHW)):
            if val != 9:
                total_hw[val] += (valoresHW[val])
    if cont % 5 == 0:
        media_hw = []
        for val in range(len(total_hw)):
            if val != 9:
                media_hw.append(round((total_hw[val] / cont),1))
        media_hw.append(total_hw[9])
        print('\nmédia nos 5 segundos:', media_hw)
        print('\n', end='')
        total_hw = []
        cont = 0
        mysql.insert(tuple(media_hw))
    # Slack = analiseHardware.alertarSlack(valoresHW)
    # print(Slack)
    #time.sleep(1)