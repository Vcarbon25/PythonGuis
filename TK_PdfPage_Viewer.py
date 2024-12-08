import tkinter as TK
from tkinter import filedialog
import PyPDF2 as pdf
from PIL import Image, ImageTk
from tkinter import messagebox
import fitz

root = TK.Tk()
root.config(background="Blue")
MainContainer = TK.LabelFrame(root)
MainContainer.pack()

LbFile = TK.Label(MainContainer, text="fileName")
LbFile.grid(row=0, column=0)

BOpenFile = TK.Button(MainContainer, text="Choose File")
BOpenFile.grid(row=1, column=0)

ContLstPages = TK.LabelFrame(MainContainer, text="Paginas", border=3)
ContLstPages.grid(row=2, column=0)

ScrollLB = TK.Scrollbar(ContLstPages)
ScrollLB.pack(side="right", fill="y")

LstPages = [1, 2]
LBPages = TK.Listbox(
    ContLstPages, listvariable=LstPages, yscrollcommand=ScrollLB.set, width=18
)
ScrollLB.config(command=LBPages.yview)

ContWorking = TK.LabelFrame(MainContainer, text="Operation Mode", border=3, background="blue")
ContWorking.grid(row=3, column=1)

LBPages.pack()

ContPag = TK.LabelFrame(MainContainer, text="Conteudo", background="white")
ContPag.grid(row=2, column=1)

# Create a frame to hold the canvas and scrollbars
canvas_frame = TK.Frame(ContPag)
canvas_frame.pack(fill=TK.BOTH, expand=True)

# Canvas with scroll region
Page = TK.Canvas(canvas_frame, height=400, width=400, 
                 scrollregion=(0, 0, 1000, 1000))
Page.pack(side=TK.LEFT, fill=TK.BOTH, expand=True)

# Vertical Scrollbar
YScroll = TK.Scrollbar(canvas_frame, orient=TK.VERTICAL, command=Page.yview)
YScroll.pack(side=TK.RIGHT, fill=TK.Y)

# Horizontal Scrollbar
XScroll = TK.Scrollbar(canvas_frame, orient=TK.HORIZONTAL, command=Page.xview)
XScroll.pack(side=TK.BOTTOM, fill=TK.X)

# Configure canvas scrolling
Page.config(yscrollcommand=YScroll.set, xscrollcommand=XScroll.set)

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