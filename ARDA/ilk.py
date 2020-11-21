import sys
from PyQt5.QtWidgets import QApplication,QMainWindow

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,220)
        self.setWindowTitle("İlk Pencere")
        self.show

if __name__ == "__main__":
    app=QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())