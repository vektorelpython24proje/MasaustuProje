from PyQt5 import uic,QtWidgets
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import  QImage,QPixmap
import cv2

class App(QMainWindow):
    
def __init__(self):
        super().__init__()
        self.timer=QTimer()
        uic.loadUi(r"IBRAHIM\kamera.ui",self)
        self.setWindowTitle("Kamera Aç/Kapat")
        self.initUI()
        

    def initUI(self):
        self.camop.clicked.connect(self.camOpen)
        self.camclose.clicked.connect(self.camClose)
        self.show()

    def camOpen(self):
        print("Kamerayı açtım")
        self.cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

    def camClose(self):
        print("Kamerayı kapattım")


if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec())