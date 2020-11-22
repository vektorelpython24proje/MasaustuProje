from PyQt5 import uic,QtWidgets
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import  QImage,QPixmap
import cv2

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"IBRAHIM\kamera.ui",self)
        self.setWindowTitle("Kamera Aç/Kapat")
        self.initUI()
        

    def initUI(self):
        self.show()

    def camOpen(self):
        pass

    def camClose(self):
        pass


if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec())