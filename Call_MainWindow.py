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
        # Menu
        self.ui.actionClose.triggered.connect(app.exit)
        self.ui.actionOpen_File.triggered.connect(self.OpenFile_chooseFile)
        self.ui.actionGray.triggered.connect(self.ImageGray)
        self.ui.actionRGB.triggered.connect(self.ImageRGB)
        # Button
        self.ui.File_Btn.clicked.connect(self.OpenFile_chooseFile)
        self.ui.Save_File_Btn.clicked.connect()
        # Label
        self.ui.ImageLabel.mousePressEvent = self.Show_Mouse_Press_Position

    def OpenFile_chooseFile(self):  # Open File
        self.file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(self, "選擇檔案", self.cwd, "ALL Files (*);; PNG Files (*.png);; Jpg Files (*.jpg) ")
        if self.file_name == "":
            self.ui.statusbar.showMessage("取消開檔")
            return 0
        else:
            self.ui.statusbar.showMessage("開檔成功")
            self.oriImg = cv.imread(filename=self.file_name)
            self.ui.menu_2.setEnabled(True)
            self.ShowImage(self.oriImg)

    def SaveFile(self):


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

    def ImageRGB(self):
        self.ui.ImageLabel.setPixmap(QtGui.QPixmap.fromImage(self.qimg))
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())