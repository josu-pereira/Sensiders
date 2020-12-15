class AlgoritmoGraficos:
    def __init__(self):
        self.valores = []
        self.valores_segundo = []
        self.hora = []
        self.hora_segundo = []
        self.ultimoDado = 0
        self.temp = 0
        self.sql = None
        self.connBanco()

        # self.hr = 3600
        # self.dia = 0
        # self.smn = 0

    def connBanco(self):
        from sqlAzure import Sql
        self.sql = Sql('adminlocal', '#Gfgrupo11c', '1433', 'bdProjetoSensiders', 'serversensiders.database.windows.net')
        self.sql.connect()

    def calcHora(self, id_maquina, nome_componente):
        from datetime import datetime

        # horaDado = self.conn.selectUltimaHora(3, 3)
        horaDado = self.sql.selectUltimaHora(id_maquina, nome_componente)
        if bool(horaDado):
            self.ultimoDado = horaDado[-1][-1]

            totalDado = 0
            qntd = 0
            self.valores = []
            self.hora = []
            self.temp = 450

            for i in range(len(horaDado)):
                pos = (i * -1) - 1
                ts = round(datetime.timestamp(horaDado[pos][-1]))
                for j in range(-4, 8):
                    if ts == round(datetime.timestamp(self.ultimoDado)) - self.temp - j:
                        self.hora.append(str(round(self.temp / 60)) + " min")
                        self.valores.append(round((totalDado / qntd), 1))
                        self.temp += 450
                        # hora.append(datetime.fromtimestamp(ts))
                        totalDado = 0
                        qntd = 0
                    else:
                        totalDado += float(horaDado[pos][0])
                        qntd += 1

            self.hora.append(str(round(self.temp / 60)) + " min")
            self.valores.append(round((totalDado / qntd), 1))
            dados = [self.valores, self.hora, horaDado[0][1]]
            return dados
        else:
            return horaDado

    def calcDuasHoras(self, id_maquina, nome_componente):
        from datetime import datetime

        # duashorasDado = self.conn.selectDuasHora(3,3)
        duashorasDado = self.sql.selectDuasHora(id_maquina, nome_componente)
        if not bool(duashorasDado):
            return duashorasDado
        else:
            self.ultimoDado = duashorasDado[-1][-1]

            inicial_segundo_loop = 0
            totalDado = 0
            qntd = 0
            self.valores = []
            self.valores_segundo = []
            self.hora = []
            self.hora_segundo = []
            self.temp = 450 # 8 MINUTOS
            terminou_loop = False

            for i in range(len(duashorasDado)):
                pos = (i * -1) - 1
                ts = round(datetime.timestamp(duashorasDado[pos][-1]))
                for j in range(-4, 8):
                    if ts == round(datetime.timestamp(self.ultimoDado)) - self.temp - j:
                        self.hora.append(str(round(self.temp / 60)) + " min")
                        self.valores.append(round((totalDado / qntd), 1))
                        self.temp += 450
                        # hora.append(datetime.fromtimestamp(ts))
                        totalDado = 0
                        qntd = 0
                        if self.temp == 4050:
                            terminou_loop = True
                            break
                    else:
                        totalDado += float(duashorasDado[pos][0])
                        qntd += 1
                if terminou_loop:
                    inicial_segundo_loop = i
                    break

            #self.hora.append(str(round(self.temp / 60)) + " min")
            #self.valores.append(round((totalDado / qntd), 1))

            for i in range(inicial_segundo_loop, len(duashorasDado)):
                pos = (i * -1) - 1
                ts = round(datetime.timestamp(duashorasDado[pos][-1]))
                for j in range(-4, 8):
                    if ts == round(datetime.timestamp(self.ultimoDado)) - self.temp - j:
                        self.hora_segundo.append(str(round(self.temp / 60)) + " min")
                        self.valores_segundo.append(round((totalDado / qntd), 1))
                        self.temp += 450
                        # hora.append(datetime.fromtimestamp(ts))
                        totalDado = 0
                        qntd = 0
                    else:
                        totalDado += float(duashorasDado[pos][0])
                        qntd += 1

            self.hora_segundo.append(str(round(self.temp / 60)) + " min")
            self.valores_segundo.append(round((totalDado / qntd), 1))

            dados = [[self.valores, self.valores_segundo], [self.hora, self.hora_segundo], duashorasDado[0][1]]
            return dados

    def calcDia(self, id_maquina, nome_componente):
        from datetime import datetime

        # diaDado = self.conn.selectDia(3,3)
        diaDado = self.sql.selectDia(id_maquina, nome_componente)
        if not bool(diaDado):
            return diaDado
        else:
            self.ultimoDado = diaDado[-1][-1]

            totalDado = 0
            qntd = 0
            self.valores = []
            self.hora = []
            self.temp = 10800 / 3  # 3 horas (180 minutos)

            for i in range(len(diaDado)):
                pos = (i * -1) - 1
                ts = round(datetime.timestamp(diaDado[pos][-1]))
                for j in range(-4, 8):
                    if ts == round(datetime.timestamp(self.ultimoDado)) - self.temp - j:
                        self.hora.append(str(round(self.temp / 3600)) + " hrs")
                        self.valores.append(round((totalDado / qntd), 1))
                        self.temp += 10800 / 3
                        # hora.append(datetime.fromtimestamp(ts))
                        totalDado = 0
                        qntd = 0
                    else:
                        totalDado += float(diaDado[pos][0])
                        qntd += 1

            self.hora.append(str(round(self.temp / 3600)) + " hrs")
            self.valores.append(round((totalDado / qntd), 1))
            dados = [self.valores, self.hora, diaDado[0][1]]
            return dados

    def calcDiaInteiro(self, id_maquina, nome_componente):
        from datetime import datetime

        # diaDado = self.conn.selectDia(3,3)
        diaDado = self.sql.selectDia(id_maquina, nome_componente)
        if not bool(diaDado):
            return diaDado
        else:
            self.ultimoDado = diaDado[-1][-1]

            totalDado = 0
            qntd = 0
            self.valores = []
            self.hora = []
            self.temp = 7200  # 2 horas (120 minutos)

            for i in range(len(diaDado)):
                pos = (i * -1) - 1
                ts = round(datetime.timestamp(diaDado[pos][-1]))
                for j in range(-4, 8):
                    if ts == round(datetime.timestamp(self.ultimoDado)) - self.temp - j:
                        self.hora.append(str(round(self.temp / 3600)) + " hrs")
                        self.valores.append(round((totalDado / qntd), 1))
                        self.temp += 7200
                        # hora.append(datetime.fromtimestamp(ts))
                        totalDado = 0
                        qntd = 0
                    else:
                        totalDado += float(diaDado[pos][0])
                        qntd += 1

            self.hora.append(str(round(self.temp / 3600)) + " hrs")
            self.valores.append(round((totalDado / qntd), 1))
            dados = [self.valores, self.hora, diaDado[0][1]]
            return dados

    def calcDoisDias(self, id_maquina, nome_componente):
        from datetime import datetime

        # doisdiasDado = self.conn.selectDoisDias(3, 3)
        doisdiasDado = self.sql.selectDoisDias(id_maquina, nome_componente)
        if not bool(doisdiasDado):
            return doisdiasDado
        else:

            self.ultimoDado = doisdiasDado[-1][-1]

            inicial_segundo_loop = 0
            totalDado = 0
            qntd = 0
            self.valores = []
            self.valores_segundo = []
            self.hora = []
            self.hora_segundo = []
            self.temp = 3600  # 1 hora
            terminou_loop = False

            for i in range(len(doisdiasDado)):
                pos = (i * -1) - 1
                ts = round(datetime.timestamp(doisdiasDado[pos][-1]))
                for j in range(-4, 8):
                    if ts == round(datetime.timestamp(self.ultimoDado)) - self.temp - j:
                        self.hora.append(str(round(self.temp / 3600)) + " hrs")
                        self.valores.append(round((totalDado / qntd), 1))
                        self.temp += 3600
                        # hora.append(datetime.fromtimestamp(ts))
                        totalDado = 0
                        qntd = 0
                        if self.temp == 86400:
                            terminou_loop = True
                            break
                    else:
                        totalDado += float(doisdiasDado[pos][0])
                        qntd += 1
                if terminou_loop:
                    inicial_segundo_loop = i
                    break

            inseriuSegundoDia = False
            for i in range(inicial_segundo_loop, len(doisdiasDado)):
                pos = (i * -1) - 1
                ts = round(datetime.timestamp(doisdiasDado[pos][-1]))
                for j in range(-4, 8):
                    if ts == round(datetime.timestamp(self.ultimoDado)) - self.temp - j:
                        self.hora_segundo.append(str(round(self.temp / 3600)) + " hrs")
                        self.valores_segundo.append(round((totalDado / qntd), 1))
                        self.temp += 3600
                        # hora.append(datetime.fromtimestamp(ts))
                        totalDado = 0
                        qntd = 0
                        inseriuSegundoDia = True
                    else:
                        totalDado += float(doisdiasDado[pos][0])
                        qntd += 1

            if inseriuSegundoDia:
                self.hora_segundo.append(str(round(self.temp / 3600)) + " hrs")
                self.valores_segundo.append(round((totalDado / qntd), 1))
            dados = [[self.valores, self.valores_segundo], [self.hora, self.hora_segundo], doisdiasDado[0][1]]
            return dados

    def calcSemanaOLD(self, id_maquina, nome_componente):
        from datetime import datetime
        # semanaDado = self.conn.selectSemana(3, 3)
        semanaDado = self.sql.selectSemana(id_maquina, nome_componente)
        if not bool(semanaDado):
            return semanaDado
        else:
            self.ultimoDado = semanaDado[-1][-1]

            totalDado = 0
            qntd = 0
            self.valores = []
            self.hora = []
            self.temp = 75600  # 21 horas (1260 minutos)

            for i in range(len(semanaDado)):
                pos = (i * -1) - 1
                ts = round(datetime.timestamp(semanaDado[pos][-1]))
                for j in range(-4, 8):
                    if ts == round(datetime.timestamp(self.ultimoDado)) - self.temp - j:
                        self.hora.append(str(round(self.temp / 3600)) + " hrs")
                        self.valores.append(round((totalDado / qntd), 1))
                        self.temp += 75600
                        # hora.append(datetime.fromtimestamp(ts))
                        totalDado = 0
                        qntd = 0
                    else:
                        totalDado += float(semanaDado[pos][0])
                        qntd += 1

            self.hora.append(str(round(self.temp / 3600)) + " hrs")
            self.valores.append(round((totalDado / qntd), 1))
            dados = [self.valores, self.hora, semanaDado[0][1]]
            return dados

    def calcSemana(self, id_maquina, nome_componente):
        import time
        # semanaDado = self.conn.selectSemana(3, 3)
        semanaDado = self.sql.selectSemana(id_maquina, nome_componente)
        if not bool(semanaDado):
            return semanaDado
        else:
            self.ultimoDado = semanaDado[-1][-1]
            mesUltimoDia = self.ultimoDado.day

            qtdDias = 0
            totalDado = 0
            qntd = 0
            self.valores = []
            self.hora = []

            i = 0
            while i < len(semanaDado):
                pos = (i * -1) - 1
                if semanaDado[pos][-1].day == mesUltimoDia:
                    totalDado += float(semanaDado[pos][0])
                    qntd += 1
                else:
                    if totalDado != 0:
                        diasAtras = time.localtime().tm_mday - mesUltimoDia
                        if diasAtras < 0:
                            diasAtras += 30
                        if diasAtras != 0:
                            self.hora.append(str(diasAtras) + " dias")
                        else:
                            self.hora.append("hoje")
                        self.valores.append(round((totalDado / qntd), 1))
                    qtdDias += 1
                    if mesUltimoDia - 1 == 0:
                        mesUltimoDia = 31
                        i -= 1
                    else:
                        mesUltimoDia -= 1
                        i -= 1
                    totalDado = 0
                    qntd = 0
                i += 1

            diasAtras = time.localtime().tm_mday - mesUltimoDia
            if diasAtras < 0:
                diasAtras = abs(diasAtras) + time.localtime().tm_mday
            self.hora.append(str(diasAtras) + " dias")
            self.valores.append(round((totalDado / qntd), 1))
            dados = [self.valores, self.hora, semanaDado[0][1]]
            return dados

    def calcDuasSemanas(self, id_maquina, nome_componente):
        import time

        # duasSemanasDado = self.conn.selectQuacDias(3, 3)
        duasSemanasDado = self.sql.selectQuacDias(id_maquina, nome_componente)
        if not bool(duasSemanasDado):
            return duasSemanasDado
        else:
            self.ultimoDado = duasSemanasDado[-1][-1]
            diaAtual = self.ultimoDado.day

            inicial_segundo_loop = 0
            qtdDias = 0
            totalDado = 0
            qntd = 0
            self.valores = []
            self.valores_segundo = []
            self.hora = []
            self.hora_segundo = []

            i = 0
            while i < len(duasSemanasDado):
                pos = (i * -1) - 1
                if duasSemanasDado[pos][-1].day == diaAtual:
                    totalDado += float(duasSemanasDado[pos][0])
                    qntd += 1
                else:
                    if totalDado != 0:
                        diasAtras = time.localtime().tm_mday - diaAtual
                        if diasAtras < 0:
                            diasAtras += 30
                        if diasAtras != 0:
                            self.hora.append(str(diasAtras) + " dias")
                        else:
                            self.hora.append("hoje")
                        self.valores.append(round((totalDado / qntd), 1))
                    qtdDias += 1
                    if diaAtual - 1 == 0:
                        diaAtual = 31
                        i -= 1
                    else:
                        diaAtual -= 1
                        i -= 1
                    if diasAtras == 7:
                        break
                    totalDado = 0
                    qntd = 0
                i += 1

            if totalDado != 0:
                diasAtras = time.localtime().tm_mday - diaAtual
                if diasAtras < 0:
                    diasAtras += 30
                self.hora.append(str(diasAtras) + " dias")
                self.valores.append(round((totalDado / qntd), 1))
            totalDado = 0
            qntd = 0

            while i < len(duasSemanasDado):
                pos = (i * -1) - 1
                if duasSemanasDado[pos][-1].day == diaAtual:
                    totalDado += float(duasSemanasDado[pos][0])
                    qntd += 1
                else:
                    if totalDado != 0:
                        diasAtras = time.localtime().tm_mday - diaAtual
                        if diasAtras < 0:
                            diasAtras += 30
                        if diasAtras != 0:
                            self.hora.append(str(diasAtras) + " dias")
                        else:
                            self.hora.append("hoje")
                        self.valores_segundo.append(round((totalDado / qntd), 1))
                    qtdDias += 1
                    if diaAtual - 1 == 0:
                        diaAtual = 31
                        i -= 1
                    else:
                        diaAtual -= 1
                        i -= 1
                    totalDado = 0
                    qntd = 0
                i += 1

            if totalDado != 0:
                diasAtras = time.localtime().tm_mday - diaAtual
                if diasAtras < 0:
                    diasAtras += 30
                self.hora_segundo.append(str(diasAtras) + " dias")
                self.valores_segundo.append(round((totalDado / qntd), 1))
            dados = [[self.valores, self.valores_segundo], [self.hora, self.hora_segundo], duasSemanasDado[0][1]]
            return dados

    def calcMes(self, id_maquina, nome_componente):
        import time

        # mesDado = self.conn.selectMes(3, 3)
        mesDado = self.sql.selectMes(id_maquina, nome_componente)
        if not bool(mesDado):
            return mesDado
        else:
            self.ultimoDado = mesDado[-1][-1]
            mesUltimoDia = self.ultimoDado.day
            qtdDias = 0

            totalDado = 0
            qntd = 0
            self.valores = []
            self.hora = []

            i = 0
            while i < len(mesDado):
                pos = (i * -1) - 1
                if mesDado[pos][-1].day == mesUltimoDia:
                    totalDado += float(mesDado[pos][0])
                    qntd += 1
                else:
                    if totalDado != 0:
                        diasAtras = time.localtime().tm_mday - mesUltimoDia
                        if diasAtras < 0:
                            # diasAtras = abs(diasAtras) + time.localtime().tm_mday
                            diasAtras += 30
                        if diasAtras != 0:
                            self.hora.append(str(diasAtras) + " dias")
                        else:
                            self.hora.append("hoje")
                        self.valores.append(round((totalDado / qntd), 1))
                    qtdDias += 1
                    if mesUltimoDia - 1 == 0:
                        mesUltimoDia = 31
                        i -= 1
                    else:
                        mesUltimoDia -= 1
                        i -= 1
                    totalDado = 0
                    qntd = 0
                i += 1

            diasAtras = time.localtime().tm_mday - mesUltimoDia
            if diasAtras < 0:
                diasAtras += 30
            self.hora.append(str(diasAtras) + " dias")
            self.valores.append(round((totalDado / qntd), 1))
            dados = [self.valores, self.hora, mesDado[0][1]]
            return dados

    def resetData(self):
        self.valores = []
        self.hora = []
        self.ultimoDado = 0
        self.temp = 0
