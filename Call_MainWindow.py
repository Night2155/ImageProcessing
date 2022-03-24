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
        #self.ui.actionOpen_File.setShortcut('Ctrl+O')
        self.ui.actionClose.triggered.connect(app.exit)
        self.ui.actionOpen_File.triggered.connect(self.OpenFile_chooseFile)

    def OpenFile_chooseFile(self):
        #file_name, file_type = QtWidgets.QFileDialog.getExistingDirectory(self, "選擇檔案", self.cwd, "All Files (*);;PNG Files (*.png)")
        file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(self, "選擇檔案", self.cwd, "PNG Files (*.png);; Jpg Files (*.jpg)")
        if file_name == "":
            print("取消選擇檔案")
            return 0
        else:
            self.ui.statusbar.showMessage("開檔成功")
            self.ui.frame


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())