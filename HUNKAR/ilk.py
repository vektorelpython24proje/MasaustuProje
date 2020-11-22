import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
from PyQt5 import uic,QtWidgets

# from ilkUI import Ui_MainWindow

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("HUNKAR\ilk.ui",self)
        self.initUI()

    def initUI(self):
        # self.setGeometry(300,300,300,220)
        # self.setWindowTitle("İlk pencere")
        # self.btIptal.clicked.connect(self.temizle)
        # btn = QPushButton("Düğme",self)
        # btn.move(50,50)
        # btn.clicked.connect()
        # self.ui.setupUi(self)
        # self.ui.btIptal.clicked.connect(self.tiklandi)
        self.tbl.setRowCount(1)
        self.tbl.setColumnCount(2)
        self.btGiris.clicked.connect(self.girisYap)
        self.btIptal.clicked.connect(self.temizle)
        self.cmb.currentTextChanged.connect(self.sonuc)
        self.show()
    
    def girisYap(self):
        # if self.txtUserName.text() == "hunkar":
        #     if self.txtSifre.text() == "12345*":
        #         print("Giriş Başarılı")
        numRows = self.tbl.rowCount()
        kullanici = QtWidgets.QTableWidgetItem(self.txtUserName.text())
        sifre = QtWidgets.QTableWidgetItem(self.txtSifre.text())
        self.tbl.setItem(numRows-1,0,kullanici)
        self.tbl.setItem(numRows-1,1,sifre)
        self.tbl.setRowCount(numRows+1)
        self.cmb.addItem(self.txtUserName.text())

    def sonuc(self):
        sonuc = self.cmb.currentText()
        self.lblSonuc.setText(sonuc)
    
    def temizle(self):
        self.textUserName.setText("")
        self.textSifre.setText("")
        self.close()

    # def tiklandi(self):
    #     print("Tıklandı")

if __name__== "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
        
    