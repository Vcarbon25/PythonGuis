
import tkinter as TK
from tkinter import filedialog
import PyPDF2 as pdf
from PIL import Image, ImageTk
from tkinter import messagebox
import fitz

root = TK.Tk()
root.config(background="Blue")
menubar = TK.Menu(root) #This will be the main hub for the top menu
FilesMenu = TK.Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=FilesMenu)
MainContainer = TK.LabelFrame(root)
MainContainer.pack()
global Document
LbFile = TK.Label(MainContainer, text="fileName")
LbFile.grid(row=0, column=0,columnspan=2)



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
Opc = TK.StringVar()
Opc.set("Img")
RBPageImag = TK.Radiobutton(MainContainer,text="Render Page",variable=Opc,value="Img")
RBPageText = TK.Radiobutton(MainContainer,text="Page Text",variable=Opc,value="Txt")
RBPageImag.grid(row=3,column=0)
RBPageText.grid(row=4,column=0)
ContPag = TK.LabelFrame(MainContainer, text="Conteudo", background="white")
ContPag.grid(row=2, column=1,rowspan=3)

# Create a frame to hold the canvas and scrollbars
canvas_frame = TK.Frame(ContPag)
canvas_frame.pack(fill=TK.BOTH, expand=True)

# Canvas with scroll region
PageImg = TK.Canvas(canvas_frame, height=400, width=400, 
                 scrollregion=(0, 0, 1000, 1000))
PageText = TK.Text(canvas_frame, height=30,width=60)


# Vertical Scrollbar
YScroll = TK.Scrollbar(canvas_frame, orient=TK.VERTICAL, command=PageImg.yview)
YScroll.pack(side=TK.RIGHT, fill=TK.Y)

# Horizontal Scrollbar
XScroll = TK.Scrollbar(canvas_frame, orient=TK.HORIZONTAL, command=PageImg.xview)
XScroll.pack(side=TK.BOTTOM, fill=TK.X)

PageImg.pack(side=TK.LEFT, fill=TK.BOTH, expand=True)
# Configure canvas scrolling
PageImg.config(yscrollcommand=YScroll.set, xscrollcommand=XScroll.set)

FileN = ""

def PdfParser(FileN):
    LBPages.delete(0, TK.END)
    global LstPages
    leitor = pdf.PdfReader(FileN)
    LstPages = list(range(1, len(leitor.pages) + 1))
    print(LstPages)
    LBPages.insert(0, *LstPages)
    global Document
    Document = fitz.open(FileN)

def Open_File():
    global FileN
    FileN = filedialog.askopenfilename()
    Name = FileN.split("/")
    LbFile.config(text=str(Name[-1]))
    FileExt = Name[-1].split(".")[-1]
    if FileExt == "pdf":
        PdfParser(FileN)

FilesMenu.add_command(label="Open File",command=Open_File)

def Operation_Change():
    Option = Opc.get()
    for child in canvas_frame.winfo_children():
        child.pack_forget()
    if Option =="Txt":
        PageText.pack()
    elif Option=="Img":
        YScroll.pack(side=TK.RIGHT, fill=TK.Y)
        XScroll.pack(side=TK.BOTTOM, fill=TK.X)
        PageImg.pack()
        
RBPageImag.config(command=Operation_Change)
RBPageText.config(command=Operation_Change)
def ShowText(num):
    PageText.delete("1.0",TK.END)
    content = Document[num].get_text()
    PageText.insert("1.0",content)
    

def RenderPage(num):
    # Clear previous content
    PageImg.delete("all")
    
    # render page
    
    zoom = 1
    mat = fitz.Matrix(zoom, zoom)
    pag = Document.load_page(num)
    PixMat = pag.get_pixmap(matrix=mat)
    
    # Convert to PIL Image
    Img = Image.frombytes("RGB", [PixMat.width, PixMat.height], PixMat.samples)
    
    # Create PhotoImage
    ImgTk = ImageTk.PhotoImage(Img)
    
    # Display image on canvas
    PageImg.create_image(0, 0, anchor='nw', image=ImgTk)
    PageImg.image = ImgTk  # Keep a reference
    
    # Update scroll region to match image size
    PageImg.config(scrollregion=(0, 0, PixMat.width, PixMat.height))

def LBSelChange(a):
    IndexSelected = int(LBPages.curselection()[0])
    RenderPage(IndexSelected)  # Adjust index to 0-based
    ShowText(IndexSelected)

LBPages.bind("<<ListboxSelect>>", LBSelChange)
root.config(menu=menubar)
root.mainloop()