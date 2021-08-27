class CadastrarMaquina:
    def __init__(self):
        import psutil
        from sys import platform
        self.user = 'adminlocal'
        self.password = '#Gfgrupo11c'
        self.port = '1433'
        self.database = 'bdProjetoSensiders'
        self.server = 'serversensiders.database.windows.net'
        self.sql = None
        self.cursor = None
        self.componentes = ('CPU', 'RAM', 'HD', 'DOWNLOAD', 'UPLOAD', 'TEMPERATURA', 'SWAP', 'TASKS')
        self.total_componentes = (100, round(psutil.virtual_memory()[0] / (2**20)), round(psutil.disk_usage(('/' if platform == 'linux' else 'C://'))[0] / (2**30)), 10000, 50000, 100, round(psutil.swap_memory()[0] / (2**20)), 600)
        self.loginMaquina = ""
        self.senhaMaquina = ""
        self.componentes_escolhidos = []
        self.totais_escolhidos = []
        self.descricaoMaquina = ""
        self.hash_mac = ""
        self.fkFilial = 0
    
    def connect(self):
        import pyodbc
        try:
            self.sql = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}'+';SERVER='+self.server+';PORT='+self.port+';DATABASE='+self.database+';UID='+self.user+';PWD='+self.password)
            self.cursor = self.sql.cursor()
        except Exception as err:
            print(err)
            raise

    def close(self):
        self.sql.close()

    def hashing_mac(self):
        from getmac import get_mac_address as gma
        import hashlib
        import os
        mac = gma()
        mac = str(mac).encode('utf8')
        machash = hashlib.sha256()
        machash.update(mac)
        self.hash_mac = machash.hexdigest()

    def insert_maqcomp(self, idMaq, idComp):
        query = ("INSERT INTO MaquinaComponente (fkMaquina, fkComponente) VALUES (?, ?)")
        try:
            self.cursor.execute(query, idMaq, idComp)
            self.sql.commit()
            print('Máquina-Componente cadastrado com sucesso!')
        except Exception as err:
            print(err)
            self.sql.rollback()
            self.close()

    def insert_componente(self, nome_componente, total_componente): 
        query = ("INSERT INTO Componente (nomeComponente, totalComponente) VALUES (?, ?)")
        try:
            self.cursor.execute(query, nome_componente, total_componente)
            self.sql.commit()
            print('Componente cadastrado com sucesso!')
        except Exception as err:
            print(err)
            self.sql.rollback()
            self.close()

    def insert_maquina(self): 
        query = ("INSERT INTO Maquina (descricaoMaquina, fkFilial, hashmac) VALUES (?, ?, ?)")
        try:
            self.cursor.execute(query, self.descricaoMaquina, self.fkFilial, self.hash_mac)
            self.sql.commit()
            print('Máquina cadastrada com sucesso!')
        except Exception as err:
            print(err)
            self.sql.rollback()
            self.close()

    def select_machines(self):
        query = ("SELECT * FROM Maquina")
        try:
            self.cursor.execute(query)
            dadosColetados = self.cursor.fetchall()
            return dadosColetados
        except Exception as err:
            print(err)
            self.close()
        
    def select_components(self):
        query = ("SELECT * FROM Componente")
        try:
            self.cursor.execute(query)
            dadosColetados = self.cursor.fetchall()
            return dadosColetados
        except Exception as err:
            print(err)
            self.close()

    def select_user(self):
        query = ("SELECT * FROM usuario WHERE emailUsuario = ? AND senhaUsuario = ?")
        try:
            self.cursor.execute(query, self.loginMaquina, self.senhaMaquina)
            dadosColetados = self.cursor.fetchall()
            return dadosColetados
        except Exception as err:
            print(err)
            self.close()

    def boas_vindas(self):
        from getpass import getpass
        self.connect()
        print("\nBem vindo ao Cadastro de Maquina da Sensiders!")
        print("Realize o seu login e senha para cadastrar esta máquina")
        self.loginMaquina = input("\nE-mail: ")
        self.senhaMaquina = getpass("Senha: ")
        dados = self.select_user()
        if bool(dados):
            print("Logado com sucesso!")
            self.fkFilial = dados[0][-1]
            self.main()
        else:
            print("\nE-mail ou senha incorretos!")

    def main(self):
        self.descricaoMaquina = input("\nDê uma descrição para esta máquina: ")
        self.componentes_escolhidos = []
        self.totais_escolhidos = []
        if self.descricaoMaquina != "" and self.descricaoMaquina != " ":
            maquinas = self.select_machines()
            for m in maquinas:
                if self.descricaoMaquina == m[1]:
                    print("Você digitou uma descrição que já existe!")
                    print("Reiniciando...")
                    self.main()
            print("\nEscolha seus componentes:")
            for comp in range(len(self.componentes)):
                c = input("Componente " + self.componentes[comp] + " ? [y/n] ")
                c = True if c.lower() == "y" else False
                if c is True:
                    self.componentes_escolhidos.append(self.componentes[comp])
                    self.totais_escolhidos.append(self.total_componentes[comp])
            if bool(self.componentes_escolhidos):
                print("\nVocê escolheu os componentes:")
                msg = ""
                for i in self.componentes_escolhidos:
                    msg += i + ", "
                msg = msg[:-2]
                print(msg)
                conf = input("\nConfirmar ? [y/n] ")
                conf = True if conf.lower() == "y" else False
                if conf:
                    self.hashing_mac()
                    self.insert_maquina()
                    idMaquinaCadastrada = self.select_machines()[-1][0]
                    for z in range(len(self.componentes_escolhidos)):
                        self.insert_componente(self.componentes_escolhidos[z], self.totais_escolhidos[z])
                    posicao_componentes = len(self.componentes_escolhidos) * -1
                    id_componentes = []
                    componentes_cadastrados = self.select_components()[posicao_componentes:]
                    for j in componentes_cadastrados:
                        id_componentes.append(j[0])
                    for i in range(len(id_componentes)):
                        self.insert_maqcomp(idMaquinaCadastrada, id_componentes[i])
                else:
                    print("Reiniciando...\n")
                    self.main()
            else:
                print("\nVocê não cadastrou nenhum componente...")
                print("Reiniciando...\n")
                self.main()
        else:
            print("Insira uma descrição para a máquina!\n")
            self.main()

if __name__ == "__main__":
    cm = CadastrarMaquina()
    cm.boas_vindas()