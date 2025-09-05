import tkinter as TK
#set window
root=TK.Tk()
root.geometry("500x500")
LbTest = TK.Label(root,text="Dragable")
LbTest.place(x=50,y=50)

#the next functions will perform the drag operation

def Drag_Start(event): 
    #this function is trigerred when we click in the element we will be dragging
    event.widget.StartX = event.x
    event.widget.StartY = event.y

def Movement(event): 
    #this function is trigerred when movving the mouse while pressing the button
    NewX = event.widget.winfo_x()+(event.x-event.widget.StartX)
    NewY = event.widget.winfo_y()+(event.y-event.widget.StartY)
    #now update the widget with new positions
    event.widget.place(x=NewX,y=NewY)

#now bint the functions to the actions
LbTest.bind("<ButtonPress-1>",Drag_Start)
LbTest.bind("<B1-Motion>",Movement)

root.mainloop()