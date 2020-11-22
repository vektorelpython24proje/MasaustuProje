import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
from PyQt5 import uic,QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage,QPixmap
import cv2

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"BERKE\Kamera.ui",self)
        self.initUI()


    def initUI(self):
        self.show()

    def KameraAc(self):
        pass

    def KameraKapat(self):
        pass

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        ex = App()
        sys.exit(app.exec_())