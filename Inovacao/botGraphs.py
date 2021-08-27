class Sensiders:
    def __init__(self, uso_programa=0):
        self.resposta = ""
        self.usos_programa = uso_programa
        self.decide_grafico = False
        self.pede_ajuda = False
        self.graficos = {
            'linha': False,
            'barra': False,
            'gauge': False,
            'pizza': False,
            'donut': False
        }
        self.decide_dado_grafico = False
        self.tipo_dado_grafico = {
            'hora': False,
            'dia': False,
            'semana': False,
            'mes': False,
            'duplo': False
        }
        self.modo_escuro = False
        self.componente_escolhido = ''
        self.decide_componente = False
        self.decide_maquina = False
        self.maquina_escolhida = 0
        self.decide_componente_errado = False
        self.info_maquinas = False
        self.info_componentes = False
        self.tipo_dado = {
            'mediaPorComponente': False,
            'valorComponente': False,
            'valorTodosComponentes': False,
            'todasMaquinas': False,
            'todosComponentes': False,
            'todasMaqPeloComponente': False
        }
        self.todas_maquinas = set()
        self.reiniciar = {
            'deseja_reiniciar': False,
            'valor_reinicio': 0
        }

    def separa_palavras(self, texto):
        import re
        sentencas = re.split(r'\W+', texto)
        if sentencas[-1] == '':
            del sentencas[-1]
        return sentencas

    def retiraAcentos(self, texto):
        import unicodedata
        try:
            texto = unicode(texto, 'utf-8')
        except NameError:
            pass
        texto = unicodedata.normalize('NFD', texto) \
            .encode('ascii', 'ignore') \
            .decode("utf-8")
        return str(texto)

    def analiseBancoPalavras(self, dado_texto="", inserirDados=False, conseguiuInserir=1):
        from machlearn import ml
        banco_ml = ml.BancoML()  # INSTANCIEI O BANCO SQLITE
        if inserirDados:
            banco_ml.inserirBanco(dado_texto, conseguiuInserir)
        else:
            # from machlearn import algoritmoML
            # alg = algoritmoML.Algoritmo() # INSTANCIEI O ALGORITMO PARA TRATAR OS DADOS DO BANCO
            # todas_palavras = banco_ml.selectBanco()
            # info = alg.tratar_palavras(todas_palavras)
            from analyWords import analysisWords
            analyword = analysisWords()
            dados = analyword.verificarAnalise()

            return dados

    def enviarMsg(self, texto):
        from message import sendMsg
        sendMsg(texto)

    def pegarDados(self, info, componente=None, maquina=None):
        from sqlAzure import Sql
        sql = Sql('adminlocal', '#Gfgrupo11c', '1433', 'bdProjetoSensiders', 'serversensiders.database.windows.net')
        sql.connect()

        if info['mediaPorComponente']:

            dados = sql.selectAvgComp(maquina, componente)
            total = 0
            qtd = 0
            for d in dados:
                qtd += 1
                total += float(d[0])
            dados = round(total / qtd)

            return dados, componente
        elif info['valorComponente']:

            dados = sql.selectResultComp(maquina, componente)
            valores = []
            tempo = []
            for i in range(len(dados)):
                i = (i + 1) * -1
                valores.append(dados[i][0])
                t = dados[i][2].strftime("%H:%M:%S")
                tempo.append(t)

            return tempo, valores, componente
        elif info['valorTodosComponentes']:
            dados = sql.selectResult(maquina)

            return dados
        elif info['todasMaquinas']:
            dados = sql.selectMachines()

            return dados
        elif info['todosComponentes']:
            dados = sql.selectComp(componente)

            return dados
        elif info['todasMaqPeloComponente']:
            dados = sql.selectMachinesByComp(componente)

            return dados

    def analisa_maquinas(self):
        for p in self.resposta:
            if p.isnumeric():
                self.maquina_escolhida = int(p)
                self.decide_maquina = True
                break
        self.tipo_dado['todosComponentes'] = True
        dados = self.pegarDados(self.tipo_dado, self.maquina_escolhida)
        tem_componente_escolhido = False
        for com in dados:
            if self.componente_escolhido in str(com[0]):
                # caso tenha o componente escolhido
                tem_componente_escolhido = True
        if not tem_componente_escolhido:
            self.decide_componente_errado = True
            self.enviarMsg(str("Este componente não está cadastrado para a maquina " + str(
                self.maquina_escolhida) + "...\nAqui estão todos os componentes cadastrados desta máquina:"))
            if len(dados) > 0:
                msg = ""
                msg += ("Total de *" + str(len(dados)) + "* componentes em uso.\n")
                for d in dados:
                    msg += ("\n• nome: *" + str(d[0]) + "*")
                self.enviarMsg(msg)
                self.reiniciar['valor_reinicio'] = 1
                self.reiniciar['deseja_reiniciar'] = True
            else:
                self.enviarMsg("...\nEsta máquina não possui componentes ou não está cadastrada")
                self.reiniciar['valor_reinicio'] = 1
                self.reiniciar['deseja_reiniciar'] = True

    def analisaGraphs(self, analise_externa=False):
        import wordbase.charts as charts
        import wordbase.components as components

        for palavra in self.resposta:
            palavra = palavra.lower()
            # if palavra != "" and palavra != " " and palavra not in stpwrds:
            if palavra != "" and palavra != " ":
                if palavra in charts.tipos_graficos() and not analise_externa:
                    self.pede_ajuda = True
                    break
                if palavra in charts.escuro():
                    self.modo_escuro = True
                if palavra in charts.linha():
                    if not self.decide_grafico:
                        self.graficos['linha'] = True
                        self.decide_grafico = True
                elif palavra in charts.barra():
                    if not self.decide_grafico:
                        self.graficos['barra'] = True
                        self.decide_grafico = True
                elif palavra in charts.gauge():
                    if not self.decide_grafico:
                        self.graficos['gauge'] = True
                        self.decide_grafico = True
                elif palavra in charts.pizza():
                    if not self.decide_grafico:
                        self.graficos['pizza'] = True
                        self.decide_grafico = True
                elif palavra in charts.donut():
                    if not self.decide_grafico:
                        self.graficos['donut'] = True
                        self.decide_grafico = True
                if palavra in components.cpu():
                    if not self.decide_componente:
                        self.componente_escolhido = "CPU"
                        self.decide_componente = True
                elif palavra in components.ram():
                    if not self.decide_componente:
                        self.componente_escolhido = "RAM"
                        self.decide_componente = True
                elif palavra in components.hd():
                    if not self.decide_componente:
                        self.componente_escolhido = "HD"
                        self.decide_componente = True
                elif palavra in components.download():
                    if not self.decide_componente:
                        self.componente_escolhido = "DOWNLOAD"
                        self.decide_componente = True
                elif palavra in components.upload():
                    if not self.decide_componente:
                        self.componente_escolhido = "UPLOAD"
                        self.decide_componente = True
                elif palavra in components.temperatura():
                    if not self.decide_componente:
                        self.componente_escolhido = "TEMPERATURA"
                        self.decide_componente = True
                elif palavra in components.swap():
                    if not self.decide_componente:
                        self.componente_escolhido = "SWAP"
                        self.decide_componente = True
                elif palavra in components.tasks():
                    if not self.decide_componente:
                        self.componente_escolhido = "TASKS"
                        self.decide_componente = True
                if palavra in charts.hora():
                    self.tipo_dado_grafico['hora'] = True
                    self.decide_dado_grafico = True
                    for p in self.resposta:
                        if palavra in charts.duplo():
                            self.tipo_dado_grafico['duplo'] = True
                elif palavra in charts.dia():
                    self.tipo_dado_grafico['dia'] = True
                    self.decide_dado_grafico = True
                    for p in self.resposta:
                        if palavra in charts.duplo():
                            self.tipo_dado_grafico['duplo'] = True
                elif palavra in charts.semana():
                    self.tipo_dado_grafico['semana'] = True
                    self.decide_dado_grafico = True
                    for p in self.resposta:
                        if palavra in charts.duplo():
                            self.tipo_dado_grafico['duplo'] = True
                elif palavra in charts.mes():
                    self.tipo_dado_grafico['mes'] = True
                    self.decide_dado_grafico = True
                if palavra in components.maquinas() and not self.decide_grafico and not self.decide_componente and not analise_externa:
                    self.info_maquinas = True
                    break
                elif palavra in components.hardware() and not self.decide_grafico and not self.decide_componente and not analise_externa:
                    self.info_componentes = True
                    break

        for palavra in self.resposta:
            if palavra.isnumeric() and self.decide_grafico and self.decide_componente:
                self.maquina_escolhida = int(palavra)
                self.decide_maquina = True
                break

    def analisarSugestaoML(self):
        import botEmotion
        from message import getLastMsg

        sugestao = self.analiseBancoPalavras()

        msg = ""
        msg += "Me parece que você não informou o componente para visualização..."
        msg += "\nMas segundo minhas análises, o melhor gráfico para você seria um "
        msg += ("com o componente *" + sugestao[1] + "* da máquina *" + str(sugestao[2]) + "*")
        msg += "\nO que você achou da minha sugestão?"
        self.enviarMsg(msg)

        rsp = getLastMsg()
        emotion = botEmotion.BotSensiders()
        emotion.respostaUnfor = rsp  # sem tratativa
        rsp = emotion.retiraAcentos(rsp)
        rsp = emotion.separa_palavras(rsp)
        emotion.resposta = rsp  # com tratativa
        # emotion.analisaComportamento() # MUDADO POIS ESTAREI CRIANDO NOVO METODO SOMENTE PARA ISSO
        emotion.analisaSugestao()
        self.componente_escolhido = sugestao[1]
        self.maquina_escolhida = sugestao[2]
        if emotion.valorPositivo or emotion.emocao['feliz']:
            self.enviarMsg("Eu sabia que você iria gostar muito deste gráfico! \U0001F60A")
            return sugestao
        elif emotion.valorNegacao or emotion.emocao['estressado']:
            self.enviarMsg("Que pena que você não gostou! \U0001F625 Irei considerar isto na próxima vez! \U0001F61E")
            return sugestao
        elif emotion.emocao['neutro']:
            self.enviarMsg("Hmm, espero que este gráfico te deixe feliz! \U0001F913")
            return sugestao
        else:
            self.enviarMsg("Irei te enviar este gráfico! \U0001F609")
            return sugestao

    def pegarDadosGrafico(self, tipoDado, componente="CPU", maquina=3):
        if not self.decide_dado_grafico:
            from dataGraphs import DataGraphs as Graphics
            algoritmoDados = Graphics(maquina, componente)
            dadosNormal = algoritmoDados.calcNormal()
            # dadosDuplo = algoritmoDados.calcDuplo()
            # if dadosNormal[0] < dadosDuplo[0] and not self.tipo_dado['mediaPorComponente']:
            if not self.tipo_dado['mediaPorComponente']:
                dados = dadosNormal
                return dados[1]
            # elif dadosNormal[0] < dadosDuplo[0] and self.tipo_dado['mediaPorComponente']:
            elif self.tipo_dado['mediaPorComponente']:
                dado = dadosNormal
                media = round(sum(dado[1][0]) / len(dado[1][0]))
                return [media]
            else:
                # dados = dadosDuplo
                dados = dadosNormal
                return dados[1]
        else:
            import algGraphs as algGraphs
            ob = algGraphs.AlgoritmoGraficos()

            if self.tipo_dado_grafico['hora'] and not self.tipo_dado_grafico['duplo']:
                dados = ob.calcHora(maquina, componente)
                if self.tipo_dado['mediaPorComponente']:
                    if bool(dados):
                        dados = [round(sum(dados[0]) / len(dados[0]))]
                    else:
                        dados = [0]
            elif self.tipo_dado_grafico['hora'] and self.tipo_dado_grafico['duplo']:
                dados = ob.calcDuasHoras(maquina, componente)
                if self.tipo_dado['mediaPorComponente']:
                    if bool(dados):
                        dados = [round(sum(dados[0][0]) / len(dados[0][0]))]
                    else:
                        dados = [0]
            elif self.tipo_dado_grafico['dia'] and not self.tipo_dado_grafico['duplo']:
                umDia = ob.calcDia(maquina, componente)
                if len(umDia[0]) > 12:
                    # dados = ob.calcDiaInteiro(maquina, componente)
                    dados = umDia
                else:
                    dados = umDia
                if self.tipo_dado['mediaPorComponente']:
                    if bool(dados):
                        dados = [round(sum(dados[0]) / len(dados[0]))]
                    else:
                        dados = [0]
            elif self.tipo_dado_grafico['dia'] and self.tipo_dado_grafico['duplo']:
                dados = ob.calcDoisDias(maquina, componente)
                if self.tipo_dado['mediaPorComponente']:
                    if bool(dados):
                        dados = [round(sum(dados[0][0]) / len(dados[0][0]))]
                    else:
                        dados = [0]
            elif self.tipo_dado_grafico['semana'] and not self.tipo_dado_grafico['duplo']:
                dados = ob.calcSemana(maquina, componente)
                if self.tipo_dado['mediaPorComponente']:
                    if bool(dados):
                        dados = [round(sum(dados[0]) / len(dados[0]))]
                    else:
                        dados = [0]
            elif self.tipo_dado_grafico['semana'] and self.tipo_dado_grafico['duplo']:
                dados = ob.calcDuasSemanas(maquina, componente)
                if self.tipo_dado['mediaPorComponente']:
                    if bool(dados):
                        dados = [round(sum(dados[0][0]) / len(dados[0][0]))]
                    else:
                        dados = [0]
            elif self.tipo_dado_grafico['mes']:
                dados = ob.calcMes(maquina, componente)
                if self.tipo_dado['mediaPorComponente']:
                    if bool(dados):
                        dados = [round(sum(dados[0]) / len(dados[0]))]
                    else:
                        dados = [0]
            else:
                dados = self.pegarDados(tipoDado)

            return dados

    def geraGraphs(self):
        import wordbase.Respostas as Respostas
        from random import randrange
        import graficos

        if not self.decide_grafico and not self.pede_ajuda and not self.info_componentes and not self.info_maquinas:
            pass
            """
            print("Não entendi o que você quer")
            print("...")
            """
            #
            # TODO:
            # FAZER PROPRIA ANALISE
            #
            for palavra in self.resposta:
                palavra = palavra.lower()
                if palavra == 'velocidade':
                    gauge = True
                    decide_grafico = True
        elif self.info_maquinas:
            msg = ""
            msg += ("Aqui estão todas as máquinas cadastradas:")
            self.tipo_dado['todasMaquinas'] = True
            dados = self.pegarDados(self.tipo_dado)
            msg += ("\nTotal de *" + str(len(dados)) + "* máquinas cadastradas.\n")
            for d in dados:
                msg += ("\n• nome: *" + str(d[1]) + "* || ID: *" + str(d[0]) + "*")
                self.todas_maquinas.add(int(d[0]))
            msg += ("\nAgora você pode me pedir para ver os componentes de uma máquina de sua escolha!")
            #
            # TODO:
            # TER QUE INSERIR DADOS TODAS AS VEZES ANTES DE RESETAR
            #
            self.enviarMsg(msg)
            self.analiseBancoPalavras(self.resposta, True, 0)
            self.reiniciar['valor_reinicio'] = 1
            self.reiniciar['deseja_reiniciar'] = True
        elif self.info_componentes:
            msg = ""
            msg += ("Aqui estão todos os componentes cadastrados desta máquina:")
            num_maquina = False
            for r in self.resposta:
                if r.isnumeric():
                    num_maquina = int(r)
                    break
            if (not bool(self.todas_maquinas) or (num_maquina in self.todas_maquinas)) and bool(num_maquina):
                self.tipo_dado['todosComponentes'] = True
                dados = self.pegarDados(self.tipo_dado, num_maquina)
                if len(dados) > 0:
                    msg += ("\nTotal de *" + str(len(dados)) + "* componentes em uso.\n")
                    for d in dados:
                        msg += ("\n• nome: *" + str(d[0]) + "*")
                    #                    
                    # OU ELE PODE FAZER O SEGUINTE
                    # TODO:
                    # FAZER ANALISE PARA REQUESITAR GRAFICO
                    """
                    a = analisarComportamento()
                    -> RETORNA BOOLEANO (caso tenha dados suficientes) e DADOS
                    """
                    a = False  # EXEMPLO
                    if a:
                        msg += ("\nVocê gostaria de um gráfico X?")
                    else:
                        msg += ("\nAgora você pode me pedir para ver um gráfico de sua escolha!")

                else:
                    msg += ("\n...\nEsta máquina não possui componentes ou não está cadastrada")
            elif not bool(self.todas_maquinas) and bool(num_maquina):
                msg += ("\n...\nEsta máquina não possui componentes ou não está cadastrada")
            elif not num_maquina:
                msg += ("...\nVocê não informou o ID da maquina!")
            else:
                msg += ("\nEsta máquina não está cadastrada...\nPara ver as máquinas cadastradas digite 'máquinas'")
            self.enviarMsg(msg)
            self.analiseBancoPalavras(self.resposta, True, 0)
            self.reiniciar['valor_reinicio'] = 1
            self.reiniciar['deseja_reiniciar'] = True
        elif self.pede_ajuda:
            msg = ""
            msg += ("\nTIPOS DE GRAFICOS:")
            msg += ("\n• linha\n• gauge\n• barra\n• pizza\n• donut\n")
            msg += (
                "\nINFORMAÇÕES:\n• escolher componente para analisar situação\n• escolher periodo de analise\n• escolher maquina para analisar\n")
            msg += (
                "\nTIPOS DE DADOS P/ GRÁFICOS:\n• dados da ultima hora\n• dados das ultimas 2 horas\n• dados do dia\n• dados dos ultimos 2 dias\n• dados da semana\n• dados dos ultimos 14 dias\n• dados do mês\n")
            msg += (
                "\nDETALHES:\n• me peça para ver as maquinas disponiveis\n• me peça para ver os componentes disponiveis de uma maquina em especifico (informe o ID)\n")
            msg += ("\nEXTRAS:\n• modo escuro (padrão = desligado)\n")
            msg += (
                "\nEXEMPLOS:\n• Me mostre todas as maquinas cadastradas!\n• Me fale os componentes da maquina com ID 3\n• Um grafico de linha com o componente cpu da maquina 2 por favor\n• Grafico de gauge com o componente disco da maquina 3\n")
            self.enviarMsg(msg)
            self.analiseBancoPalavras(self.resposta, True, 0)
            self.reiniciar['valor_reinicio'] = 1
            self.reiniciar['deseja_reiniciar'] = True
        elif self.graficos['linha']:

            ### TODO:
            # SE USUARIO NAO INFORMAR MAQUINA...
            #
            ## 1: FAZER ANALISE DE MAQUINA MAIS USADA/MAIS PREJUDICADA
            # > E INDICAR UTILIZAÇÃO (FALAR SE ELE QUER MESMO)
            #
            ## 2: PEDIR PARA USUARIO ESCREVER NUMERO DA MAQUINA DA
            # > QUAL ELE QUER OBSERVAR (EX: "linha cpu da maquina 3")
            #

            # if self.decide_maquina:
            self.tipo_dado['valorComponente'] = True
            if self.decide_componente and not self.decide_componente_errado:
                # CODIGO ANTIGO
                # data = self.pegarDados(self.tipo_dado, self.componente_escolhido, self.maquina_escolhida)
                data = self.pegarDadosGrafico(self.tipo_dado, self.componente_escolhido, self.maquina_escolhida)
                """
            elif self.decide_componente_errado:
                print("Este componente não está cadastrado para a maquina", self.maquina_escolhida, "...")
                
                # TODO:
                # FAZER ANALISE DE ALGUM COMPONENTE (?????)
                # -> desnecessário neste caso?
                #
                # >>>> DECIDI MOSTRAR OS COMPONENTES
                """
            else:
                sugestao = self.analisarSugestaoML()
                data = self.pegarDadosGrafico(self.tipo_dado, sugestao[1], sugestao[2])
                # data = self.pegarDadosGrafico(self.tipo_dado, analise_componente, maq)
            if not self.decide_componente_errado:
                rnd = randrange(0, len(Respostas.res_prepara_grafico()))
                self.enviarMsg(Respostas.res_prepara_grafico()[rnd])
                graficos.linha(data[1], data[0], self.componente_escolhido, self.modo_escuro)
                self.usos_programa += 2
                self.analiseBancoPalavras(self.resposta, True)
                self.reiniciar['valor_reinicio'] = self.usos_programa
                self.reiniciar['deseja_reiniciar'] = True
            else:
                self.analiseBancoPalavras(self.resposta, True, 0)
                self.reiniciar['valor_reinicio'] = 1
                self.reiniciar['deseja_reiniciar'] = True
        elif self.graficos['barra']:
            self.tipo_dado['valorComponente'] = True
            if self.decide_componente and not self.decide_componente_errado:
                data = self.pegarDadosGrafico(self.tipo_dado, self.componente_escolhido, self.maquina_escolhida)
                """
            elif self.decide_componente_errado:
                print("Este componente não está cadastrado para a maquina", self.maquina_escolhida, "...")
                """
            else:
                sugestao = self.analisarSugestaoML()
                data = self.pegarDadosGrafico(self.tipo_dado, sugestao[1], sugestao[2])

            if not self.decide_componente_errado:
                rnd = randrange(0, len(Respostas.res_prepara_grafico()))
                self.enviarMsg(Respostas.res_prepara_grafico()[rnd])
                graficos.barra(data[1], data[0], self.componente_escolhido, self.modo_escuro)
                self.usos_programa += 2
                self.analiseBancoPalavras(self.resposta, True)
                self.reiniciar['valor_reinicio'] = self.usos_programa
                self.reiniciar['deseja_reiniciar'] = True
            else:
                self.analiseBancoPalavras(self.resposta, True, 0)
                self.reiniciar['valor_reinicio'] = 1
                self.reiniciar['deseja_reiniciar'] = True
        elif self.graficos['gauge']:
            self.tipo_dado['mediaPorComponente'] = True
            if self.decide_componente and not self.decide_componente_errado:
                data = self.pegarDadosGrafico(self.tipo_dado, self.componente_escolhido, self.maquina_escolhida)
                """
            elif self.decide_componente_errado:
                print("Este componente não está cadastrado para a maquina", self.maquina_escolhida, "...")
                """
            else:
                sugestao = self.analisarSugestaoML()
                data = self.pegarDadosGrafico(self.tipo_dado, sugestao[1], sugestao[2])

            if not self.decide_componente_errado:
                rnd = randrange(0, len(Respostas.res_prepara_grafico()))
                self.enviarMsg(Respostas.res_prepara_grafico()[rnd])
                graficos.gauge(data[0], self.componente_escolhido, "%", self.modo_escuro)
                self.usos_programa += 2
                self.analiseBancoPalavras(self.resposta, True)
                self.reiniciar['valor_reinicio'] = self.usos_programa
                self.reiniciar['deseja_reiniciar'] = True
            else:
                self.analiseBancoPalavras(self.resposta, True, 0)
                self.reiniciar['valor_reinicio'] = 1
                self.reiniciar['deseja_reiniciar'] = True
        elif self.graficos['pizza']:
            self.tipo_dado['mediaPorComponente'] = True
            if self.decide_componente and not self.decide_componente_errado:
                if self.componente_escolhido in {'CPU', 'RAM', 'HD', 'SWAP'}:
                    data = self.pegarDadosGrafico(self.tipo_dado, self.componente_escolhido, self.maquina_escolhida)
                    info_data = [((self.componente_escolhido + " em uso"), data[0]),
                                 ((self.componente_escolhido + " disponível"), 100 - data[0])]
                elif self.componente_escolhido in {'DOWNLOAD', 'UPLOAD'}:
                    data_down = self.pegarDadosGrafico(self.tipo_dado, "DOWNLOAD", self.maquina_escolhida)
                    data_up = self.pegarDadosGrafico(self.tipo_dado, "UPLOAD", self.maquina_escolhida)
                    info_data = [(("Velocidade de " + "DOWNLOAD"), data_down[0]),
                                 (("Velocidade de " + "UPLOAD"), data_up[0])]
                    self.componente_escolhido = "REDE"
                else:
                    self.decide_componente_errado = True
                #
                # TODO:
                # GRAFICO DE GAUGE/PIZZA/DONUT NÃO FAZ
                # SENTIDO USAR VALORES NÃO PERCENTUAIS
                # (ex: DOWNLOAD, UPLOAD, TEMPERATURA, TASKS)
                # 
                # >> FAZER SUGESTÃO PARA ESCOLHER OUTRO GRÁFICO
                #
                """
            elif self.decide_componente_errado:
                print("Este componente não está cadastrado para a maquina", self.maquina_escolhida, "...")
                """
            else:
                sugestao = self.analisarSugestaoML()
                data = self.pegarDadosGrafico(self.tipo_dado, sugestao[1], sugestao[2])
                # data = self.pegarDadosGrafico(self.tipo_dado, self.componente_escolhido, self.maquina_escolhida)
                info_data = [((data[1] + " em uso"), data[0]), ((data[1] + " disponível"), 100 - data[0])]

            if not self.decide_componente_errado:
                rnd = randrange(0, len(Respostas.res_prepara_grafico()))
                self.enviarMsg(Respostas.res_prepara_grafico()[rnd])
                if self.componente_escolhido != "REDE":
                    graficos.pizza(info_data, self.componente_escolhido, "%", self.modo_escuro)
                else:
                    graficos.pizza(info_data, self.componente_escolhido, "KB/s", self.modo_escuro)
                self.usos_programa += 2
                self.analiseBancoPalavras(self.resposta, True)
                self.reiniciar['valor_reinicio'] = self.usos_programa
                self.reiniciar['deseja_reiniciar'] = True
            else:
                self.analiseBancoPalavras(self.resposta, True, 0)
                self.reiniciar['valor_reinicio'] = 1
                self.reiniciar['deseja_reiniciar'] = True
        elif self.graficos['donut']:
            self.tipo_dado['mediaPorComponente'] = True
            if self.decide_componente and not self.decide_componente_errado:
                if self.componente_escolhido in {'CPU', 'RAM', 'HD', 'SWAP'}:
                    data = self.pegarDadosGrafico(self.tipo_dado, self.componente_escolhido, self.maquina_escolhida)
                    # data = self.pegarDadosGrafico(self.tipo_dado, self.componente_escolhido, self.maquina_escolhida)
                    info_data = [((self.componente_escolhido + " em uso"), data[0]),
                                 ((self.componente_escolhido + " disponível"), 100 - data[0])]
                elif self.componente_escolhido in {'DOWNLOAD', 'UPLOAD'}:
                    data_down = self.pegarDadosGrafico(self.tipo_dado, "DOWNLOAD", self.maquina_escolhida)
                    # data = self.pegarDadosGrafico(self.tipo_dado, self.componente_escolhido, self.maquina_escolhida)
                    data_up = self.pegarDadosGrafico(self.tipo_dado, "UPLOAD", self.maquina_escolhida)
                    # data = self.pegarDadosGrafico(self.tipo_dado, self.componente_escolhido, self.maquina_escolhida)
                    info_data = [(("Velocidade de " + "DOWNLOAD"), data_down[0]),
                                 (("Velocidade de " + "UPLOAD"), data_up[0])]
                    self.componente_escolhido = "REDE"
                else:
                    self.decide_componente_errado = True
                # data = self.pegarDados(self.tipo_dado, self.componente_escolhido, self.maquina_escolhida)
                # info_data = [((data[1] + " em uso"), data[0]), ((data[1] + " disponível"), 100 - data[0])]
                """
            elif self.decide_componente_errado:
                print("Este componente não está cadastrado para a maquina", self.maquina_escolhida, "...")
                """
            else:
                sugestao = self.analisarSugestaoML()
                data = self.pegarDadosGrafico(self.tipo_dado, sugestao[1], sugestao[2])
                # data = self.pegarDadosGrafico(self.tipo_dado, self.componente_escolhido, self.maquina_escolhida)
                info_data = [((self.componente_escolhido + " em uso"), data[0]),
                             ((self.componente_escolhido + " disponível"), 100 - data[0])]

            if not self.decide_componente_errado:
                rnd = randrange(0, len(Respostas.res_prepara_grafico()))
                self.enviarMsg(Respostas.res_prepara_grafico()[rnd])
                if self.componente_escolhido != "REDE":
                    graficos.donut(info_data, self.componente_escolhido, "%", self.modo_escuro)
                else:
                    graficos.donut(info_data, self.componente_escolhido, "KB/s", self.modo_escuro)
                self.usos_programa += 2
                self.analiseBancoPalavras(self.resposta, True)
                self.reiniciar['valor_reinicio'] = self.usos_programa
                self.reiniciar['deseja_reiniciar'] = True
            else:
                self.analiseBancoPalavras(self.resposta, True, 0)
                self.reiniciar['valor_reinicio'] = 1
                self.reiniciar['deseja_reiniciar'] = True
        else:
            pass

    def verificaGraficoCorreto(self):
        if self.decide_grafico and self.decide_componente and self.decide_maquina:
            self.analisa_maquinas()
        elif self.decide_grafico and self.decide_componente and not self.decide_maquina:
            # TODO:
            #### (DESEJAVEL)
            # FAZER ANALISE DE PEDIDOS
            # PARA TRAZER MAQUINA MAIS USADA
            # COMO SUGESTAO

            msg = ""
            msg += ("Você não nos informou a máquina de visualização...")
            self.tipo_dado['todasMaqPeloComponente'] = True
            dados = self.pegarDadosGrafico(self.tipo_dado, self.componente_escolhido)
            msg += ("\nAqui estão todas as máquinas cadastradas com este componente:")
            msg += ("\nTotal de *" + str(
                len(dados)) + "* máquinas cadastradas com o componente *" + self.componente_escolhido + "*.\n")
            for d in dados:
                msg += ("\n• nome: *" + str(d[0]) + "* || ID: *" + str(d[1]) + "*")
                self.todas_maquinas.add(int(d[1]))
            msg += ("\nInforme o ID para a correta visualização, caso precise de ajuda digite 'help'")
            self.analiseBancoPalavras(self.resposta, True, 0)
            self.reiniciar['valor_reinicio'] = 1
            self.reiniciar['deseja_reiniciar'] = True

    def iniciar(self):
        import graficos
        import wordbase.StopWords as stopword

        if self.usos_programa == 1:
            self.resposta = input("> ")
        elif self.usos_programa > 1 and not self.decide_grafico and not self.decide_componente:
            self.resposta = input("Como você se sente com esta situação atual? \U0001F914\n> ")
        elif self.usos_programa > 2 and self.decide_grafico and self.decide_componente:
            self.resposta = input("Mais informações a caminho? \U0001F914\n> ")
        elif self.usos_programa == 0:
            self.resposta = input(
                "Sou o seu assistente pessoal SextaFeira! \U0001F609\nSe precisar de ajuda digite 'help'\n> ")
        self.resposta = self.retiraAcentos(self.resposta)
        self.resposta = self.separa_palavras(self.resposta)

        stpwrds = stopword.stopwordPT()

        data_analysis = self.analisaGraphs()

        self.verificaGraficoCorreto()

        if self.reiniciar['deseja_reiniciar']:
            self.resetData(self.reiniciar['valor_reinicio'])
            self.iniciar()
        else:
            self.geraGraphs()

        if self.reiniciar['deseja_reiniciar']:
            self.resetData(self.reiniciar['valor_reinicio'])
            self.iniciar()

    def resetData(self, uso_programa=0):
        self.resposta = ""
        self.usos_programa = uso_programa
        self.decide_grafico = False
        self.pede_ajuda = False
        self.graficos = {
            'linha': False,
            'barra': False,
            'gauge': False,
            'pizza': False,
            'donut': False
        }
        self.modo_escuro = False
        self.componente_escolhido = ''
        self.decide_componente = False
        self.decide_maquina = False
        self.maquina_escolhida = 0
        self.decide_componente_errado = False
        self.info_maquinas = False
        self.info_componentes = False
        self.tipo_dado = {
            'mediaPorComponente': False,
            'valorComponente': False,
            'valorTodosComponentes': False,
            'todasMaquinas': False,
            'todosComponentes': False,
            'todasMaqPeloComponente': False
        }
        self.reiniciar = {
            'deseja_reiniciar': False,
            'valor_reinicio': 0
        }
        self.decide_dado_grafico = False
        self.tipo_dado_grafico = {
            'hora': False,
            'dia': False,
            'semana': False,
            'mes': False,
            'duplo': False
        }


if __name__ == "__main__":
    bot = Sensiders()
    # bot.iniciar()
    bot.tipo_dado['mediaPorComponente'] = True
    bot.decide_dado_grafico = True
    bot.tipo_dado_grafico['hora'] = True
    # bot.tipo_dado_grafico['dia'] = True
    # bot.tipo_dado_grafico['semana'] = True
    # bot.tipo_dado_grafico['mes'] = True
    data = bot.pegarDadosGrafico(bot.tipo_dado, "HD", 3)
    print(data)
    """
    CODIGO QUE PODE SER USADO NO FUTURO
    for i in data[1]:
        if 'dia' in i:
            print('é de dia sim')
            break
    """
    import graficos
    # graficos.linha(data[1], data[0], data[2], True, True, True)
    # graficos.gauge(data, "CPU", "%", True, True)
