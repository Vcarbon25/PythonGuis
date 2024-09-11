#pip install PyQt6

import PyQt6.QtWidgets as Qt

app=Qt.QApplication([])

window = Qt.QWidget()
'''
#line Layouts
button1 = Qt.QLabel("One")
button2 = Qt.QLabel("Two")
button3 = Qt.QLabel("Three")
button4 = Qt.QLabel("Four")
button5 = Qt.QLabel("Five")

#layout = Qt.QVBoxLayout(window)
layout = Qt.QHBoxLayout(window)
layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)
layout.addWidget(button4)
layout.addWidget(button5)
'''
'''
#grid lauout
layout = Qt.QGridLayout(window)
L1=Qt.QLabel("first")
L2 =Qt.QLabel("Second")
L3=Qt.QLabel("third expanded")
L4=Qt.QLabel("Fourth")
layout.addWidget(L1, 0, 0)
layout.addWidget(L2, 0, 1)
layout.addWidget(L3,1,0,1,2)
layout.addWidget(L4,2,0)
'''
#Form Layout
layout = Qt.QFormLayout(window)
L1=Qt.QLabel("1st info: ")
T1=Qt.QLineEdit()
L2=Qt.QLabel("2nd info")
T2=Qt.QLineEdit()
layout.addRow(L1, T1)
layout.addRow(L2,T2)
window.show()
app.exec()