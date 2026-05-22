import uteis as ut

class Calculadora():
    def __init__(self):
        self.acumulador = 0

    def soma(self, valor1,valor2):
        self.acumulador = valor1 + valor2
        return self.acumulador

    def subtracao(self, valor1,valor2):
        self.acumulador = valor1 - valor2
        return self.acumulador

    def multiplicacao(self, valor1, valor2):
        self.acumulador = valor1 * valor2
        return self.acumulador

    def divisao(self, valor1, valor2):
        self.acumulador = valor1 / valor2
        return self.acumulador
        
