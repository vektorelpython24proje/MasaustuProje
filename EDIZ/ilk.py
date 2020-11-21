import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
from PyQt5 import uic,QtWidgets

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"EDIZ\ilk.ui",self)  # graphical user interface
        self.initUI()
    
    def initUI(self):
        self.tbl.setRowCount(1)
        self.tbl.setColumnCount(2)
        self.btGiris.clicked.connect(self.girisYap)
        self.btIptal.clicked.connect(self.temizle)
        self.show()

    def girisYap(self):
        numRows = self.tbl.rowCount()
        kullanici = QtWidgets.QTableWidgetItem(self.txtUserName.text())
        sifre = QtWidgets.QTableWidgetItem(self.txtSifre.text())
        self.tbl.setItem(numRows-1,0,kullanici)
        self.tbl.setItem(numRows-1,1,sifre)
        self.tbl.setRowCount(numRows+1)
        self.cmb.addItem(self.txtUserName.text())

    def temizle(self):
        self.txtUserName.setText("")
        self.txtSifre.setText("")
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
