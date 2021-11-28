
class Coisa:
    def __init__(self, estado_inicial=None):
        self.estado_inicial = estado_inicial

    def __repr__(self):
        # Objeto na forma de string
        return '{}'.format(getattr(self, '__name__', self.__class__.__name__))

    def mostrar_estado(self):
        # Mostra o estado do agente
        return str(self.estado)

    def vivo(self):
        return hasattr(self, 'vivo') and self.vivo


class Agente(Coisa):
    def __init__(self, nome, estado_inicial=None):
        self.nome = nome
        super().__init__(estado_inicial)
        self.funcao_agente = ''
        self.historico_percepcoes = {}
        self.contador = 0

# Esquerda, direita, aspirar, noOp

    # Recebe do meio exterior. Pode ser de um sensor, mas nesse caso é do teclado
    
    def percepcao(self, local):
        print(local.items())
        elemento = local.get(self.contador)
        return elemento

        # Aonde eu estou?
        #O que eu quero fazer?
            #quero limpar tudo
        #Como vou fazer?

    def acao_agente(self, locais):
        elemento = self.percepcao(locais)
        print(elemento)

    def historico(self):
        return self.historico_percepcoes
            # dicio[chave] = valor
                
        # recebo um local: verifico se este local já foi limpo.
        # se sim, passo para o próximo, senão verifico e chamo a função do agente.

    # mostra o resultado da função agente
    def saida(self):
        return self.funcao_agente()


class Ambiente(Coisa):
    def __init__(self, estado_inicial=None):
        self.estado_inicial = estado_inicial
        self.agentes = []
        self.locais = {"A":"sujo", "B":"limpo", "C":"limpo","D":"limpo"}

    def get_agentes(self):
        print('Lista de agentes \n')
        for i in self.agentes:
            print(i.nome)

    def get_locais(self):
        return self.locais

    def size(self):
        return len(self.locais)



# Esquerda,d
# adicionar chave: dicio[chave] = valor


ambiente = Ambiente(True)
print('Visão do ambiente')

locais = ambiente.get_locais()
print(locais)


agente = Agente("agente1", "0")

print(f'Local inicial: {agente.estado_inicial}')



print(agente.percepcao(locais))


