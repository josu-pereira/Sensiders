class analysisWords:
    def __init__(self):
        import machlearn.ml as ml
        aibot = ml.BancoML()
        self.todas_palavras = aibot.selectBanco()

    def analisar(self):
        lbl_palavras = []
        qtd_palavras = []
        contador = 0
        for w in self.todas_palavras:
            actualWord = w[0]
            if not actualWord in lbl_palavras:
                qtd = 0
                for j in range(contador, len(self.todas_palavras)):
                    if actualWord == self.todas_palavras[j][0]:
                        qtd += 1
                lbl_palavras.append(actualWord)
                qtd_palavras.append(qtd)
                contador += 1

        tam = len(qtd_palavras)
        for i in range(tam):
            act = i
            for j in range(i, tam):
                if qtd_palavras[j] > qtd_palavras[i] and qtd_palavras[j] > qtd_palavras[act]:
                    act = j
            qtd_palavras[act], qtd_palavras[i] = qtd_palavras[i], qtd_palavras[act]
            lbl_palavras[act], lbl_palavras[i] = lbl_palavras[i], lbl_palavras[act]
        info = (qtd_palavras, lbl_palavras)

        return info

    def pegarRelevantes(self, conseguiuPrimeira=True):
        dataText = self.analisar()
        totalEntradas = sum(dataText[0])

        numText = []
        allText = []
        cont = 0
        while dataText[0][cont] >= (totalEntradas * (0.05 if conseguiuPrimeira else 0.01)):
            numText.append(dataText[0][cont])
            allText.append(dataText[1][cont])
            cont += 1
        newData = [numText, allText]
        return newData

    def verificarAnalise(self, primeiraTentativa=True):
        import botGraphs
        data = self.pegarRelevantes()
        graph = botGraphs.Sensiders()
        graph.resposta = data[1]
        graph.analisaGraphs(True)
        if graph.decide_grafico or graph.decide_componente or graph.decide_maquina:
            tipo_grafico = ""
            for i in graph.tipo_dado_grafico.items():
                if i[1] is True: tipoDado = (i[0])
            for k in graph.graficos.items():
                if k[1] is True: tipo_grafico = (k[0])
            return tipo_grafico, graph.componente_escolhido, graph.maquina_escolhida
        else:
            mltest = analysisWords()
            data = mltest.verificarAnalise(False)
            return data


if __name__ == '__main__':
    mltest = analysisWords()
    data = mltest.verificarAnalise()
    print(data)