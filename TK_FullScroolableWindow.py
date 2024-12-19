import tkinter as tk

root=tk.Tk()

root.title("Full Scroolable Screen")
root.geometry("500x500")
#first create a main container in the root
MainContainer = tk.Frame(root)
MainContainer.pack(fill=tk.BOTH, expand=1)

#create the canvas that will group the scroll bars and window
Cvs = tk.Canvas(MainContainer)
Cvs.pack(side=tk.LEFT,fill=tk.BOTH, expand=1)
#put the scrollbar
YScroll = tk.Scrollbar(MainContainer,orient=tk.VERTICAL,command=Cvs.yview)
YScroll.pack(side=tk.RIGHT,fill=tk.Y)
XScroll = tk.Scrollbar(root,orient=tk.HORIZONTAL,command=Cvs.xview)
XScroll.pack(side=tk.BOTTOM,fill=tk.X)

#configure canvas
Cvs.configure(yscrollcommand=YScroll.set)
Cvs.configure(xscrollcommand=XScroll.set)
Cvs.bind('<Configure>', lambda e: Cvs.configure(scrollregion=Cvs.bbox('all')))

InnerFrame = tk.Frame(Cvs)

Cvs.create_window((0,0),window=InnerFrame,anchor='nw')
for element in range(50):
    if element==3:
        for sub in range(20):
            tk.Button(InnerFrame ,text="Button 3 x "+str(sub)).grid(row=3,column=sub)
    else:
        tk.Button(InnerFrame,  text="Element "+str(element)+" x 1").grid(row=element,column=1)

root.mainloop()
