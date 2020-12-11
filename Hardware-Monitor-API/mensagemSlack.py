def enviarMensagemSlack(mensagem):
    from requests import post
    url = '' # canal do Slack
    #pload = {'text': mensagem}
    url = url + mensagem
    try:
        #post(url, json = pload)
        post(url)
        print(mensagem)
    except:
        print("\nERRO no Slack! (URL)")
        #print(mensagem, "\n")

if __name__ == '__main__':
    try:
        enviarMensagemSlack('Testando o slack')
        print('slack ok!')
    except:
        print('erro no slack')
