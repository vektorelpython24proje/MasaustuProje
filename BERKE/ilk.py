import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
from PyQt5 import uic

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"BERKE\ilk.ui",self)
        self.initUI()

    def initUI(self):
        self.btnGiris.clicked.connect(self.girisYap)
        self.btnIptal.clicked.connect(self.temizle)
        self.show()
    

    def girisYap(self):
        if self.txtUserName.text() == "BERKE":
            if self.txtSifre.text()== "12345":
                print("Giriş Başarılı")

    def temizle(self):
        self.txtUserName.setText("")
        self.txtSifre.setText("")
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())