
class Coisa:
    def __init__(self, estado=None):
        self.estado = estado

    def __repr__(self):
        # Objeto na forma de string
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
        self.historico_percepcoes = {}

# Esquerda, direita, aspirar, noOp
    def acao_agente(self, conteudo):
        return "limpo"

    # Recebe do meio exterior. Pode ser de um sensor, mas nesse caso é do teclado
    
    def percepcao(self):
        print(f'Local inicial: {self.estado}')
        valor = ''


        # for chave in local_inicial.keys():
        #     if self.historico_percepcoes.get(chave):
        #         print('O local já foi verificado')
        #         continue
        #     else:
        #         valor = local_inicial[chave]
        #         print(valor)
        #         self.historico_percepcoes[chave] = valor
            
    def historico(self):
        return self.historico_percepcoes
            # dicio[chave] = valor
                
        # recebo um local: verifico se este local já foi limpo.
        # se sim, passo para o próximo, senão verifico e chamo a função do agente.

    # mostra o resultado da função agente
    def saida(self):
        return self.funcao_agente(self.historico_percepcoes)


class Ambiente(Coisa):
    def __init__(self, estado_inicial=None):
        self.estado_inicial = estado_inicial
        # São literalmente objetos ao redor que não sejam agentes
        self.objetos_no_ambiente = []
        self.agentes = []
        self.locais = {"A":"sujo", "B":"limpo", "C":"limpo","D":"limpo"}

    def adicionar_agente(self, agente):
        self.agentes.append(agente)

    def get_agentes(self):
        print('Lista de agentes \n')
        for i in self.agentes:
            print(i.nome)

    def adicionar_objeto(self, objeto):
        self.objetos_no_ambiente.append(objeto())

    # def adicionar_local(self, local, conteudo):
    #     local = local.upper()
    #     if local in self.locais.keys():
    #         print('O local já existe!') 

    #     if conteudo != 'sujo' and conteudo != 'limpo':
    #         print('Local só poder ser sujo ou limpo')

    #     else:
    #         self.locais[local] = conteudo

    def get_locais(self):

        return self.locais
        # for local in self.locais.keys():
            # print(f'O local {local} está {self.locais[local]}')


# Esquerda, direita, aspirar, noOp

# adicionar chave: dicio[chave] = valor


ambiente = Ambiente(True)
print('Visão do ambiente')

print(ambiente.get_locais())



agente = Agente("agente1", "A")
agente2 = Agente("agente2", "B")
ambiente.adicionar_agente(agente)
ambiente.adicionar_agente(agente2)

agente.percepcao()




