import tkinter as tk
from tkinter import ttk
"""
# full page tabs
root = tk.Tk()
root.title("Tabbed Interface Example")
root.geometry("400x300")

# Create a Notebook (tabbed container)
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Create individual tabs
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

# Add tabs to the Notebook
notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.add(tab3, text="Tab 3")

# Add content to each tab
label1 = tk.Label(tab1, text="This is the content of Tab 1")
label1.pack(padx=20, pady=20)

label2 = tk.Label(tab2, text="Welcome to Tab 2")
label2.pack(padx=20, pady=20)

label3 = tk.Label(tab3, text="Tab 3 is here!")
label3.pack(padx=20, pady=20)

"""
#small tabs for widgets
root = tk.Tk()
root.config(bg="LightBlue")
LbMain = tk.Label(root, text="Semi Tabs")
LbMain.grid(row=0,column=0)

TabGroup = ttk.Notebook(root,height=200,width=200)

Tab1 = tk.Frame(TabGroup)
Tab2 = tk.Frame(TabGroup)
Tab3 = tk.Frame(TabGroup)

TabGroup.add(Tab1, text="1st Tab")
TabGroup.add(Tab2, text="2nd Tab")
TabGroup.add(Tab3, text="3th Tab")
TabGroup.grid(row=0,column=1)
Lb1 = tk.Label(Tab1,text="inside first Tab")
Lb1.pack()
Lb2 = tk.Label(Tab2, text="inside second tab")
Lb2.pack()
Lb3 = tk.Label(Tab3, text = "inside third tab")
Lb3.pack()
root.mainloop()
