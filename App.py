from tkinter import *
from tkinter import ttk
from math import sqrt



def calcular(entrada):
    return eval(entrada)


def botoes(button):
    if button in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/', '.', '√','3.14159','²']:
        lista.append(button)
        return label.config(text=lista)


def binds(botao):
    if botao.keysym in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/', '.']:
        lista.append(botao.keysym)
    elif botao.char in ['+', '-', '*', '/', '.']:
        lista.append(botao.char)
    return label.config(text=lista)


def _botao_igual(resposta=None):
    resposta = ''.join(lista)
    resposta = calcular(resposta)
    return label_resposta.config(text=resposta)

def _limpa():
    lista.pop()
    return label.config(text=lista)
# lista que ira conter os numeros para calcular


lista = []
resposta = None

root = Tk()
root.geometry('500x250')
root.resizable(width=False, height=False)

# Frame que mostra a expressao sendo digitada
tela_da_expressao = ttk.Frame(root, padding=5, borderwidth=1, width=300, height=50, relief=SUNKEN)
tela_da_expressao.grid(row=1, column=0)

label = ttk.Label(tela_da_expressao, textvariable=lista,width=65)
label.grid()

# Frame que mostra a resposta da expressao


tela_de_resposta = ttk.Frame(root, padding=5, borderwidth=1, width=300, height=50, relief=SUNKEN)
tela_de_resposta.grid(column=0, row=0)

label_resposta = ttk.Label(tela_de_resposta, textvariable=resposta, width=65)
label_resposta.grid(column=0, row=0)


# quadro dos botoes
quadro = ttk.Frame(root, padding=60)
quadro.grid(column=0, row=2)

# botoes de 0 a 9
botao1 = ttk.Button(quadro, text='1', command=lambda: botoes('1'))
botao1.grid(column=0, row=0)
botao2 = ttk.Button(quadro, text='2', command=lambda: botoes('2'))
botao2.grid(column=1, row=0)
botao3 = ttk.Button(quadro, text='3', command=lambda: botoes('3'))
botao3.grid(column=2, row=0)
botao4 = ttk.Button(quadro, text='4', command=lambda: botoes('4'))
botao4.grid(column=0, row=1)
botao5 = ttk.Button(quadro, text='5', command=lambda: botoes('5'))
botao5.grid(column=1, row=1)
botao6 = ttk.Button(quadro, text='6', command=lambda: botoes('6'))
botao6.grid(column=2, row=1)
botao7 = ttk.Button(quadro, text='7', command=lambda: botoes('7'))
botao7.grid(column=0, row=2)
botao8 = ttk.Button(quadro, text='8', command=lambda: botoes('8'))
botao8.grid(column=1, row=2)
botao9 = ttk.Button(quadro, text='9', command=lambda: botoes('9'))
botao9.grid(column=2, row=2)
botao0 = ttk.Button(quadro, text='0', command=lambda: botoes('0'))
botao0.grid(column=0, row=3)
botao_raiz = ttk.Button(quadro, text='√', command= lambda: botoes('√'))
botao_raiz.grid(column=4, row=1)
botao_pi = ttk.Button(quadro, text='π', command=lambda: botoes('3.14159'))
botao_pi.grid(column=4, row=2)
botao_exp = ttk.Button(quadro,text='x²', command= lambda: botoes('²'))
botao_exp.grid(column=4, row=3)


# botoes dos operadores
botao_soma = ttk.Button(quadro, text='+', command=lambda: botoes('+'))
botao_soma.grid(column=3, row=3)
botao_subtracao = ttk.Button(quadro, text='-', command=lambda: botoes('-'))
botao_subtracao.grid(column=3, row=2)
botao_divisao = ttk.Button(quadro, text='/', command=lambda: botoes('/'))
botao_divisao.grid(column=3, row=1)
botao_multiplicacao = ttk.Button(quadro, text='*', command=lambda: botoes('*'))
botao_multiplicacao.grid(column=3, row=0)
botao_dot = ttk.Button(quadro, text='.', command=lambda: botoes('.'))
botao_dot.grid(column=1, row=3)
botao_igual = ttk.Button(quadro, text='=', command=_botao_igual)
botao_igual.grid(column=2, row=3)
botao_apaga = ttk.Button(quadro, text='del', command=_limpa)
botao_apaga.grid(column=4, row=0)


root.bind("<Return>", _botao_igual)
root.bind("<Key>", binds)
root.mainloop()


if __name__ == '__main__':
    print(lista)
    print(resposta)
