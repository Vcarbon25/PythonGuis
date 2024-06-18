from tkinter import *

root = Tk()  # abre o widget raiz, a janela que será manipulada,
etiqueta1 = Label(root, text="label 1")
etiqueta2 = Label(root, text="label 2")
# a posição (0,0) do grid, está no canto superior esquerdo
"""
esse posicionamento é apenas relativo aos widgets dentro, mas permite mais controle do que pack()
"""
etiqueta1.grid(row=0, column=0)
etiqueta2.grid(row=1, column=1)

root.mainloop()
