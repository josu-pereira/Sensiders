class DataGraphs:
    def __init__(self, id_maquina, nome_componente, dados_duplos=False):
        self.id_maquina_escolhida = id_maquina
        self.nome_componente_escolhido = nome_componente
        self.umaHora = None
        self.duasHoras = None
        self.umDia = None
        self.umDiaInteiro = None
        self.doisDias = None
        self.umaSemana = None
        self.duasSemanas = None
        self.umMes = None
        if dados_duplos:
            self.async_define()
        else:
            self.async_define_singular()

    def definir_dados(self, num):
        from algGraphs import AlgoritmoGraficos
        ob = AlgoritmoGraficos()
        if num == 0:
            dado = (ob.calcHora(self.id_maquina_escolhida, self.nome_componente_escolhido))
        elif num == 1:
            dado = (ob.calcDuasHoras(self.id_maquina_escolhida, self.nome_componente_escolhido))
        elif num == 2:
            dado = (ob.calcDia(self.id_maquina_escolhida, self.nome_componente_escolhido))
        elif num == 3:
            dado = (ob.calcDiaInteiro(self.id_maquina_escolhida, self.nome_componente_escolhido))
        elif num == 4:
            dado = (ob.calcDoisDias(self.id_maquina_escolhida, self.nome_componente_escolhido))
        elif num == 5:
            dado = (ob.calcSemana(self.id_maquina_escolhida, self.nome_componente_escolhido))
        elif num == 6:
            dado = (ob.calcDuasSemanas(self.id_maquina_escolhida, self.nome_componente_escolhido))
        elif num == 7:
            dado = (ob.calcMes(self.id_maquina_escolhida, self.nome_componente_escolhido))
        return dado

    def definir_dados_singular(self, num):
        from algGraphs import AlgoritmoGraficos
        ob = AlgoritmoGraficos()
        if num == 0:
            dado = (ob.calcHora(self.id_maquina_escolhida, self.nome_componente_escolhido))
        elif num == 1:
            dado = (ob.calcDia(self.id_maquina_escolhida, self.nome_componente_escolhido))
        elif num == 2:
            dado = (ob.calcSemana(self.id_maquina_escolhida, self.nome_componente_escolhido))
        elif num == 3:
            dado = (ob.calcMes(self.id_maquina_escolhida, self.nome_componente_escolhido))
        return dado

    def async_define_singular(self):
        import multiprocessing as mp
        pool = mp.Pool(mp.cpu_count())
        results = []
        results = pool.map_async(self.definir_dados_singular, range(4)).get()
        pool.close()
        pool.join()
        for i in range(len(results)):
            if i == 0:
                self.umaHora = results[i]
            elif i == 1:
                self.umDia = results[i]
            elif i == 2:
                self.umaSemana = results[i]
            elif i == 3:
                self.umMes = results[i]

    def async_define(self):
        import multiprocessing as mp
        pool = mp.Pool(mp.cpu_count())
        results = []
        results = pool.map_async(self.definir_dados, range(8)).get()
        pool.close()
        pool.join()
        for i in range(len(results)):
            if i == 0:
                self.umaHora = results[i]
            elif i == 1:
                self.duasHoras = results[i]
            elif i == 2:
                self.umDia = results[i]
            elif i == 3:
                self.umDiaInteiro = results[i]
            elif i == 4:
                self.doisDias = results[i]
            elif i == 5:
                self.umaSemana = results[i]
            elif i == 6:
                self.duasSemanas = results[i]
            elif i == 7:
                self.umMes = results[i]

    def calcNormal(self):
        dataNormal = [self.umaHora, self.umDia, self.umaSemana, self.umMes]
        menorMedia = [100000]
        for d in dataNormal:
            # print(d[0])
            if bool(d):
                multiplicaValores = 1
                for i in range(0, len(d[0])):
                    multiplicaValores = multiplicaValores * d[0][i]
                mediaAtual = float((multiplicaValores ** (1 / len(d[0]))))
                if mediaAtual < menorMedia[0]:
                    menorMedia = [mediaAtual, d]

        return menorMedia

    def calcDuplo(self):
        dataDuplo = [self.duasHoras, self.doisDias, self.duasSemanas]
        menorMediaDuplo = [100000]
        for d in dataDuplo:
            # print(d[0])
            mediaAtual = 0
            valCont = 0
            for val in range(len(d[0])):
                if len(d[0][val]) != 0:
                    mediaAtual += sum(d[0][val]) / len(d[0][val])
                    valCont = val + 1
            mediaAtual = mediaAtual / valCont
            if mediaAtual < menorMediaDuplo[0]:
                menorMediaDuplo = [mediaAtual, d]

        return menorMediaDuplo


def main():
    import algGraphs as algGraphs

    ob = algGraphs.AlgoritmoGraficos()

    umaHora = ob.calcHora()
    duasHoras = ob.calcDuasHoras() # DUPLO
    umDia = ob.calcDia()
    umDiaInteiro = ob.calcDiaInteiro()
    doisDias = ob.calcDoisDias() # DUPLO
    umaSemana = ob.calcSemana()
    duasSemanas = ob.calcDuasSemanas() # DUPLO
    umMes = ob.calcMes()

    dataNormal = [umaHora, umDia, umDiaInteiro, umaSemana, umMes]
    dataDuplo = [duasHoras, doisDias, duasSemanas]
    menorMedia = [100000]
    menorMediaDuplo = [100000]

    for d in dataNormal:
        # print(d[0])
        # mediaAtual = sum(d[0]) / len(d[0])
        multiplicaValores = 1
        for i in range(0, len(d[0])):
            multiplicaValores = multiplicaValores * d[0][i]
        mediaAtual = float((multiplicaValores ** (1 / len(d[0]))))

        print("MÉDIA =", mediaAtual)
        if mediaAtual < menorMedia[0]:
            menorMedia = [mediaAtual, d]

    print(round((menorMedia[0]), 2), "\n", menorMedia[1])
    # import graficos
    # graficos.linha(menorMedia[1][1], menorMedia[1][0], menorMedia[1][2], True)
    for d in dataDuplo:
        # print(d[0])
        mediaAtual = 0
        valCont = 0
        for val in range(len(d[0])):
            if len(d[0][val]) != 0:
                mediaAtual += sum(d[0][val]) / len(d[0][val])
                valCont = val + 1
        mediaAtual = mediaAtual / valCont
        print("MÉDIA =", mediaAtual)
        if mediaAtual < menorMediaDuplo[0]:
            menorMediaDuplo = [mediaAtual, d]

    print(round((menorMediaDuplo[0]), 2), "\n", menorMediaDuplo[1])
    # import graficos
    # graficos.linhaDuplo(menorMediaDuplo[1][1], menorMediaDuplo[1][0], menorMediaDuplo[1][2], ['Esta Hora', 'Hora passada'], True)


if __name__ == '__main__':
    import time
    s = time.perf_counter()
    # main()
    print("Tratando dados para gráficos...")
    self = DataGraphs(3, "CPU")
    data = self.calcNormal()
    for x in data:
        print(x)
    # self.async_define()
    # print(self.umDiaInteiro)
    # print(self.umDia)
    # a = self.calcNormal()
    # print(round(sum(a[1][0]) / len(a[1][0])))
    dataNormal = [
        self.umaHora,
        self.umDia,
        self.umDiaInteiro,
        self.umaSemana,
        self.umMes
    ]
    dataDuplo = [self.duasHoras, self.doisDias, self.duasSemanas]
    print("\nDados singulares")
    for i in dataNormal:
        print(i)
    print("\nDados duplos")
    for j in dataDuplo:
        print(j)

    elapsed = time.perf_counter() - s
    print(f"\n{__file__} executed in {elapsed:0.2f} seconds.")
