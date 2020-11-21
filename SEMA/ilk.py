import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
from PyQt5 import uic


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"SEMA\ilk.ui",self)
        self.initUI()

    def initUI(self):
        self.tbl.setRowCount(10)
        self.tbl.setColumnCount(2)
        self.btGiris.clicked.connect(self.girisYap)
        self.btIptal.clicked.connect(self.temizle)
        self.show()

    def girisYap(self):
        pass
    
    def temizle(self):
        self.txtUserName.setText("")
        self.txtSifre.setText("")
        self.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
