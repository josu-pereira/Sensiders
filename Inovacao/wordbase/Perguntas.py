import os
def inicio(condicao_horario, usuario = "Pessoa"):
    pergunta = [
        'Como você está hoje {}? '.format(usuario),
        'Como está indo sua {} {}? '.format(condicao_horario, usuario),
        'Está tudo bem com você {}? '.format(usuario),
        'Olá {}! Tudo bem com você? '.format(usuario),
        'Oi! está tudo bem? '
    ]

    # se feliz por causa dos dados => você parece feliz <Felipe>!
    # se estressado => parece que seu dia não está indo muito bem...
    # se neutro => 
    return pergunta

def segunda():
    pergunta = [
        'Me diga como está indo seu dia',
        'Eu gostaria de saber mais do seu dia.',
        'Como vai o seu dia?'
    ]

    return pergunta