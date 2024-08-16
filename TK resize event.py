import tkinter as TK
root=TK.Tk()
Lwidth = TK.Label(root,text="window width is :")
Lheight = TK.Label(root,text="window height is:")
Lwidth.grid(row=0,column=0)
Lheight.grid(row=1,column=0)
def size_changed(a):
    width = root.winfo_width()
    height = root.winfo_height()
    Lheight.config(text="window height is: "+str(height))
    Lwidth.config(text="window width is: "+str(width))

root.bind("<Configure>",size_changed)
root.mainloop()
