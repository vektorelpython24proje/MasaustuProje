import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
from PyQt5 import uic,QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage,QPixmap
import cv2
import numpy as np


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.isChanged = True
        uic.loadUi(r"ARDA\Kamera.ui",self)  # graphical user interface
        self.initUI()

    def initUI(self):
        self.btAc.clicked.connect(self.KameraAc)
        self.btKapat.setEnabled(False)
        self.btKapat.clicked.connect(self.KameraKapat)
        self.Slider.valueChanged.connect(self.SliderDegisti)
        self.btKaydet.clicked.connect(self.Kaydet)
        self.Slider.setValue(30)
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

    def SliderDegisti(self):
        self.pB.setValue(self.Slider.value())


    def Goster(self):
        while True:
            ret,frame = self.cam.read()
            buyukFaktor = self.Slider.value()/100
            frame = cv2.resize(frame,None,fx=buyukFaktor,fy=buyukFaktor,interpolation=cv2.INTER_AREA)
            height,width,channel = frame.shape  # (640,480,3)
            step = channel*width # (3*480)

            if self.chkSmooth.isChecked():
                kernel = np.ones((15,15),np.float32)/225
                # print(kernel)
                frame = cv2.filter2D(frame,-1,kernel)
            
            if self.chkGaussian.isChecked():
                frame = cv2.GaussianBlur(frame,(15,15),-2)
            
            if self.chkMedian.isChecked():
                frame = cv2.medianBlur(frame,15)

            if self.chkLiteral.isChecked():
                frame = cv2.bilateralFilter(frame,15,75,75)
            #---------------------------------
            qImg = QImage(frame.data,width,height,step,QImage.Format_BGR888)  # farklı kanallardan aldığı veriyi
            # bir resim olarak ekrana yansıtmak üzere QImage kullanıldı
            self.lblCam.setPixmap(QPixmap.fromImage(qImg)) # Alınan resmi label içerisinde gösterebilmek için
            # QPixmap kullanıldı
            #--------------------------------
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        self.cam.release()
        self.timer.stop()    

    def KameraKapat(self):
        try:
            self.cam.release()
        except:
            pass
        self.timer.stop()
        self.close()


    def Kaydet(self):
        pix = self.lblCam.pixmap()
        import io
        from PIL import Image
        from PyQt5.QtCore import QBuffer
        img = pix.toImage()
        buffer = QBuffer()
        buffer.open(QBuffer.ReadWrite)
        img.save(buffer,"JPG")
        pil_im = Image.open(io.BytesIO(buffer.data()))

        secenekler = QFileDialog.Options()
        # secenekler |= QFileDialog.DontUseNativeDialog
        dosyaismi,_ = QFileDialog.getSaveFileName(self,"Kaydetme","","Bütün Dosyalar(*);;Resim Dosyaları (*.jpg)",options=secenekler)
        if dosyaismi:
            print(dosyaismi)
            pil_im.save(dosyaismi+".jpg")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
