import tkinter as TK

root = TK.Tk()

def Input():
    InputW = TK.Toplevel(root)
    In1 = TK.Entry(InputW,width=20)
    In1.pack()
    In2 = TK.Entry(InputW,width=20)
    In2.pack()
    def CloseInputs():
        vl1=In1.get()
        vl2=In2.get()
        print(f"inputs are {vl1} and {vl2}")
        InputW.destroy()
    BtClose=TK.Button(InputW,text="Close",command=CloseInputs)
    BtClose.pack()
BtSecond=TK.Button(root,text="Open Second Window",command=Input)
BtSecond.pack()


root.mainloop()