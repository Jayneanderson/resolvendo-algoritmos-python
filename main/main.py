
class Coisa:
  def __init__(self, estado = None):
    self.estado = estado
  
  #Isso aqui é para imprimir sem usar print
  def __repr__(self):
    #Objeto na forma de strinf
    return '{}'.format(getattr(self, '__name__', self.__class__.__name__))

  def mostrar_estado(self):
    ## Mostra o estado do agente
    return str(self.estado)

  def vivo(self):
    return hasattr(self, 'vivo') and self.vivo

class Agente(Coisa):
  def __init__(self, estado = None, funcao_agente = None):
    super().__init__(estado)

    if funcao_agente == None:
      def acao(*entradas): #aqui é para indicar que podem ter várias entradas
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



class Ambiente():

  def __init__(self, estado_inicial = None):
    self.estado_inicial = estado_inicial
    #São literalmente objetos ao redor que não sejam agentes
    self.objetos_no_ambiente = []
    self.agentes = []
    self.locais = {}

  def percepcao(self, agente):
    #Percepção do agente
    return agente
  
  def adicionar_agente(self, agente):
    self.agentes.append(agente)

  def listar_agentes(self):
    return self.agentes
  
  def adicionar_objeto(self, objeto):
    self.objetos_no_ambiente.append(objeto)

  def adicionar_local(self, local):
    local = local.upper()
    if local in self.locais.keys():
      print('O local já existe!')
    
    else:
      self.locais[local] = self.estado_inicial

  def show_locais(self):
    print(self.locais.keys())


# Esquerda, direita, aspirar, noOp

# adicionar chave: dicio[chave] = valor


ambiente = Ambiente("Sujo")
ambiente.adicionar_local('A')
ambiente.adicionar_local('B')
ambiente.adicionar_local('b')
ambiente.adicionar_local('a')

ambiente.show_locais()

agente = Agente(True, 'E')

