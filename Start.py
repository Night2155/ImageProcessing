import sys
from PyQt5 import QtWidgets,QtGui,QtCore
from MainWindow import Ui_MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    window = Ui_MainWindow()
    window.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())