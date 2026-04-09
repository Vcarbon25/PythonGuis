import tkinter as TK
import cv2
import numpy as np

root = TK.Tk()
Canva = TK.Canvas(root,height=400,width=400,background="LightGray")
Canva.grid(row=0,column=0,columnspan=2)
Xlb=TK.Label(root,text="X:  ").grid(row=1,column=0)
XInput = TK.Scale(root,from_=-1024, to=1024, orient=TK.HORIZONTAL,length=400)
XInput.grid(row=1,column=1)
Ylb=TK.Label(root,text="Y:  ").grid(row=2,column=0)
YInput = TK.Scale(root,from_=-1024, to=1024, orient=TK.HORIZONTAL,length=400)
YInput.grid(row=2,column=1)
def UpdateInputs():
    Xvalue = XInput.get()
    YValue=YInput.get()
    Canva.delete('all')
    Xnormalized = Xvalue*200/1024
    YNormalized= YValue*-200/1024
    Canva.create_line(200,200,Xnormalized+200,YNormalized+200, arrow=TK.LAST, width=4,fill='black')
    
    root.after(100,UpdateInputs)
    #the above line will wait for the miliseconds informed first, and call de designated function


UpdateInputs() #starts the update recursion                                
root.mainloop()