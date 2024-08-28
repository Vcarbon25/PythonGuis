#requirement pip install lxml
import tkinter  as TK
from tkinter import filedialog
from lxml import etree


root = TK.Tk()
#set window size
root.geometry("700x350")
#set screens top menu
up = root.winfo_toplevel() #get screen's top border location
root.menuBar = TK.Menu(up)
up["menu"] = root.menuBar
root.subMenu = TK.Menu(root.menuBar)
root.menuBar.add_cascade(label="File", menu=root.subMenu)
#Add a Vertical Scrollbar
scroll_v = TK.Scrollbar(root)
scroll_v.pack(side= TK.RIGHT,fill="y")

#Add a Horizontal Scrollbar
scroll_h = TK.Scrollbar(root, orient= TK.HORIZONTAL)
scroll_h.pack(side= TK.BOTTOM, fill= "x")


#Add a Text widget
text = TK.Text(root, height= 500, width= 350, yscrollcommand= scroll_v.set,
xscrollcommand = scroll_h.set, wrap= TK.NONE, font= ('Helvetica 15'))
text.pack(fill = TK.BOTH, expand=0)

def OpenFile():
    arq=filedialog.askopenfilename(initialdir="Documents")
    parser=etree.XMLParser(recover=True,encoding="utf-8", remove_blank_text=True)
    XMLFile = etree.parse(arq,parser=parser)
    
    text.delete('1.0',TK.END)
    text.insert('1.0', etree.tostring(XMLFile, pretty_print=True,encoding=str))
root.subMenu.add_command(label="Open",command=OpenFile)
#Attact the scrollbar with the text widget
scroll_h.config(command = text.xview)
scroll_v.config(command = text.yview)

root.mainloop()