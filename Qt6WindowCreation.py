#pip install PyQt6

import PyQt6.QtWidgets as Qt

app = Qt.QApplication([])
label = Qt.QLabel('Hello World!')
label.show()
app.exec()

