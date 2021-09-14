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
