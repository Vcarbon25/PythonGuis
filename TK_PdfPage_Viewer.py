import tkinter as TK
from tkinter import filedialog
import PyPDF2 as pdf
from PIL import Image, ImageTk
from tkinter import messagebox
import fitz

root=TK.Tk()

root.title("Pdf Applicarion")
root.geometry('750x600')
#first to create the scroolable screen
#create a main container in the root
MainContainer = TK.Frame(root)
MainContainer.pack(fill=TK.BOTH, expand=1)

#create the canvas that will group the scroll bars and window
Cvs = TK.Canvas(MainContainer,height=1200,width=800)
Cvs.pack(side=TK.LEFT,fill=TK.BOTH, expand=1)
#put the scrollbar
YScroll = TK.Scrollbar(MainContainer,orient=TK.VERTICAL,command=Cvs.yview,width=15)
YScroll.pack(side=TK.RIGHT,fill=TK.Y)
XScroll = TK.Scrollbar(root,orient=TK.HORIZONTAL,command=Cvs.xview)
XScroll.pack(side=TK.BOTTOM,fill=TK.X)

#configure canvas
Cvs.configure(yscrollcommand=YScroll.set)
Cvs.configure(xscrollcommand=XScroll.set)
Cvs.bind('<Configure>', lambda e: Cvs.configure(scrollregion=Cvs.bbox('all')))

InnerFrame = TK.Frame(Cvs)

Cvs.create_window((0,0),window=InnerFrame,anchor='nw')
#From this point all the widgets ,ust be inserted in the Inner Frame

LbFile = TK.Label(InnerFrame, text="fileName")
LbFile.grid(row=0, column=0,columnspan=3)

BOpenFile = TK.Button(InnerFrame, text="Choose File")
BOpenFile.grid(row=1, column=0)

ContLstPages = TK.LabelFrame(InnerFrame, text="Paginas", border=3)
ContLstPages.grid(row=2, column=0)

ScrollLB = TK.Scrollbar(ContLstPages)
ScrollLB.pack(side="right", fill="y")

LstPages = [1, 2]
LBPages = TK.Listbox(
    ContLstPages, listvariable=LstPages, yscrollcommand=ScrollLB.set, width=18
)
ScrollLB.config(command=LBPages.yview)

ContWorking = TK.LabelFrame(InnerFrame, text="Operation Mode", border=3, background="blue")
ContWorking.grid(row=3, column=1)

LBPages.pack()


# Canvas with scroll region
Page = TK.Canvas(InnerFrame,height=1200,width=800)
Page.grid(row=2, column=2,rowspan=4)

FileN = ""

def PdfParser(FileN):
    LBPages.delete(0, TK.END)
    global LstPages
    leitor = pdf.PdfReader(FileN)
    LstPages = list(range(1, len(leitor.pages) + 1))
    print(LstPages)
    LBPages.insert(0, *LstPages)

def Open_File():
    global FileN
    FileN = filedialog.askopenfilename()
    Name = FileN.split("/")
    LbFile.config(text=str(Name[-1]))
    FileExt = Name[-1].split(".")[-1]
    if FileExt == "pdf":
        PdfParser(FileN)

BOpenFile.config(command=Open_File)

def RenderPage(num):
    # Clear previous content
    Page.delete("all")
    
    # Open document and render page
    DispDoc = fitz.open(FileN)
    zoom = 1
    mat = fitz.Matrix(zoom, zoom)
    pag = DispDoc.load_page(num)
    PixMat = pag.get_pixmap(matrix=mat)
    
    # Convert to PIL Image
    Img = Image.frombytes("RGB", [PixMat.width, PixMat.height], PixMat.samples)
    
    # Create PhotoImage
    ImgTk = ImageTk.PhotoImage(Img)
    
    # Display image on canvas
    Page.create_image(0, 0, anchor='nw', image=ImgTk)
    Page.image = ImgTk  # Keep a reference
    
    # Update scroll region to match image size
    Page.config(scrollregion=(0, 0, PixMat.width, PixMat.height))

def LBSelChange(a):
    IndexSelected = int(LBPages.curselection()[0])
    RenderPage(IndexSelected - 1)  # Adjust index to 0-based

LBPages.bind("<<ListboxSelect>>", LBSelChange)
root.mainloop()