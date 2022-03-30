import os
from PyQt5 import QtWidgets, QtGui, QtCore
import ImageProcess
from MainWindow import Ui_MainWindow  # 引入主畫面設計
import sys
import cv2 as cv
from Show_plot import Figure_Canvas
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.cwd = os.getcwd()
        self.file_name = ""
        movie = QtGui.QMovie("image\\PartyBird.gif")  # 設定 Gif
        self.ui.Gif_Label.setMovie(movie)  # 放入 Label 輸出
        movie.start()
        # Menu
        self.ui.actionClose.triggered.connect(app.exit)
        self.ui.actionOpen_File.triggered.connect(self.OpenFile_chooseFile)
        self.ui.actionGray.triggered.connect(self.ImageGray)
        self.ui.actionRGB.triggered.connect(self.ImageRGB)
        self.ui.actionSave_File.triggered.connect(self.SaveFile)
        self.ui.actionTresholding.triggered.connect(self.image_Threshold)
        self.ui.actionHistogram.triggered.connect(self.image_Hist)
        self.ui.actionROI.triggered.connect(self.Label_mouse_Event)
        # Button
        self.ui.Show_Hist_Btn.clicked.connect(self.Show_Hist)
        # Slider
        self.ui.Set_Threshold_Value_Slider.valueChanged.connect(self.Threshold_Value_Change)

    def Label_mouse_Event(self):
        self.ui.ImageLabel.mousePressEvent = self.Get_Press_Position
        self.ui.ImageLabel.mouseReleaseEvent = self.Mouse_Realease
        self.ui.ImageLabel.mouseMoveEvent = self.Mouse_Move

    def Get_Press_Position(self, event):
        self.X0, self.Y0 = event.x(), event.y()
        #self.ui.Show_ROI_Info.setText(f'{event.x()=}{event.y()=}')

    def Mouse_Realease(self, event):
        self.X1, self.Y1 = event.x(), event.y()
        self.LX, self.TY = min(self.X1, self.X0), min(self.Y1, self.Y0)
        self.RX, self.DY = max(self.X1, self.X0), max(self.Y1, self.Y0)
        height, width = (self.DY - self.TY), (self.RX - self.LX)
        if self.file_name == "":
            self.ui.statusbar.showMessage("未選取影像無法截出ROI")
            self.ui.Show_ROI_Info.setText(f"ROI : \n{height=} {width=}")
        else:
            #ROI_image = self.cv2_image[int(self.TY):int(self.TY)+int(height), int(self.LX):int(self.LX)+int(width)]
            ROI_image = self.cv2_image[int(self.TY):int(self.DY), int(self.LX):int(self.RX)]
            cv.namedWindow("ROI Image", cv.WINDOW_NORMAL)
            cv.imshow("ROI Image", ROI_image)
            self.ui.Show_ROI_Info.setText(f"ROI : \n{height=} {width=}")
            cv.waitKey(0)
            cv.destroyAllWindows()

    def Mouse_Move(self, event):
        self.flag = True

    def OpenFile_chooseFile(self):  # Open File
        self.file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(self, "選擇檔案",
                                                                          self.cwd, "ALL Files (*);; PNG Files (*.png);; Jpg Files (*.jpg) ")
        if self.file_name == "":
            self.ui.statusbar.showMessage("取消開檔")
            return 0
        else:
            self.ui.statusbar.showMessage("開檔成功")
            self.oriImg = cv.imread(filename=self.file_name)
            self.cv2_image = self.oriImg.copy()
            self.ui.menu_2.setEnabled(True)
            self.ShowImage(self.oriImg)
            self.ui.Set_Threshold_Value_Slider.setEnabled(False)

    def SaveFile(self):
        if self.file_name == "":
            self.ui.statusbar.showMessage("無檔案可儲存")
            return 0
        else:
            self.ui.statusbar.showMessage("存檔成功")
            savepath, file_type = QtWidgets.QFileDialog.getSaveFileName(self, "Image_Save", "Image", "PNG File (*.png);;Jpg Files (*.jpg)")
            if savepath == "":
                return 0
            else:
                cv.imwrite(savepath, self.cv2_image)

    def Show_Hist(self):
        if self.file_name == "":
            return 0
        else:
            self.ui.Image_Info_label.setText(f"圖片資訊 : 高{self.cv2_image.shape[0]} 寬{self.cv2_image.shape[1]}")
            self.ui.statusbar.showMessage("顯示影像直方圖")
            #ImageProcess.Show_Histogram(self.cv2_image)
            figure = Figure_Canvas()
            figure.Show_Histogram(self.cv2_image)

    def image_Hist(self):
        img_hist = ImageProcess.Histogram(self.oriImg)
        self.cv2_image = img_hist
        height, width = img_hist.shape[:2]
        qHist_Img = QtGui.QImage(img_hist, width, height, width, QtGui.QImage.Format.Format_Indexed8)
        pixmap = QtGui.QPixmap.fromImage(qHist_Img)
        self.ui.ImageLabel.setPixmap(pixmap)
        self.ui.Image_Info_label.setText(f"圖片資訊 : 高{height} 寬{width}")
        self.ui.statusbar.showMessage("影像直方圖均衡化")
        self.ui.Set_Threshold_Value_Slider.setEnabled(False)

    def image_Threshold(self):  # 顯示二值化後圖像
        self.threshold_image = ImageProcess.Thresholding(self.oriImg, self.ui.Set_Threshold_Value_Slider.value())
        self.cv2_image = self.threshold_image
        height, width = self.threshold_image.shape[:2]
        qThreshold_image = QtGui.QImage(self.threshold_image, width, height, width, QtGui.QImage.Format.Format_Indexed8)
        pixmap = QtGui.QPixmap.fromImage(qThreshold_image)
        self.ui.ImageLabel.setPixmap(pixmap)
        self.ui.Image_Info_label.setText(f"圖片資訊 : 高{height} 寬{width}")
        self.ui.statusbar.showMessage("二值化影像")
        self.ui.Set_Threshold_Value_Slider.setEnabled(True)

    def Threshold_Value_Change(self):  # 二值化 slider 改變數值
        self.ui.Text_label_Threshold_value.setText(str(self.ui.Set_Threshold_Value_Slider.value()))
        self.image_Threshold()

    def ShowImage(self, img):
        height, width, channel = img.shape
        bytesPerline = 3*width
        self.qimg = QtGui.QImage(img, width, height, bytesPerline, QtGui.QImage.Format_RGB888).rgbSwapped()
        pixmap = QtGui.QPixmap.fromImage(self.qimg)
        self.ui.ImageLabel.resize(width, height)
        self.ui.ImageLabel.setPixmap(pixmap)
        self.ui.Image_Info_label.setText(f"圖片資訊 : 高{height} 寬{width}")
        self.ui.statusbar.showMessage("RGB影像")

    def ImageGray(self):
        #img_gray = cv.imread(self.file_name,cv.IMREAD_GRAYSCALE)
        img_gray = ImageProcess.GrayImg(self.oriImg)
        self.cv2_image = img_gray
        height, width = img_gray.shape[:2]
        #self.ui.statusbar.showMessage(f"{img_gray.shape}")
        self.qGrayImg = QtGui.QImage(img_gray, width, height, width, QtGui.QImage.Format.Format_Indexed8)
        pixmap = QtGui.QPixmap.fromImage(self.qGrayImg)
        self.ui.ImageLabel.setPixmap(pixmap)
        self.ui.Image_Info_label.setText(f"圖片資訊 : 高{height} 寬{width}")
        self.ui.statusbar.showMessage("灰階影像")
        self.ui.Set_Threshold_Value_Slider.setEnabled(False)

    def ImageRGB(self):
        self.ui.ImageLabel.setPixmap(QtGui.QPixmap.fromImage(self.qimg))
        self.cv2_image = self.oriImg
        height, width, channel = self.cv2_image.shape
        self.ui.Image_Info_label.setText(f"圖片資訊 : 高{height} 寬{width}")
        self.ui.statusbar.showMessage("RGB影像")
        self.ui.Set_Threshold_Value_Slider.setEnabled(False)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())