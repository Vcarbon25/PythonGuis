
# importing only  those functions  
# which are needed 
import tkinter as tk 


  
# creating tkinter window 
root = tk.Tk() 
root.title('Menu Demonstration') 

def  func():
    print("clicked 1 cascate, 1 button")  
# Creating Menubar 
menubar = tk.Menu(root) 

# Adding File Menu and commands 
M1 = tk.Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Cascate 1', menu = M1) 
M1.add_command(label ='Bt1', command = func) 
M1.add_command(label ='Bt2', command = lambda: print("Cascate 1 Bt2")) 
M1.add_separator() 
M1.add_command(label ='Exit', command = root.destroy) 
  
# Adding Edit Menu and commands 
M2 = tk.Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Cascate 2', menu = M2) 
M2.add_command(label ='Bt1', command = lambda: print("cascate 2 Bt1")) 
 
  
M3 = tk.Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Cascate 3', menu = M3) 
M3.add_command(label ='', command = lambda:print("Clicked phanton Button")) #Buttons don't need a string for function, but they will allocate space
M3.add_separator() 
M3.add_command(label ='Demo', command = lambda: print("clicked cascate 3 Bt2")) 

  
# display Menu 
root.config(menu = menubar) 
root.mainloop() 
