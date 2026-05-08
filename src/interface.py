import tkinter as tk
import calculadora as calc

class Calculadora_app():
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Calculadora")
        self.janela.geometry("400x500")

    def executa(self):
        self.janela.mainloop()


if __name__ == "__main__":
    app = Calculadora_app()
    app.executa()