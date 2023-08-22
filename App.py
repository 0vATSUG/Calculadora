from tkinter import *
from tkinter import ttk
from math import sqrt

class App():
    lista = []
    resposta = None

    def __init__(self) -> None:

        self.root = Tk()
        self.root.geometry('500x250')
        self.root.resizable(width=False, height=False)

        # Frame que mostra a expressao sendo digitada
        self.tela_da_expressao = ttk.Frame(self.root, padding=5, borderwidth=1, width=300, height=50, relief=SUNKEN)
        self.tela_da_expressao.grid(row=1, column=0)
        self.label = ttk.Label(self.tela_da_expressao, textvariable=App.lista,width=65)
        self.label.grid()

        # Frame que mostra a resposta da expressao
        self.tela_de_resposta = ttk.Frame(self.root, padding=5, borderwidth=1, width=300, height=50, relief=SUNKEN)
        self.tela_de_resposta.grid(column=0, row=0)
        self.label_resposta = ttk.Label(self.tela_de_resposta, textvariable=App.resposta, width=65)
        self.label_resposta.grid(column=0, row=0)

        # quadro dos botoes
        self.quadro = ttk.Frame(self.root, padding=60)
        self.quadro.grid(column=0, row=2)

        # botoes dos operadores
        self.botao_soma = ttk.Button(self.quadro, text='+', command=lambda: self.botoes('+'))
        self.botao_soma.grid(column=3, row=3)
        self.botao_subtracao = ttk.Button(self.quadro, text='-', command=lambda: self.botoes('-'))
        self.botao_subtracao.grid(column=3, row=2)
        self.botao_divisao = ttk.Button(self.quadro, text='/', command=lambda: self.botoes('/'))
        self.botao_divisao.grid(column=3, row=1)
        self.botao_multiplicacao = ttk.Button(self.quadro, text='*', command=lambda: self.botoes('*'))
        self.botao_multiplicacao.grid(column=3, row=0)
        self.botao_dot = ttk.Button(self.quadro, text='.', command=lambda: self.botoes('.'))
        self.botao_dot.grid(column=1, row=3)
        self.botao_igual = ttk.Button(self.quadro, text='=', command=self._botao_igual)
        self.botao_igual.grid(column=2, row=3)
        self.botao_apaga = ttk.Button(self.quadro, text='del', command=self._limpa)
        self.botao_apaga.grid(column=4, row=0)

        # botoes de 0 a 9 
        self.botao1 = ttk.Button(self.quadro, text='1', command=lambda: self.botoes('1'))
        self.botao1.grid(column=0, row=0)
        self.botao2 = ttk.Button(self.quadro, text='2', command=lambda: self.botoes('2'))
        self.botao2.grid(column=1, row=0)
        self.botao3 = ttk.Button(self.quadro, text='3', command=lambda: self.botoes('3'))
        self.botao3.grid(column=2, row=0)
        self.botao4 = ttk.Button(self.quadro, text='4', command=lambda: self.botoes('4'))
        self.botao4.grid(column=0, row=1)
        self.botao5 = ttk.Button(self.quadro, text='5', command=lambda: self.botoes('5'))
        self.botao5.grid(column=1, row=1)
        self.botao6 = ttk.Button(self.quadro, text='6', command=lambda: self.botoes('6'))
        self.botao6.grid(column=2, row=1)
        self.botao7 = ttk.Button(self.quadro, text='7', command=lambda: self.botoes('7'))
        self.botao7.grid(column=0, row=2)
        self.botao8 = ttk.Button(self.quadro, text='8', command=lambda: self.botoes('8'))
        self.botao8.grid(column=1, row=2)
        self.botao9 = ttk.Button(self.quadro, text='9', command=lambda: self.botoes('9'))
        self.botao9.grid(column=2, row=2)
        self.botao0 = ttk.Button(self.quadro, text='0', command=lambda: self.botoes('0'))
        self.botao0.grid(column=0, row=3)
        self.botao_raiz = ttk.Button(self.quadro, text='√', command= lambda: self.botoes('√'))
        self.botao_raiz.grid(column=4, row=1)
        self.botao_pi = ttk.Button(self.quadro, text='π', command=lambda: self.botoes('3.14159'))
        self.botao_pi.grid(column=4, row=2)
        self.botao_exp = ttk.Button(self.quadro,text='x²', command= lambda: self.botoes('²'))
        self.botao_exp.grid(column=4, row=3)

        
        self.root.bind("<Return>", self._botao_igual)
        self.root.bind("<Key>", self.binds)
        self.root.mainloop()


    def calcular(self, entrada: str) -> int: 
        return eval(entrada)


    def botoes(self, button: str) -> str:
        if button in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/', '.', '√','3.14159','²']:
            App.lista.append(button)
            return self.label.config(text=App.lista)


    def binds(self, botao):
        if botao.keysym in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/', '.']:
            App.lista.append(botao.keysym)
        elif botao.char in ['+', '-', '*', '/', '.']:
            App.lista.append(botao.char)
        return self.label.config(text=App.lista)


    def _botao_igual(self, resposta=None):
        resposta = ''.join(App.lista)
        resposta = self.calcular(resposta)
        return self.label_resposta.config(text=resposta)

    def _limpa(self):
        App.lista.pop()
        return self.label.config(text=App.lista)
# lista que ira conter os numeros para calcular


if __name__ == '__main__':
    main = App()
    