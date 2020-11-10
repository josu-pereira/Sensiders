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
            print(self.sql)
            self.cursor = self.sql.cursor()
        except Exception as err:
            print(err)
            enviarMensagemSlack("\nERRO:\nConexão com o banco de dados falhou!")
            raise

    def insert(self, data):
        query = (
            "INSERT INTO DadosMaquina (data_cpu, data_mem, data_disk, data_download, data_upload, cpu_temperature, data_swap, tarefasExec, fkmaquina) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)" 
        )
        values = data
        try:
            print('Inserindo Valores')
            self.cursor.execute(query,values)

            self.sql.commit()
        except Exception as err:
            print(err)
            self.sql.rollback()
            self.close()

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
            enviarMensagemSlack("\nERRO:\nInsert no banco de dados falhou!")
            self.close()
    
    # Fechando conexão
    def close(self):
        self.sql.close()
