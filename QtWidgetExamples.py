import sys

#from PyQt6.QtCore import Qt
import PyQt6.QtWidgets as Qw

# Subclass QMainWindow to customize your application's main window
class MainWindow(Qw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = Qw.QVBoxLayout()
        widgets = [
            Qw.QCheckBox,
            Qw.QComboBox,
            Qw.QDateEdit,
            Qw.QDateTimeEdit,
            Qw.QDial,
            Qw.QDoubleSpinBox,
            Qw.QFontComboBox,
            Qw.QLCDNumber,
            Qw.QLabel,
            Qw.QLineEdit,
            Qw.QProgressBar,
            Qw.QPushButton,
            Qw.QRadioButton,
            Qw.QSlider,
            Qw.QSpinBox,
            Qw.QTimeEdit,
        ]

        for w in widgets:
            layout.addWidget(w())

        widget = Qw.QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

app = Qw.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()