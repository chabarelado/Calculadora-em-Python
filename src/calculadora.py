import uteis as ut

class Caculadora():
    def __init__(self):
        self.acumulador = 0
        self.operacao = None
        self.numero = 0

    def define_operador(self, operador):
        self.operacao = operador

        if self.operacao == '+':
            self.soma()

        elif self.operacao == '-':
            self.subtracao()

        elif self.operacao == '*':
            self.multiplicacao()

        elif self.operacao == '/':
            self.divisao()

        else:
            return False    
        

    def define_numero(self, numero):
        self.numero = numero
        pass

    def soma(self):
        pass

    def subtracao(a, b):
        pass

    def multiplicacao(a, b):
        pass

    def divisao(a, b):
        pass
        
