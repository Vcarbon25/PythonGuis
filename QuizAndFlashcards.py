import tkinter as TK
from tkinter import filedialog
import pandas as pd

class App:
    def __init__(self, master=None):
        master.title("Flashcards")
        master.geometry("350x300")
        #trying to create a top ,enubar
        self.top = master.winfo_toplevel()
        master.MenuBar = TK.Menu(self.top)
        self.M1 = TK.Menu(master.MenuBar, tearoff=0)
        master.MenuBar.add_cascade(label="File",menu=self.M1)
        #normal screen
        self.LbFileN = TK.Label(master,text="lb")
        self.LbFileN.grid(row=0,column=0)
        self.BtOpen = TK.Button(master, text="Select File")
        self.BtOpen.grid(row=1,column=0,pady=10)
        self.BtOpen.bind("<Button-1>",self.LoadFile)
        self.Opr = TK.StringVar()
        self.Opr.set(" ")
        self.RbFlash = TK.Radiobutton(master, text="Flashcards", variable=self.Opr,value="Flashcards", command=self.Disp_FlashC)
        self.RbFlash.grid(row=3,column=0)
        self.RbFlash.flash()
        self.RbQuiz = TK.Radiobutton(master, text="Quiz", variable=self.Opr,value="Quiz",command=self.Disp_FlashC)
        self.RbQuiz.grid(row=4,column=0)
       
        #self.BtFlashC.bind("<Button-1>", self.Disp_FlashC)
        self.CardCnt = TK.Frame(master, width=200, height=200,bg="CYAN")
        self.CardCnt.pack_propagate(False)
        self.CardCnt.grid(row=0,column=1,rowspan=5,columnspan=3,padx=20)
        
        self.LBHint = TK.Label(self.CardCnt, text="Hint goes here")
        
        self.LBAnswer = TK.Label(self.CardCnt, text="Here goes answer")
        
        self.BtShAnswer = TK.Button(self.CardCnt,text="Show Answer",command=lambda: self.LBAnswer.config(text=self.LData[self.Index][1]))
        
        self.Answer = TK.IntVar()
        self.Answer.set(99)
        self.CntAnsw = TK.LabelFrame(self.CardCnt,text="Answers")
        self.RbAsw1 = TK.Radiobutton(self.CntAnsw, text="Opc 0", value=0, variable=self.Answer)
        self.RbAsw1.grid(row=0,column=0)
        self.RbAsw2 = TK.Radiobutton(self.CntAnsw, text="Opc 1", value=1, variable=self.Answer)
        self.RbAsw2.grid(row=0,column=1)
        self.RbAsw3 = TK.Radiobutton(self.CntAnsw, text="Opc 2", value=2, variable=self.Answer)
        self.RbAsw3.grid(row=1,column=0)
        self.RbAsw4 = TK.Radiobutton(self.CntAnsw, text="Opc 3", value=3, variable=self.Answer)
        self.RbAsw4.grid(row=1,column=1)
        self.BtBck = TK.Button(master,text="<",command=self.Previous_Card)
        self.BtBck.grid(row=5,column=1)
        self.BtFrw = TK.Button(master,text=">",command=self.Card_Forward)
        self.BtFrw.grid(row=5,column=3)
        self.Index=0
        self.LData=[]

    def LoadFile(self,event):
        self.FIleN = filedialog.askopenfilename(initialdir="Desktop")
        print(self.FIleN)
        Nm = self.FIleN.split('/')
        self.LbFileN.config(text=Nm[-1])
        
    def Disp_FlashC(self):
        try:
            opc=self.Opr.get()
            for child in self.CardCnt.winfo_children():
                child.grid_forget()
            if opc=="Flashcards":
                self.LBHint.grid(row=0,column=0,pady=20)
                self.LBAnswer.grid(row=2,column=0)
                self.BtShAnswer.grid(row=3,column=0)
            if opc=="Quiz":
                self.LBHint.grid(row=0,column=0,pady=20)
                self.LBAnswer.grid(row=2,column=0)
                self.CntAnsw.grid(row=2,column=0)
            print(opc)
            print(self.FIleN)
            Data =pd.read_excel(self.FIleN)
            print(Data)
            self.LData = list(zip(Data['Question'],Data["Correct_Answer"],Data['Wrong_Answer1'],Data["Wrong_Answer2"],Data["Wrong_Answer3"]))
            print("\n ",self.LData)
            self.LBHint.config(text=self.LData[self.Index][0])
            self.LBAnswer.config(text="____")
            
        except Exception as E:
            print(E)
    
    def Card_Forward(self):
        self.Index +=1
        if self.Index > len(self.LData)-1: #to keep the index variable inside the document lenght
            self.Index=0
        

        self.LBHint.config(text=self.LData[self.Index][0])
        self.LBAnswer.config(text="____")
    
    def Previous_Card(self):
        self.Index -=1
        if self.Index < 0: #to keep the index variable inside the document lenght
          self.Index = len(self.LData)-1 

        
        
        self.LBHint.config(text=self.LData[self.Index][0])
        self.LBAnswer.config(text="____")
root=TK.Tk()
App(root)
root.mainloop()