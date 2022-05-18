import numpy as np
import os
from PyQt5 import QtWidgets, QtGui, QtCore
from ImageProcess import ImageProcess
from MainWindow_V3 import Ui_MainWindow  # 引入主畫面設計
import sys
import cv2 as cv
import matplotlib.pyplot as plt
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.MainWindow_Ui_Setup()
        self.MainWindow_Function_Binding()

    def MainWindow_Ui_Setup(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.cwd = os.getcwd()
        self.file_name = ""
        self.counter = 0
        self.oriHeight = self.ui.ImageLabel.height()
        self.oriWidth = self.ui.ImageLabel.width()

        # GIF Label
        movie = QtGui.QMovie("image\\PartyBird.gif")  # 設定 Gif
        self.ui.Gif_Label.setMovie(movie)  # 放入 Label 輸出
        movie.start()  # GIF 播放

    def MainWindow_Function_Binding(self):
        # Menu 1 選單
        self.ui.actionClose.triggered.connect(app.exit)  # 關閉平台
        self.ui.actionOpen_File.triggered.connect(self.OpenFile_chooseFile)  # 開啟影像
        self.ui.actionSave_File.triggered.connect(self.SaveFile)  # 儲存影像
        # Menu 2 色彩選項
        self.ui.actionGray.triggered.connect(self.ImageGray)  # 轉換灰階影像
        self.ui.actionRGB.triggered.connect(self.ImageRGB)  # 轉換原始圖像
        self.ui.actionTresholding.triggered.connect(self.image_Threshold)  # 影像二值化
        self.ui.actionHistogram.triggered.connect(self.image_Hist)  # 灰階均衡化
        self.ui.actionHSV.triggered.connect(self.ImageHSV)  # 轉換 HSV 影像
        # Menu 3 小工具
        self.ui.actionROI.triggered.connect(self.Label_mouse_Event_ROI)  # 選取ROI
        self.ui.actionaffine_transform.triggered.connect(self.Affine_Transform)  # 仿射轉換
        self.ui.actionperspective_transform.triggered.connect(self.Label_mouse_Event_perspective)  # 透視轉換
        self.ui.actionShow_Hist.triggered.connect(self.Show_Hist)
        # Menu 4 影像處理
        self.ui.actionGuassion.triggered.connect(self.GaussionBlur)  # 模糊影像
        self.ui.actionCanny.triggered.connect(self.Canny)  # 邊緣擷取
        self.ui.actionNoise.triggered.connect(self.ClearNoise)  # 雜訊處理
        # Slider 調整二值化閥值
        self.ui.Set_Threshold_Value_Slider.valueChanged.connect(self.Threshold_Value_Change)
        # Slider 旋轉影像
        self.ui.AngelSlider.valueChanged.connect(self.AngelValueChange)
        # Slider 左右平移影像
        self.ui.VerticalMoveSlider.valueChanged.connect(self.Slider_Move_Image)
        # Slider 上下平移影像
        self.ui.horizontalMoveSlider.valueChanged.connect(self.Slider_Move_Image)
        # Slider 調整縮放倍率
        self.ui.ScaleSlider.valueChanged.connect(self.ScaleValueChange)
        self.ui.MinThresholdSlider.valueChanged.connect(self.MinThresoldChange)
        self.ui.MaxThresholdSlider.valueChanged.connect(self.MaxThresoldChange)

    def Statusbar_Show_Message(self, message):
        self.ui.statusbar.showMessage(message)

    # 顯示圖像在ImageLabel
    def Show_On_ImageLabel(self, img):
        self.cv2_image = img
        if len(img.shape) == 3:
            height, width, channel = img.shape
            bytesPerline = 3 * width
            self.qimg = QtGui.QImage(img, width, height, bytesPerline, QtGui.QImage.Format_RGB888).rgbSwapped()
            pixmap = QtGui.QPixmap.fromImage(self.qimg)
            self.Statusbar_Show_Message("RGB影像")
        elif len(img.shape) == 2:
            height, width = img.shape
            bytesPerline = width
            self.qGrayimg = QtGui.QImage(img, width, height, bytesPerline, QtGui.QImage.Format.Format_Indexed8)
            pixmap = QtGui.QPixmap.fromImage(self.qGrayimg)

        self.ui.scrollArea.setMaximumSize(width, height)
        if height <= self.ui.scrollArea.height():
            self.ui.scrollArea.setMaximumSize(QtCore.QSize(self.ui.scrollArea.width(), height))
        if width <= self.ui.scrollArea.width():
            self.ui.scrollArea.setMaximumSize(QtCore.QSize(width, self.ui.scrollArea.height()))
        self.ui.ImageLabel.setPixmap(pixmap)

    # Menu1 選單函式
    def OpenFile_chooseFile(self):  # Open File
        self.file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(self, "選擇檔案",
                                                                          os.getcwd(), "ALL Files (*);; PNG Files (*.png);; Jpg Files (*.jpg) ")
        if self.file_name == "":
            self.Statusbar_Show_Message("取消開檔")
            return 0
        else:
            self.Statusbar_Show_Message("開檔成功")
            self.oriImg = cv.imread(filename=self.file_name)  # 最初所載入的影像
            self.cv2_image = self.oriImg.copy()  # 目前Label所顯示的影像
            self.Ui_Enabled_Setup()
            self.Show_Image_Info_On_Label()
            self.Show_On_ImageLabel(self.oriImg)

    def Show_Image_Info_On_Label(self):
        file_size = os.path.getsize(self.file_name)
        filename = os.path.basename(self.file_name)
        width, height = self.oriImg.shape[:2]
        self.ui.Image_Info_label.setText(f"檔案名稱 : {filename} 檔案大小 : {round(file_size / 1024, 2)}KB 尺寸 : {height}X{width}")

    def Ui_Enabled_Setup(self):
        self.ui.menu_2.setEnabled(True)
        self.ui.menu_3.setEnabled(True)
        self.ui.menu_4.setEnabled(True)
        self.ui.actionSave_File.setEnabled(True)
        self.ui.ScaleSlider.setEnabled(True)  # 偏移倍率
        self.ui.AngelSlider.setEnabled(True)  # 角度
        self.ui.VerticalMoveSlider.setEnabled(True)  # 垂直
        self.ui.horizontalMoveSlider.setEnabled(True)  # 水平
        self.ui.MaxThresholdSlider.setEnabled(True)
        self.ui.MinThresholdSlider.setEnabled(True)

    def SaveFile(self):  # 儲存影像
        if self.file_name == "":
            self.Statusbar_Show_Message("無檔案可儲存")
            return 0
        else:
            savepath, file_type = QtWidgets.QFileDialog.getSaveFileName(self, "Image_Save", "Image", "PNG File (*.png);;Jpg Files (*.jpg)")
            if savepath == "":
                self.Statusbar_Show_Message("取消存檔")
                return 0
            else:
                cv.imwrite(savepath, self.cv2_image)
                self.Statusbar_Show_Message("存檔成功")

    # Menu2 色彩選項函式
    def ImageGray(self):  # 轉換為灰階影像
        img_gray = ImageProcess.GrayImg(self.oriImg)
        self.Show_On_ImageLabel(img_gray)
        self.Statusbar_Show_Message("灰階影像")
        self.counter = 0

    def ImageRGB(self):  # 轉換為原始圖片
        self.Show_On_ImageLabel(self.oriImg)
        self.ui.statusbar.showMessage("RGB影像")
        self.counter = 0

    def image_Hist(self):  # 灰階影像均衡化
        img_hist = ImageProcess.Histogram(self.oriImg)
        self.Show_On_ImageLabel(img_hist)
        self.Statusbar_Show_Message("影像均衡化")
        self.counter = 0

    def image_Threshold(self):  # 顯示二值化後圖像
        threshold_image = ImageProcess.Thresholding(self.oriImg, self.ui.Set_Threshold_Value_Slider.value())
        self.Show_On_ImageLabel(threshold_image)
        self.Statusbar_Show_Message("二值化影像")
        self.counter = 0

    def Threshold_Value_Change(self):  # 二值化 slider 改變數值
        self.ui.Text_label_Threshold_value.setText(str(self.ui.Set_Threshold_Value_Slider.value()))


    def ImageHSV(self):  # 轉換為HSV通道
        img_HSV = ImageProcess.HSV(self.oriImg)
        self.Show_On_ImageLabel(img_HSV)
        self.Statusbar_Show_Message("HSV影像")
        self.counter = 0

    # Menu3 小工具函式
    def Label_mouse_Event_ROI(self):  # ROI滑鼠監聽事件
        self.ui.ImageLabel.mousePressEvent = self.Get_Press_Position
        self.ui.ImageLabel.mouseReleaseEvent = self.Mouse_Realease_ROI
        self.ui.ImageLabel.mouseMoveEvent = self.Mouse_Move
        self.ui.ImageLabel.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.setPerapective = False

    def Label_mouse_Event_perspective(self):  # Perspective滑鼠監聽事件
        self.ui.ImageLabel.mousePressEvent = self.Get_Press_Position
        self.ui.ImageLabel.mouseMoveEvent = self.Mouse_Move
        self.ui.ImageLabel.mouseReleaseEvent = self.Mouse_Release_Perspective
        self.ui.ImageLabel.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.setPerapective = True
        self.points = []

    def Get_Press_Position(self, event):  # 按下左鍵 記錄滑鼠位置
        self.X0, self.Y0 = event.x(), event.y()
        if self.setPerapective :
            if len(self.points) < 4:
                self.points.append([event.x(), event.y()])

    def Mouse_Realease_ROI(self, event):  # 放開滑鼠計算ROI位置、大小
        X1, Y1 = event.x(), event.y()
        if (self.X0 != X1) or (self.Y0 != Y1):  # 防止使用者點擊同一位置
            LX, TY = min(X1, self.X0), min(Y1, self.Y0)
            RX, DY = max(X1, self.X0), max(Y1, self.Y0)
            height, width = (DY - TY), (RX - LX)
            if height or width != 0:
                ImageProcess.Show_ROI_Image(self.cv2_image, TY, DY, LX, RX)
                self.ui.ROI_Label.setText(f"ROI 大小 高 : {height} 寬 : {width}")
                self.Statusbar_Show_Message(f"X0 = {LX} Y0 = {TY} X1 = {RX} Y2 = {DY}")
                self.ui.ImageLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            else:
                self.Statusbar_Show_Message("影像未選取")
                self.ui.ImageLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
                return 0

    def Mouse_Release_Perspective(self, event):  # 放開滑鼠計算透視函式陣列
        if len(self.points) == 4:
            self.Statusbar_Show_Message(f"{self.points}")
            ImageProcess.Show_Perspective_Image(self.cv2_image, self.points)
            self.points = []
            self.setPerapective = False
            self.ui.ImageLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def Mouse_Move(self, event):
        self.Statusbar_Show_Message(f"X = {event.x()} Y = {event.y()}")

    def Affine_Transform(self):  # 仿射轉換
        height, width = self.oriImg.shape[:2]
        Transform = self.cv2_image
        x = self.ui.VerticalMoveSlider.value()
        y = self.ui.horizontalMoveSlider.value()
        scale = self.ui.ScaleSlider.value()/10
        if x and y != 0:
            m = np.float32([[1, scale, x], [scale, 1, y]])
            affineImg = cv.warpAffine(Transform, m, (width, height))
            self.Show_On_ImageLabel(affineImg)
        else:
            return 0

    def Show_Hist(self):  # 顯示影像直方圖
        if self.file_name == "":
            self.Statusbar_Show_Message("未載入影像 無法顯示直方圖")
            return 0
        else:
            self.ui.Image_Info_label.setText(f"圖片資訊 : 高{self.cv2_image.shape[0]} 寬{self.cv2_image.shape[1]}")
            self.Statusbar_Show_Message("顯示影像直方圖")
            ImageProcess.Show_Histogram(self.cv2_image)

    # Menu4 影像處理
    def GaussionBlur(self):  # 高斯濾波 模糊化
        GaussionImg = ImageProcess.Gaussion(self.oriImg, 21, 50)
        self.cv2_image = GaussionImg
        self.Show_On_ImageLabel(GaussionImg)
        self.Statusbar_Show_Message("影像模糊化")

    def Canny(self):  # Canny 邊緣擷取
        self.Max = self.ui.MaxThresholdValue.text()
        self.Min = self.ui.MinThresholdValue.text()
        GrayImg = ImageProcess.GrayImg(self.oriImg)
        ClearImg = ImageProcess.Gaussion(GrayImg, 3, 0)
        CannyImg = ImageProcess.Canny(ClearImg, Max=int(self.Max), Min=int(self.Min))
        self.cv2_image = CannyImg
        self.Show_On_ImageLabel(CannyImg)
        self.Statusbar_Show_Message("影像邊緣擷取")

    def ClearNoise(self):  # 中值濾波
        ClearImg = ImageProcess.Median(self.oriImg, 3, 0)
        self.cv2_image = ClearImg
        self.Show_On_ImageLabel(ClearImg)
        self.Statusbar_Show_Message("雜訊處理")

    # Slider 旋轉影像
    def AngelValueChange(self):
        if self.counter == 0:
            self.NoChange = self.cv2_image
            self.counter = 1
        if self.counter > 0:
            angel = self.ui.AngelSlider.value()
            self.ui.AngelValue.setText(str(angel))
            TurnImg = ImageProcess.Change_Angel_Image(self.oriImg, angel, self.NoChange)
            self.Show_On_ImageLabel(TurnImg)

    # 上下左右平移影像
    def Slider_Move_Image(self):
        if self.counter == 0:
            self.NoChange = self.cv2_image
            self.counter = 1
        if self.counter > 0:
            x = self.ui.horizontalMoveSlider.value()
            y = self.ui.VerticalMoveSlider.value()
            if self.sender() == self.ui.horizontalMoveSlider:
                self.ui.MoveRightValue.setText(str(x))
            elif self.sender() == self.ui.VerticalMoveSlider:
                self.ui.MoveUpDownValue.setText(str(y))
            MoveImg = ImageProcess.Move_Image(self.oriImg, self.NoChange, x, y)
            self.Show_On_ImageLabel(MoveImg)

    def MaxThresoldChange(self):
        self.ui.MaxThresholdValue.setText(str(self.ui.MaxThresholdSlider.value()))

    def MinThresoldChange(self):
        self.ui.MinThresholdValue.setText(str(self.ui.MinThresholdSlider.value()))

    def ScaleValueChange(self):
        self.ui.ScaleValue.setText(str(self.ui.ScaleSlider.value()/10))

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())