import requests, json, time


def getLastMsg(tempoLimite=1):
    from tokenSlack import getUrlMessages
    url = getUrlMessages()
    corpoAnterior = (json.loads(requests.get(url).content)).get("messages")
    for mensag in range(len(corpoAnterior)):
        #if corpoAnterior[mensag].get("user") == "U019P8L39HU": # FELIPE
        if corpoAnterior[mensag].get("bot_id") != "B01AGMUJQP6": # SE NAO FOR BOT
        #if corpoAnterior[mensag].get("user") == "U019F8FPYLF": # RONNY
            lastMsg = corpoAnterior[mensag].get("text")
            break

    limite = tempoLimite * 60  # ESPERA POR 2 MINUTOS
    for i in range(limite):
        time.sleep(1)
        corpo = requests.get(url)
        mensagensSlack = (json.loads(corpo.content)).get("messages")
        for texto in range(len(mensagensSlack)):
            #if mensagensSlack[texto].get("user") == "U019P8L39HU": # FELIPE
            if mensagensSlack[texto].get("bot_id") != "B01AGMUJQP6": # SE NAO FOR BOT
            #if mensagensSlack[texto].get("user") == "U019F8FPYLF": # RONNY
                if mensagensSlack[texto].get("text") != lastMsg:
                    msg = mensagensSlack[texto].get("text")
                    return msg
                else:
                    break

    return False


def sendMsg(msg):
    from tokenSlack import getUrlWebhook
    url = getUrlWebhook() + msg
    #pload = {'text': msg}
    requests.post(url)


def getInfo():
    from tokenSlack import getPersonalInformation
    url = getPersonalInformation()
    nome_usuario = (json.loads(requests.get(url).content))['profile'].get('real_name')
    return nome_usuario


if __name__ == "__main__":
    sendMsg('teste')
    a = getLastMsg()
    if a:
        print(a)
    else:
        print('Está de mal comigo?')
