class BotSensiders:
    def __init__(self):
        self.resposta = ""
        self.respostaUnfor = ""
        self.nome_usuario = ""
        self.enviar_usuario = ""
        self.valorIntensidade = False
        self.valorNegacao = False
        self.valorPositivo = False
        self.conseguiuResponder = False
        self.ia_watson = [False]
        self.emocao = {
            'feliz': False,
            'estressado': False,
            'neutro': False,
            'duvida': False
        }
        self.condicao_horario = self.condHorario()

    def separa_palavras(self, texto):
        import re
        sentencas = re.split(r'\W+', texto)
        if sentencas[-1] == '':
            del sentencas[-1]
        return sentencas

    def retiraAcentos(self, texto):
        import unicodedata
        try:
            texto = unicode(texto, 'utf-8')
        except NameError:
            pass
        texto = unicodedata.normalize('NFD', texto) \
            .encode('ascii', 'ignore') \
            .decode("utf-8")
        return str(texto)

    def condHorario(self):
        import time
        horario = time.localtime()[3]
        if 4 <= horario <= 11:
            condicao_hora = 'manhã'
        elif 12 <= horario <= 18:
            condicao_hora = 'tarde'
        else:
            condicao_hora = 'noite'
        return condicao_hora

    def enviarMsg(self, texto):
        from message import sendMsg
        sendMsg(texto)

    def watson(self, txt_usr):
        traducao = ""
        try:
            from nlu import NLU
            from googletrans import Translator
            t = Translator()
            traducao = (t.translate(txt_usr, src='pt', dest='en')).text
            print(traducao)
        except Exception as e:
            print(e)
            try:
                import translators as ts
                traducao = ts.bing(txt_usr, 'pt', 'en')
                print(traducao)
            except Exception as e:
                print(e)
                try:
                    import translators as ts
                    # TODO:
                    # FAZER UMA FUNCAO ASYNCRONA QUE ESPERA UM VALOR DESSA LIB
                    # PARA PREVINIR O LOOP INFINITO QUE ELA FICA AS VEZES
                    traducao = ts.google(txt_usr, 'pt', 'en')
                    print(traducao)
                except Exception as e:
                    print(e)
                    try:
                        from translate import Translator  # TRADUCAO HORRIVEL
                        translator = Translator(from_lang="pt", to_lang="en")
                        traducao = translator.translate(txt_usr)  # TRADUCAO HORRIVEL
                        print(traducao)
                    except Exception as e:
                        print(e)
                        return [False]
        try:
            emocao = NLU(traducao)
            return [True, emocao]
        except Exception as e:
            return [False]

    def analisaSugestao(self):
        import wordbase.Emocoes as Emocoes

        if len(self.resposta) > 3:
            self.ia_watson = self.watson(self.respostaUnfor)

        if self.ia_watson[0]:
            sentimento_feliz = True if (self.ia_watson[1][0]['label'] == 'positive') else False
            if sentimento_feliz:
                self.conseguiuResponder = True
                self.emocao['feliz'] = True
            else:
                self.conseguiuResponder = True
                self.emocao['estressado'] = True
        else:
            for palavra in self.resposta:
                if palavra.lower() == 'muito':
                    self.valorIntensidade = True
                if palavra.lower() == 'nao':
                    self.valorNegacao = True
                if palavra.lower() == 'sim':
                    self.valorPositivo = True
                if palavra.lower() in Emocoes.feliz():
                    self.emocao['feliz'] = True
                    self.conseguiuResponder = True
                    break
                elif palavra.lower() in Emocoes.estressado():
                    self.emocao['estressado'] = True
                    self.conseguiuResponder = True
                    break
                elif palavra.lower() == 'bem' and self.valorIntensidade:
                    self.emocao['feliz'] = True
                    self.conseguiuResponder = True
                    break
                elif palavra.lower() == 'bem' and self.valorNegacao:
                    self.emocao['estressado'] = True
                    self.conseguiuResponder = True
                    break
                elif palavra.lower() in Emocoes.neutro():
                    self.emocao['neutro'] = True
                    self.conseguiuResponder = True
                    break
                elif palavra.lower() == 'sei' and self.valorNegacao:
                    self.enviar_usuario = ("Como você não sabe o que está sentindo? \U0001F914")
                    self.emocao['duvida'] = True
                    self.conseguiuResponder = True
                    break

    def acao_comportamento(self):
        if self.emocao['feliz'] or self.emocao['neutro']:
            # EMOÇÃO POSITIVA
            msg = ""
            msg += "Sempre mantenha a calma, pois uma situação imprevista pode acontecer. \U0001F605"
            msg += "\nE se der algo de errado, acredite que dará tudo certo, porque " \
                   "a situação melhorará!"
            msg += "\nPorque a vida não é imutável! \U0001F60C Portanto jamais tenha um dogma sobre " \
                   "qualquer situação ruim."
            msg += "\nUm dia em que situação das máquinas não estiverem bem, " \
                   "eu irei te trazer estes dados e " \
                   "assim você será capaz de tomar atitudes para resolver estes problemas! \U0001F60E"
            self.enviar_usuario = msg
        elif self.emocao['estressado']:
            # EMOÇÃO NEGATIVA
            msg = ""
            msg += "Lembre-se de um momento positivo, um dia que você esteve feliz, " \
                   "um dia em que estava dando tudo certo!"
            msg += "\nNeste dia, você estava muito alegre porque no seu trabalho estava indo " \
                   "tudo tão bem, e assim você era capaz de apresentar bons resultados! \U0001F913"
            msg += "\nPense em Contextos ou situações que tiveram solução e você conseguiu " \
                   "ter algum resultado! \U0001F609"
            msg += "\nVai dar tudo certo! \U0001F605"
            self.enviar_usuario = msg
        else:
            # BOT NÃO ENTENDE
            msg = ""
            msg += "Sempre mantenha a calma, pois uma situação imprevista pode acontecer. \U0001F605"
            msg += "\nMas no final irá dar tudo certo! \U0001F605"
            self.enviar_usuario = msg

    def analisaComportamento(self):
        import wordbase.Perguntas as Perguntas
        import wordbase.Emocoes as Emocoes
        import wordbase.Respostas as Respostas
        from random import randrange

        if len(self.resposta) > 3:
            self.ia_watson = self.watson(self.respostaUnfor)

        if self.ia_watson[0]:
            # WATSON FUNCIONANDO
            sentimento_feliz = True if (self.ia_watson[1][0]['label'] == 'positive') else False
            data_emotion = {
                't': self.ia_watson[1][1]['sadness'] * 100,
                'a': self.ia_watson[1][1]['joy'] * 100,
                'm': self.ia_watson[1][1]['fear'] * 100,
                'd': self.ia_watson[1][1]['disgust'] * 100,
                'r': self.ia_watson[1][1]['anger'] * 100
            }
            if sentimento_feliz:
                rnd = randrange(0, len(Respostas.res_feliz()))
                self.enviar_usuario = (Respostas.res_feliz(self.nome_usuario)[rnd])
                self.conseguiuResponder = True
                self.emocao['feliz'] = True
            else:
                rnd = randrange(0, len(Respostas.res_estressado()))
                self.enviar_usuario = (Respostas.res_estressado()[rnd])
                self.conseguiuResponder = True
                self.emocao['estressado'] = True
        else:
            # WATSON NAO FUNCIONANDO

            # self.resposta = self.retiraAcentos(self.resposta)
            # self.resposta = self.separa_palavras(self.resposta)

            #
            # TODO:
            # resolver caso seja 'to bem não' => contradição
            #
            for palavra in self.resposta:
                if palavra.lower() == 'muito':
                    self.valorIntensidade = True
                if palavra.lower() == 'nao':
                    self.valorNegacao = True
                if palavra.lower() in Emocoes.feliz():
                    rnd = randrange(0, len(Respostas.res_feliz()))
                    self.enviar_usuario = (Respostas.res_feliz(self.nome_usuario)[rnd])
                    self.emocao['feliz'] = True
                    self.conseguiuResponder = True
                    break
                elif palavra.lower() in Emocoes.estressado():
                    rnd = randrange(0, len(Respostas.res_estressado()))
                    self.enviar_usuario = (Respostas.res_estressado()[rnd])
                    self.emocao['estressado'] = True
                    self.conseguiuResponder = True
                    break
                elif palavra.lower() == 'bem' and self.valorIntensidade:
                    rnd = randrange(0, len(Respostas.res_feliz()))
                    self.enviar_usuario = (Respostas.res_feliz(self.nome_usuario)[rnd])
                    self.emocao['feliz'] = True
                    self.conseguiuResponder = True
                    break
                elif palavra.lower() == 'bem' and self.valorNegacao:
                    rnd = randrange(0, len(Respostas.res_estressado()))
                    self.enviar_usuario = (Respostas.res_estressado()[rnd])
                    self.emocao['estressado'] = True
                    self.conseguiuResponder = True
                    break
                elif palavra.lower() in Emocoes.neutro():
                    rnd = randrange(0, len(Respostas.res_neutro()))
                    self.enviar_usuario = (Respostas.res_neutro()[rnd])
                    self.emocao['neutro'] = True
                    self.conseguiuResponder = True
                    break
                elif palavra.lower() == 'sei' and self.valorNegacao:
                    self.enviar_usuario = ("Como você não sabe o que está sentindo? \U0001F914")
                    self.emocao['duvida'] = True
                    self.conseguiuResponder = True
                    break

    def boasVindas(self):
        mensagemBoasVindas = ("Sou o seu assistente pessoal SextaFeira! \U0001F609")
        return mensagemBoasVindas

    def naoConseguiuResponder(self):
        from random import randrange
        import wordbase.Respostas as Respostas
        rnd = randrange(0, len(Respostas.res_nao_entende()))
        self.enviar_usuario = (Respostas.res_nao_entende()[rnd])

    def perguntarInicial(self):
        import wordbase.Perguntas as Perguntas
        from random import randrange

        perguntaInicial = Perguntas.inicio(self.condicao_horario, self.nome_usuario)
        rnd = randrange(0, len(perguntaInicial))

        return perguntaInicial[rnd]

    def naoResponde(self):
        import wordbase.Respostas as Respostas
        from random import randrange

        rnd = randrange(0, len(Respostas.res_nao_responde()))
        self.enviar_usuario = (Respostas.res_nao_responde()[rnd])
        self.conseguiuResponder = False

    def iniciar(self):
        import wordbase.Perguntas as Perguntas
        import wordbase.Emocoes as Emocoes
        import wordbase.Respostas as Respostas
        import random, os

        self.condicao_horario = self.condHorario()

        self.nome_usuario = os.getlogin().capitalize()

        perguntaInicial = Perguntas.inicio(self.condicao_horario)
        rnd = random.randrange(0, len(perguntaInicial))

        self.resposta = input(perguntaInicial[rnd])

        self.analisaComportamento()
        self.enviarMsg(self.enviar_usuario)

    def resetData(self):
        self.resposta = ""
        self.respostaUnfor = ""
        self.nome_usuario = ""
        self.enviar_usuario = ""
        self.valorIntensidade = False
        self.valorNegacao = False
        self.valorPositivo = False
        self.conseguiuResponder = False
        self.ia_watson = [False]
        self.emocao = {
            'feliz': False,
            'estressado': False,
            'neutro': False,
            'duvida': False
        }
        self.condicao_horario = self.condHorario()


if __name__ == "__main__":
    b = BotSensiders()
    b.iniciar()
