# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Trial3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from tkinter import FLAT
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import pyqtgraph as pg
import qdarkstyle


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1377, 868)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        ##self.centralwidget.setMinimumHeight(40)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Instrument0_icon = QtWidgets.QLabel(self.tab)
        self.Instrument0_icon.setMaximumSize(QtCore.QSize(60, 60))
        self.Instrument0_icon.setText("")
        self.Instrument0_icon.setPixmap(QtGui.QPixmap("pianoaftereffect.png"))
        self.Instrument0_icon.setScaledContents(True)
        self.Instrument0_icon.setObjectName("Instrument0_icon")
        self.gridLayout_4.addWidget(self.Instrument0_icon, 3, 0, 1, 1)
        self.Instrument0_verticalSlider = QtWidgets.QSlider(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Instrument0_verticalSlider.sizePolicy().hasHeightForWidth())
        self.Instrument0_verticalSlider.setSizePolicy(sizePolicy)
        self.Instrument0_verticalSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Instrument0_verticalSlider.setMaximum(10)
        self.Instrument0_verticalSlider.setMinimum(-10)
        self.Instrument0_verticalSlider.setSingleStep(1)
        self.Instrument0_verticalSlider.setPageStep(1)
        self.Instrument0_verticalSlider.setProperty("value", 1)
        self.Instrument0_verticalSlider.setSliderPosition(1)
        self.Instrument0_verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.Instrument0_verticalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Instrument0_verticalSlider.setTickInterval(1)
        self.Instrument0_verticalSlider.setObjectName("Instrument0_verticalSlider")
        self.gridLayout_4.addWidget(self.Instrument0_verticalSlider, 1, 0, 1, 1)
        self.Instrument0_lcdNumber = QtWidgets.QLCDNumber(self.tab)
        self.Instrument0_lcdNumber.setAutoFillBackground(False)
        self.Instrument0_lcdNumber.setLineWidth(1)
        self.Instrument0_lcdNumber.setMidLineWidth(0)
        self.Instrument0_lcdNumber.setDigitCount(3)
        self.Instrument0_lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.Instrument0_lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Instrument0_lcdNumber.setProperty("value", 1)
        self.Instrument0_lcdNumber.setProperty("intValue", 1)
        self.Instrument0_lcdNumber.setObjectName("Instrument0_lcdNumber")
        self.gridLayout_4.addWidget(self.Instrument0_lcdNumber, 2, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.Instrument1_verticalSlider = QtWidgets.QSlider(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Instrument1_verticalSlider.sizePolicy().hasHeightForWidth())
        self.Instrument1_verticalSlider.setSizePolicy(sizePolicy)
        self.Instrument1_verticalSlider.setMaximum(10)
        self.Instrument1_verticalSlider.setMinimum(-10)
        self.Instrument1_verticalSlider.setSingleStep(1)
        self.Instrument1_verticalSlider.setPageStep(1)
        self.Instrument1_verticalSlider.setProperty("value", 1)
        self.Instrument1_verticalSlider.setSliderPosition(1)
        self.Instrument1_verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.Instrument1_verticalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Instrument1_verticalSlider.setTickInterval(1)
        self.Instrument1_verticalSlider.setObjectName("Instrument1_verticalSlider")
        self.gridLayout_7.addWidget(self.Instrument1_verticalSlider, 1, 0, 1, 1)
        self.Instrument1_lcdNumber = QtWidgets.QLCDNumber(self.tab)
        self.Instrument1_lcdNumber.setDigitCount(3)
        self.Instrument1_lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Instrument1_lcdNumber.setProperty("intValue", 1)
        self.Instrument1_lcdNumber.setObjectName("Instrument1_lcdNumber")
        self.gridLayout_7.addWidget(self.Instrument1_lcdNumber, 2, 0, 1, 1)
        self.Instrument1_icon = QtWidgets.QLabel(self.tab)
        self.Instrument1_icon.setMaximumSize(QtCore.QSize(60, 60))
        self.Instrument1_icon.setText("")
        self.Instrument1_icon.setPixmap(QtGui.QPixmap("Drumicon (21).png"))
        self.Instrument1_icon.setScaledContents(True)
        self.Instrument1_icon.setObjectName("Instrument1_icon")
        self.gridLayout_7.addWidget(self.Instrument1_icon, 3, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_7)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.Instrument2_lcdNumber = QtWidgets.QLCDNumber(self.tab)
        self.Instrument2_lcdNumber.setDigitCount(3)
        self.Instrument2_lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Instrument2_lcdNumber.setProperty("intValue", 1)
        self.Instrument2_lcdNumber.setObjectName("Instrument2_lcdNumber")
        self.gridLayout_8.addWidget(self.Instrument2_lcdNumber, 2, 0, 1, 1)
        self.Instrument2_verticalSlider = QtWidgets.QSlider(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Instrument2_verticalSlider.sizePolicy().hasHeightForWidth())
        self.Instrument2_verticalSlider.setSizePolicy(sizePolicy)
        self.Instrument2_verticalSlider.setMaximum(10)
        self.Instrument2_verticalSlider.setMinimum(-10)
        self.Instrument2_verticalSlider.setSingleStep(1)
        self.Instrument2_verticalSlider.setPageStep(1)
        self.Instrument2_verticalSlider.setProperty("value", 1)
        self.Instrument2_verticalSlider.setSliderPosition(1)
        self.Instrument2_verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.Instrument2_verticalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Instrument2_verticalSlider.setTickInterval(1)
        self.Instrument2_verticalSlider.setObjectName("Instrument2_verticalSlider")
        self.gridLayout_8.addWidget(self.Instrument2_verticalSlider, 1, 0, 1, 1)
        self.Instrument2_icon = QtWidgets.QLabel(self.tab)
        self.Instrument2_icon.setMaximumSize(QtCore.QSize(60, 60))
        self.Instrument2_icon.setText("")
        self.Instrument2_icon.setPixmap(QtGui.QPixmap("Vocalsicon.png"))
        self.Instrument2_icon.setScaledContents(True)
        self.Instrument2_icon.setObjectName("Instrument2_icon")
        self.gridLayout_8.addWidget(self.Instrument2_icon, 3, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_8)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Spectrogram_label = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Spectrogram_label.setFont(font)
        self.Spectrogram_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Spectrogram_label.setObjectName("Spectrogram_label")
        self.verticalLayout_3.addWidget(self.Spectrogram_label)
       
        self.figure=plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.axis=self.figure.add_subplot(111)
        self.canvas.draw()
        self.axis.set_xlabel("time (in seconds)")
        self.axis.set_ylabel("frequency (Hz)")
        self.verticalLayout_3.addWidget(self.canvas)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Soundsignal_lable = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Soundsignal_lable.setFont(font)
        self.Soundsignal_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.Soundsignal_lable.setObjectName("Soundsignal_lable")
        self.verticalLayout_2.addWidget(self.Soundsignal_lable)
        self.Soundsignal_graphicsView = PlotWidget(self.tab)
        self.Soundsignal_graphicsView.setObjectName("Soundsignal_graphicsView")
        self.Soundsignal_graphicsView.setLabel('bottom', 'Time', 's')
        self.Soundsignal_graphicsView.setLabel('left', 'AMP', 'dp')
        self.Soundsignal_graphicsView.showGrid(True,True)
        self.verticalLayout_2.addWidget(self.Soundsignal_graphicsView)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.Music_listView = QtWidgets.QListWidget(self.tab)
        self.Music_listView.setObjectName("Music_listView")
        self.verticalLayout.addWidget(self.Music_listView)
        self.Volume_label = QtWidgets.QLabel(self.tab)
        self.Volume_label.setObjectName("Volume_label")
        self.verticalLayout.addWidget(self.Volume_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Volume_horizontalSlider = QtWidgets.QSlider(self.tab)
        self.Volume_horizontalSlider.setMaximum(100)
        self.Volume_horizontalSlider.setProperty("value", 100)
        self.Volume_horizontalSlider.setTracking(True)
        self.Volume_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.Volume_horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Volume_horizontalSlider.setObjectName("Volume_horizontalSlider")
        self.horizontalLayout_2.addWidget(self.Volume_horizontalSlider)
        self.Volume_lcdNumber = QtWidgets.QLCDNumber(self.tab)
        self.Volume_lcdNumber.setProperty("intValue", 100)
        self.Volume_lcdNumber.setObjectName("Volume_lcdNumber")
        self.horizontalLayout_2.addWidget(self.Volume_lcdNumber)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Start_pushButton = QtWidgets.QPushButton(self.tab)
        self.Start_pushButton.setObjectName("Start_pushButton")
        self.horizontalLayout.addWidget(self.Start_pushButton)
        #self.Pause_pushButton = QtWidgets.QPushButton(self.tab)
        #self.Pause_pushButton.setObjectName("Pause_pushButton")
        #self.horizontalLayout.addWidget(self.Pause_pushButton)
        #self.checkBox = QtWidgets.QCheckBox(self.tab)
        #self.checkBox.setObjectName("checkBox")
        #self.horizontalLayout.addWidget(self.checkBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.VirtualInstrument_Tab = QtWidgets.QTabWidget(self.tab_2)
        self.VirtualInstrument_Tab.setIconSize(QtCore.QSize(408, 40))
        self.VirtualInstrument_Tab.setObjectName("VirtualInstrument_Tab")
        self.Instrument_0 = QtWidgets.QWidget()
        self.Instrument_0.setObjectName("Instrument_0")
        self.Instrumet0_photo_label = QtWidgets.QLabel(self.Instrument_0)
        self.Instrumet0_photo_label.setGeometry(QtCore.QRect(11, 82, 1291, 601))
        self.Instrumet0_photo_label.setText("")
        self.Instrumet0_photo_label.setPixmap(QtGui.QPixmap("Vpiano.jpg"))
        self.Instrumet0_photo_label.setScaledContents(True)
        self.Instrumet0_photo_label.setObjectName("Instrumet0_photo_label")
        self.pushButtonPianoleft1 = QtWidgets.QPushButton(self.Instrument_0, flat=True)
        self.pushButtonPianoleft1.setGeometry(QtCore.QRect(15, 460, 170, 200))
        self.pushButtonPianoleft1.setText('')
        self.pushButtonPianoleft1.setFlat(True)
        self.pushButtonPianoleft1.setObjectName("pushButtonPianoleft1")
        self.pushButtonPianoleft2 = QtWidgets.QPushButton(self.Instrument_0)
        self.pushButtonPianoleft2.setGeometry(QtCore.QRect(200, 460, 170, 200))
        self.pushButtonPianoleft2.setFlat(False)
        self.pushButtonPianoleft2.setObjectName("pushButtonPianoleft2")
        self.pushButtonPianoleft3 = QtWidgets.QPushButton(self.Instrument_0)
        self.pushButtonPianoleft3.setGeometry(QtCore.QRect(385, 460, 170, 200))
        self.pushButtonPianoleft3.setFlat(True)
        self.pushButtonPianoleft3.setObjectName("pushButtonPianoleft3")
        self.pushButtonPianoleft4 = QtWidgets.QPushButton(self.Instrument_0)
        self.pushButtonPianoleft4.setGeometry(QtCore.QRect(570, 460, 170, 200))
        self.pushButtonPianoleft4.setObjectName("pushButtonPianoleft4")
        self.pushButtonPianoleft5 = QtWidgets.QPushButton(self.Instrument_0)
        self.pushButtonPianoleft5.setGeometry(QtCore.QRect(755, 460, 170, 200))
        self.pushButtonPianoleft5.setObjectName("pushButtonPianoleft5")
        self.pushButtonPianoleft6 = QtWidgets.QPushButton(self.Instrument_0)
        self.pushButtonPianoleft6.setGeometry(QtCore.QRect(940, 460, 170, 200))
        self.pushButtonPianoleft6.setObjectName("pushButtonPianoleft6")
        self.pushButtonPianoleft7 = QtWidgets.QPushButton(self.Instrument_0)
        self.pushButtonPianoleft7.setGeometry(QtCore.QRect(1125, 460, 170, 200))
        self.pushButtonPianoleft7.setObjectName("pushButtonPianoleft7")
        self.pushButtonPianoleftblack1 = QtWidgets.QPushButton(self.Instrument_0)
        self.pushButtonPianoleftblack1.setGeometry(QtCore.QRect(110, 85, 120, 370))
        self.pushButtonPianoleftblack1.setObjectName("pushButtonPianoleftblack1")
        self.pushButtonPianoleftblack2 = QtWidgets.QPushButton(self.Instrument_0)
        self.pushButtonPianoleftblack2.setGeometry(QtCore.QRect(335, 85, 120, 370))
        self.pushButtonPianoleftblack2.setObjectName("pushButtonPianoleftblack2")
        self.pushButtonPianoleftblack3 = QtWidgets.QPushButton(self.Instrument_0)
        self.pushButtonPianoleftblack3.setGeometry(QtCore.QRect(660, 85, 120, 370))
        self.pushButtonPianoleftblack3.setObjectName("pushButtonPianoleftblack3")
        self.pushButtonPianoleftblack4 = QtWidgets.QPushButton(self.Instrument_0)
        self.pushButtonPianoleftblack4.setGeometry(QtCore.QRect(870, 85, 120, 370))
        self.pushButtonPianoleftblack4.setObjectName("pushButtonPianoleftblack4")
        self.pushButtonPianoleftblack5 = QtWidgets.QPushButton(self.Instrument_0)
        self.pushButtonPianoleftblack5.setGeometry(QtCore.QRect(1080, 85, 120, 370))
        self.pushButtonPianoleftblack5.setObjectName("pushButtonPianoleftblack5")
        self.pushButtonPianoleft1.setStyleSheet("background-color: transparent")
        self.pushButtonPianoleft2.setStyleSheet("background-color: transparent")
        self.pushButtonPianoleft3.setStyleSheet("background-color: transparent")
        self.pushButtonPianoleft4.setStyleSheet("background-color: transparent")
        self.pushButtonPianoleft5.setStyleSheet("background-color: transparent")
        self.pushButtonPianoleft6.setStyleSheet("background-color: transparent")
        self.pushButtonPianoleft7.setStyleSheet("background-color: transparent")
        self.pushButtonPianoleftblack1.setStyleSheet("background-color: transparent")
        self.pushButtonPianoleftblack2.setStyleSheet("background-color: transparent")
        self.pushButtonPianoleftblack3.setStyleSheet("background-color: transparent")
        self.pushButtonPianoleftblack4.setStyleSheet("background-color: transparent")
        self.pushButtonPianoleftblack5.setStyleSheet("background-color: transparent")
        self.comboBox = QtWidgets.QComboBox(self.Instrument_0)
        self.comboBox.setGeometry(QtCore.QRect(11, 11, 180, 27))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pianoaftereffect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.VirtualInstrument_Tab.addTab(self.Instrument_0, icon, "")
        self.Instrument_1 = QtWidgets.QWidget()
        self.Instrument_1.setObjectName("Instrument_1")
        self.Instrumet1_photo_label = QtWidgets.QLabel(self.Instrument_1)
        self.Instrumet1_photo_label.setGeometry(QtCore.QRect(10, 0, 1301, 671))
        self.Instrumet1_photo_label.setText("")
        self.Instrumet1_photo_label.setPixmap(QtGui.QPixmap("yamaha_nobg\'.png"))
        self.Instrumet1_photo_label.setScaledContents(True)
        self.Instrumet1_photo_label.setObjectName("Instrumet1_photo_label")
        self.pushButton_Ride = QtWidgets.QPushButton(self.Instrument_1)
        self.pushButton_Ride.setGeometry(QtCore.QRect(110, 20, 301, 91))
        self.pushButton_Ride.setFlat(True)
        self.pushButton_Ride.setStyleSheet("background-color: transparent")
        self.pushButton_Ride.setObjectName("pushButton_Ride")
        self.pushButton_Hi = QtWidgets.QPushButton(self.Instrument_1)
        self.pushButton_Hi.setGeometry(QtCore.QRect(1040, 127, 241, 71))
        self.pushButton_Hi.setObjectName("pushButton_Hi")
        self.pushButton_Hi.setStyleSheet("background-color: transparent")

        self.pushButton_Crash = QtWidgets.QPushButton(self.Instrument_1)
        self.pushButton_Crash.setGeometry(QtCore.QRect(860, 27, 331, 61))
        self.pushButton_Crash.setObjectName("pushButton_Crash")
        self.pushButton_Crash.setStyleSheet("background-color: transparent")
        self.pushButton_Base = QtWidgets.QPushButton(self.Instrument_1)
        self.pushButton_Base.setGeometry(QtCore.QRect(410, 390, 241, 161))
        self.pushButton_Base.setFlat(True)
        self.pushButton_Base.setStyleSheet("background-color: transparent")
        self.pushButton_Base.setObjectName("pushButton_Base")
        self.pushButton_Snare = QtWidgets.QPushButton(self.Instrument_1 )
        self.pushButton_Snare.setGeometry(QtCore.QRect(780, 310, 231, 61))
        self.pushButton_Snare.setObjectName("pushButton_Snare")
        self.pushButton_Snare.setStyleSheet("background-color: transparent")
        self.pushButton_FloorTom = QtWidgets.QPushButton(self.Instrument_1)
        self.pushButton_FloorTom.setGeometry(QtCore.QRect(310, 290, 241, 51))
        self.pushButton_FloorTom.setObjectName("pushButton_FloorTom")
        self.pushButton_FloorTom.setStyleSheet("background-color: transparent")
        self.pushButton_HiTom = QtWidgets.QPushButton(self.Instrument_1)
        self.pushButton_HiTom.setGeometry(QtCore.QRect(670, 190, 191, 91))
        self.pushButton_HiTom.setObjectName("pushButton_HiTom")
        self.pushButton_HiTom.setStyleSheet("background-color: transparent")

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Drumicon (21).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.VirtualInstrument_Tab.addTab(self.Instrument_1, icon1, "")
        self.Instrument_2 = QtWidgets.QWidget()
        self.Instrument_2.setObjectName("Instrument_2")
        self.Instrumet2_photo_label = QtWidgets.QLabel(self.Instrument_2)
        self.Instrumet2_photo_label.setGeometry(QtCore.QRect(10, 90, 1291, 591))
        self.Instrumet2_photo_label.setText("")
        self.Instrumet2_photo_label.setPixmap(QtGui.QPixmap("xylophone.png"))
        self.Instrumet2_photo_label.setScaledContents(True)
        self.Instrumet2_photo_label.setObjectName("Instrumet2_photo_label")
        self.pushButton_chord_0 = QtWidgets.QPushButton(self.Instrument_2)
        self.pushButton_chord_0.setGeometry(QtCore.QRect(70, 265, 120, 160))
        self.pushButton_chord_0.setObjectName("pushButton_chord_0")
        self.pushButton_chord_1 = QtWidgets.QPushButton(self.Instrument_2)
        self.pushButton_chord_1.setGeometry(QtCore.QRect(220, 255, 120, 190))
        self.pushButton_chord_1.setFlat(False)
        self.pushButton_chord_1.setObjectName("pushButton_chord_1")
        self.pushButton_chord_2 = QtWidgets.QPushButton(self.Instrument_2)
        self.pushButton_chord_2.setGeometry(QtCore.QRect(365, 245, 125, 210))
        self.pushButton_chord_2.setObjectName("pushButton_chord_2")
        self.pushButton_chord_3 = QtWidgets.QPushButton(self.Instrument_2)
        self.pushButton_chord_3.setGeometry(QtCore.QRect(515, 235, 125, 230))
        self.pushButton_chord_3.setObjectName("pushButton_chord_3")
        self.pushButton_chord_4 = QtWidgets.QPushButton(self.Instrument_2)
        self.pushButton_chord_4.setGeometry(QtCore.QRect(660, 225, 130, 250))
        self.pushButton_chord_4.setObjectName("pushButton_chord_4")
        self.pushButton_chord_5 = QtWidgets.QPushButton(self.Instrument_2)
        self.pushButton_chord_5.setGeometry(QtCore.QRect(805, 215, 135, 270))
        self.pushButton_chord_5.setObjectName("pushButton_chord_5")
        self.pushButton_chord_6 = QtWidgets.QPushButton(self.Instrument_2)
        self.pushButton_chord_6.setGeometry(QtCore.QRect(950, 208, 135, 280))
        self.pushButton_chord_6.setObjectName("pushButton_chord_5")
        self.pushButton_chord_7 = QtWidgets.QPushButton(self.Instrument_2)
        self.pushButton_chord_7.setGeometry(QtCore.QRect(1095, 200, 145, 290))
        self.pushButton_chord_7.setObjectName("pushButton_chord_5")
        self.pushButton_chord_0.setStyleSheet("background-color: transparent")
        self.pushButton_chord_1.setStyleSheet("background-color: transparent")
        self.pushButton_chord_2.setStyleSheet("background-color: transparent")
        self.pushButton_chord_3.setStyleSheet("background-color: transparent")
        self.pushButton_chord_4.setStyleSheet("background-color: transparent")
        self.pushButton_chord_5.setStyleSheet("background-color: transparent")
        self.pushButton_chord_6.setStyleSheet("background-color: transparent")
        self.pushButton_chord_7.setStyleSheet("background-color: transparent")
        self.layoutWidget = QtWidgets.QWidget(self.Instrument_2)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 11, 292, 100))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")


        #self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.centralwidget)
        #self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        #self.verticalLayout_8.setObjectName("verticalLayout_8")
        
        self.Volume_horizontalSlider_xylo = QtWidgets.QSlider(self.centralwidget)
        self.Volume_horizontalSlider_xylo.setMaximum(100)
        self.Volume_horizontalSlider_xylo.setProperty("value", 100)
        self.Volume_horizontalSlider_xylo.setTracking(True)
        self.Volume_horizontalSlider_xylo.setOrientation(QtCore.Qt.Horizontal)
        self.Volume_horizontalSlider_xylo.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Volume_horizontalSlider_xylo.setObjectName("Volume_horizontalSlider_xylo")

        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.looplineedit=QtWidgets.QLineEdit(self.centralwidget)#
        self.looplineedit.setObjectName("looplinedit")#
        self.labelofVolXylophone = QtWidgets.QLabel(self.layoutWidget)
        ##
        self.labelofVolXylophone.setObjectName("Volume")##
        self.verticalLayout_7.addWidget(self.label)
        self.verticalLayout_7.addWidget(self.looplineedit)#
        self.verticalLayout_7.addWidget(self.labelofVolXylophone)##
        self.verticalLayout_7.addWidget(self.Volume_horizontalSlider_xylo)###
        
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        #self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("xylophoneiconbg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.VirtualInstrument_Tab.addTab(self.Instrument_2, icon2, "")
        self.gridLayout_3.addWidget(self.VirtualInstrument_Tab, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1377, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.VirtualInstrument_Tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Spectrogram_label.setText(_translate("MainWindow", "Spectrogram"))
        self.Soundsignal_lable.setText(_translate("MainWindow", "Sound Signal"))
        self.label_3.setText(_translate("MainWindow", "Loaded Signal"))
        self.Volume_label.setText(_translate("MainWindow", "Volume:"))
        self.Start_pushButton.setText(_translate("MainWindow", "Playing"))
        #self.Pause_pushButton.setText(_translate("MainWindow", "Pause"))
        #self.checkBox.setText(_translate("MainWindow", "Spectrogram "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Emphasizer"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Playing from C3 - B3"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Playing from C4 - B4"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Playing from C5 - B5"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Playing from C6 - B6"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Playing from C7 - B7"))
        self.pushButton_Ride.setText(_translate("MainWindow", "Ride"))
        self.pushButton_Hi.setText(_translate("MainWindow", "Tom"))
        self.pushButton_Crash.setText(_translate("MainWindow", "Crash"))
        self.pushButton_Base.setText(_translate("MainWindow", "Bass"))
        self.pushButton_Snare.setText(_translate("MainWindow", "Snare"))
        self.pushButton_FloorTom.setText(_translate("MainWindow", "MedTom"))
        self.pushButton_HiTom.setText(_translate("MainWindow", "Hat"))
        self.pushButton_chord_0.setText(_translate("MainWindow", "C"))
        self.pushButton_chord_1.setText(_translate("MainWindow", "D"))
        self.pushButton_chord_2.setText(_translate("MainWindow", "E"))
        self.pushButton_chord_3.setText(_translate("MainWindow", "F"))
        self.pushButton_chord_4.setText(_translate("MainWindow", "G"))
        self.pushButton_chord_5.setText(_translate("MainWindow", "A"))
        self.pushButton_chord_6.setText(_translate("MainWindow", " B"))
        self.pushButton_chord_7.setText(_translate("MainWindow", "C_2"))
        self.pushButtonPianoleft1.setText(_translate("MainWindow", ""))
        self.pushButtonPianoleft2.setText(_translate("MainWindow", "C_2"))
        self.pushButtonPianoleft3.setText(_translate("MainWindow", "C_3"))
        self.pushButtonPianoleft4.setText(_translate("MainWindow", "C_4"))
        self.pushButtonPianoleft5.setText(_translate("MainWindow", "C_5"))
        self.pushButtonPianoleft6.setText(_translate("MainWindow", "C_6"))
        self.pushButtonPianoleft7.setText(_translate("MainWindow", "C_7"))
        self.pushButtonPianoleftblack1.setText(_translate("MainWindow", "B_1"))
        self.pushButtonPianoleftblack2.setText(_translate("MainWindow", "B_2"))
        self.pushButtonPianoleftblack3.setText(_translate("MainWindow", "B_3"))
        self.pushButtonPianoleftblack4.setText(_translate("MainWindow", "B_4"))
        self.pushButtonPianoleftblack5.setText(_translate("MainWindow", "B_5"))
        self.label.setText(_translate("MainWindow", "loops"))
        self.looplineedit.setText(_translate("MainWindow","0"))#
        self.labelofVolXylophone.setText(_translate("MainWindow","Volume"))##
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Virtual Instruments"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())