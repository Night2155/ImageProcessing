import os

from PyQt5 import QtWidgets, QtGui, QtCore
from MainWindow import Ui_MainWindow  # 引入UI設計檔

import sys
import cv2 as cv
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.cwd = os.getcwd()
        self.file_name = ""
        self.thres_value = int(self.ui.Set_Threshold_Value_Slider.value())
        # Menu
        self.ui.actionClose.triggered.connect(app.exit)
        self.ui.actionOpen_File.triggered.connect(self.OpenFile_chooseFile)
        self.ui.actionGray.triggered.connect(self.ImageGray)
        self.ui.actionRGB.triggered.connect(self.ImageRGB)
        self.ui.actionSave_File.triggered.connect(self.SaveFile)
        self.ui.actionTresholding.triggered.connect(self.image_Threshold)
        self.ui.actionHistogram.triggered.connect(self.image_Hist)
        # Button
        #self.ui.File_Btn.clicked.connect(self.OpenFile_chooseFile)
        #self.ui.Save_File_Btn.clicked.connect()
        self.ui.Show_Hist_Btn.clicked.connect(self.Show_Hist)
        # Label
        self.ui.ImageLabel.mousePressEvent = self.Show_Mouse_Press_Position
        # Slider
        self.ui.Set_Threshold_Value_Slider.valueChanged.connect(self.Threshold_Value_Change)


    def OpenFile_chooseFile(self):  # Open File
        self.file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(self, "選擇檔案",
                                                                          self.cwd, "ALL Files (*);; PNG Files (*.png);; Jpg Files (*.jpg) ")
        if self.file_name == "":
            self.ui.statusbar.showMessage("取消開檔")
            return 0
        else:
            self.ui.statusbar.showMessage("開檔成功")
            self.oriImg = cv.imread(filename=self.file_name)
            self.ui.menu_2.setEnabled(True)
            self.ShowImage(self.oriImg)
            self.ui.Set_Threshold_Value_Slider.setEnabled(False)

    def Show_Hist(self):
        return 0

    def image_Hist(self):
        return 0

    def image_Threshold(self):  # 顯示二值化後圖像
        gray = cv.cvtColor(self.oriImg, cv.COLOR_RGB2GRAY)
        ret, self.threshold_image = cv.threshold(gray, self.thres_value, 255, cv.THRESH_BINARY)
        height, width = self.threshold_image.shape[:2]
        qThreshold_image = QtGui.QImage(self.threshold_image, width, height, width, QtGui.QImage.Format.Format_Indexed8)
        pixmap = QtGui.QPixmap.fromImage(qThreshold_image)
        self.ui.ImageLabel.setPixmap(pixmap)
        self.ui.Set_Threshold_Value_Slider.setEnabled(True)
        return 0

    def Threshold_Value_Change(self):  # 二值化 slider 改變數值
        self.ui.Text_label_Threshold_value.setText(str(self.thres_value))
        self.thres_value = int(self.ui.Set_Threshold_Value_Slider.value())
        self.image_Threshold()
        return 0

    def SaveFile(self):
        return 0

    def Show_Mouse_Press_Position(self, event):
        self.ui.statusbar.showMessage(f"[show_mouse_press] : {event.x()}, {event.y()}, {event.button()}")

    def ShowImage(self, img):
        height, width, channel = img.shape
        bytesPerline = 3*width
        self.qimg = QtGui.QImage(img, width, height, bytesPerline, QtGui.QImage.Format_RGB888).rgbSwapped()
        pixmap = QtGui.QPixmap.fromImage(self.qimg)
        self.ui.ImageLabel.resize(width, height)
        self.ui.ImageLabel.setPixmap(pixmap)
        self.ui.statusbar.showMessage(f"ImageInfo : {height=}, {width=}, {channel=}")

    def ImageGray(self):

        #img_gray = cv.imread(self.file_name,cv.IMREAD_GRAYSCALE)
        img_gray = cv.cvtColor(self.oriImg, cv.COLOR_BGR2GRAY)
        height, width = img_gray.shape[:2]
        self.ui.statusbar.showMessage(f"{img_gray.shape}")
        self.qGrayImg = QtGui.QImage(img_gray, width, height, width, QtGui.QImage.Format.Format_Indexed8)
        pixmap = QtGui.QPixmap.fromImage(self.qGrayImg)
        self.ui.ImageLabel.setPixmap(pixmap)
        self.ui.Set_Threshold_Value_Slider.setEnabled(False)

    def ImageRGB(self):
        self.ui.ImageLabel.setPixmap(QtGui.QPixmap.fromImage(self.qimg))
        self.ui.Set_Threshold_Value_Slider.setEnabled(False)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())