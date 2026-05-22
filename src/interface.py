import tkinter as tk
from calculadora import Calculadora 

class CalculadoraApp(): 
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Calculadora")
        self.janela.geometry("450x500")
        self.resultado = 0

        self.operador = None
        self.primeiro_numero = None
        self.segundo_numero = None
        self.calc = Calculadora()

    
        for i in range(5):

            self.janela.grid_rowconfigure(i, weight=1)

        for i in range(4):

            self.janela.grid_columnconfigure(i, weight=1)


        self.display = tk.Entry(self.janela, font=("Arial", 24), border=10, justify="right", bd=5)
        self.display.grid(row=0, column=0, columnspan=4, pady=10, sticky="nsew")

        self.botoes_numerais = [['7', '8', '9', '/'],
                                ['4', '5', '6', 'x'],
                                ['1', '2', '3', '-'],
                                ['0', '.', '=', '+']]
        

        for linha, valor in enumerate(self.botoes_numerais):
            for coluna, texto in enumerate(valor):
                botao = self.cria_botoes(texto=texto, linha=linha+1, coluna=coluna)
                

    def executa(self):
        self.janela.mainloop()

    def cria_botoes(self, texto, linha, coluna):
        if texto.isdigit() or texto == '.':
            comando = lambda texto=texto: self.define_numero(texto)
        elif texto == '=':
            comando = self.calcula
        else:
            comando = lambda texto=texto: self.define_operadores(texto)
        
        botao = tk.Button(self.janela, text=texto, command=comando)
        botao.grid(row=linha, column=coluna,padx=1, pady=1,sticky="nsew")

    
    def define_operadores(self, operador):
        self.operador = operador
        try:
            self.primeiro_numero = float(self.display.get())
        except ValueError:
            self.display.insert(tk.END, 'Erro')

        self.display.delete(0, tk.END)
        
    def define_numero(self, numero):
        self.display.insert(tk.END, numero)

    def calcula(self):

        try:
            self.segundo_numero = float(self.display.get())
        except ValueError:
            self.display.insert(tk.END, 'Erro')

        if self.operador == '+':
            self.resultado =  self.calc.soma(self.primeiro_numero, self.segundo_numero)

        elif self.operador == '-':
            self.resultado =  self.calc.subtracao(self.primeiro_numero, self.segundo_numero)    
        
        elif self.operador == 'x':
            self.resultado =  self.calc.multiplicacao(self.primeiro_numero, self.segundo_numero)

        elif self.operador == '/':
            self.resultado =  self.calc.divisao(self.primeiro_numero, self.segundo_numero)

        self.display.delete(0, tk.END)
        self.display.insert(tk.END, str(self.resultado))
        print(self.resultado)


if __name__ == "__main__":
    app = CalculadoraApp()
    app.executa()