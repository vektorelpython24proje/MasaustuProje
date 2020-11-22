import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
from PyQt5 import uic,QtWidgets

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"BERKE\ilk.ui",self)
        self.initUI()

    def initUI(self):
        self.btnGiris.clicked.connect(self.girisYap)
        self.btnIptal.clicked.connect(self.temizle)
        self.tbl.setRowCount(1)
        self.tbl.setColumnCount(2)
        self.cbx.currentTextChanged.connect(self.sonuc)
        self.show()
    

    def girisYap(self):
        numRows = self.tbl.rowCount()
        kullanici = QtWidgets.QTableWidgetItem(self.txtUserName.text())
        sifre = QtWidgets.QTableWidgetItem(self.txtSifre.text())
        self.tbl.setItem(numRows-1,0,kullanici)
        self.tbl.setItem(numRows-1,1,sifre)
        self.tbl.setRowCount(numRows+1)
        self.cbx.addItem(self.txtUserName.text())
        
    def sonuc(self):
        sonuc = self.cbx.currentText()
        self.lblSonuc.setText(sonuc)

    def temizle(self):
        self.txtUserName.setText("")
        self.txtSifre.setText("")
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

    # UI ekranının python kodu olarak dökümünü almak
    # cmd Anaconda Prompta geç 
    # cd (ui dosyası dizini) 
    # pyuic5 ilk.ui -o ilkUI.py --> (Bu UI için)
