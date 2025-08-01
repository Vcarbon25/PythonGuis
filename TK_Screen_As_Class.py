import tkinter as TK


class Application:
    def __init__(self, master=None):
        master.geometry('300x300')
        self.top = master.winfo_toplevel()
        self.menubar = TK.Menu(self.top)
        self.top['menu'] = self.menubar
        
        self.Dr1 = TK.Menu(self.menubar,tearoff=1)
        self.menubar.add_cascade(label='1st drop',menu=self.Dr1)
        self.Dr1.add_command(label="BtAction",command=lambda: self.mudarTexto('a'))

        self.widget1 = TK.Frame(master)
        self.widget1.pack()
        self.msg = TK.Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Calibri", "9", "italic")
        self.msg.pack()
        self.sair = TK.Button(self.widget1)
        self.sair["text"] = "Clique aqui"
        self.sair["font"] = ("Calibri", "9")
        self.sair["width"] = 10
        self.sair.bind("<Button-1>", self.mudarTexto)
        self.sair.pack()

    def mudarTexto(self, event):
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"


root = TK.Tk()
Application(root)
root.mainloop()
