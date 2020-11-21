from PyQt5 import uic
import sys
from PyQt5.QtWidgets import QApplication,QDialog

class App(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"IBRAHIM\ilk.ui",self)
        self.initUI()

    def initUI(self):
        self.bgiris.clicked.connect(self.girisyap)
        self.biptal.clicked.connect(self.temizle)
        self.show()

    def girisyap(self):
        if self.txtUsername.text()=="Echore04":
            if self.txtPass.text()=="123456":
                print("Giriş Yapıldı")

    def temizle(self):
        self.txtUsername.setText("")
        self.txtSifre.setText("")
        self.close()

    def tiklandi():
        self.txtUsername.setText("")
        self.txtPass.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec())