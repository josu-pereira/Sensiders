def tratarTexto(classe, texto):
    texto = classe.retiraAcentos(texto)
    texto = classe.separa_palavras(texto)
    classe.resposta = texto

    return texto


def main():
    import botGraphs  # bot que gera os graficos e analisa requisição deles
    import botEmotion  # bot  que analisa as emoções do usuário
    import time
    from message import getLastMsg
    from message import getInfo

    graph = botGraphs.Sensiders()
    emoti = botEmotion.BotSensiders()

    vezes_respondido = 1

    emoti.nome_usuario = getInfo()  # PEGAR O NOME DO SLACK
    emoti.enviarMsg(emoti.boasVindas() + "\n" + emoti.perguntarInicial())

    while True:
        feedback_graficos = False

        if 1 < graph.usos_programa <= 3:
            emoti.enviarMsg("Como você se sente com esta situação atual? \U0001F914")
            resposta_user = getLastMsg()
            feedback_graficos = True
        elif graph.usos_programa > 3:
            emoti.enviarMsg("Mais informações a caminho? \U0001F914")
            resposta_user = getLastMsg()
        else:
            resposta_user = getLastMsg()

        if resposta_user:  # se o usuario digitar alguma coisa

            vezes_respondido += 1
            pediu_grafico = False
            informou_emocoes = False

            tratarTexto(emoti, resposta_user)  # TRATATIVA DE TEXTO DIGITADO
            tratarTexto(graph, resposta_user)
            
            emoti.respostaUnfor = resposta_user  # TEXTO SEM TRATATIVA PARA O WATSON

            emoti.analisaComportamento()  # analisa o que o usuario respondeu baseado nos graficos
            graph.analisaGraphs()  # analisa o que o usuario respondeu baseado nas emocoes

            if not feedback_graficos:  # caso ele nao tenha pedido um grafico anteriormente
                if graph.decide_grafico or graph.pede_ajuda or graph.decide_componente or graph.info_maquinas or graph.info_componentes or graph.decide_maquina:
                    pediu_grafico = True  # pediu alguma informacao relacionada a graficos
                elif emoti.conseguiuResponder:
                    informou_emocoes = True  # informou emocoes
                elif not emoti.conseguiuResponder:
                    emoti.naoConseguiuResponder()  # nao conseguiu entender nada que o usuario informou
                    emoti.enviarMsg(emoti.enviar_usuario)
            else:  # caso pediu grafico anteriormente
                if emoti.conseguiuResponder:
                    informou_emocoes = True  # usuario informou emocoes
                elif graph.decide_grafico or graph.pede_ajuda or graph.decide_componente or graph.info_maquinas or graph.info_componentes or graph.decide_maquina:
                    pediu_grafico = True  # usuario pediu alguma informacao relacionada a graficos
                elif not emoti.conseguiuResponder:
                    emoti.naoConseguiuResponder()  # nao conseguiu entender nada que o usuario informou
                    emoti.enviarMsg(emoti.enviar_usuario)
                    
            if pediu_grafico and not informou_emocoes:
                # se ele pediu grafico
                graph.verificaGraficoCorreto()  # verifica se o grafico pedido esta correto
                if graph.reiniciar['deseja_reiniciar']:  # caso esteja errado e precise reiniciar os dados
                    graph.resetData(graph.reiniciar['valor_reinicio'])
                else:  # caso esteja correta as informacoes
                    graph.geraGraphs()  # gera o grafico pedido
                    graph.usos_programa = 0  # reseta o valor de quantidades de uso
            elif informou_emocoes and not pediu_grafico:
                # se ele informou emocoes
                emoti.enviarMsg(emoti.enviar_usuario)  # enviar mensagem de acordo com emocao
                if feedback_graficos:
                    # caso tenha pedido graficos anteriormente
                    graph.usos_programa += 2  # aumenta usos do programa
                elif vezes_respondido == 2:
                    emoti.acao_comportamento()
                    emoti.enviarMsg(emoti.enviar_usuario)
                    emoti.enviarMsg("Digite 'help' para me pedir ajuda sobre o que posso te fornecer!")
                else:
                    # caso nao tenha pedido grafico anteriormente

                    # emoti.acao_comportamento()
                    # emoti.enviarMsg(emoti.enviar_usuario)
                    """
                    TODO:
                    * Verificar se a emoção é boa, ruim ou neutra
                    * Perguntar o que achou do gráfico recebido
                    """
                ## TODO: FAZER ALGUMA COISA DEPENDENDO DO HUMOR
                # O QUE?
                # >>> ANALISAR SUGESTOES DA KALINE E DO BRANDAO
            else:
                graph.resetData(0)  # caso nao tenha conseguido nenhum dos dois, resetar dados
                emoti.resetData()
            
            emoti.resetData()  # resetar dados de emocoes
            if graph.reiniciar['deseja_reiniciar']:  # caso precise reiniciar dados de graficos
                graph.resetData(graph.reiniciar['valor_reinicio'])
            print("%")
        elif vezes_respondido > 1 and not resposta_user:
            # caso usuario esteve respondendo recentemente e nao respondeu nesta vez
            emoti.naoResponde()
            emoti.enviarMsg(emoti.enviar_usuario)
            graph.resetData(0)
            emoti.resetData()
            vezes_respondido = 1
            print("$")
        else:
            # caso usuario nao esteve respondendo
            graph.resetData(0)
            emoti.resetData()
            print("#")
        time.sleep(1)


if __name__ == "__main__":
    main()
