from PyQt5 import QtWidgets, QtGui, QtCore
from MainWindow import Ui_MainWindow # 引入UI設計檔
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Menu
        self.ui.actionOpen_File.setShortcut('Ctrl+O')
        self.ui.actionClose.triggered.connect(app.exit)
        self.ui.actionOpen_File.triggered.connect(QtWidgets.QFileDialog.getExistingDirectory())



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())