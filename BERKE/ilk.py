import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
from PyQt5 import uic

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"BERKE\ilk.ui",self)
        self.initUI()

    def initUI(self):
        
        
        
        self.btnIptal.clicked.connect(self.tiklandi)
        

        self.show()
    
    def tiklandi(self):
        print("Tiklandi")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())