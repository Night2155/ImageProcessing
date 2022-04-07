import os
from PyQt5 import QtWidgets, QtGui, QtCore
import ImageProcess
from MainWindow import Ui_MainWindow  # 引入主畫面設計
import sys
import cv2 as cv
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.cwd = os.getcwd()
        self.file_name = ""
        # GIF Label
        movie = QtGui.QMovie("image\\PartyBird.gif")  # 設定 Gif
        self.ui.Gif_Label.setMovie(movie)  # 放入 Label 輸出
        movie.start()  # GIF 播放

        self.oriHeight = self.ui.ImageLabel.height()
        self.oriWidth = self.ui.ImageLabel.width()
        # Menu 1
        self.ui.actionClose.triggered.connect(app.exit)  # 關閉平台
        self.ui.actionOpen_File.triggered.connect(self.OpenFile_chooseFile)  # 開啟影像
        self.ui.actionSave_File.triggered.connect(self.SaveFile)  # 儲存影像
        # Menu 2
        self.ui.menu_2.setEnabled(False)
        self.ui.actionGray.triggered.connect(self.ImageGray)  # 轉換灰階影像
        self.ui.actionRGB.triggered.connect(self.ImageRGB)  # 轉換原始圖像
        self.ui.actionTresholding.triggered.connect(self.image_Threshold)  # 影像二值化
        self.ui.actionHistogram.triggered.connect(self.image_Hist)  # 灰階均衡化
        self.ui.actionHSV.triggered.connect(self.ImageHSV)  # 轉換 HSV 影像
        # Menu 3
        self.ui.menu_3.setEnabled(False)
        self.ui.actionROI.triggered.connect(self.Label_mouse_Event)  # 選取ROI
        # Button
        self.ui.Show_Hist_Btn.clicked.connect(self.Show_Hist)  # 顯示影像直方圖
        # Slider
        self.ui.Set_Threshold_Value_Slider.valueChanged.connect(self.Threshold_Value_Change)  # 調整二值化閥值

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

        else:
            if height or width != 0:
                ROI_image = self.cv2_image[int(self.TY):int(self.DY), int(self.LX):int(self.RX)]
                cv.namedWindow("ROI Image", cv.WINDOW_NORMAL)
                cv.imshow("ROI Image", ROI_image)
                self.ui.Show_ROI_Info.setText(f"高 : {height} \n寬 : {width}")
                if cv.waitKey() == 27:
                    cv.destroyAllWindows()
            else:
                self.ui.statusbar.showMessage("影像未選取")

    def Mouse_Move(self, event):
        self.ui.statusbar.showMessage(f"X = {event.x()} Y = {event.y()}")

    def OpenFile_chooseFile(self):  # Open File
        self.file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(self, "選擇檔案",
                                                                          self.cwd, "ALL Files (*);; PNG Files (*.png);; Jpg Files (*.jpg) ")
        if self.file_name == "":
            self.ui.statusbar.showMessage("取消開檔")
            return 0
        else:
            self.ui.statusbar.showMessage("開檔成功")
            self.oriImg = cv.imread(filename=self.file_name)  # 最初所載入的影像
            self.cv2_image = self.oriImg.copy()  # 目前Label所顯示的影像
            self.ui.menu_2.setEnabled(True)
            self.ui.menu_3.setEnabled(True)
            self.ShowImage(self.oriImg)

    def SaveFile(self):
        if self.file_name == "":
            self.ui.statusbar.showMessage("無檔案可儲存")
            return 0
        else:
            self.ui.statusbar.showMessage("存檔成功")
            savepath, file_type = QtWidgets.QFileDialog.getSaveFileName(self, "Image_Save", "Image", "PNG File (*.png);;Jpg Files (*.jpg)")
            if savepath == "":
                self.ui.statusbar.showMessage("取消存檔")
                return 0
            else:
                cv.imwrite(savepath, self.cv2_image)

    def ShowImage(self, img):
        self.cv2_image = img
        if len(img.shape) == 3:
            height, width, channel = img.shape
            bytesPerline = 3*width
            self.qimg = QtGui.QImage(img, width, height, bytesPerline, QtGui.QImage.Format_RGB888).rgbSwapped()
            pixmap = QtGui.QPixmap.fromImage(self.qimg)
            self.ui.Image_Info_label.setText(f"圖片資訊 : 高{height} 寬{width}")
            self.ui.statusbar.showMessage("RGB影像")
        elif len(img.shape) == 2 :
            height, width = img.shape
            bytesPerline = width
            self.qGrayimg = QtGui.QImage(img, width, height, bytesPerline, QtGui.QImage.Format.Format_Indexed8)
            pixmap = QtGui.QPixmap.fromImage(self.qGrayimg)

        self.ui.scrollArea.resize(self.oriWidth, self.oriHeight)
        if height <= self.ui.scrollArea.height():
            self.ui.scrollArea.resize(QtCore.QSize(self.ui.scrollArea.width(), height))
        if width <= self.ui.scrollArea.width():
            self.ui.scrollArea.resize(QtCore.QSize(width, self.ui.scrollArea.height()))
        self.ui.ImageLabel.setPixmap(pixmap)

    def Show_Hist(self):  # 顯示影像直方圖
        if self.file_name == "":
            self.ui.statusbar.showMessage("未載入影像 無法顯示直方圖")
            return 0
        else:
            self.ui.Image_Info_label.setText(f"圖片資訊 : 高{self.cv2_image.shape[0]} 寬{self.cv2_image.shape[1]}")
            self.ui.statusbar.showMessage("顯示影像直方圖")
            ImageProcess.Show_Histogram(self.cv2_image)

    def image_Hist(self):
        img_hist = ImageProcess.Histogram(self.oriImg)
        self.ShowImage(img_hist)
        self.ui.Image_Info_label.setText(f"圖片資訊 : 高{self.oriImg.shape[0]} 寬{self.oriImg.shape[1]}")
        self.ui.statusbar.showMessage("影像均衡化")
        self.ui.Set_Threshold_Value_Slider.setEnabled(False)

    def image_Threshold(self):  # 顯示二值化後圖像
        threshold_image = ImageProcess.Thresholding(self.oriImg, self.ui.Set_Threshold_Value_Slider.value())
        self.ShowImage(threshold_image)
        self.ui.Image_Info_label.setText(f"圖片資訊 : 高{self.oriImg.shape[0]} 寬{self.oriImg.shape[1]}")
        self.ui.statusbar.showMessage("二值化影像")
        self.ui.Set_Threshold_Value_Slider.setEnabled(True)

    def Threshold_Value_Change(self):  # 二值化 slider 改變數值
        self.ui.Text_label_Threshold_value.setText(str(self.ui.Set_Threshold_Value_Slider.value()))
        self.image_Threshold()

    def ImageGray(self):
        img_gray = ImageProcess.GrayImg(self.oriImg)
        self.ShowImage(img_gray)
        self.ui.Image_Info_label.setText(f"圖片資訊 : 高{self.oriImg.shape[0]} 寬{self.oriImg.shape[1]}")
        self.ui.statusbar.showMessage("灰階影像")
        self.ui.Set_Threshold_Value_Slider.setEnabled(False)

    def ImageRGB(self):
        self.ui.ImageLabel.setPixmap(QtGui.QPixmap.fromImage(self.qimg))
        self.cv2_image = self.oriImg
        height, width, channel = self.cv2_image.shape
        self.ui.Image_Info_label.setText(f"圖片資訊 : 高{height} 寬{width}")
        self.ui.statusbar.showMessage("RGB影像")
        self.ui.Set_Threshold_Value_Slider.setEnabled(False)

    def ImageHSV(self):
        img_HSV = ImageProcess.HSV(self.oriImg)
        self.ShowImage(img_HSV)
        self.ui.Image_Info_label.setText(f"圖片資訊 : 高{self.oriImg.shape[0]} 寬{self.oriImg.shape[1]}")
        self.ui.statusbar.showMessage("HSV影像")

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())