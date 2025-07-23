import tkinter as TK
import pandas as pd
import tkinter as TK
from tkinter import messagebox
class Mes():
  def __init__(self,master=None):
    self.BaseWdg = TK.Frame(master)
    self.BaseWdg.pack()
    self.TextOut = TK.Text(self.BaseWdg,width=50,height=20,background="white")
    self.TextOut.grid(row=0,column=0,columnspan=5)
    self.BtOpen = TK.Button(self.BaseWdg,text="Open Month",command=self.OpenMonth)
    self.BtOpen.grid(row=1,column=0)
    self.BtTransac = TK.Button(self.BaseWdg,text="Add transaction",command=self.Operation)
    self.BtTransac.grid(row=1,column=1)
    self.BtUpdate = TK.Button(self.BaseWdg,text="Update Transaction",command=self.UpdateTrs)
    self.BtUpdate.grid(row=1,column=2)
    self.BtDelete = TK.Button(self.BaseWdg, text="Delete Row",command=self.DelTrs)
    self.BtDelete.grid(row=1,column=3)
    
    self.LbIndex = TK.Label(self.BaseWdg,text="Index")
    self.LbIndex.grid(row=2,column=0)
    self.LbDate=TK.Label(self.BaseWdg,text="Date")
    self.LbDate.grid(row=2,column=1)
    self.LbDesc = TK.Label(self.BaseWdg,text="Description")
    self.LbDesc.grid(row=2,column=2)
    self.LbCode = TK.Label(self.BaseWdg,text="Code")
    self.LbCode.grid(row=2,column=3)
    self.LbValue = TK.Label(self.BaseWdg,text="Value")
    self.LbValue.grid(row=2,column=4)
    self.InIndex = TK.Entry(self.BaseWdg,width=10)
    self.InIndex.grid(row=3,column=0)
    self.InDate = TK.Entry(self.BaseWdg,width=10)
    self.InDate.grid(row=3,column=1)
    self.InDesc = TK.Entry(self.BaseWdg,width=10)
    self.InDesc.grid(row=3,column=2)
    self.InCode = TK.Entry(self.BaseWdg,width=10)
    self.InCode.grid(row=3,column=3)
    self.InValue = TK.Entry(self.BaseWdg,width=10)
    self.InValue.grid(row=3,column=4)

  def OpenMonth(self):
    self.Open = TK.Toplevel(self.BaseWdg)
    self.LbMonth = TK.Label(self.Open,text="Month Name")
    self.LbMonth.grid(row=0,column=0)
    self.InMonth = TK.Entry(self.Open,width=15)
    self.InMonth.grid(row=0,column=1)
    self.LbStrtBal = TK.Label(self.Open,text="InitialBalance")
    self.LbStrtBal.grid(row=1,column=0)
    self.InStrtBal = TK.Entry(self.Open,width=15)
    self.InStrtBal.grid(row=1,column=1)
    self.FnsOpen=TK.Button(self.Open,text="OK",command=self.CreateMonth)
    self.FnsOpen.grid(row=2,column=0)
    
  def CreateMonth(self):
    try:
      Nome = self.InMonth.get()
      LastBalance=float(self.InStrtBal.get())
      self.Month=str(Nome)
      self.PreviousBalance=float(LastBalance)
      self.Transac = pd.DataFrame(columns=["Day","Description", "Code", "Valor"])
      self.TotalCongregacao=0
      self.TotalOM=0
      self.TotalDespesas=0
      self.Remessa=0
      self.TotalJuros=0
      self.ShowData()
      self.Open.destroy()
    except:
      messagebox.showinfo("Error", "Please Review the Inputs, numbers must be seppareted by dots (.)")
  
  def ShowData(self):
    self.TextOut.delete('1.0',TK.END)
    self.TextOut.insert('1.1',f"Month {self.Month} initial value is {self.PreviousBalance}\n")
    self.TextOut.insert('2.1',self.Transac)

  def Operation(self):
    try:
      day = self.InDate.get()
      desc = self.InDesc.get()
      cod = self.InCode.get()
      try: 
        valor = float(self.InValue.get())
      except:
        messagebox.showinfo("Number error", "Value must have . as decimal separator")
      self.Transac.loc[len(self.Transac)]=[day,desc,cod,valor]
      self.InCode.delete(0,TK.END)
      self.InDate.delete(0,TK.END)
      
      self.InDesc.delete(0,TK.END)
      self.InValue.delete(0,TK.END)
      self.ShowData()
    except:
      messagebox.showinfo("Operation error", "Month isn't open")

  def UpdateTrs(self):
    try:
      index = int(self.InIndex.get())
      day = self.InDate.get()
      desc = self.InDesc.get()
      cod = self.InCode.get()
      try: 
        valor = float(self.InValue.get())
      except:
        messagebox.showinfo("Number error", "Value must have . as decimal separator")
      self.Transac.loc[index]=[day,desc,cod,valor]
      self.InCode.delete(0,TK.END)
      self.InDate.delete(0,TK.END)
      
      self.InDesc.delete(0,TK.END)
      self.InValue.delete(0,TK.END)
      self.ShowData()
    except:
      messagebox.showinfo("Operation error", "Index out of range")
    
    
  def DelTrs(self):
    try:
      index=int(self.InIndex.get())
      self.Transac.drop(index='length', level=index)
      self.ShowData()
    except:
      messagebox.showinfo("Operation Error","Index out of range")


root = TK.Tk()
Mes(root)
root.mainloop()
