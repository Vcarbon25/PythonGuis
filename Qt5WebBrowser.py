from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class MyWebBrowser(QMainWindow):

    def __init__(self):

        self.window = QWidget()
        self.window.setWindowTitle("Will be bot")

        self.layout=QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)
        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)
        self.frw_btn = QPushButton("->")
        self.frw_btn.setMinimumHeight(30)
        self.bk_btn = QPushButton("<-")
        self.bk_btn.setMinimumHeight(30)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.bk_btn)
        self.horizontal.addWidget(self.frw_btn)
        
        self.browser = QWebEngineView()

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.frw_btn.clicked.connect(self.browser.back)
        self.bk_btn.clicked.connect(self.browser.forward)

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("http://www.google.com.br"))

        self.window.setLayout(self.layout)
        self.window.show()

        def navigate(self, url):
            if not url.startswith("http"):
                url = "http://"+url
                self.url_bar.setText(url)
                self.browser.setUrl(QUrl(url))

app = QApplication([])
window = MyWebBrowser()
app.exec()