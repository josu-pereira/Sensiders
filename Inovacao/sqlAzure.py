import pyodbc

class Sql:
    def __init__(self, user, password, port, database, server):
        self.user = user
        self.password = password
        self.port = port
        self.database = database
        self.server = server
        self.sql = None
        self.cursor = None

    #Estabelecendo uma conexão
    def connect(self):
        try:
            self.sql = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}'+';SERVER='+self.server+';PORT='+self.port+';DATABASE='+self.database+';UID='+self.user+';PWD='+self.password)
            #Criando cursor para manipulação do banco.
            print(self.sql)
            self.cursor = self.sql.cursor()
        except Exception as err:
            print(err)
            raise

    def selectComp(self, maquina): # função do select que retorna o componente + idMaqComp
        sql_select_query = ("select nomeComponente, idMaqComp from MaquinaComponente, Componente, Maquina where fkMaquina = idMaquina and fkComponente = idComponente and idMaquina = " + str(maquina))
        try:
            self.cursor.execute(sql_select_query)
            dadosColetados = self.cursor.fetchall()
            return dadosColetados
        except Exception as err:
            print(err)
            self.close()

    def selectCompByName(self, NomeMaquina): # função do select que retorna o componente + idMaqComp
        sql_select_query = ("select nomeComponente, idMaqComp from MaquinaComponente, Componente, Maquina where fkMaquina = idMaquina and fkComponente = idComponente and descricaoMaquina = '" + str(NomeMaquina) + "'")
        try:
            self.cursor.execute(sql_select_query)
            dadosColetados = self.cursor.fetchall()
            return dadosColetados
        except Exception as err:
            print(err)
            self.close()

    def selectResult(self, maquina):
        sql_select_query = ("select top 8 leitura, nomeComponente, dataHora from LeituraMaquina, MaquinaComponente, Componente, Maquina where fkMaquina = idMaquina and fkComponente = idComponente and idMaqComp = fkMaqComp and fkMaquina = " + str(maquina) + " order by dataHora desc")
        try:
            self.cursor.execute(sql_select_query)
            dadosColetados = self.cursor.fetchall()
            return dadosColetados
        except Exception as err:
            print(err)
            self.close()

    def selectResultComp(self, maquina, componente):
        sql_select_query = ("select top 8 leitura, nomeComponente, dataHora from LeituraMaquina, MaquinaComponente, Componente, Maquina where fkMaquina = idMaquina and fkComponente = idComponente and idMaqComp = fkMaqComp and fkMaquina = " + str(maquina) + " and nomeComponente = '" + componente + "' order by dataHora desc")
        try:
            self.cursor.execute(sql_select_query)
            dadosColetados = self.cursor.fetchall()
            return dadosColetados
        except Exception as err:
            print(err)
            self.close()

    def selectAvgComp(self, maquina, componente):
        sql_select_query = ("select leitura from LeituraMaquina, MaquinaComponente, Componente, Maquina where fkMaquina = idMaquina and fkComponente = idComponente and idMaqComp = fkMaqComp and fkMaquina = " + str(maquina) + " and nomeComponente = '" + componente + "' order by dataHora desc")
        try:
            self.cursor.execute(sql_select_query)
            dadosColetados = self.cursor.fetchall()
            return dadosColetados
        except Exception as err:
            print(err)
            self.close()

    def selectMachines(self):
        sql_select_query = ("select idMaquina, descricaoMaquina from Maquina")
        try:
            self.cursor.execute(sql_select_query)
            dadosColetados = self.cursor.fetchall()
            return dadosColetados
        except Exception as err:
            print(err)
            self.close()

    def selectMachinesByComp(self, componente):
        sql_select_query = ("select descricaoMaquina, idMaquina, nomeComponente from Maquina, Componente, MaquinaComponente where fkMaquina = idMaquina and fkComponente = idComponente and nomeComponente = ?")
        try:
            self.cursor.execute(sql_select_query, componente)
            dadosColetados = self.cursor.fetchall()
            return dadosColetados
        except Exception as err:
            print(err)
            self.close()

    def newInsert(self, data): # função do novo insert de leitura dos componentes que o cliente escolheu
        query = ("INSERT INTO LeituraMaquina (leitura, dataHora, fkMaqComp) VALUES (?, ?, ?)")
        values = data
        try:
            print('Inserindo Valores')
            self.cursor.execute(query,values)
            self.sql.commit()
        except Exception as err:
            print(err)
            self.sql.rollback()
            self.close()
    
    def selectUltimaHora(self, id_maquina, nome_componente):
        query = "SELECT LeituraMaquina.leitura, Componente.nomeComponente, LeituraMaquina.dataHora " \
                "FROM LeituraMaquina " \
                "INNER JOIN MaquinaComponente on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp " \
                "INNER JOIN Componente ON Componente.idComponente = MaquinaComponente.fkComponente " \
                "WHERE dataHora >= DATEADD(HOUR, -4, GETDATE()) " \
                "AND Componente.nomeComponente = ? AND MaquinaComponente.fkMaquina = ?"
        try:
            self.cursor.execute(query, nome_componente, id_maquina)
            # self.cursor.execute("Exec sp_DadosUltimaHora %s, %s" % (nome_componente, id_maquina))
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            print(err)
            self.close()

    def selectDuasHora(self, id_maquina, nome_componente):
        query = "SELECT LeituraMaquina.leitura, Componente.nomeComponente, LeituraMaquina.dataHora " \
                "FROM LeituraMaquina " \
                "INNER JOIN MaquinaComponente " \
                "on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp " \
                "INNER JOIN Componente " \
                "ON Componente.idComponente = MaquinaComponente.fkComponente " \
                "WHERE dataHora >= DATEADD(HOUR, -5, GETDATE()) " \
                "AND Componente.nomeComponente = ? " \
                "AND MaquinaComponente.fkMaquina = ?"
        try:
            self.cursor.execute(query, nome_componente, id_maquina)
            # self.cursor.execute("Exec sp_DadosUltimaDuasHora %s, %s" % (nome_componente, id_maquina))
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            print(err)
            self.close()

    def selectDia(self, id_maquina, nome_componente):
        query = "SELECT LeituraMaquina.leitura, Componente.nomeComponente, LeituraMaquina.dataHora " \
                "FROM LeituraMaquina " \
                "INNER JOIN MaquinaComponente " \
                "on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp " \
                "INNER JOIN Componente " \
                "ON Componente.idComponente = MaquinaComponente.fkComponente " \
                "WHERE dataHora >= DATEADD(DAY, -1, GETDATE()) " \
                "AND Componente.nomeComponente = ? " \
                "AND MaquinaComponente.fkMaquina = ?"
        try:
            self.cursor.execute(query, nome_componente, id_maquina)
            # self.cursor.execute("Exec sp_DadosUltimoDia %s, %s" % (nome_componente, id_maquina))
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            print(err)
            self.close()

    def selectDoisDias(self, id_maquina, nome_componente):
        query = "SELECT LeituraMaquina.leitura, Componente.nomeComponente, LeituraMaquina.dataHora " \
                "FROM LeituraMaquina " \
                "INNER JOIN MaquinaComponente " \
                "on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp " \
                "INNER JOIN Componente " \
                "ON Componente.idComponente = MaquinaComponente.fkComponente " \
                "WHERE dataHora >= DATEADD(DAY, -2, GETDATE()) " \
                "AND Componente.nomeComponente = ? " \
                "AND MaquinaComponente.fkMaquina = ?"
        try:
            self.cursor.execute(query, nome_componente, id_maquina)
            # self.cursor.execute("Exec sp_DadosUltimoDoisDias %s, %s" % (nome_componente, id_maquina))
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            print(err)
            self.close()

    def selectSemana(self, id_maquina, nome_componente):
        query = "SELECT LeituraMaquina.leitura, Componente.nomeComponente, LeituraMaquina.dataHora " \
                "FROM LeituraMaquina " \
                "INNER JOIN MaquinaComponente " \
                "on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp " \
                "INNER JOIN Componente " \
                "ON Componente.idComponente = MaquinaComponente.fkComponente " \
                "WHERE dataHora >= DATEADD(WEEK, -1, GETDATE()) " \
                "AND Componente.nomeComponente = ? " \
                "AND MaquinaComponente.fkMaquina = ?"
        try:
            self.cursor.execute(query, nome_componente, id_maquina)
            # self.cursor.execute("Exec sp_DadosUltimaSemana %s, %s" % (nome_componente, id_maquina))
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            print(err)
            self.close()

    def selectQuacDias(self, id_maquina, nome_componente):
        query = "SELECT LeituraMaquina.leitura, Componente.nomeComponente, LeituraMaquina.dataHora " \
                "FROM LeituraMaquina " \
                "INNER JOIN MaquinaComponente " \
                "on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp " \
                "INNER JOIN Componente " \
                "ON Componente.idComponente = MaquinaComponente.fkComponente " \
                "WHERE dataHora >= DATEADD(DAY, -14, GETDATE()) " \
                "AND Componente.nomeComponente = ? " \
                "AND MaquinaComponente.fkMaquina = ?"
        try:
            self.cursor.execute(query, nome_componente, id_maquina)
            # self.cursor.execute("Exec sp_DadosUltimosQuacDias %s, %s" % (nome_componente, id_maquina))
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            print(err)
            self.close()

    def selectMes(self, id_maquina, nome_componente):
        query = "SELECT LeituraMaquina.leitura, Componente.nomeComponente, LeituraMaquina.dataHora " \
                "FROM LeituraMaquina " \
                "INNER JOIN MaquinaComponente " \
                "on MaquinaComponente.idMaqComp = LeituraMaquina.fkMaqComp " \
                "INNER JOIN Componente " \
                "ON Componente.idComponente = MaquinaComponente.fkComponente " \
                "WHERE dataHora >= DATEADD(MONTH, -1, GETDATE()) " \
                "AND Componente.nomeComponente = ? " \
                "AND MaquinaComponente.fkMaquina = ?"
        try:
            self.cursor.execute(query, nome_componente, id_maquina)
            # self.cursor.execute("Exec sp_DadosUltimoMes %s, %s" % (nome_componente, id_maquina))
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            print(err)
            self.close()
    
    # Fechando conexão
    def close(self):
        self.sql.close()


if __name__ == '__main__':
    # TESTE DO SELECT
    a = Sql('adminlocal', '#Gfgrupo11c', '1433', 'bdProjetoSensiders', 'serversensiders.database.windows.net')
    a.connect()
    b = a.selectUltimaHora(3, "CPU")
    print(b)
