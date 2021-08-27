class Banco:
    def __init__(self):
        self.execSql = object

    def conectarBanco(self):
        import pyodbc
        import datetime

        server = 'serversensiders.database.windows.net'
        database = 'bdProjetoSensiders'
        user = 'adminlocal'
        password = '#Gfgrupo11c'
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server}' + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + user + ';PWD=' + password)

        self.execSql = conn.cursor()

    def selectUltimaHora(self, maq, comp):
        self.conectarBanco()
        self.execSql.execute("Exec sp_DadosUltimaHora %s, %s" % (maq, comp))
        result = self.execSql.fetchall()
        return result

    def selectDuasHora(self, maq, comp):
        self.conectarBanco()
        self.execSql.execute("Exec sp_DadosUltimaDuasHora %s, %s" % (maq, comp))
        result = self.execSql.fetchall()
        return result

    def selectDia(self, maq, comp):
        self.conectarBanco()
        self.execSql.execute("Exec sp_DadosUltimoDia %s, %s" % (maq, comp))
        result = self.execSql.fetchall()
        return result

    def selectDoisDias(self, maq, comp):
        self.conectarBanco()
        self.execSql.execute("Exec sp_DadosUltimoDoisDias %s, %s" % (maq, comp))
        result = self.execSql.fetchall()
        return result

    def selectSemana(self, maq, comp):
        self.conectarBanco()
        self.execSql.execute("Exec sp_DadosUltimaSemana %s, %s" % (maq, comp))
        result = self.execSql.fetchall()
        return result

    def selectQuacDias(self, maq, comp):
        self.conectarBanco()
        self.execSql.execute("Exec sp_DadosUltimosQuacDias %s, %s" % (maq, comp))
        result = self.execSql.fetchall()
        return result

    def selectMes(self, maq, comp):
        self.conectarBanco()
        self.execSql.execute("Exec sp_DadosUltimoMes %s, %s" % (maq, comp))
        result = self.execSql.fetchall()
        return result
