import json, requests
from mensagemSlack import enviarMensagemSlack

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
