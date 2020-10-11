import psutil, time, sys, json, requests, os

def gerarTemperatura():
    try:
        dados = (requests.get("http://localhost:9000/data.json",auth=("user","pass"))).json()["Children"][0]["Children"][1]["Children"][1]["Children"]
        for d in range(len(dados)):
            if "CPU Package" in dados[d]["Text"]:
                temperatura = int((dados[d]["Value"])[:-5])
        return (temperatura)
    except:
        print("\nERROR:\nLigue o Open Hardware Monitor na porta 9000 para receber Temperaturas no Windows\n")
        enviarMensagemSlack("Ligue o Open Hardware Monitor para receber Temperaturas!")
        return 0

def getCPU():
    valCPU = psutil.cpu_percent() # percentual de CPU
    return valCPU

def getRAM():
    valRAM = psutil.virtual_memory()[2] # percentual de RAM
    return valRAM

def getHD():
    valHD = psutil.disk_usage('/')[3] # percentual de ocupação HD na raiz
    return valHD

def getDownloadAndUpload():
    oldDownload = psutil.net_io_counters()[1] # pega os dados de download antes de 1s
    oldUpload = psutil.net_io_counters()[0]
    time.sleep(1) # espera 1s para o calculo KiB/s
    newDownload = psutil.net_io_counters()[1] # pega os dados de download depois de 1s
    newUpload = psutil.net_io_counters()[0]

    # assim realiza o calculo do novo - antigo para saber o uso durante o 1s
    valDownload = round((newDownload - oldDownload) / (2**10)) # KiB/s Download
    valUpload = round((newUpload - oldUpload) / (2**10)) # KiB/s Upload

    return (valDownload, valUpload)

def getTemp():
    if sys.platform == 'linux': # se o OS for linux
        if not "Microsoft" in os.uname(): # se NAO for WSL
            dadosTemp = psutil.sensors_temperatures(fahrenheit=False)
            if bool(dadosTemp): # se estiver em linux nativo
                tempCPU = dadosTemp.get('coretemp')[0][1] # temperatura CPU (celsius)
            else: # se estiver em linux VM (ex: virtualBox)
                tempCPU = 0 # (TODO: deixamos como 0 enquanto OHM não conseguir pegar pela VM)
        else: # se for WSL
            tempCPU = gerarTemperatura()
    elif sys.platform == 'win32': # se OS for Windows
        tempCPU = gerarTemperatura()

    return tempCPU

def getSWAP():
    valSWAP = psutil.swap_memory()[3] # percentual de SWAP
    return valSWAP

def getTASKS():
    valTASKS = len(psutil.pids()) # quantidade de tarefas/processos em execução
    return valTASKS

"""
def dadosHardware():
    valNET = getDownloadAndUpload()

    valDownload = valNET[0]
    valUpload = valNET[1]
    valCPU = getCPU()
    valRAM = getRAM()
    valHD = getHD()
    tempCPU = getTemp()    
    valSWAP = getSWAP()
    valTASKS = getTASKS()

    maquina = 1

    t = time.localtime()
    valTEMPO = ('{}-{}-{} {}:{}:{}'.format(t[0], t[1], t[2], t[3], t[4], t[5]))

    hardware = {
    'cpu': valCPU,
    'memory': valRAM,
    'disk': valHD,
    'download': valDownload,
    'upload': valUpload,
    'temp': tempCPU,
    'swap': valSWAP,
    'tasks': valTASKS, 
    'maquina': maquina
    }
    print(hardware)

    dadosHW = (valCPU, valRAM, valHD, valDownload, valUpload, tempCPU, valSWAP, valTASKS, maquina, valTEMPO)
    return [dadosHW, hardware]
"""

def inserirComponentes(componentes, valMaquina):

    hardware = { # define dicionario (JSON) para analisar no SLACK os alertas & também visualização dos dados no terminal
    'cpu': 0,
    'memory': 0,
    'disk': 0,
    'download': 0,
    'upload': 0,
    'temp': 0,
    'swap': 0,
    'tasks': 0, 
    'maquina': valMaquina
    }

    valNET = getDownloadAndUpload() # pega os valores de Rede (executa aqui porque demora 1 segundo para poder realizar o calculo de KiB/s)

    t = time.localtime() # pega o tempo de agora
    valTEMPO = ('{}-{}-{} {}:{}:{}'.format(t[0], t[1], t[2], t[3], t[4], t[5])) # converte as medidas para inserção no banco

    dados = [] # inicia array dos dados

    for componente in componentes: # para cada componente em uso
        if 'CPU' in componente[0]: # se for CPU
            CPU = getCPU() # pega o valor do uso de CPU
            hardware['cpu'] = CPU # coloca no dicionario o valor
            dados.append((CPU, valTEMPO, componente[1])) # concatena os dados de CPU para a inserção no banco (utiliza "componente[1]" porque é o id do componente em uso)
        elif 'RAM' in componente[0]:
            RAM = getRAM()
            hardware['memory'] = RAM
            dados.append((RAM, valTEMPO, componente[1]))
        elif 'HD' in componente[0]:
            HD = getHD()
            hardware['disk'] = HD
            dados.append((HD, valTEMPO, componente[1]))
        elif 'DOWNLOAD' in componente[0]:
            DOWNLOAD = valNET[0]
            hardware['download'] = DOWNLOAD
            dados.append((DOWNLOAD, valTEMPO, componente[1]))
        elif 'UPLOAD' in componente[0]:
            UPLOAD = valNET[1]
            hardware['upload'] = UPLOAD
            dados.append((UPLOAD, valTEMPO, componente[1]))
        elif 'TEMPERATURA' in componente[0]:
            TEMPERATURA = getTemp()
            hardware['temp'] = TEMPERATURA
            dados.append((TEMPERATURA, valTEMPO, componente[1]))
        elif 'SWAP' in componente[0]:
            SWAP = getSWAP()
            hardware['swap'] = SWAP
            dados.append((SWAP, valTEMPO, componente[1]))
        elif 'TASKS' in componente[0]:
            TASKS = getTASKS()
            hardware['tasks'] = TASKS
            dados.append((TASKS, valTEMPO, componente[1]))

    print(hardware)
    print(alertarSlack(hardware))
    return dados
    
def alertarSlack(valores):
    if (valores['cpu'] >= 65) or (valores['memory'] >= 60) or (valores['disk'] >= 70) or (valores['download'] >= 3000) or (valores['upload'] >= 1000) or (valores['temp'] >= 60) or (valores['swap'] >= 50) or (valores['tasks'] >= 400):
        condicao = ''
        if valores['cpu'] >= 65:
            condicao += "CPU em alto uso, "
        if valores['memory'] >= 60:
            condicao += "RAM em alto uso, "
        if valores['disk'] >= 70:
            condicao += "HD em alto uso, "
        if valores['download'] >= 3000:
            condicao += "Download em alto uso, "
        if valores['upload'] >= 1000:
            condicao += "Upload em alto uso, "
        if valores['temp'] >= 60:
            condicao += "Temperatura alta, "
        if valores['swap'] >= 50:
            condicao += "SWAP em alto uso, "
        if valores['tasks'] >= 400:
            condicao += "Muitas tarefas em uso, "

        condicao = condicao[0:-2] + '.'
        enviarMensagemSlack(condicao)
        return condicao
    else:
        return "Hardware OK!"

def enviarMensagemSlack(mensagem):
    url = '' # canal do Slack
    pload = {'text': mensagem}
    try:
        requests.post(url, json = pload)
    except:
        print("\nERRO no Slack! (URL)\n")
