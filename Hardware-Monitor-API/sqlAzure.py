from analiseHardware import enviarMensagemSlack
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
            print("Azure =", self.sql)
            self.cursor = self.sql.cursor()
        except Exception as err:
            print(err)
            enviarMensagemSlack("\nERRO:\nConexão com o banco de dados falhou!")
            raise

    def selectComp(self, maquina): # função do select que retorna o componente + idMaqComp
        sql_select_query = ("select nomeComponente, idMaqComp from MaquinaComponente, Componente, Maquina where fkMaquina = idMaquina and fkComponente = idComponente and hashmac = ?")
        try:
            self.cursor.execute(sql_select_query, maquina)
            dadosColetados = self.cursor.fetchall()
            return dadosColetados
        except Exception as err:
            print(err)
            enviarMensagemSlack("\nERRO:\nSelect no banco de dados falhou!")
            self.close()
    
    def select_machine_name(self, hashmac):
        sql_select_query = ("SELECT descricaoMaquina FROM Maquina where hashmac = ?")
        try:
            self.cursor.execute(sql_select_query, hashmac)
            dadosColetados = self.cursor.fetchall()
            return dadosColetados
        except Exception as err:
            print(err)
            enviarMensagemSlack("\nERRO:\nSelect no banco de dados falhou!")
            self.close()

    def newInsert(self, data): # função do novo insert de leitura dos componentes que o cliente escolheu
        query = ("INSERT INTO LeituraMaquina (leitura, dataHora, fkMaqComp) VALUES (?, ?, ?)")
        values = data
        try:
            self.cursor.execute(query,values)
            self.sql.commit()
            print('Valores Inseridos no Azure')
        except Exception as err:
            print(err)
            self.sql.rollback()
            enviarMensagemSlack("\nERRO:\nInsert no banco de dados falhou!")
            self.close()

    def multi_insert(self, data): # função do novo insert de leitura dos componentes que o cliente escolheu
        query = ("INSERT INTO LeituraMaquina (leitura, dataHora, fkMaqComp) VALUES (?, ?, ?)")
        values = data
        try:
            for i in data:
                self.cursor.execute(query, i)
            self.sql.commit()
            print('Valores Inseridos no Azure')
        except Exception as err:
            print(err)
            self.sql.rollback()
            enviarMensagemSlack("\nERRO:\nInsert no banco de dados falhou!")
            self.close()
    
    # Fechando conexão
    def close(self):
        self.sql.close()
