import psutil, time, sys, json, requests, os

def gerarTemperatura():
    dados = (requests.get("http://localhost:9000/data.json",auth=("user","pass"))).json()["Children"][0]["Children"][1]["Children"][1]["Children"]
    for d in range(len(dados)):
        if "CPU Package" in dados[d]["Text"]:
            temperatura = int((dados[d]["Value"])[:-5])

    return (temperatura)


def dadosHardware():
    oldDownload = psutil.net_io_counters()[1]
    oldUpload = psutil.net_io_counters()[0]
    time.sleep(1)
    valCPU = psutil.cpu_percent() # percentual de CPU
    valRAM = psutil.virtual_memory()[2] # percentual de RAM
    valHD = psutil.disk_usage('/')[3] # percentual de ocupação HD

    newDownload = psutil.net_io_counters()[1] 
    newUpload = psutil.net_io_counters()[0]
    valDownload = round((newDownload - oldDownload) / (2**10)) # KB/s Download
    valUpload = round((newUpload - oldUpload) / (2**10)) # KB/s Upload
    oldDownload = newDownload
    oldUpload = newUpload
    maquina = 1

    if sys.platform == 'linux':
        if not "Microsoft" in os.uname():
            tempCPU = psutil.sensors_temperatures(fahrenheit=False).get('coretemp')[0][1] # temperatura CPU (celsius)
        else:
            tempCPU = 0
    else if sys.platform == 'win32':
        tempCPU = gerarTemperatura()
    valSWAP = psutil.swap_memory()[3] # percentual de SWAP
    valTASKS = len(psutil.pids()) # quantidade de tarefas em execução

    hardware = {
    'cpu': valCPU,
    'memory': valRAM,
    'disk': valHD,
    'download': valDownload,
    'upload': valUpload,
    'temp': tempCPU,
    'swap': valSWAP,
    'tasks': valTASKS, 
    'maquina': 1
    }
    print(hardware)

    dadosHW = (valCPU, valRAM, valHD, valDownload, valUpload, tempCPU, valSWAP, valTASKS, maquina)
    return dadosHW
    
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

if __name__ == '__main__':
    while True:
        valores = dadosHardware()
        condicoes = alertarSlack(valores)
        print(condicoes)