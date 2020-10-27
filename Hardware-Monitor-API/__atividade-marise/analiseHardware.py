import psutil, time, sys, json, requests, os

def gerarTemperatura():
    try:
        dados = (requests.get("http://localhost:9000/data.json",auth=("user","pass"))).json()["Children"][0]["Children"][1]["Children"]
        dados_temp = dados[1]["Children"]
        dados_clock = dados[0]["Children"]
        clock = 0
        qtdNucleos = 0
        for c in range(len(dados_clock)):
            if "CPU Core" in dados_clock[c]["Text"]:
                qtdNucleos += 1
                actual_clock = ''
                for letra in  dados_clock[c]["Value"]:
                    if letra == ',':
                        break
                    else:
                        actual_clock += letra
                        
                clock += int(actual_clock)

        for d in range(len(dados_temp)):
            if "CPU Package" in dados_temp[d]["Text"]:
                temperatura = int((dados_temp[d]["Value"])[:-5])

        clock = clock / qtdNucleos

        return (temperatura, clock)
    except:
        print('ligue o ohm')
        return (0,0)


def dadosHardware():
    oldDownload = psutil.net_io_counters()[1]
    oldUpload = psutil.net_io_counters()[0]
    time.sleep(1)
    valCPU = psutil.cpu_percent() # percentual de CPU
    valRAM = psutil.virtual_memory()[2] # percentual de RAM
    if sys.platform == 'linux':
        valHD = psutil.disk_usage('/')[3] # percentual de ocupação HD
    elif sys.platform == 'win32':
        valHD = psutil.disk_usage('C://')[3] # percentual de ocupação HD
    newDownload = psutil.net_io_counters()[1] 
    newUpload = psutil.net_io_counters()[0]
    valDownload = round((newDownload - oldDownload) / (2**10)) # KB/s Download
    valUpload = round((newUpload - oldUpload) / (2**10)) # KB/s Upload
    oldDownload = newDownload
    oldUpload = newUpload

    if sys.platform == 'linux':
        if "Microsoft" in os.uname()[2]:
            dados_ohm = gerarTemperatura()
            tempCPU = dados_ohm[0]
            valCLOCK = dados_ohm[1]
        else:
            tempCPU = psutil.sensors_temperatures(fahrenheit=False).get('coretemp')[0][1] # temperatura CPU (celsius)
            valCLOCK = psutil.cpu_freq()[0]
    elif sys.platform == 'win32':
        dados_ohm = gerarTemperatura()
        tempCPU = dados_ohm[0]
        valCLOCK = dados_ohm[1]


    valSWAP = psutil.swap_memory()[3] # percentual de SWAP
    valTASKS = len(psutil.pids()) # quantidade de tarefas em execução

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
    'clock': valCLOCK,
    'time': valTEMPO
    }
    print(hardware)

    dadosHW = (valCPU, valRAM, valHD, valDownload, valUpload, tempCPU, valSWAP, valTASKS, valCLOCK, valTEMPO)
    return dadosHW

"""   
def alertarSlack(valores):
    url = 'https://hooks.slack.com/services/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' # canal do Slack

    if (valores[0] >= 65) or (valores[1] >= 60) or (valores[2] >= 70) or (valores[3] >= 3000) or (valores[4] >= 1000) or (valores[5] >= 60) or (valores[6] >= 50) or (valores[7] >= 400):
        condicao = ''
        if valores[0] >= 65:
            condicao += "CPU em alto uso, "
        if valores[1] >= 60:
            condicao += "RAM em alto uso, "
        if valores[2] >= 70:
            condicao += "HD em alto uso, "
        if valores[3] >= 3000:
            condicao += "Download em alto uso, "
        if valores[4] >= 1000:
            condicao += "Upload em alto uso, "
        if valores[5] >= 60:
            condicao += "Temperatura alta, "
        if valores[6] >= 50:
            condicao += "SWAP em alto uso, "
        if valores[7] >= 400:
            condicao += "Muitas tarefas em uso, "

        condicao = condicao[0:-2] + '.'
        pload = {'text': condicao}
        requests.post(url, json = pload)
        return condicao
    else:
        return "Hardware OK!"
"""
