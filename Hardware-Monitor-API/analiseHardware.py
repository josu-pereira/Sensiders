import time, json, requests
from mensagemSlack import enviarMensagemSlack
import geradorDados

def inserirComponentes(componentes, valMaquina):

    hardware = { # define dicionario (JSON) para analisar no SLACK os alertas & também visualização dos dados no terminal
    'cpu': 0,
    'memory': 0,
    'disk': 0,
    'download': 0,
    'upload': 0,
    'temp': 0,
    'swap': 0,
    'tasks': 0
    }

    valNET = geradorDados.getDownloadAndUpload() # pega os valores de Rede (executa aqui porque demora 1 segundo para poder realizar o calculo de KiB/s)

    t = time.localtime() # pega o tempo de agora
    valTEMPO = ('{}-{}-{} {}:{}:{}'.format(t[0], t[1], t[2], t[3], t[4], t[5])) # converte as medidas para inserção no banco

    dados = [] # inicia array dos dados

    for componente in componentes: # para cada componente em uso
        if 'CPU' in componente[0]: # se for CPU
            CPU = geradorDados.getCPU() # pega o valor do uso de CPU
            hardware['cpu'] = CPU # coloca no dicionario o valor
            dados.append((CPU, valTEMPO, componente[1])) # concatena os dados de CPU para a inserção no banco (utiliza "componente[1]" porque é o id do componente em uso)
        elif 'RAM' in componente[0]:
            RAM = geradorDados.getRAM()
            hardware['memory'] = RAM
            dados.append((RAM, valTEMPO, componente[1]))
        elif 'HD' in componente[0]:
            HD = geradorDados.getHD()
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
            TEMPERATURA = geradorDados.getTemp()
            hardware['temp'] = TEMPERATURA
            dados.append((TEMPERATURA, valTEMPO, componente[1]))
        elif 'SWAP' in componente[0]:
            SWAP = geradorDados.getSWAP()
            hardware['swap'] = SWAP
            dados.append((SWAP, valTEMPO, componente[1]))
        elif 'TASKS' in componente[0]:
            TASKS = geradorDados.getTASKS()
            hardware['tasks'] = TASKS
            dados.append((TASKS, valTEMPO, componente[1]))

    print(hardware)
    print(alertarSlack(valMaquina, hardware))
    return dados

def alertarSlack(maquina, valores, metricas={'cpu': 65,'memory': 60,'disk': 70,'download': 3000,'upload': 1000,'temp': 60,'swap': 50,'tasks': 400,}):
    if (valores['cpu'] >= metricas['cpu']) or (valores['memory'] >= metricas['memory']) or (valores['disk'] >= metricas['disk']) or (valores['download'] >= metricas['download']) or (valores['upload'] >= metricas['upload']) or (valores['temp'] >= metricas['temp']) or (valores['swap'] >= metricas['swap']) or (valores['tasks'] >= metricas['tasks']):
        condicao = ''
        if valores['cpu'] >= metricas['cpu']:
            condicao += "CPU em alto uso, "
        if valores['memory'] >= metricas['memory']:
            condicao += "RAM em alto uso, "
        if valores['disk'] >= metricas['disk']:
            condicao += "HD em alto uso, "
        if valores['download'] >= metricas['download']:
            condicao += "Download em alto uso, "
        if valores['upload'] >= metricas['upload']:
            condicao += "Upload em alto uso, "
        if valores['temp'] >= metricas['temp']:
            condicao += "Temperatura alta, "
        if valores['swap'] >= metricas['swap']:
            condicao += "SWAP em alto uso, "
        if valores['tasks'] >= metricas['tasks']:
            condicao += "Muitas tarefas em uso, "

        condicao = maquina.capitalize() + ": " + condicao[0:-2] + '.'
        enviarMensagemSlack(condicao)
        return condicao
    else:
        condicao = maquina.capitalize() + ": " + "Hardware OK!"
        return condicao
