# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1167, 890)
        MainWindow.setMouseTracking(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ROI_Label = QtWidgets.QLabel(self.centralwidget)
        self.ROI_Label.setGeometry(QtCore.QRect(940, 30, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setUnderline(True)
        self.ROI_Label.setFont(font)
        self.ROI_Label.setObjectName("ROI_Label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 20, 821, 761))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 817, 757))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.ImageLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ImageLabel.setGeometry(QtCore.QRect(0, 0, 811, 751))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(36)
        self.ImageLabel.setFont(font)
        self.ImageLabel.setMouseTracking(False)
        self.ImageLabel.setAutoFillBackground(False)
        self.ImageLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ImageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ImageLabel.setObjectName("ImageLabel")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.Set_Threshold_Value_Slider = QtWidgets.QSlider(self.centralwidget)
        self.Set_Threshold_Value_Slider.setEnabled(False)
        self.Set_Threshold_Value_Slider.setGeometry(QtCore.QRect(940, 350, 160, 22))
        self.Set_Threshold_Value_Slider.setMaximum(255)
        self.Set_Threshold_Value_Slider.setProperty("value", 127)
        self.Set_Threshold_Value_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Set_Threshold_Value_Slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.Set_Threshold_Value_Slider.setObjectName("Set_Threshold_Value_Slider")
        self.Text_label = QtWidgets.QLabel(self.centralwidget)
        self.Text_label.setGeometry(QtCore.QRect(940, 270, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.Text_label.setFont(font)
        self.Text_label.setObjectName("Text_label")
        self.Text_label_0 = QtWidgets.QLabel(self.centralwidget)
        self.Text_label_0.setGeometry(QtCore.QRect(940, 320, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.Text_label_0.setFont(font)
        self.Text_label_0.setObjectName("Text_label_0")
        self.Text_label_255 = QtWidgets.QLabel(self.centralwidget)
        self.Text_label_255.setGeometry(QtCore.QRect(1080, 320, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.Text_label_255.setFont(font)
        self.Text_label_255.setObjectName("Text_label_255")
        self.Image_Info_label = QtWidgets.QLabel(self.centralwidget)
        self.Image_Info_label.setGeometry(QtCore.QRect(60, 800, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.Image_Info_label.setFont(font)
        self.Image_Info_label.setObjectName("Image_Info_label")
        self.Show_Hist_Btn = QtWidgets.QPushButton(self.centralwidget)
        self.Show_Hist_Btn.setGeometry(QtCore.QRect(940, 430, 121, 31))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(16)
        self.Show_Hist_Btn.setFont(font)
        self.Show_Hist_Btn.setObjectName("Show_Hist_Btn")
        self.Show_ROI_Info = QtWidgets.QLabel(self.centralwidget)
        self.Show_ROI_Info.setGeometry(QtCore.QRect(940, 90, 171, 131))
        self.Show_ROI_Info.setText("")
        self.Show_ROI_Info.setObjectName("Show_ROI_Info")
        self.Text_label_Threshold_value = QtWidgets.QLabel(self.centralwidget)
        self.Text_label_Threshold_value.setGeometry(QtCore.QRect(1060, 270, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.Text_label_Threshold_value.setFont(font)
        self.Text_label_Threshold_value.setObjectName("Text_label_Threshold_value")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1167, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setEnabled(False)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionGray = QtWidgets.QAction(MainWindow)
        self.actionGray.setObjectName("actionGray")
        self.actionRGB = QtWidgets.QAction(MainWindow)
        self.actionRGB.setObjectName("actionRGB")
        self.actionHistogram = QtWidgets.QAction(MainWindow)
        self.actionHistogram.setObjectName("actionHistogram")
        self.actionSave_File = QtWidgets.QAction(MainWindow)
        self.actionSave_File.setObjectName("actionSave_File")
        self.actionTresholding = QtWidgets.QAction(MainWindow)
        self.actionTresholding.setObjectName("actionTresholding")
        self.menu.addAction(self.actionOpen_File)
        self.menu.addAction(self.actionSave_File)
        self.menu.addAction(self.actionClose)
        self.menu_2.addAction(self.actionGray)
        self.menu_2.addAction(self.actionRGB)
        self.menu_2.addAction(self.actionHistogram)
        self.menu_2.addAction(self.actionTresholding)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "影像處理平台"))
        self.ROI_Label.setText(_translate("MainWindow", "ROI 大小"))
        self.ImageLabel.setText(_translate("MainWindow", "No Image"))
        self.Text_label.setText(_translate("MainWindow", "二值化閥值 :"))
        self.Text_label_0.setText(_translate("MainWindow", "0"))
        self.Text_label_255.setText(_translate("MainWindow", "255"))
        self.Image_Info_label.setText(_translate("MainWindow", "圖片資訊 :"))
        self.Show_Hist_Btn.setText(_translate("MainWindow", "影像直方圖"))
        self.Text_label_Threshold_value.setText(_translate("MainWindow", " 127"))
        self.menu.setTitle(_translate("MainWindow", "選單"))
        self.menu_2.setTitle(_translate("MainWindow", "色彩選項"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionOpen_File.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionGray.setText(_translate("MainWindow", "影像灰階"))
        self.actionRGB.setText(_translate("MainWindow", "轉換原始圖片"))
        self.actionHistogram.setText(_translate("MainWindow", "影像直方圖均衡化"))
        self.actionSave_File.setText(_translate("MainWindow", "Save File"))
        self.actionTresholding.setText(_translate("MainWindow", "影像二值化"))
