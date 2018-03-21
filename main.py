# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(673, 294)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("alarm-outline/alarm-outline/32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hrsLabel = QtWidgets.QLCDNumber(self.centralwidget)
        self.hrsLabel.setStyleSheet("color: rgb(255, 255, 0);")
        self.hrsLabel.setDigitCount(2)
        self.hrsLabel.setProperty("value", 0.0)
        self.hrsLabel.setProperty("intValue", 0)
        self.hrsLabel.setObjectName("hrsLabel")
        self.horizontalLayout.addWidget(self.hrsLabel)
        self.minsLabel = QtWidgets.QLCDNumber(self.centralwidget)
        self.minsLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.minsLabel.setDigitCount(2)
        self.minsLabel.setProperty("value", 0.0)
        self.minsLabel.setProperty("intValue", 0)
        self.minsLabel.setObjectName("minsLabel")
        self.horizontalLayout.addWidget(self.minsLabel)
        self.secsLabel = QtWidgets.QLCDNumber(self.centralwidget)
        self.secsLabel.setDigitCount(2)
        self.secsLabel.setProperty("value", 0.0)
        self.secsLabel.setProperty("intValue", 0)
        self.secsLabel.setObjectName("secsLabel")
        self.horizontalLayout.addWidget(self.secsLabel)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 673, 26))
        self.menubar.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(85, 0, 255);\n"
"selection-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(255, 255, 0);")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAlarms = QtWidgets.QMenu(self.menubar)
        self.menuAlarms.setObjectName("menuAlarms")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionSet_Alarms = QtWidgets.QAction(MainWindow)
        self.actionSet_Alarms.setObjectName("actionSet_Alarms")
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuAlarms.addAction(self.actionSet_Alarms)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAlarms.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "mzAlarmy"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAlarms.setTitle(_translate("MainWindow", "Alarms"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSettings.setText(_translate("MainWindow", "Settings..."))
        self.actionSet_Alarms.setText(_translate("MainWindow", "Set Alarms"))

