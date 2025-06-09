import tkinter as TK
from tkinter import filedialog
import json


root=TK.Tk()


File=1 #initialize a global variable
Content =""
BtAbrir = TK.Button(root,text="Abrir Arq")
BtAbrir.grid(row=0,column=0)
LbKeys = TK.Listbox(root,height=12)
LbKeys.grid(row=0,column=1)
TbSaida = TK.Text(root,width=30,height=20)
TbSaida.grid(row=0,column=2)

def JSONParse(fl):
    with open(fl,"r") as FL:
        global File
        File = json.load(FL)
        global Content
        #Content =json.loads(File)
        chaves = File.keys()
        print(chaves,type(chaves))
        ch=0
        for key in File:
            LbKeys.insert(ch,key)
            ch+=1

def AbrirF():
    arq=filedialog.askopenfilename(initialdir="Desktop")
    print(arq)
    global File
    
    if arq.split(".")[-1] =="json":
        print("arquivo JSON")
        JSONParse(arq)

BtAbrir.config(command=AbrirF)

def Selchanged(a):
    indice = int(LbKeys.curselection()[0])
    Chave = LbKeys.get(indice)
    print(Chave)
    global File
    print(File.get(Chave))
    TbSaida.delete('1.0','end')
    
    TbSaida.insert(TK.END,File.get(Chave))

LbKeys.bind("<<ListboxSelect>>",Selchanged)
root.mainloop()