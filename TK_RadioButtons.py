import tkinter as TK

root = TK.Tk()
root.title = "RadioButtons"

# r=TK.IntVar()
# r.set("0")

Modes = [
    ("calabresa", "calabresa"),
    ("cogumelo", "cogumelo"),
    ("queijo", "queijo"),
    ("cebola", "cebola"),
]
pizza = TK.StringVar()
pizza.set("massa")

for text, mode in Modes:
    radioButton = TK.Radiobutton(root, text=text, variable=pizza, value=mode)
    radioButton.pack()


def clicado(value):
    etiqueta = TK.Label(root, text=value)
    etiqueta.pack()
    return


# RButton1=TK.Radiobutton(root, text="1", variable=r,value=1,command=lambda: clicado(r.get()))
# RButton2=TK.Radiobutton(root,text="2", variable=r,value=2,command= lambda: clicado(r.get()))
# RButton1.pack()
# RButton2.pack()
# etiqueta=TK.Label(root,text=r.get())
# etiqueta.pack()

root.mainloop()
