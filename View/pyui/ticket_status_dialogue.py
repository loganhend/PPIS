# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ticket_status_dialogue.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QToolTip, QMessageBox, QLabel, QWidget, QDialog)

class Ui_Dialog2(QDialog, object):
    def __init__(self, c, m):
        super().__init__()
        self.model = m
        self.controller = c

        self.setObjectName("Dialog")
        self.resize(400, 300)
        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.groupBox_2.setMinimumSize(QtCore.QSize(400, 300))
        self.groupBox_2.setMaximumSize(QtCore.QSize(400, 300))
        self.groupBox_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border: 5px solid;\n"
                                      "border-color: #FE938C;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 11, 381, 281))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setMinimumSize(QtCore.QSize(170, 40))
        self.label_14.setMaximumSize(QtCore.QSize(170, 16777215))
        self.label_14.setStyleSheet("font: 12pt \"Stencil\";\n"
                                    "color:  rgb(5, 102, 141);\n"
                                    "border: 0px;")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_6.addWidget(self.label_14)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem2)
        self.sendReviewButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.sendReviewButton_3.setMinimumSize(QtCore.QSize(100, 40))
        self.sendReviewButton_3.setStyleSheet("background-color: rgb(254, 147, 140);\n"
                                              "font: 15pt  \"Stencil\";\n"
                                              "color: white;")
        self.sendReviewButton_3.setObjectName("sendReviewButton_3")
        self.horizontalLayout_11.addWidget(self.sendReviewButton_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.sendReviewButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.sendReviewButton_2.setMinimumSize(QtCore.QSize(100, 40))
        self.sendReviewButton_2.setStyleSheet("background-color: rgb(254, 147, 140);\n"
                                              "font: 15pt  \"Stencil\";\n"
                                              "color: white;")
        self.sendReviewButton_2.setObjectName("sendReviewButton_2")
        self.horizontalLayout_10.addWidget(self.sendReviewButton_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_14.setText(_translate("Dialog", "SPECIFY NEW STATUS"))
        self.sendReviewButton_3.setText(_translate("Dialog", "INACTIVE"))
        self.sendReviewButton_2.setText(_translate("Dialog", "ACTIVE"))