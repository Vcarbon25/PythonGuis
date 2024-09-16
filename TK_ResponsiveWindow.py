import tkinter as TK

root = TK.Tk()
BtAdd = TK.Button(root,text="Add row:")
BtAdd.grid(row=0,column=0)
LFContainer = TK.LabelFrame(root,text="content",height=300,width=250)
LFContainer.grid(row=0,column=1)

def AddRow():
    LFAtr=TK.LabelFrame(LFContainer,text="atr",width=70,height=50,padx=20,pady=10)
    LFAtr.pack()
    EnInfo = TK.Entry(LFAtr)
    EnInfo.grid(row=0,column=0)
    

BtAdd.config(command=AddRow)
root.mainloop()