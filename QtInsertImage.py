import PyQt6.QtWidgets as Qt 
from PyQt6.QtGui import QPixmap
app = Qt.QApplication([])
window = Qt.QWidget()
layout=Qt.QGridLayout(window)
window.setWindowTitle("Complex_APP")
Bt=Qt.QPushButton("Select File")
layout.addWidget(Bt,0,0)
LbImg=Qt.QLabel("teste")
layout.addWidget(LbImg,0,1)
def Clicou():
    fname = Qt.QFileDialog.getOpenFileName(window,"Escolha","Documents/")
    print(fname[0],type(fname[0]))
    pixmap = QPixmap(fname[0])
    LbImg.setPixmap(pixmap)
    LbImg.setScaledContents(True)
Bt.clicked.connect(Clicou)

window.show()
app.exec()