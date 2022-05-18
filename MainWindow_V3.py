# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow_V3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(863, 805)
        MainWindow.setMouseTracking(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Image_Info_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.Image_Info_label.setFont(font)
        self.Image_Info_label.setText("")
        self.Image_Info_label.setObjectName("Image_Info_label")
        self.gridLayout.addWidget(self.Image_Info_label, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMaximumSize(QtCore.QSize(841, 541))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.ImageLabel = QtWidgets.QLabel()
        self.ImageLabel.setGeometry(QtCore.QRect(0, 0, 841, 541))
        self.ImageLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(36)
        self.ImageLabel.setFont(font)
        self.ImageLabel.setMouseTracking(False)
        self.ImageLabel.setAutoFillBackground(False)
        self.ImageLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ImageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ImageLabel.setObjectName("ImageLabel")
        self.scrollArea.setWidget(self.ImageLabel)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.ROI_Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setUnderline(False)
        self.ROI_Label.setFont(font)
        self.ROI_Label.setObjectName("ROI_Label")
        self.verticalLayout_5.addWidget(self.ROI_Label)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.AngelSlider = QtWidgets.QSlider(self.centralwidget)
        self.AngelSlider.setEnabled(False)
        self.AngelSlider.setMaximumSize(QtCore.QSize(250, 16777215))
        self.AngelSlider.setMinimum(-360)
        self.AngelSlider.setMaximum(360)
        self.AngelSlider.setOrientation(QtCore.Qt.Horizontal)
        self.AngelSlider.setObjectName("AngelSlider")
        self.horizontalLayout.addWidget(self.AngelSlider)
        self.AngelValue = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.AngelValue.setFont(font)
        self.AngelValue.setObjectName("AngelValue")
        self.horizontalLayout.addWidget(self.AngelValue)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.horizontalMoveSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalMoveSlider.setEnabled(False)
        self.horizontalMoveSlider.setMaximumSize(QtCore.QSize(250, 16777215))
        self.horizontalMoveSlider.setMinimum(-400)
        self.horizontalMoveSlider.setMaximum(400)
        self.horizontalMoveSlider.setProperty("value", 0)
        self.horizontalMoveSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalMoveSlider.setObjectName("horizontalMoveSlider")
        self.horizontalLayout_2.addWidget(self.horizontalMoveSlider)
        self.MoveRightValue = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.MoveRightValue.setFont(font)
        self.MoveRightValue.setObjectName("MoveRightValue")
        self.horizontalLayout_2.addWidget(self.MoveRightValue)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.VerticalMoveSlider = QtWidgets.QSlider(self.centralwidget)
        self.VerticalMoveSlider.setEnabled(False)
        self.VerticalMoveSlider.setMaximumSize(QtCore.QSize(250, 16777215))
        self.VerticalMoveSlider.setMinimum(-400)
        self.VerticalMoveSlider.setMaximum(400)
        self.VerticalMoveSlider.setProperty("value", 0)
        self.VerticalMoveSlider.setOrientation(QtCore.Qt.Horizontal)
        self.VerticalMoveSlider.setObjectName("VerticalMoveSlider")
        self.horizontalLayout_3.addWidget(self.VerticalMoveSlider)
        self.MoveUpDownValue = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.MoveUpDownValue.setFont(font)
        self.MoveUpDownValue.setObjectName("MoveUpDownValue")
        self.horizontalLayout_3.addWidget(self.MoveUpDownValue)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 4)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.ScaleSlider = QtWidgets.QSlider(self.centralwidget)
        self.ScaleSlider.setEnabled(False)
        self.ScaleSlider.setMaximumSize(QtCore.QSize(250, 16777215))
        self.ScaleSlider.setMinimum(0)
        self.ScaleSlider.setMaximum(10)
        self.ScaleSlider.setSingleStep(0)
        self.ScaleSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ScaleSlider.setObjectName("ScaleSlider")
        self.horizontalLayout_4.addWidget(self.ScaleSlider)
        self.ScaleValue = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.ScaleValue.setFont(font)
        self.ScaleValue.setObjectName("ScaleValue")
        self.horizontalLayout_4.addWidget(self.ScaleValue)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 5)
        self.horizontalLayout_4.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Text_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.Text_label.setFont(font)
        self.Text_label.setObjectName("Text_label")
        self.horizontalLayout_5.addWidget(self.Text_label)
        self.Set_Threshold_Value_Slider = QtWidgets.QSlider(self.centralwidget)
        self.Set_Threshold_Value_Slider.setEnabled(False)
        self.Set_Threshold_Value_Slider.setMaximumSize(QtCore.QSize(250, 16777215))
        self.Set_Threshold_Value_Slider.setMaximum(255)
        self.Set_Threshold_Value_Slider.setProperty("value", 127)
        self.Set_Threshold_Value_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Set_Threshold_Value_Slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.Set_Threshold_Value_Slider.setObjectName("Set_Threshold_Value_Slider")
        self.horizontalLayout_5.addWidget(self.Set_Threshold_Value_Slider)
        self.Text_label_Threshold_value = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.Text_label_Threshold_value.setFont(font)
        self.Text_label_Threshold_value.setObjectName("Text_label_Threshold_value")
        self.horizontalLayout_5.addWidget(self.Text_label_Threshold_value)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 5)
        self.horizontalLayout_5.setStretch(2, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.MaxThresholdSlider = QtWidgets.QSlider(self.centralwidget)
        self.MaxThresholdSlider.setEnabled(False)
        self.MaxThresholdSlider.setMaximumSize(QtCore.QSize(250, 16777215))
        self.MaxThresholdSlider.setMaximum(400)
        self.MaxThresholdSlider.setProperty("value", 400)
        self.MaxThresholdSlider.setOrientation(QtCore.Qt.Horizontal)
        self.MaxThresholdSlider.setObjectName("MaxThresholdSlider")
        self.horizontalLayout_6.addWidget(self.MaxThresholdSlider)
        self.MaxThresholdValue = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.MaxThresholdValue.setFont(font)
        self.MaxThresholdValue.setObjectName("MaxThresholdValue")
        self.horizontalLayout_6.addWidget(self.MaxThresholdValue)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 4)
        self.horizontalLayout_6.setStretch(2, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.MinThresholdSlider = QtWidgets.QSlider(self.centralwidget)
        self.MinThresholdSlider.setEnabled(False)
        self.MinThresholdSlider.setMaximumSize(QtCore.QSize(250, 16777215))
        self.MinThresholdSlider.setMaximum(400)
        self.MinThresholdSlider.setOrientation(QtCore.Qt.Horizontal)
        self.MinThresholdSlider.setObjectName("MinThresholdSlider")
        self.horizontalLayout_7.addWidget(self.MinThresholdSlider)
        self.MinThresholdValue = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.MinThresholdValue.setFont(font)
        self.MinThresholdValue.setObjectName("MinThresholdValue")
        self.horizontalLayout_7.addWidget(self.MinThresholdValue)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 4)
        self.horizontalLayout_7.setStretch(2, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)
        self.Gif_Label = QtWidgets.QLabel(self.centralwidget)
        self.Gif_Label.setMinimumSize(QtCore.QSize(150, 110))
        self.Gif_Label.setMaximumSize(QtCore.QSize(150, 110))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        self.Gif_Label.setFont(font)
        self.Gif_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Gif_Label.setObjectName("Gif_Label")
        self.horizontalLayout_9.addWidget(self.Gif_Label)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.gridLayout.addLayout(self.verticalLayout_5, 2, 0, 1, 1)
        self.gridLayout.setRowStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 863, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setEnabled(False)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setEnabled(False)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setEnabled(False)
        self.menu_4.setObjectName("menu_4")
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
        self.actionGray.setEnabled(True)
        self.actionGray.setObjectName("actionGray")
        self.actionRGB = QtWidgets.QAction(MainWindow)
        self.actionRGB.setObjectName("actionRGB")
        self.actionHistogram = QtWidgets.QAction(MainWindow)
        self.actionHistogram.setObjectName("actionHistogram")
        self.actionSave_File = QtWidgets.QAction(MainWindow)
        self.actionSave_File.setEnabled(False)
        self.actionSave_File.setObjectName("actionSave_File")
        self.actionTresholding = QtWidgets.QAction(MainWindow)
        self.actionTresholding.setObjectName("actionTresholding")
        self.actionROI = QtWidgets.QAction(MainWindow)
        self.actionROI.setObjectName("actionROI")
        self.action123 = QtWidgets.QAction(MainWindow)
        self.action123.setObjectName("action123")
        self.actionHSV = QtWidgets.QAction(MainWindow)
        self.actionHSV.setObjectName("actionHSV")
        self.actionGuassion = QtWidgets.QAction(MainWindow)
        self.actionGuassion.setObjectName("actionGuassion")
        self.actionCanny = QtWidgets.QAction(MainWindow)
        self.actionCanny.setObjectName("actionCanny")
        self.actionNoise = QtWidgets.QAction(MainWindow)
        self.actionNoise.setObjectName("actionNoise")
        self.actionaffine_transform = QtWidgets.QAction(MainWindow)
        self.actionaffine_transform.setObjectName("actionaffine_transform")
        self.actionperspective_transform = QtWidgets.QAction(MainWindow)
        self.actionperspective_transform.setObjectName("actionperspective_transform")
        self.actionShow_Hist = QtWidgets.QAction(MainWindow)
        self.actionShow_Hist.setObjectName("actionShow_Hist")
        self.menu.addAction(self.actionOpen_File)
        self.menu.addAction(self.actionSave_File)
        self.menu.addAction(self.actionClose)
        self.menu_2.addAction(self.actionGray)
        self.menu_2.addAction(self.actionRGB)
        self.menu_2.addAction(self.actionHistogram)
        self.menu_2.addAction(self.actionTresholding)
        self.menu_2.addAction(self.actionHSV)
        self.menu_3.addAction(self.actionROI)
        self.menu_3.addAction(self.actionaffine_transform)
        self.menu_3.addAction(self.actionperspective_transform)
        self.menu_3.addAction(self.actionShow_Hist)
        self.menu_4.addAction(self.actionGuassion)
        self.menu_4.addAction(self.actionCanny)
        self.menu_4.addAction(self.actionNoise)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "影像處理平台"))
        self.ImageLabel.setText(_translate("MainWindow", "No Image"))
        self.ROI_Label.setText(_translate("MainWindow", "ROI 大小"))
        self.label_3.setText(_translate("MainWindow", "旋轉角度"))
        self.AngelValue.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "水平平移量"))
        self.MoveRightValue.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "垂直平移量"))
        self.MoveUpDownValue.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "偏移倍率"))
        self.ScaleValue.setText(_translate("MainWindow", "0.0"))
        self.Text_label.setText(_translate("MainWindow", "二值化閥值"))
        self.Text_label_Threshold_value.setText(_translate("MainWindow", " 127"))
        self.label.setText(_translate("MainWindow", "最大閥值"))
        self.MaxThresholdValue.setText(_translate("MainWindow", "400"))
        self.label_2.setText(_translate("MainWindow", "最小閥值"))
        self.MinThresholdValue.setText(_translate("MainWindow", "0"))
        self.Gif_Label.setText(_translate("MainWindow", "GIF"))
        self.menu.setTitle(_translate("MainWindow", "選單"))
        self.menu_2.setTitle(_translate("MainWindow", "色彩選項"))
        self.menu_3.setTitle(_translate("MainWindow", "小工具"))
        self.menu_4.setTitle(_translate("MainWindow", "影像處理"))
        self.actionOpen_File.setText(_translate("MainWindow", "開啟檔案"))
        self.actionOpen_File.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionClose.setText(_translate("MainWindow", "關閉平台"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionGray.setText(_translate("MainWindow", "影像灰階"))
        self.actionRGB.setText(_translate("MainWindow", "轉換原始圖片"))
        self.actionHistogram.setText(_translate("MainWindow", "灰階影像均衡化"))
        self.actionSave_File.setText(_translate("MainWindow", "儲存檔案"))
        self.actionSave_File.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionTresholding.setText(_translate("MainWindow", "影像二值化"))
        self.actionROI.setText(_translate("MainWindow", "選取 ROI"))
        self.action123.setText(_translate("MainWindow", "HSV"))
        self.actionHSV.setText(_translate("MainWindow", "轉換HSV影像"))
        self.actionGuassion.setText(_translate("MainWindow", "模糊化"))
        self.actionCanny.setText(_translate("MainWindow", "邊緣擷取"))
        self.actionNoise.setText(_translate("MainWindow", "雜訊處理"))
        self.actionaffine_transform.setText(_translate("MainWindow", "仿射轉換"))
        self.actionperspective_transform.setText(_translate("MainWindow", "透視投影轉換"))
        self.actionShow_Hist.setText(_translate("MainWindow", "影像直方圖"))