import os

from PyQt5 import QtWidgets, QtGui, QtCore
from MainWindow import Ui_MainWindow # 引入UI設計檔
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.cwd = os.getcwd()
        # Menu

        self.ui.actionClose.triggered.connect(app.exit)
        self.ui.actionOpen_File.triggered.connect(self.OpenFile_chooseFile)
        self.ui.File_Btn.clicked.connect(self.OpenFile_chooseFile)
        self.ui.ImageLabel.mousePressEvent = self.Show_Mouse_Press_Position
    def OpenFile_chooseFile(self):
        file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(self, "選擇檔案", self.cwd, " PNG Files (*.png);; Jpg Files (*.jpg) ")
        if file_name == "":
            self.ui.statusbar.showMessage("取消開檔")
            return 0
        else:
            self.ui.statusbar.showMessage("開檔成功")
            img = QtGui.QPixmap(file_name)

            self.ui.ImageLabel.setPixmap(img)
            self.ui.ImageLabel.resize(img.width(), img.width())

    def Show_Mouse_Press_Position(self, event):
        self.ui.statusbar.showMessage(f"[show_mouse_press] {event.x()=}, {event.y()=}, {event.button()=}")


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())