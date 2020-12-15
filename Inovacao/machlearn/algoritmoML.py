class Algoritmo:
    def __init__(self):
        self.usr_act = False
        self.resposta = ""

    def ordenar_lista(self, lista, lblsLista):
        tam = len(lista)

        for i in range(tam):

            act = i

            for j in range(i, tam): 

                if lista[j] > lista[i] and lista[j] > lista[act]:

                    act = j

            lista[act], lista[i] = lista[i], lista[act]
            lblsLista[act], lblsLista[i] = lblsLista[i], lblsLista[act]

        return [lista, lblsLista]

    def tratar_palavras(self, palavras):
        
        #[['ola','oie','oi'], [2,6,4]]
        #info = [lbl_wrds, qtd_wrds]

        lbl_palavras = []
        qtd_palavras = []
        contador = 0

        for w in palavras: # PARA CADA PALAVRA QUE O USUARIO JA MANDOU

            actualWord = w[0] # PEGA A PALAVRA ATUAL

            if not actualWord in lbl_palavras: # SE A PALAVRA ATUAL JÁ NÃO TIVER SIDO LIDA

                qtd = 0 # RESETA QUANTIDADE QUE ELA APARECE

                for j in range(contador, len(palavras)): # ANDA PELA LISTA DE PALAVRAS

                    if actualWord == palavras[j][0]: # SE A PALAVRA ATUAL FOR A MESMA QUE A ATUAL DA LISTA

                        qtd += 1 # AUMENTA QUANTIDADE

                lbl_palavras.append(actualWord) # ADICIONA PALAVRA À LISTA DE PALAVRAS
                qtd_palavras.append(qtd) # ADICIONA QUANTIDADE À LISTA

                contador += 1

        informacoes = self.ordenar_lista(qtd_palavras, lbl_palavras)

        return informacoes

    def main(self):
        import ml
        #import color

        aibot = ml.BancoML()

        usr_act = input("Fazer select? [y/n] ")
        self.usr_act = True if usr_act.lower() == "y" else False
        if self.usr_act:

            todas_palavras = aibot.selectBanco()
            
            info = self.tratar_palavras(todas_palavras)

            for i in range(len(info[0])):

                print(info[0][i], ":", info[1][i])
                
        else:
            self.resposta = input('\033[1m' + "ola! " + '\033[0m')
            aibot.iniciar(self.resposta)

if __name__ == "__main__":
    testar = Algoritmo()
    testar.main()