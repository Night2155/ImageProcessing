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
        # Button
        self.ui.File_Btn.clicked.connect(self.OpenFile_chooseFile)
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
            self.ShowImage(self.oriImg)

    def Show_Mouse_Press_Position(self, event):
        self.ui.statusbar.showMessage(f"[show_mouse_press] : {event.x()}, {event.y()}, {event.button()}")

    def ShowImage(self, img):
        #img = cv.imread(path)
        height, width, channel = img.shape
        bytesPerline = 3*width
        self.qimg = QtGui.QImage(img, width, height, bytesPerline, QtGui.QImage.Format_RGB888).rgbSwapped()
        pixmap = QtGui.QPixmap.fromImage(self.qimg)
        self.ui.ImageLabel.resize(width, height)
        self.ui.ImageLabel.setPixmap(pixmap)
        self.ui.statusbar.showMessage(f"ImageInfo : {height=}, {width=}, {channel=}")

    def ImageGray(self):
        if self.file_name == "":
            return
        else:
            GrayImg #= cv.cvtColor(self.oriImg, cv.COLOR_BGR2GRAY)
            height, width = GrayImg.shape
            #pixmap = QtGui.QPixmap.fromImage(GrayImg)
            self.ui.ImageLabel.resize(width, height)
            self.ui.ImageLabel.setPixmap(pixmap)
            self.ui.statusbar.showMessage(f"ImageInfo : {height=}, {width=}")



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())