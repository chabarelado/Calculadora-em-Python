import tkinter as tk
import calculadora as calc

class CalculadoraApp(): 
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Calculadora")
        self.janela.geometry("450x500")

        for i in range(5):

            self.janela.grid_rowconfigure(i, weight=1)

        for i in range(4):

            self.janela.grid_columnconfigure(i, weight=1)


        self.display = tk.Entry(self.janela, font=("Arial", 24), border=10, justify="center", bd=5)
        self.display.grid(row=0, column=0, columnspan=3, pady=10, sticky="nsew")

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
        botao = tk.Button(self.janela, text=texto)
        botao.grid(row=linha, column=coluna,padx=1, pady=1, sticky="nsew")
        return botao
    



if __name__ == "__main__":
    app = CalculadoraApp()
    app.executa()