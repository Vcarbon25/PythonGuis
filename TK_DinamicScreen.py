import tkinter as TK
root=TK.Tk()
def InsertWidgets(screen):
    WidPart = TK.LabelFrame(screen)
    AtrName= TK.Entry(WidPart,width=30)
    AtrVl = TK.Entry(WidPart,width=30)
    connector = TK.Label(WidPart,text="-->")
    AtrName.grid(row=0,column=0)
    connector.grid(row=0,column=1)
    AtrVl.grid(row=0,column=2)
    WidPart.pack()

def click():
    InsertWidgets(root)
BTInsert = TK.Button(root,text="Click to add elements",command=click)
BTInsert.pack()
root.mainloop()