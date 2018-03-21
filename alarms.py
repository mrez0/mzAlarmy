# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alarms.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SetAlarms(object):
    def setupUi(self, SetAlarms):
        SetAlarms.setObjectName("SetAlarms")
        SetAlarms.resize(625, 430)
        self.gridLayout = QtWidgets.QGridLayout(SetAlarms)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.timeEdit = QtWidgets.QTimeEdit(SetAlarms)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.timeEdit.setFont(font)
        self.timeEdit.setObjectName("timeEdit")
        self.horizontalLayout.addWidget(self.timeEdit)
        self.add_button = QtWidgets.QPushButton(SetAlarms)
        self.add_button.setObjectName("add_button")
        self.horizontalLayout.addWidget(self.add_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.remove_button = QtWidgets.QPushButton(SetAlarms)
        self.remove_button.setEnabled(False)
        self.remove_button.setObjectName("remove_button")
        self.horizontalLayout.addWidget(self.remove_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.alarms_list = QtWidgets.QListWidget(SetAlarms)
        self.alarms_list.setObjectName("alarms_list")
        self.verticalLayout.addWidget(self.alarms_list)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.close_button = QtWidgets.QPushButton(SetAlarms)
        self.close_button.setObjectName("close_button")
        self.horizontalLayout_2.addWidget(self.close_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(SetAlarms)
        QtCore.QMetaObject.connectSlotsByName(SetAlarms)
        SetAlarms.setTabOrder(self.timeEdit, self.add_button)
        SetAlarms.setTabOrder(self.add_button, self.close_button)
        SetAlarms.setTabOrder(self.close_button, self.remove_button)
        SetAlarms.setTabOrder(self.remove_button, self.alarms_list)

    def retranslateUi(self, SetAlarms):
        _translate = QtCore.QCoreApplication.translate
        SetAlarms.setWindowTitle(_translate("SetAlarms", "Set Alarms"))
        self.timeEdit.setDisplayFormat(_translate("SetAlarms", "hh:mm"))
        self.add_button.setText(_translate("SetAlarms", "Add"))
        self.remove_button.setText(_translate("SetAlarms", "Remove"))
        self.close_button.setText(_translate("SetAlarms", "Close"))

