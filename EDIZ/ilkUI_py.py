import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
from ilkUI import Ui_MainWindow

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.initUI()
    
    def initUI(self):
        self.ui.setupUi(self)
        self.ui.btIptal.clicked.connect(self.tiklandi)
        self.show()

    def tiklandi(self):
        self.ui.txtUserName.setText("Merhaba")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
