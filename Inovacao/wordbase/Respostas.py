import os
def res_neutro():
    resposta = [
        'Ah que bom \U0001F610', 
        'Hmm, tudo bem então \U0001F610', 
        'Certo... \U0001F636', 
        'Tranquilo \U0001F636', 
        'De boa então \U0001F642', 
        'Tudo certo \U0001F642', 
        'Que bom \U0001F610'
    ]
    return resposta

def res_feliz(usuario="Pessoa"):
    resposta = [
        'Percebi sua felicidade {}! \U0001F601'.format(usuario), 
        'Que bom que você está feliz! \U0001F601', 
        'Você é uma pessoa muito alegre mesmo! \U0001F601', 
        'Ah fico muito feliz por você!! \U0001F606'
    ]
    return resposta
    
def res_estressado():
    resposta = [
        'Vejo que hoje não está sendo seu melhor dia... \U0001F61F', 
        'Calma campeão, dias melhores virão! \U0001F625', 
        'Dias de luta, dias de glória, relaxa que vai dar tudo certo \U0001F61E'
    ]
    return resposta

def res_nao_entende():
    resposta = [
        'Não entendi o que você disse \U0001F615', 
        'Não entendi o que você quis dizer... \U0001F615', 
        'Não entendi... \U0001F615', 
        'Não sou capaz de compreender isso. \U0001F615'
    ]
    return resposta

def res_nao_responde():
    resposta = [
        'Porque você não me responde?', 
        'Está de mal comigo?', 
        'Está de mal comigo? Por que não me responde?', 
        'O gato comeu a sua lingua?', 
        'Você está muito timido hoje', 
        'Vai me deixar no vácuo mesmo? tudo bem...',
        'Você está ocupado? ok...', 
        'Que mancada, conversa comigo!', 
        'Me dê um pouco de atenção!',
    ]
    return resposta

def res_prepara_grafico():
    resposta = [
        'Aguarde um momento enquanto preparamos o seu gráfico \U0001F60A',
        'Aguarde, estou preparando seu gráfico! \U0001F60A',
        'O seu gráfico estará pronto em alguns instantes! \U0001F60A'
    ]
    return resposta