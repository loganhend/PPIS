# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_park.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QToolTip, QMessageBox, QLabel, QWidget)


class Ui_aboutParkWindow(QMainWindow, object):
    def __init__(self, c, m):
        super().__init__()
        self.model = m
        self.controller = c


        aboutParkWindow = QWidget()
        self.setObjectName("aboutParkWindow")
        self.resize(500, 800)
        self.setStyleSheet("background-color: rgb(167, 191, 238);")

        self.centralwidget = QtWidgets.QWidget(aboutParkWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 503, 791))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.top_layout = QtWidgets.QHBoxLayout()
        self.top_layout.setContentsMargins(10, 20, 10, -1)
        self.top_layout.setSpacing(50)
        self.top_layout.setObjectName("top_layout")
        self.back_top_but = QtWidgets.QPushButton(self.layoutWidget)
        self.back_top_but.setMinimumSize(QtCore.QSize(100, 60))
        self.back_top_but.setMaximumSize(QtCore.QSize(100, 16777215))
        self.back_top_but.setStyleSheet("background-color: #05668D;\n"
                                        "font: 15pt  \"Stencil\";\n"
                                        "color: white;")
        self.back_top_but.setObjectName("back_top_but")
        self.back_top_but.clicked.connect(lambda: self.controller.showMenuScreen())

        self.top_layout.addWidget(self.back_top_but)
        self.top_label = QtWidgets.QLabel(self.layoutWidget)
        self.top_label.setMinimumSize(QtCore.QSize(331, 60))
        self.top_label.setMaximumSize(QtCore.QSize(331, 16777215))
        self.top_label.setStyleSheet("background-color: rgb(5, 102, 141);\n"
                                     "font: 36pt \"Stencil\";\n"
                                     "color: white;")
        self.top_label.setObjectName("top_label")
        self.top_layout.addWidget(self.top_label)
        self.verticalLayout_2.addLayout(self.top_layout)
        self.main_image = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_image.sizePolicy().hasHeightForWidth())
        self.main_image.setSizePolicy(sizePolicy)
        self.main_image.setMinimumSize(QtCore.QSize(500, 350))
        self.main_image.setMaximumSize(QtCore.QSize(500, 350))
        self.main_image.setText("")
        self.main_image.setPixmap(QtGui.QPixmap("View/img/39.png"))
        self.main_image.setObjectName("main_image")
        self.verticalLayout_2.addWidget(self.main_image)
        self.bottom_block_layout = QtWidgets.QVBoxLayout()
        self.bottom_block_layout.setContentsMargins(10, 5, 10, 5)
        self.bottom_block_layout.setSpacing(10)
        self.bottom_block_layout.setObjectName("bottom_block_layout")
        self.location_layout = QtWidgets.QHBoxLayout()
        self.location_layout.setSpacing(10)
        self.location_layout.setObjectName("location_layout")
        self.location_label = QtWidgets.QLabel(self.layoutWidget)
        self.location_label.setMinimumSize(QtCore.QSize(160, 40))
        self.location_label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.location_label.setStyleSheet("background-color: rgb(254, 147, 140);\n"
                                          "font: 20pt  \"Stencil\";\n"
                                          "color: white;\n"
                                          "padding: 10px;")
        self.location_label.setObjectName("location_label")
        self.location_layout.addWidget(self.location_label)
        self.location_info = QtWidgets.QLabel(self.layoutWidget)
        self.location_info.setMinimumSize(QtCore.QSize(280, 40))
        self.location_info.setMaximumSize(QtCore.QSize(16777215, 40))
        self.location_info.setStyleSheet("background-color: rgb(254, 147, 140);\n"
                                         "font: 15pt  \"Stencil\";\n"
                                         "color: white;\n"
                                         "padding: 10px;")
        self.location_info.setObjectName("location_info")
        self.location_layout.addWidget(self.location_info)
        self.bottom_block_layout.addLayout(self.location_layout)
        self.website_layout = QtWidgets.QHBoxLayout()
        self.website_layout.setSpacing(10)
        self.website_layout.setObjectName("website_layout")
        self.website_label = QtWidgets.QLabel(self.layoutWidget)
        self.website_label.setMinimumSize(QtCore.QSize(160, 40))
        self.website_label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.website_label.setStyleSheet("background-color: rgb(254, 147, 140);\n"
                                         "font: 20pt  \"Stencil\";\n"
                                         "color: white;\n"
                                         "padding: 10px;")
        self.website_label.setObjectName("website_label")
        self.website_layout.addWidget(self.website_label)
        self.website_info = QtWidgets.QLabel(self.layoutWidget)
        self.website_info.setMinimumSize(QtCore.QSize(280, 40))
        self.website_info.setMaximumSize(QtCore.QSize(16777215, 40))
        self.website_info.setStyleSheet("background-color: rgb(254, 147, 140);\n"
                                        "font: 15pt  \"Stencil\";\n"
                                        "color: white;\n"
                                        "padding: 10px;")
        self.website_info.setObjectName("website_info")
        self.website_layout.addWidget(self.website_info)
        self.bottom_block_layout.addLayout(self.website_layout)
        self.phone_layout = QtWidgets.QHBoxLayout()
        self.phone_layout.setSpacing(10)
        self.phone_layout.setObjectName("phone_layout")
        self.phone_label = QtWidgets.QLabel(self.layoutWidget)
        self.phone_label.setMinimumSize(QtCore.QSize(160, 40))
        self.phone_label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.phone_label.setStyleSheet("background-color: rgb(254, 147, 140);\n"
                                       "font: 20pt  \"Stencil\";\n"
                                       "color: white;\n"
                                       "padding-left: 25px;")
        self.phone_label.setObjectName("phone_label")
        self.phone_layout.addWidget(self.phone_label)
        self.phone_info = QtWidgets.QLabel(self.layoutWidget)
        self.phone_info.setMinimumSize(QtCore.QSize(280, 40))
        self.phone_info.setMaximumSize(QtCore.QSize(16777215, 40))
        self.phone_info.setStyleSheet("background-color: rgb(254, 147, 140);\n"
                                      "font: 15pt  \"Stencil\";\n"
                                      "color: white;\n"
                                      "padding: 10px;")
        self.phone_info.setObjectName("phone_info")
        self.phone_layout.addWidget(self.phone_info)
        self.bottom_block_layout.addLayout(self.phone_layout)
        self.time_layout = QtWidgets.QHBoxLayout()
        self.time_layout.setSpacing(10)
        self.time_layout.setObjectName("time_layout")
        self.time_label = QtWidgets.QLabel(self.layoutWidget)
        self.time_label.setMinimumSize(QtCore.QSize(160, 40))
        self.time_label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.time_label.setStyleSheet("background-color: rgb(254, 147, 140);\n"
                                      "font: 20pt  \"Stencil\";\n"
                                      "color: white;\n"
                                      "padding-left: 40px;")
        self.time_label.setObjectName("time_label")
        self.time_layout.addWidget(self.time_label)
        self.time_info = QtWidgets.QLabel(self.layoutWidget)
        self.time_info.setMinimumSize(QtCore.QSize(280, 40))
        self.time_info.setMaximumSize(QtCore.QSize(16777215, 40))
        self.time_info.setStyleSheet("background-color: rgb(254, 147, 140);\n"
                                     "font: 15pt  \"Stencil\";\n"
                                     "color: white;\n"
                                     "padding: 10px;")
        self.time_info.setObjectName("time_info")
        self.time_layout.addWidget(self.time_info)
        self.bottom_block_layout.addLayout(self.time_layout)
        self.description_info_label = QtWidgets.QLabel(self.layoutWidget)
        self.description_info_label.setMinimumSize(QtCore.QSize(450, 100))
        self.description_info_label.setStyleSheet("background-color: rgb(254, 147, 140);\n"
                                                  "font: 10pt  \"Stencil\";\n"
                                                  "color: white;\n"
                                                  "padding: 10px;")
        self.description_info_label.setObjectName("description_info_label")
        self.bottom_block_layout.addWidget(self.description_info_label)
        self.verticalLayout_2.addLayout(self.bottom_block_layout)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(aboutParkWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("aboutParkWindow", "WaterWorld"))
        self.back_top_but.setText(_translate("aboutParkWindow", "< BACK"))
        self.top_label.setText(_translate("aboutParkWindow", "WATER WORLD"))
        self.location_label.setText(_translate("aboutParkWindow", "LOCATION"))
        self.location_info.setText(_translate("aboutParkWindow", "text"))
        self.website_label.setText(_translate("aboutParkWindow", "WEB-SITE"))
        self.website_info.setText(_translate("aboutParkWindow", "text"))
        self.phone_label.setText(_translate("aboutParkWindow", "PHONE"))
        self.phone_info.setText(_translate("aboutParkWindow", "text"))
        self.time_label.setText(_translate("aboutParkWindow", "TIME"))
        self.time_info.setText(_translate("aboutParkWindow", "text"))
        self.description_info_label.setText(_translate("aboutParkWindow", "text"))
