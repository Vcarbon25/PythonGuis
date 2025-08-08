import tkinter as TK
from tkinter import messagebox
import tkinter.filedialog as FD
import sqlite3

class App():
    def __init__(self,master=None):

        master.title("SQL Workbench")
        self.top = master.winfo_toplevel()
        self.TopMenu = TK.Menu(self.top)
        self.top['menu'] = self.TopMenu
        
        self.Dr1 = TK.Menu(self.TopMenu,tearoff=1)
        self.TopMenu.add_cascade(label='File',menu=self.Dr1)
        self.Dr1.add_command(label='Create DB',command=self.New_DB)
        self.Dr1.add_command(label="Open DB",command=self.Open_File)
        self.Dr2 = TK.Menu(self.TopMenu,tearoff=1)
        self.TopMenu.add_cascade(label="Operations",menu=self.Dr2)
        self.Dr2.add_command(label="Commit Changes",command=self.Save)
        self.Dr2.add_command(label="SQL help", command=self.SQLHelp)
        
        self.LbFile=TK.Label(master,text="Select File")
        self.LbFile.grid(row=0,column=0)
        self.FrTextNScroll = TK.Frame(master)
        self.FrTextNScroll.grid(row=1,column=0,columnspan=3) #in this segment make possible to control y position in text widget with scrollbar
        self.ScrText=TK.Scrollbar(self.FrTextNScroll)
        self.ScrText.pack(side=TK.RIGHT,fill=TK.Y)
        self.TxInteractions = TK.Text(self.FrTextNScroll,border=2,yscrollcommand=self.ScrText.set)
        self.TxInteractions.pack()
        self.ScrText.config(command=self.TxInteractions.yview)

        #returning to main screen to insert the data
        self.LbIn = TK.Label(master,text="Input: ")
        self.LbIn.grid(row=2,column=0)
        self.TxIn = TK.Entry(master,width=60)
        self.TxIn.grid(row=2,column=1)
        self.File=''
        self.BtOk=TK.Button(master,text="Send Command",command=self.Update_Interaction)
        self.BtOk.grid(row=2,column=0)

    def Update_Interaction(self,*text):
        UserIn=self.TxIn.get()
        self.TxIn.delete(0,TK.END)
        if self.File=='':
            self.TxInteractions.insert(TK.END,"Select File\n\n")

        if UserIn.strip()!='':
            self.TxInteractions.insert(TK.END, UserIn+"\n")
            self.TxIn.delete(0,TK.END)
            try: #will execute this block in select statements
                self.cursor.execute(UserIn)
                query = self.cursor.fetchall()
                for row in query:

                    self.TxInteractions.insert(TK.END,str(row)+"\n")
            except:
                self.TxInteractions.insert(TK.END, "wasn't possible to execute above command")
        if text!="":
            self.TxInteractions.insert(TK.END, str(text)+"\n")
            
            
    def Open_File(self):
        self.File = FD.askopenfilename(initialdir="Desktop")
        self.LbFile.config(text=self.File.split("/")[-1])
        if self.File.split(".")[-1]=="db":
            self.Db=sqlite3.connect(self.File)
            self.cursor=self.Db.cursor()
            self.cursor.execute('SELECT name FROM sqlite_master WHERE type="table";')
            self.TxIn.delete(0,TK.END)
            self.Update_Interaction("Tabelas Disponiveis: "+str(self.cursor.fetchall())+"\n")
    def New_DB(self):
        self.File = FD.asksaveasfilename(initialdir="Desktop",filetypes=(("Databases","*.db"),))
       
        self.LbFile.config(text=self.File.split("/")[-1])
        if self.File.split(".")[-1]=="db":
            self.Db=sqlite3.connect(self.File)
            self.cursor=self.Db.cursor()
            self.Update_Interaction("Database Created")
    def Save(self):
        self.Db.commit()
        self.Update_Interaction("Commit")
    
    def SQLHelp(self):
        self.HelpWindow=TK.Toplevel()
        self.HelpWindow.title("SQL tips")
        self.LbReference=TK.Label(self.HelpWindow,text="Reference:  https://www.sqlite.org/")
        self.LbHelp1 = TK.Label(self.HelpWindow,text=""">>CREATE NEW TABLE\n CREATE TABLE name (Colunmname type....)
                                types can be:  text, numeric, interger, real, blob""")
        self.LbHelp1.grid(row=0,column=0)
        self.LbHelp2=TK.Label(self.HelpWindow,text=""">>GET TABLE DETAILS\n PRAGMA table_info(table_name)""")
        
        self.LbHelp2.grid(row=1,column=0)
        self.LbHelp3=TK.Label(self.HelpWindow,text=">>UPDATE TABLE COLUNMS\n ALTER TABLE tableName ADD colunmname type\n ALTER TABLE tablename DROP ColunmName")
        self.LbHelp3.grid(row=2,column=0)
        self.LbHelp4=TK.Label(self.HelpWindow,text=">>DELETE TABLE\n DROP TABLE tableName")
        self.LbHelp4.grid(row=3,column=0)
        self.LBHelp5=TK.Label(self.HelpWindow,text=""">>INSERT ROW IN TABLE\n INSERT INTO tablename VALUES(value1, value2....)""")
        self.LBHelp5.grid(row=4,column=0)
        self.LbHelp6 = TK.Label(self.HelpWindow,text=">> UPDATE ROW\n UPDATE nometabela SET colunmName=Value\n WHERE colunm condition")
        self.LbHelp6.grid(row=5,column=0)

        self.LBHelp6 = TK.Label(self.HelpWindow,text=""">>SELECT DATA FROM TABLE\nSELECT * (for all colunms\n or ) colunm names\n FROM tablename\n WHERE colum condition""")
        self.LBHelp6.grid(row=6,column=0)
        self.LbHelp7 = TK.Label(self.HelpWindow,text="""SQLite has a inert funcionality where there's an extra colunm in tables, oid,\n that contain an unique index for each colunm this index is\n great to use in select and update statements to avoid erros in data manipulation""")
        self.LbHelp7.grid(row=7,column=0)
root=TK.Tk()
App(root)
root.mainloop()