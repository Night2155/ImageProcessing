from MainWindow_V3 import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
import os
import cv2 as cv

class Functions():
    def __init__(self):
        super(Functions, self).__init__()

    def Gif(self):
        # GIF Label
        movie = QtGui.QMovie("image\\PartyBird.gif")  # 設定 Gif
        self.ui.Gif_Label.setMovie(movie)  # 放入 Label 輸出
        movie.start()  # GIF 播放

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
        self.ui.actionResetValue.setEnabled(True)
        self.ui.Set_Threshold_Value_Slider.setEnabled(True)

    def Painting(self, x, y, w, h):
        painter = QtGui.QPainter(self.ui.ImageLabel.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor('red'))
        painter.setPen(pen)
        painter.drawRect(x, y, w, h)
        painter.end()

    def Reset(self):
        self.ui.AngelSlider.setValue(0)
        self.AngelValueChange()
        self.ui.horizontalMoveSlider.setValue(0)
        self.ui.VerticalMoveSlider.setValue(0)
        self.Slider_Move_Image()
        self.ui.ScaleSlider.setValue(0)
        self.ScaleValueChange()
        self.ui.Set_Threshold_Value_Slider.setValue(127)
        self.Threshold_Value_Change()
        self.ui.MaxThresholdSlider.setValue(400)
        self.ui.MinThresholdSlider.setValue(0)
        self.MaxThresoldChange()
        self.MinThresoldChange()
