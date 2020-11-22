import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
from PyQt5 import uic,QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage,QPixmap
import cv2


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        uic.loadUi(r"SEMA\Kamera.ui",self)
        self.initUI()

    def initUI(self):
        self.btAc.clicked.connect(self.KameraAc)
        self.btKapat.setEnabled(False)
        self.btKapat.clicked.connect(self.KameraKapat)
        self.show()

    def KameraAc(self):
        if not self.timer.isActive():
            self.cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
            self.timer.start(3)
            self.btAc.setEnabled(False)
            self.btKapat.setEnabled(True)
            self.Goster()
        else:
            self.cam.release()
            self.timer.stop()
    
    def Goster(self):
        while True:
            ret,frame = self.cam.read()
            buyukFaktor = 0.4
            frame = cv2.resize(frame,None,fx=buyukFaktor,fy=buyukFactor,interpolation=cv2.INTER_AREA)
            height,width,channel = frame.shape
            step = channel*width

            qImg = QImage(frame.data,width,height,step,QImage.Format_BGR888)
            self.lblCam.setPixmap(QPixmap.fromImage(qImg))
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        
        self.cam.release()
        self.timer.stop()



    def KameraKapat(self):
        try:
            self.cam.release()
        except:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
