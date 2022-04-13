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
        MainWindow.resize(898, 834)
        MainWindow.setMouseTracking(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ROI_Label = QtWidgets.QLabel(self.centralwidget)
        self.ROI_Label.setGeometry(QtCore.QRect(710, 20, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setUnderline(False)
        self.ROI_Label.setFont(font)
        self.ROI_Label.setObjectName("ROI_Label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 20, 611, 561))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 601, 551))
        self.ImageLabel = QtWidgets.QLabel()
        self.ImageLabel.setGeometry(QtCore.QRect(0, 0, 601, 551))
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
        self.verticalLayout.addWidget(self.scrollArea)
        self.Set_Threshold_Value_Slider = QtWidgets.QSlider(self.centralwidget)
        self.Set_Threshold_Value_Slider.setEnabled(False)
        self.Set_Threshold_Value_Slider.setGeometry(QtCore.QRect(710, 260, 160, 22))
        self.Set_Threshold_Value_Slider.setMaximum(255)
        self.Set_Threshold_Value_Slider.setProperty("value", 127)
        self.Set_Threshold_Value_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Set_Threshold_Value_Slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.Set_Threshold_Value_Slider.setObjectName("Set_Threshold_Value_Slider")
        self.Text_label = QtWidgets.QLabel(self.centralwidget)
        self.Text_label.setGeometry(QtCore.QRect(710, 180, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.Text_label.setFont(font)
        self.Text_label.setObjectName("Text_label")
        self.Text_label_0 = QtWidgets.QLabel(self.centralwidget)
        self.Text_label_0.setGeometry(QtCore.QRect(710, 230, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.Text_label_0.setFont(font)
        self.Text_label_0.setObjectName("Text_label_0")
        self.Text_label_255 = QtWidgets.QLabel(self.centralwidget)
        self.Text_label_255.setGeometry(QtCore.QRect(850, 230, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.Text_label_255.setFont(font)
        self.Text_label_255.setObjectName("Text_label_255")
        self.Image_Info_label = QtWidgets.QLabel(self.centralwidget)
        self.Image_Info_label.setGeometry(QtCore.QRect(60, 590, 621, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.Image_Info_label.setFont(font)
        self.Image_Info_label.setText("")
        self.Image_Info_label.setObjectName("Image_Info_label")
        self.Show_Hist_Btn = QtWidgets.QPushButton(self.centralwidget)
        self.Show_Hist_Btn.setGeometry(QtCore.QRect(710, 320, 121, 31))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(16)
        self.Show_Hist_Btn.setFont(font)
        self.Show_Hist_Btn.setObjectName("Show_Hist_Btn")
        self.Show_ROI_Info = QtWidgets.QLabel(self.centralwidget)
        self.Show_ROI_Info.setGeometry(QtCore.QRect(710, 70, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.Show_ROI_Info.setFont(font)
        self.Show_ROI_Info.setText("")
        self.Show_ROI_Info.setTextFormat(QtCore.Qt.AutoText)
        self.Show_ROI_Info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Show_ROI_Info.setObjectName("Show_ROI_Info")
        self.Text_label_Threshold_value = QtWidgets.QLabel(self.centralwidget)
        self.Text_label_Threshold_value.setGeometry(QtCore.QRect(830, 180, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.Text_label_Threshold_value.setFont(font)
        self.Text_label_Threshold_value.setObjectName("Text_label_Threshold_value")
        self.Gif_Label = QtWidgets.QLabel(self.centralwidget)
        self.Gif_Label.setGeometry(QtCore.QRect(700, 680, 150, 110))
        self.Gif_Label.setObjectName("Gif_Label")
        self.MaxValue = QtWidgets.QLineEdit(self.centralwidget)
        self.MaxValue.setGeometry(QtCore.QRect(710, 430, 113, 20))
        self.MaxValue.setMaxLength(3)
        self.MaxValue.setObjectName("MaxValue")
        self.MinValue = QtWidgets.QLineEdit(self.centralwidget)
        self.MinValue.setGeometry(QtCore.QRect(710, 490, 113, 20))
        self.MinValue.setMaxLength(3)
        self.MinValue.setObjectName("MinValue")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(710, 390, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(710, 450, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 640, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.AngelSlider = QtWidgets.QSlider(self.centralwidget)
        self.AngelSlider.setGeometry(QtCore.QRect(170, 640, 160, 22))
        self.AngelSlider.setMinimum(-360)
        self.AngelSlider.setMaximum(360)
        self.AngelSlider.setOrientation(QtCore.Qt.Horizontal)
        self.AngelSlider.setObjectName("AngelSlider")
        self.AngelValue = QtWidgets.QLabel(self.centralwidget)
        self.AngelValue.setGeometry(QtCore.QRect(340, 640, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.AngelValue.setFont(font)
        self.AngelValue.setObjectName("AngelValue")
        self.horizontalMoveSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalMoveSlider.setGeometry(QtCore.QRect(170, 680, 161, 22))
        self.horizontalMoveSlider.setMinimum(-400)
        self.horizontalMoveSlider.setMaximum(400)
        self.horizontalMoveSlider.setProperty("value", 0)
        self.horizontalMoveSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalMoveSlider.setObjectName("horizontalMoveSlider")
        self.VerticalMoveSlider = QtWidgets.QSlider(self.centralwidget)
        self.VerticalMoveSlider.setGeometry(QtCore.QRect(170, 720, 161, 22))
        self.VerticalMoveSlider.setMinimum(-400)
        self.VerticalMoveSlider.setMaximum(400)
        self.VerticalMoveSlider.setProperty("value", 0)
        self.VerticalMoveSlider.setOrientation(QtCore.Qt.Horizontal)
        self.VerticalMoveSlider.setObjectName("VerticalMoveSlider")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 680, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 720, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.MoveRightValue = QtWidgets.QLabel(self.centralwidget)
        self.MoveRightValue.setGeometry(QtCore.QRect(340, 680, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.MoveRightValue.setFont(font)
        self.MoveRightValue.setObjectName("MoveRightValue")
        self.MoveUpDownValue = QtWidgets.QLabel(self.centralwidget)
        self.MoveUpDownValue.setGeometry(QtCore.QRect(340, 720, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.MoveUpDownValue.setFont(font)
        self.MoveUpDownValue.setObjectName("MoveUpDownValue")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 760, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.ScaleSlider = QtWidgets.QSlider(self.centralwidget)
        self.ScaleSlider.setGeometry(QtCore.QRect(170, 760, 160, 22))
        self.ScaleSlider.setMinimum(0)
        self.ScaleSlider.setMaximum(10)
        self.ScaleSlider.setSingleStep(0)
        self.ScaleSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ScaleSlider.setObjectName("ScaleSlider")
        self.ScaleValue = QtWidgets.QLabel(self.centralwidget)
        self.ScaleValue.setGeometry(QtCore.QRect(340, 760, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.ScaleValue.setFont(font)
        self.ScaleValue.setObjectName("ScaleValue")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 898, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setEnabled(True)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
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
        self.actionGray.setObjectName("actionGray")
        self.actionRGB = QtWidgets.QAction(MainWindow)
        self.actionRGB.setObjectName("actionRGB")
        self.actionHistogram = QtWidgets.QAction(MainWindow)
        self.actionHistogram.setObjectName("actionHistogram")
        self.actionSave_File = QtWidgets.QAction(MainWindow)
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
        self.ROI_Label.setText(_translate("MainWindow", "ROI 大小"))
        self.ImageLabel.setText(_translate("MainWindow", "No Image"))
        self.Text_label.setText(_translate("MainWindow", "二值化閥值 :"))
        self.Text_label_0.setText(_translate("MainWindow", "0"))
        self.Text_label_255.setText(_translate("MainWindow", "255"))
        self.Show_Hist_Btn.setText(_translate("MainWindow", "影像直方圖"))
        self.Text_label_Threshold_value.setText(_translate("MainWindow", " 127"))
        self.label.setText(_translate("MainWindow", "最大閥值"))
        self.label_2.setText(_translate("MainWindow", "最小閥值"))
        self.label_3.setText(_translate("MainWindow", "旋轉角度"))
        self.AngelValue.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "水平平移量"))
        self.label_6.setText(_translate("MainWindow", "垂直平移量"))
        self.MoveRightValue.setText(_translate("MainWindow", "0"))
        self.MoveUpDownValue.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "偏移倍率"))
        self.ScaleValue.setText(_translate("MainWindow", "0.0"))
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
