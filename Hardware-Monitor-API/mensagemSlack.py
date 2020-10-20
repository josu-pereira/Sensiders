def enviarMensagemSlack(mensagem):
    url = '' # canal do Slack
    pload = {'text': mensagem}
    try:
        requests.post(url, json = pload)
    except:
        print("\nERRO no Slack! (URL)")
        print(mensagem, "\n")

if __name__ == '__main__':
    try:
        enviarMensagemSlack('Teste no slack')
        print('slack ok!')
    except:
        print('erro no slack')
