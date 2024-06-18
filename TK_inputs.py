from tkinter import *

root = Tk()


def clique():
    texto = "o texto é: " + e.get()
    etiqueta = Label(root, text=texto)
    etiqueta.pack()


e = Entry(root, width=50, borderwidth=10)
e.pack()
botao = Button(root, text="Clique Aqui!", command=clique)
botao.pack()

root.mainloop()
