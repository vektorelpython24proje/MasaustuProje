import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
from PyQt5 import uic

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"EDIZ\ilk.ui",self)  # graphical user interface
        self.initUI()
    
    def initUI(self):

        self.btIptal.clicked.connect(self.tiklandi)
        self.show()

    def tiklandi(self):
        self.txt

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
