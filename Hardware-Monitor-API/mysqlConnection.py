from analiseHardware import enviarMensagemSlack
import mysql.connector

class Sql:
    def __init__(self, user, password, database, server):
        self.user = user
        self.password = password
        self.database = database
        self.host = server
        self.sql = None
        self.cursor = None

    #Estabelecendo uma conexão
    def connect(self):
        try:
            self.sql = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database)
            #Criando cursor para manipulação do banco.
            print("MySQL = ", self.sql)
            self.cursor = self.sql.cursor()
        except Exception as err:
            print(err)
            enviarMensagemSlack("\nERRO:\nConexão com o banco de dados falhou!")
            raise

    def selectComp(self, maquina): # função do select que retorna o componente + idMaqComp
        sql_select_query = ("select nomeComponente, idMaqComp from MaquinaComponente, Componente, Maquina where fkMaquina = idMaquina and fkComponente = idComponente and hashmac = %s")
        try:
            self.cursor.execute(sql_select_query, (str(maquina), ))
            dadosColetados = self.cursor.fetchall()
            return dadosColetados
        except Exception as err:
            print(err)
            enviarMensagemSlack("\nERRO:\nSelect no banco de dados falhou!")
            self.close()

    def select_machine_name(self, hashmac):
        sql_select_query = ("SELECT descricaoMaquina FROM Maquina where hashmac = %s")
        try:
            self.cursor.execute(sql_select_query, (str(hashmac), ))
            dadosColetados = self.cursor.fetchall()
            return dadosColetados
        except Exception as err:
            print(err)
            enviarMensagemSlack("\nERRO:\nSelect no banco de dados falhou!")
            self.close()

    def newInsert(self, data): # função do novo insert de leitura dos componentes que o cliente escolheu
        query = ("INSERT INTO LeituraMaquina (leitura, dataHora, fkMaqComp) VALUES (%s, %s, %s)")
        values = data
        try:
            self.cursor.execute(query, values)
            self.sql.commit()
            print('Valores Inseridos no MySQL')
        except Exception as err:
            print(err)
            self.sql.rollback()
            enviarMensagemSlack("\nERRO:\nInsert no banco de dados falhou!")
            self.close()

    def multi_insert(self, data): # função do novo insert de leitura dos componentes que o cliente escolheu
        query = ("INSERT INTO LeituraMaquina (leitura, dataHora, fkMaqComp) VALUES (%s, %s, %s)")
        values = data
        try:
            for i in data:
                self.cursor.execute(query, i)
            self.sql.commit()
            print('Valores Inseridos no MySQL')
        except Exception as err:
            print(err)
            self.sql.rollback()
            enviarMensagemSlack("\nERRO:\nInsert no banco de dados falhou!")
            self.close()
    
    # Fechando conexão
    def close(self):
        self.sql.close()
