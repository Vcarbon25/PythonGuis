import tkinter as TK

janela = TK.Tk()

janela.title("Option Menu Seleções")
janela.geometry("400x400")


def display_selecao(escolha1):
    escolha1 = variavel.get()
    print("valor do menu: ", escolha1, "-", type(escolha1))
    # E=TK.Label(janela,text=escolha1).pack
    if escolha1 == "primeira":
        Et1.configure(bg="blue")
    elif escolha1 == "segunda":
        Et1.configure(bg="green")
    else:
        Et1.configure(bg="purple")


def selecao2(escolha2):
    escolha2 = variavel2.get()
    if escolha2 == 1:
        Et2.configure(bg="orange")
    elif escolha2 == 2:
        Et2.configure(bg="black")
    elif escolha2 == 3:
        Et2.configure(bg="cyan")
    else:
        Et2.configure(bg="brown")


variavel = TK.StringVar()
opcoes = ["primeira", "segunda", "terceira"]
# opcoes=[1,2,3]
Drop1 = TK.OptionMenu(janela, variavel, *opcoes, command=display_selecao)
Drop1.grid(row=0, column=0)
Et1 = TK.Label(janela, width=20, height=10, bg="white")
Et1.grid(row=1, column=0)
opcoes2 = [1, 2, 3, 4]
variavel2 = TK.IntVar()
Drop2 = TK.OptionMenu(janela, variavel2, *opcoes2, command=selecao2)
Drop2.grid(row=0, column=1)
Et2 = TK.Label(janela, width=20, height=10, bg="white")
Et2.grid(row=1, column=1)

janela.mainloop()
