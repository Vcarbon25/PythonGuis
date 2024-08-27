import tkinter  as TK
from tkinter import filedialog
import json
root = TK.Tk()


root.geometry("700x350")


#Add a Vertical Scrollbar
scroll_v = TK.Scrollbar(root)
scroll_v.pack(side= TK.RIGHT,fill="y")

#Add a Horizontal Scrollbar
scroll_h = TK.Scrollbar(root, orient= TK.HORIZONTAL)
scroll_h.pack(side= TK.BOTTOM, fill= "x")

BtOpen=TK.Button(root,text="Open JSON")
BtOpen.pack()
#Add a Text widget
text = TK.Text(root, height= 500, width= 350, yscrollcommand= scroll_v.set,
xscrollcommand = scroll_h.set, wrap= TK.NONE, font= ('Helvetica 15'))
text.pack(fill = TK.BOTH, expand=0)

def OpenFile():
    arq=filedialog.askopenfilename(initialdir="Documents")
    with open(arq,'r') as doc:
        content=doc.readlines()
        text.delete('1.0',TK.END)
        text.insert('1.0', json.dumps(content,indent=1))
BtOpen.config(command=OpenFile)
#Attact the scrollbar with the text widget
scroll_h.config(command = text.xview)
scroll_v.config(command = text.yview)

root.mainloop()