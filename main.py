class Coisa:
    def __init__(self, estado=None):
        self.estado = estado

    # Isso aqui é para imprimir sem usar print
    def __repr__(self):
        # Objeto na forma de strinf
        return '{}'.format(getattr(self, '__name__', self.__class__.__name__))

    def mostrar_estado(self):
        # Mostra o estado do agente
        return str(self.estado)

    def vivo(self):
        return hasattr(self, 'vivo') and self.vivo

coisa = Coisa()

coisa.show()

class Agente(Coisa):
    def __init__(self, estado = None, funcao_agente = None):
        super().__init__(estado)

    if funcao_agente == None:
        def funcao_agente(*entradas): #aqui é para indicar que podem ter várias entradas
            return 'Ação padrão'
        self.funcao_agente = funcao_agente
        self.historico_percepcoes = []
  
    #Recebe do meio exterior. Pode ser de um sensor, mas nesse caso é do teclado
    def percepcao(self):
        entrada = input("Entre com as percepções")
        self.historico_percepcoes.append(eval(entrada))

    #mostra o resultado da função agente
        def saida(self):
            return self.funcao_agente(self.historico_percepcoes)