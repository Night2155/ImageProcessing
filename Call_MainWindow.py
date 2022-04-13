import numpy as np
import os
from PyQt5 import QtWidgets, QtGui, QtCore
import ImageProcess
from MainWindow import Ui_MainWindow  # 引入主畫面設計
import sys
import cv2 as cv
import matplotlib.pyplot as plt
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
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
        # Menu 1 選單
        self.ui.actionClose.triggered.connect(app.exit)  # 關閉平台
        self.ui.actionOpen_File.triggered.connect(self.OpenFile_chooseFile)  # 開啟影像
        self.ui.actionSave_File.triggered.connect(self.SaveFile)  # 儲存影像
        # Menu 2 色彩選項
        self.ui.menu_2.setEnabled(False)
        self.ui.actionGray.triggered.connect(self.ImageGray)  # 轉換灰階影像
        self.ui.actionRGB.triggered.connect(self.ImageRGB)  # 轉換原始圖像
        self.ui.actionTresholding.triggered.connect(self.image_Threshold)  # 影像二值化
        self.ui.actionHistogram.triggered.connect(self.image_Hist)  # 灰階均衡化
        self.ui.actionHSV.triggered.connect(self.ImageHSV)  # 轉換 HSV 影像
        # Menu 3 小工具
        self.ui.menu_3.setEnabled(False)
        self.ui.actionROI.triggered.connect(self.Label_mouse_Event_ROI)  # 選取ROI
        self.ui.actionaffine_transform.triggered.connect(self.Affine_Transform)  # 仿射轉換
        self.ui.actionperspective_transform.triggered.connect(self.Label_mouse_Event_perspective)  # 透視轉換
        # Menu 4 影像處理
        self.ui.menu_4.setEnabled(False)
        valid = QtGui.QIntValidator(0, 255, self)
        self.ui.MaxValue.setValidator(valid)
        self.ui.MinValue.setValidator(valid)
        self.ui.actionGuassion.triggered.connect(self.GaussionBlur)  # 模糊影像
        self.ui.actionCanny.triggered.connect(self.Canny)  # 邊緣擷取
        self.ui.actionNoise.triggered.connect(self.ClearNoise)  # 雜訊處理
        # Button 顯示影像直方圖
        self.ui.Show_Hist_Btn.clicked.connect(self.Show_Hist)
        # Slider 調整二值化閥值
        self.ui.Set_Threshold_Value_Slider.valueChanged.connect(self.Threshold_Value_Change)
        # Slider 旋轉影像
        self.ui.AngelSlider.valueChanged.connect(self.AngelValueChange)
        # Slider 左右平移影像
        self.ui.VerticalMoveSlider.valueChanged.connect(self.verticalChange)
        # Slider 上下平移影像
        self.ui.horizontalMoveSlider.valueChanged.connect(self.horizontalChange)
        # Slider 調整縮放倍率
        self.ui.ScaleSlider.valueChanged.connect(self.ScaleValueChange)

    # 顯示圖像在ImageLabel
    def ShowImage(self, img):
        self.cv2_image = img
        if len(img.shape) == 3:
            height, width, channel = img.shape
            bytesPerline = 3 * width
            self.qimg = QtGui.QImage(img, width, height, bytesPerline, QtGui.QImage.Format_RGB888).rgbSwapped()
            pixmap = QtGui.QPixmap.fromImage(self.qimg)
            self.ui.statusbar.showMessage("RGB影像")
        elif len(img.shape) == 2:
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

    # Menu1 選單函式
    def OpenFile_chooseFile(self):  # Open File
        self.file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(self, "選擇檔案",
                                                                          self.cwd, "ALL Files (*);; PNG Files (*.png);; Jpg Files (*.jpg) ")
        if self.file_name == "":
            self.ui.statusbar.showMessage("取消開檔")
            return 0
        else:
            self.ui.statusbar.showMessage("開檔成功")
            file_size = os.path.getsize(self.file_name)
            filename = os.path.basename(self.file_name)
            self.oriImg = cv.imread(filename=self.file_name)  # 最初所載入的影像
            self.cv2_image = self.oriImg.copy()  # 目前Label所顯示的影像
            width, height = self.oriImg.shape[:2]
            self.ui.menu_2.setEnabled(True)
            self.ui.menu_3.setEnabled(True)
            self.ui.menu_4.setEnabled(True)
            self.ShowImage(self.oriImg)
            self.ui.Image_Info_label.setText(f"檔案名稱 : {filename} 檔案大小 : {round(file_size / 1024, 2)}KB 尺寸 : {height}X{width}")

    def SaveFile(self):  # 儲存影像
        if self.file_name == "":
            self.ui.statusbar.showMessage("無檔案可儲存")
            return 0
        else:
            savepath, file_type = QtWidgets.QFileDialog.getSaveFileName(self, "Image_Save", "Image", "PNG File (*.png);;Jpg Files (*.jpg)")
            if savepath == "":
                self.ui.statusbar.showMessage("取消存檔")
                return 0
            else:
                cv.imwrite(savepath, self.cv2_image)
                self.ui.statusbar.showMessage("存檔成功")

    # Menu2 色彩選項函式
    def ImageGray(self):  # 轉換為灰階影像
        img_gray = ImageProcess.GrayImg(self.oriImg)
        self.ShowImage(img_gray)
        self.ui.statusbar.showMessage("灰階影像")
        self.ui.Set_Threshold_Value_Slider.setEnabled(False)
        self.counter = 0

    def ImageRGB(self):  # 轉換為原始圖片
        self.ShowImage(self.oriImg)
        self.ui.statusbar.showMessage("RGB影像")
        self.ui.Set_Threshold_Value_Slider.setEnabled(False)
        self.counter = 0

    def image_Hist(self):  # 灰階影像均衡化
        img_hist = ImageProcess.Histogram(self.oriImg)
        self.ShowImage(img_hist)
        self.ui.statusbar.showMessage("影像均衡化")
        self.ui.Set_Threshold_Value_Slider.setEnabled(False)
        self.counter = 0

    def image_Threshold(self):  # 顯示二值化後圖像
        threshold_image = ImageProcess.Thresholding(self.oriImg, self.ui.Set_Threshold_Value_Slider.value())
        self.ShowImage(threshold_image)
        self.ui.statusbar.showMessage("二值化影像")
        self.ui.Set_Threshold_Value_Slider.setEnabled(True)
        self.counter = 0

    def Threshold_Value_Change(self):  # 二值化 slider 改變數值
        self.ui.Text_label_Threshold_value.setText(str(self.ui.Set_Threshold_Value_Slider.value()))
        self.image_Threshold()

    def ImageHSV(self):  # 轉換為HSV通道
        img_HSV = ImageProcess.HSV(self.oriImg)
        self.ShowImage(img_HSV)
        self.ui.statusbar.showMessage("HSV影像")
        self.counter = 0

    # Menu3 小工具函式
    def Label_mouse_Event_ROI(self):  # ROI滑鼠監聽事件
        self.ui.ImageLabel.mousePressEvent = self.Get_Press_Position
        self.ui.ImageLabel.mouseReleaseEvent = self.Mouse_Realease_ROI
        self.ui.ImageLabel.mouseMoveEvent = self.Mouse_Move
        self.SetROI = True
        self.setPerapective = False

    def Label_mouse_Event_perspective(self):  # Perspective滑鼠監聽事件
        self.ui.ImageLabel.mousePressEvent = self.Get_Press_Position
        self.ui.ImageLabel.mouseMoveEvent = self.Mouse_Move
        self.ui.ImageLabel.mouseReleaseEvent = self.Mouse_Release_Perspective
        self.ui.AngelSlider.setEnabled(False)
        self.setPerapective = True
        self.points = []

    def Get_Press_Position(self, event):  # 按下左鍵 記錄滑鼠位置
        self.X0, self.Y0 = event.x(), event.y()
        if self.setPerapective :
            if len(self.points) < 4:
                self.points.append([event.x(), event.y()])

    def Mouse_Realease_ROI(self, event):  # 放開滑鼠計算ROI位置、大小
        if self.SetROI:
            self.X1, self.Y1 = event.x(), event.y()
            self.LX, self.TY = min(self.X1, self.X0), min(self.Y1, self.Y0)
            self.RX, self.DY = max(self.X1, self.X0), max(self.Y1, self.Y0)
            height, width = (self.DY - self.TY), (self.RX - self.LX)
            if self.file_name == "":
                self.ui.statusbar.showMessage("未選取影像無法截出ROI")
            else:
                if height or width != 0:
                    ROI_image = self.cv2_image[int(self.TY):int(self.DY), int(self.LX):int(self.RX)]
                    ROI_image = cv.cvtColor(ROI_image, cv.COLOR_BGR2RGB)
                    plt.axis('off')
                    plt.imshow(ROI_image)
                    plt.show()
                    self.ui.Show_ROI_Info.setText(f"高 : {height} \n寬 : {width}")
                    self.ui.statusbar.showMessage(f"X0 = {self.LX} Y0 = {self.TY} X1 = {self.RX} Y2 = {self.DY}")
                else:
                    self.ui.statusbar.showMessage("影像未選取")
        self.SetROI = False

    def Mouse_Release_Perspective(self, event):  # 放開滑鼠計算透視函式陣列
        if len(self.points) == 4:
            self.ui.statusbar.showMessage(f"{self.points}")
            width, height = self.cv2_image.shape[:2]
            pts1 = np.float32(self.points)
            pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
            m = cv.getPerspectiveTransform(pts1, pts2)
            PerspectiveImg = cv.warpPerspective(self.cv2_image, m, (width, height), cv.INTER_LINEAR)
            self.ShowImage(PerspectiveImg)
            self.cv2_image = PerspectiveImg
            self.points = []
            self.setPerapective = False
            self.ui.AngelSlider.setEnabled(True)

    def Mouse_Move(self, event):
        self.ui.statusbar.showMessage(f"X = {event.x()} Y = {event.y()}")

    def Affine_Transform(self):  # 仿射轉換
        height, width = self.oriImg.shape[:2]
        x = self.ui.VerticalMoveSlider.value()
        y = self.ui.horizontalMoveSlider.value()
        scale = self.ui.ScaleSlider.value()/10
        if x and y != 0:
            m = np.float32([[1, scale, x], [scale, 1, y]])
            affineImg = cv.warpAffine(self.oriImg, m, (width, height))
            self.ShowImage(affineImg)
            self.cv2_image = affineImg
        else:
            return 0

    def ScaleValueChange(self):
        self.ui.ScaleValue.setText(str(self.ui.ScaleSlider.value()/10))

    # Menu4 影像處理
    def GaussionBlur(self):  # 高斯濾波 模糊化
        GaussionImg = ImageProcess.Gaussion(self.oriImg, 21, 50)
        self.cv2_image = GaussionImg
        self.ShowImage(GaussionImg)
        self.ui.statusbar.showMessage("影像模糊化")

    def Canny(self):  # Canny 邊緣擷取
        self.Max = self.ui.MaxValue.text()
        self.Min = self.ui.MinValue.text()
        GrayImg = ImageProcess.GrayImg(self.oriImg)
        ClearImg = ImageProcess.Gaussion(GrayImg, 3, 0)
        if self.Max and self.Min != "":
            CannyImg = ImageProcess.Canny(ClearImg, Max=int(self.Max), Min=int(self.Min))
            self.cv2_image = CannyImg
            self.ShowImage(CannyImg)
            self.ui.statusbar.showMessage("影像邊緣擷取")
        else:
            self.ui.statusbar.showMessage("請設定最大、最小閥值")

    def ClearNoise(self):  # 中值濾波
        ClearImg = ImageProcess.Median(self.oriImg, 3, 0)
        self.cv2_image = ClearImg
        self.ShowImage(ClearImg)
        self.ui.statusbar.showMessage("雜訊處理")

    # Button 顯示直方圖
    def Show_Hist(self):  # 顯示影像直方圖
        if self.file_name == "":
            self.ui.statusbar.showMessage("未載入影像 無法顯示直方圖")
            return 0
        else:
            self.ui.Image_Info_label.setText(f"圖片資訊 : 高{self.cv2_image.shape[0]} 寬{self.cv2_image.shape[1]}")
            self.ui.statusbar.showMessage("顯示影像直方圖")
            ImageProcess.Show_Histogram(self.cv2_image)

    # Slider 旋轉影像
    def AngelValueChange(self):
        if self.counter == 0:
            self.NoChange = self.cv2_image
            self.counter = 1
        if self.counter > 0:
            Turn_Img = self.NoChange
            angel = self.ui.AngelSlider.value()
            self.ui.AngelValue.setText(str(angel))
            height, width = self.oriImg.shape[:2]
            center = (width / 2, height / 2)
            scale = 1.0
            # center = 影像中心點 angel = 旋轉角度 scale = 縮放比例
            AngelArray = cv.getRotationMatrix2D(center, int(angel), scale)
            TurnImg = cv.warpAffine(Turn_Img, AngelArray, (width, height))
            self.ShowImage(TurnImg)

    # Slider 上下平移影像
    def verticalChange(self):
        if self.counter == 0:
            self.NoChange = self.cv2_image
            self.counter = 1
        if self.counter > 0:
            x = self.ui.horizontalMoveSlider.value()
            y = self.ui.VerticalMoveSlider.value()
            self.ui.MoveUpDownValue.setText(str(y))
            height, width = self.oriImg.shape[:2]
            # x = x軸偏移量 y = y軸偏移量
            MoveArray = np.float32([[1, 0, x], [0, 1, y]])
            MoveImg = cv.warpAffine(self.oriImg, MoveArray, (width, height))
            self.ShowImage(MoveImg)

    # Slider 左右平移影像
    def horizontalChange(self):
        if self.counter == 0:
            self.NoChange = self.cv2_image
            self.counter = 1
        if self.counter > 0:
            x = self.ui.horizontalMoveSlider.value()
            y = self.ui.VerticalMoveSlider.value()
            self.ui.MoveRightValue.setText(str(x))
            height, width = self.oriImg.shape[:2]
            # x = x軸偏移量 y = y軸偏移量
            MoveArray = np.float32([[1, 0, x], [0, 1, y]])
            MoveImg = cv.warpAffine(self.oriImg, MoveArray, (width, height))
            self.ShowImage(MoveImg)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())