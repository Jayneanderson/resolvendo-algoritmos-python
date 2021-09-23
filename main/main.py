
class Coisa:
    def __init__(self, estado=None):
        self.estado = estado

    def __repr__(self):
        # Objeto na forma de strinf
        return '{}'.format(getattr(self, '__name__', self.__class__.__name__))

    def mostrar_estado(self):
        # Mostra o estado do agente
        return str(self.estado)

    def vivo(self):
        return hasattr(self, 'vivo') and self.vivo


class Agente(Coisa):
    def __init__(self, nome, estado=None):
        self.nome = nome
        super().__init__(estado)
        self.funcao_agente = ''
        self.historico_percepcoes = []

# Esquerda, direita, aspirar, noOp
    # def aspirar(self, local):

        

    # Recebe do meio exterior. Pode ser de um sensor, mas nesse caso é do teclado
    def percepcao(self):
        entrada = input("Entre com as percepções")
        self.historico_percepcoes.append(eval(entrada))

    # mostra o resultado da função agente
    def saida(self):
        return self.funcao_agente(self.historico_percepcoes)


class Ambiente(Coisa):
    def __init__(self, estado_inicial=None):
        self.estado_inicial = estado_inicial
        # São literalmente objetos ao redor que não sejam agentes
        self.objetos_no_ambiente = []
        self.agentes = []
        self.locais = {}

    def percepcao(self, agente):
        # Percepção do agente
        return agente

    def adicionar_agente(self, agente):
        self.agentes.append(agente)

    def getAgentes(self):
        print('Lista de agentes \n')
        for i in self.agentes:
            print(i.nome)

    def adicionar_objeto(self, objeto):
        self.objetos_no_ambiente.append(objeto())

    def adicionar_local(self, local, conteudo):
        local = local.upper()
        if local in self.locais.keys() :
            print('O local já existe!') 

        if conteudo != 'sujo' and conteudo != 'limpo':
            print('Local só poder ser sujo ou limpo')

        else:
            self.locais[local] = conteudo

    def getLocais(self):
        for local in self.locais.keys():
            print(f'O local {local} está {self.locais[local]}')


# Esquerda, direita, aspirar, noOp

# adicionar chave: dicio[chave] = valor


ambiente = Ambiente(True)
print('Locais \n')

ambiente.adicionar_local('A', 'sujo')
ambiente.adicionar_local('B', 'sujo')

ambiente.getLocais()

agente = Agente("agente1", True)
agente2 = Agente("agente2", True)
ambiente.adicionar_agente(agente)
ambiente.adicionar_agente(agente2)




