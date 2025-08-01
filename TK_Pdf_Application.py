"""
requirements
    pip install fitz
    pip install Pillow
    
"""
import tkinter as TK
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
import fitz

root = TK.Tk()
root.config(background="Blue")
menubar = TK.Menu(root) #This will be the main hub for the top menu
FilesMenu = TK.Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=FilesMenu)
MiscOperations = TK.Menu(menubar,tearoff=1)
menubar.add_cascade(label="Edit",menu=MiscOperations)
MainContainer = TK.LabelFrame(root)
MainContainer.pack(fill="both")
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
InZoom = TK.Entry(MainContainer,width=8)
InZoom.grid(row=3,column=0)
Opc = TK.StringVar()
Opc.set("Img")
RBPageImag = TK.Radiobutton(MainContainer,text="Render Page",variable=Opc,value="Img")
RBPageText = TK.Radiobutton(MainContainer,text="Page Text",variable=Opc,value="Txt")
RBPageImag.grid(row=4,column=0)
RBPageText.grid(row=5,column=0)
ContPag = TK.LabelFrame(MainContainer, text="Conteudo", background="white")
ContPag.grid(row=2, column=1,rowspan=5)

# Create a frame to hold the canvas and scrollbars
canvas_frame = TK.Frame(ContPag)
canvas_frame.pack(fill=TK.BOTH, expand=True)

# Canvas with scroll region
PageImg = TK.Canvas(canvas_frame, height=550,width=600,
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
    global Document
    Document = fitz.open(FileN)
    LstPages = list(range(len(Document)))
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
    try:
        zoom = float(InZoom.get())
    except:
        messagebox.showinfo("Erro no zoom","Informe um numero com . de saparador decimal")
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
    print(str(root.winfo_width())+" "+str(root.winfo_height()))

LBPages.bind("<<ListboxSelect>>", LBSelChange)

def CutPdf():
    Page2Cut = int(LBPages.curselection()[0])
    LastPage=len(Document)
    name1=filedialog.asksaveasfilename(initialdir="Documents",title="Nome 1 pdf",filetypes=[("PDF files", "*.pdf")])
    Newdoc1=fitz.open()
    Newdoc1.insert_pdf(Document,from_page=0,to_page=Page2Cut)
    Newdoc1.save(name1)
    name2=filedialog.asksaveasfilename(initialdir="Documents",title="Nome 2 PDF",filetypes=[("PDF files", "*.pdf")])
    NewDoc2=fitz.open()
    NewDoc2.insert_pdf(Document,from_page=Page2Cut+1,to_page=LastPage)
    NewDoc2.save(name2)
MiscOperations.add_command(label="Cut pdf",command=CutPdf) 

def MergePdfs():
    file2 = filedialog.askopenfile(filetypes=[("PDF files",'*.pdf')])
    doc2=fitz.open(file2)
    Document.insert_pdf(doc2)
    ArquivoNovo=filedialog.asksaveasfilename(filetypes=[("PDF","*.pdf")])
    Document.save(ArquivoNovo)

MiscOperations.add_command(label="merge pdfs",command=MergePdfs)

def Export_Menu():
    
    ExpMenu = TK.Toplevel(root)
    LbIn=TK.Label(ExpMenu, text="Initial page")
    LbIn.grid(row=0,column=0)
    StrPgIn=TK.Entry(ExpMenu,width=4)
    StrPgIn.grid(row=0,column=1)
    LbEnd = TK.Label(ExpMenu,text="Last Page")
    LbEnd.grid(row=1,column=0)
    EndPgIn=TK.Entry(ExpMenu,width=4)
    EndPgIn.grid(row=1,column=1)
    #seting the combobox
    OutFormat=["text", "blocks", "words", "html","xhtml", "json", "xml"]
    Escolha=TK.StringVar()
    Escolha.set("text")
    OutForatIn=TK.OptionMenu(ExpMenu,Escolha,*OutFormat)
    OutForatIn.grid(row=3,column=0)

    def Export():
        try:
            StartPage=int(StrPgIn.get())
            EndPage = int(EndPgIn.get())
            OutData=''
            for i in range(StartPage,EndPage+1):
                OutData+= Document[i].get_text(str(Escolha.get()))
            
            filepath=filedialog.asksaveasfilename(initialdir="Desktop")
            OutFile = open(filepath,"w",encoding='utf8')
            OutFile.write(OutData)
            OutFile.close()
        except:
            messagebox.showerror("Input Error","Page Numbers must be Integers")
    
    BtExport=TK.Button(ExpMenu,text="Export data",command=Export)
    BtExport.grid(row=3,column=2)
MiscOperations.add_command(label="Extraction",command=Export_Menu)

root.config(menu=menubar)
root.mainloop()