import tkinter as TK
from tkinter import Label, messagebox

root = TK.Tk()
root.title = "mostrar caixa de mensagem"


def popup():
    retorno = messagebox.askquestion("Esse é o título", "Esse o corpo")
    if retorno == "yes":
        etiqueta = TK.Label(root, text="botão pressionado yes").pack()
    elif retorno == "no":
        etiqueta = TK.Label(root, text="botão pressionado no").pack()


Botao = TK.Button(root, text="abrir mensagem", command=popup)
Botao.pack()

TK.mainloop()
