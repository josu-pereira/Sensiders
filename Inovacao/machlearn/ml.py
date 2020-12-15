class BancoML:
    def __init__(self):
        self.resposta = ""
        self.quantidade = 0
        self.__con = object
        self.__c = object

    def __iniciarBanco(self):
        import sqlite3
        self.__con = sqlite3.connect("machlearn/machlearn.db")
        self.__c = self.__con.cursor()
        self.__criarBanco()

    def __criarBanco(self):
        self.__c.execute(
            "CREATE TABLE IF NOT EXISTS palavras (palavra TEXT, geraDado INTEGER, dataHora DATETIME)"
        )

    def __deletarBanco(self):
        self.__c.execute("DROP TABLE palavras")

    def __deletarTabelas(self):
        self.__c.execute("DELETE FROM palavras")

    def insertBanco(self, dados):
        self.__iniciarBanco()
        dados = tuple(dados,)
        self.__c.execute("INSERT INTO palavras(palavra, geraDado, dataHora) VALUES (?, ?, ?)", dados)
        self.__con.commit()

    def separa_palavras(self, texto):
        import re
        sentencas = re.split(r'(\W+)', texto)
        if sentencas[-1] == '':
            del sentencas[-1]
        return sentencas

    def getDateTime(self):
        import time
        t = time.localtime()
        valTEMPO = (f'{t[0]}-{t[1]}-{t[2]} {t[3]}:{t[4]}:{t[5]}')
        return valTEMPO

    def selectBanco(self):
        self.__iniciarBanco()
        dadosSelect = self.__c.execute("SELECT palavra, geraDado, dataHora FROM palavras")
        selectAll = dadosSelect.fetchall()
        return selectAll

    def iniciar(self, texto, conseguiuInserir = 1):
        from machlearn.stpwrd import stopwordPT
        stopwords = stopwordPT()
        self.resposta = texto
        self.__iniciarBanco()
        self.resposta = self.separa_palavras(self.resposta)
        for palavra in self.resposta:
            if palavra != "" and palavra != " " and palavra not in stopwords:
                datahora = self.getDateTime()
                self.insertBanco([palavra, 1, datahora])

    def inserirBanco(self, texto, conseguiuInserir = 1):
        from machlearn.stpwrd import stopwordPT
        stopwords = stopwordPT()
        self.resposta = texto
        for palavra in self.resposta:
            if palavra != "" and palavra != " " and palavra not in stopwords:
                datahora = self.getDateTime()
                self.insertBanco([palavra, conseguiuInserir, datahora])
        print("Inserido texto para ML")

if __name__ == "__main__":
    ml = BancoML()
