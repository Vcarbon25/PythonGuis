import tkinter as TK 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


def plot():

    
    fig = Figure(figsize = (4, 4), dpi = 300)

    X=[0,1,2,3,4,5,6,7,8,9]
    Y=[-1,0,1,0,-1,0,1,0,-1,0]
    # adding the subplot
    plot1 = fig.add_subplot(111)
  
    # plotting the graph
    plot1.plot(X,Y)

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master = root)  
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

# the main Tkinter window
root = TK.Tk()

# setting the title 
root.title('Plotting in Tkinter')

# dimensions of the main window
root.geometry("500x500")

# button that displays the plot
Btplt = TK.Button(root, command = plot,text = "Plot")

# place the button 
# in main window
Btplt.pack()

# run the gui
root.mainloop()