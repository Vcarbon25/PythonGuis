import tkinter as TK

window = TK.Tk()
root = TK.LabelFrame(window,text="application")
root.pack()

BtAdd = TK.Button(root,text="Add row:")
BtAdd.grid(row=0,column=0)
BtDel= TK.Button(root,text="Delete row")
BtDel.grid(row=1,column=0)
CvContainer = TK.Canvas(root,height=300,width=250)
CvContainer.grid(row=0,column=1)
YScroll = TK.Scrollbar(CvContainer,orient='vertical')
YScroll.pack(side=TK.RIGHT,fill="y")
CvContainer.config(yscrollcommand=YScroll.set)
YScroll.config(command=CvContainer.yview)

def AddRow():
    LFAtr=TK.LabelFrame(CvContainer,text="atr",width=70,height=50,padx=20,pady=10)
    LFAtr.pack()
    EnInfo = TK.Entry(LFAtr)
    EnInfo.grid(row=0,column=0)
    
def Del_Row():
    Elements = CvContainer.winfo_children()
    Elements[-1].pack_forget()
BtAdd.config(command=AddRow)
BtDel.config(command=Del_Row)
root.mainloop()