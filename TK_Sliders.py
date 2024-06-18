import tkinter as TK

root = TK.Tk()
root.title("Sliders")
root.geometry("800x400")


def clique(x):
    valor = horizontal.get()
    etiqueta = TK.Label(root, text=valor).pack()
    root.geometry(str(horizontal.get()) + "x400")


horizontal = TK.Scale(root, from_=0, to=1000, orient=TK.HORIZONTAL, command=clique)
horizontal.pack()

botao = TK.Button(root, text="atualizar valor", command=clique).pack()


root.mainloop()
