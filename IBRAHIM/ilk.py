from PyQt5 import uic,QtWidgets
import sys
from PyQt5.QtWidgets import QApplication,QDialog

class App(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"IBRAHIM\ilk.ui",self)
        self.initUI()

    def initUI(self):
        self.table.setRowCount(1)
        self.table.setColumnCount(2)
        self.bgiris.clicked.connect(self.girisyap)
        self.biptal.clicked.connect(self.temizle)
        self.show()

    def girisyap(self):
        numRows = self.table.rowCount()
        kullanici = QtWidgets.QTableWidgetItem(self.txtUsername.text())
        sifre = QtWidgets.QTableWidgetItem(self.txtPass.text())
        self.table.setItem(numRows-1,0,kullanici)
        self.table.setItem(numRows-1,1,sifre)
        self.table.setRowCount(numRows+1)
        self.cmb.addItem(self.txtUsername.text())
    
    def sonuc():
        sonuc=self.cmb.currentText
        self.l3.setText(sonuc)

    def temizle(self):
        self.txtUsername.setText("")
        self.txtSifre.setText("")
        self.close()

    def tiklandi(self):
        self.txtUsername.setText("")
        self.txtPass.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec())