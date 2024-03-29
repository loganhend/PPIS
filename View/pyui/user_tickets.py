# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User_tickets.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QToolTip, QMessageBox, QLabel, QWidget)

class Ui_UserTicketsScreen(QMainWindow, object):
    def __init__(self, c, m):
        super().__init__()
        self.model = m
        self.controller = c

        UserTicketsScreen = QWidget()
        self.setObjectName("UserTicketsScreen")
        self.resize(500, 800)
        self.setStyleSheet("background-color: rgb(167, 191, 238);")

        self.centralwidget = QtWidgets.QWidget(UserTicketsScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 1, 503, 796))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 50)
        self.verticalLayout_5.setSpacing(30)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
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
        self.back_top_but.clicked.connect(lambda: self.controller.showPersonalScreen())

        self.top_layout.addWidget(self.back_top_but)
        self.top_my_tickets_label = QtWidgets.QLabel(self.layoutWidget)
        self.top_my_tickets_label.setMinimumSize(QtCore.QSize(331, 60))
        self.top_my_tickets_label.setMaximumSize(QtCore.QSize(331, 60))
        self.top_my_tickets_label.setStyleSheet("background-color: rgb(5, 102, 141);\n"
                                                "font: 35pt \"Stencil\";\n"
                                                "color: white;")
        self.top_my_tickets_label.setObjectName("top_my_tickets_label")
        self.top_layout.addWidget(self.top_my_tickets_label)
        self.verticalLayout_5.addLayout(self.top_layout)
        self.central_tickets_layout = QtWidgets.QVBoxLayout()
        self.central_tickets_layout.setContentsMargins(15, -1, 15, -1)
        self.central_tickets_layout.setSpacing(20)
        self.central_tickets_layout.setObjectName("central_tickets_layout")
        self.firts_ticket_box = QtWidgets.QGroupBox(self.layoutWidget)
        self.firts_ticket_box.setMinimumSize(QtCore.QSize(470, 160))
        self.firts_ticket_box.setMaximumSize(QtCore.QSize(470, 160))
        self.firts_ticket_box.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "border: 5px solid;\n"
                                            "border-color: #FE938C;")
        self.firts_ticket_box.setTitle("")
        self.firts_ticket_box.setObjectName("firts_ticket_box")
        self.layoutWidget1 = QtWidgets.QWidget(self.firts_ticket_box)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 448, 142))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.first_ticket_name_label = QtWidgets.QLabel(self.layoutWidget1)
        self.first_ticket_name_label.setMinimumSize(QtCore.QSize(200, 40))
        self.first_ticket_name_label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.first_ticket_name_label.setStyleSheet("font: 25pt \"Stencil\";\n"
                                                   "color:  rgb(5, 102, 141);\n"
                                                   "border: 0px;")
        self.first_ticket_name_label.setObjectName("first_ticket_name_label")
        self.horizontalLayout_2.addWidget(self.first_ticket_name_label)
        self.first_number_layout = QtWidgets.QHBoxLayout()
        self.first_number_layout.setObjectName("first_number_layout")
        self.first_number_label = QtWidgets.QLabel(self.layoutWidget1)
        self.first_number_label.setMinimumSize(QtCore.QSize(150, 40))
        self.first_number_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.first_number_label.setStyleSheet("font: 25pt \"Stencil\";\n"
                                              "color:  rgb(5, 102, 141);\n"
                                              "border: 0px;")
        self.first_number_label.setObjectName("first_number_label")
        self.first_number_layout.addWidget(self.first_number_label)
        self.first_number_info = QtWidgets.QLabel(self.layoutWidget1)
        self.first_number_info.setMinimumSize(QtCore.QSize(80, 40))
        self.first_number_info.setMaximumSize(QtCore.QSize(80, 16777215))
        self.first_number_info.setStyleSheet("font: 25pt \"Stencil\";\n"
                                             "color:  rgb(5, 102, 141);\n"
                                             "border: 0px;")
        self.first_number_info.setObjectName("first_number_info")
        self.first_number_layout.addWidget(self.first_number_info)
        self.horizontalLayout_2.addLayout(self.first_number_layout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.first_date_layout = QtWidgets.QHBoxLayout()
        self.first_date_layout.setObjectName("first_date_layout")
        self.first_date_info = QtWidgets.QLabel(self.layoutWidget1)
        self.first_date_info.setMinimumSize(QtCore.QSize(150, 40))
        self.first_date_info.setMaximumSize(QtCore.QSize(250, 16777215))
        self.first_date_info.setStyleSheet("font: 10pt \"Stencil\";\n"
                                           "color:  #00A676;\n"
                                           "border: 0px;")
        self.first_date_info.setObjectName("first_date_info")
        self.first_date_layout.addWidget(self.first_date_info)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.first_date_layout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.first_date_layout)
        self.first_buttons_layout = QtWidgets.QHBoxLayout()
        self.first_buttons_layout.setObjectName("first_buttons_layout")
        self.first_change_date_but = QtWidgets.QPushButton(self.layoutWidget1)
        self.first_change_date_but.setMinimumSize(QtCore.QSize(100, 40))
        self.first_change_date_but.setStyleSheet("background-color: rgb(254, 147, 140);\n"
                                                 "font: 15pt  \"Stencil\";\n"
                                                 "color: white;")
        self.first_change_date_but.setObjectName("first_change_date_but")
        self.first_buttons_layout.addWidget(self.first_change_date_but)
        self.first_return_but = QtWidgets.QPushButton(self.layoutWidget1)
        self.first_return_but.setMinimumSize(QtCore.QSize(100, 40))
        self.first_return_but.setStyleSheet("background-color: rgb(254, 147, 140);\n"
                                            "font: 15pt  \"Stencil\";\n"
                                            "color: white;")
        self.first_return_but.setObjectName("first_return_but")
        self.first_buttons_layout.addWidget(self.first_return_but)
        self.first_show_qr_but = QtWidgets.QPushButton(self.layoutWidget1)
        self.first_show_qr_but.setMinimumSize(QtCore.QSize(100, 40))
        self.first_show_qr_but.setStyleSheet("background-color: rgb(254, 147, 140);\n"
                                             "font: 15pt  \"Stencil\";\n"
                                             "color: white;")
        self.first_show_qr_but.setObjectName("first_show_qr_but")
        self.first_buttons_layout.addWidget(self.first_show_qr_but)
        self.verticalLayout.addLayout(self.first_buttons_layout)
        self.central_tickets_layout.addWidget(self.firts_ticket_box)
        self.second_ticket_box = QtWidgets.QGroupBox(self.layoutWidget)
        self.second_ticket_box.setMinimumSize(QtCore.QSize(470, 160))
        self.second_ticket_box.setMaximumSize(QtCore.QSize(470, 160))
        self.second_ticket_box.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "border: 5px solid;\n"
                                             "border-color: #FE938C;")
        self.second_ticket_box.setTitle("")
        self.second_ticket_box.setObjectName("second_ticket_box")
        self.layoutWidget2 = QtWidgets.QWidget(self.second_ticket_box)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 10, 448, 142))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.second_ticket_name_label = QtWidgets.QLabel(self.layoutWidget2)
        self.second_ticket_name_label.setMinimumSize(QtCore.QSize(200, 40))
        self.second_ticket_name_label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.second_ticket_name_label.setStyleSheet("font: 25pt \"Stencil\";\n"
                                                    "color:  rgb(5, 102, 141);\n"
                                                    "border: 0px;")
        self.second_ticket_name_label.setObjectName("second_ticket_name_label")
        self.horizontalLayout_5.addWidget(self.second_ticket_name_label)
        self.second_number_layout = QtWidgets.QHBoxLayout()
        self.second_number_layout.setObjectName("second_number_layout")
        self.second_number_label = QtWidgets.QLabel(self.layoutWidget2)
        self.second_number_label.setMinimumSize(QtCore.QSize(150, 40))
        self.second_number_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.second_number_label.setStyleSheet("font: 25pt \"Stencil\";\n"
                                               "color:  rgb(5, 102, 141);\n"
                                               "border: 0px;")
        self.second_number_label.setObjectName("second_number_label")
        self.second_number_layout.addWidget(self.second_number_label)
        self.second_number_info = QtWidgets.QLabel(self.layoutWidget2)
        self.second_number_info.setMinimumSize(QtCore.QSize(80, 40))
        self.second_number_info.setMaximumSize(QtCore.QSize(80, 16777215))
        self.second_number_info.setStyleSheet("font: 25pt \"Stencil\";\n"
                                              "color:  rgb(5, 102, 141);\n"
                                              "border: 0px;")
        self.second_number_info.setObjectName("second_number_info")
        self.second_number_layout.addWidget(self.second_number_info)
        self.horizontalLayout_5.addLayout(self.second_number_layout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.second_date_layout = QtWidgets.QHBoxLayout()
        self.second_date_layout.setObjectName("second_date_layout")
        self.second__date_info = QtWidgets.QLabel(self.layoutWidget2)
        self.second__date_info.setMinimumSize(QtCore.QSize(150, 40))
        self.second__date_info.setMaximumSize(QtCore.QSize(250, 16777215))
        self.second__date_info.setStyleSheet("font: 10pt \"Stencil\";\n"
                                             "color:  #00A676;\n"
                                             "border: 0px;")
        self.second__date_info.setObjectName("second__date_info")
        self.second_date_layout.addWidget(self.second__date_info)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.second_date_layout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.second_date_layout)
        self.second_buttons_layout = QtWidgets.QHBoxLayout()
        self.second_buttons_layout.setObjectName("second_buttons_layout")
        self.second_change_date_but = QtWidgets.QPushButton(self.layoutWidget2)
        self.second_change_date_but.setMinimumSize(QtCore.QSize(100, 40))
        self.second_change_date_but.setStyleSheet("background-color: rgb(254, 147, 140);\n"
                                                  "font: 15pt  \"Stencil\";\n"
                                                  "color: white;")
        self.second_change_date_but.setObjectName("second_change_date_but")
        self.second_buttons_layout.addWidget(self.second_change_date_but)
        self.second_return_but = QtWidgets.QPushButton(self.layoutWidget2)
        self.second_return_but.setMinimumSize(QtCore.QSize(100, 40))
        self.second_return_but.setStyleSheet("background-color: rgb(254, 147, 140);\n"
                                             "font: 15pt  \"Stencil\";\n"
                                             "color: white;")
        self.second_return_but.setObjectName("second_return_but")
        self.second_buttons_layout.addWidget(self.second_return_but)
        self.second__show_qr_but = QtWidgets.QPushButton(self.layoutWidget2)
        self.second__show_qr_but.setMinimumSize(QtCore.QSize(100, 40))
        self.second__show_qr_but.setStyleSheet("background-color: rgb(254, 147, 140);\n"
                                               "font: 15pt  \"Stencil\";\n"
                                               "color: white;")
        self.second__show_qr_but.setObjectName("second__show_qr_but")
        self.second_buttons_layout.addWidget(self.second__show_qr_but)
        self.verticalLayout_2.addLayout(self.second_buttons_layout)
        self.central_tickets_layout.addWidget(self.second_ticket_box)
        self.third_ticket_box = QtWidgets.QGroupBox(self.layoutWidget)
        self.third_ticket_box.setMinimumSize(QtCore.QSize(470, 160))
        self.third_ticket_box.setMaximumSize(QtCore.QSize(470, 160))
        self.third_ticket_box.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "border: 5px solid;\n"
                                            "border-color: #FE938C;")
        self.third_ticket_box.setTitle("")
        self.third_ticket_box.setObjectName("third_ticket_box")
        self.layoutWidget_3 = QtWidgets.QWidget(self.third_ticket_box)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 10, 448, 142))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.third_ticket_name_label = QtWidgets.QLabel(self.layoutWidget_3)
        self.third_ticket_name_label.setMinimumSize(QtCore.QSize(200, 40))
        self.third_ticket_name_label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.third_ticket_name_label.setStyleSheet("font: 25pt \"Stencil\";\n"
                                                   "color:  rgb(5, 102, 141);\n"
                                                   "border: 0px;")
        self.third_ticket_name_label.setObjectName("third_ticket_name_label")
        self.horizontalLayout_10.addWidget(self.third_ticket_name_label)
        self.third_number_layout = QtWidgets.QHBoxLayout()
        self.third_number_layout.setObjectName("third_number_layout")
        self.third_number_label = QtWidgets.QLabel(self.layoutWidget_3)
        self.third_number_label.setMinimumSize(QtCore.QSize(150, 40))
        self.third_number_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.third_number_label.setStyleSheet("font: 25pt \"Stencil\";\n"
                                              "color:  rgb(5, 102, 141);\n"
                                              "border: 0px;")
        self.third_number_label.setObjectName("third_number_label")
        self.third_number_layout.addWidget(self.third_number_label)
        self.third_number_info = QtWidgets.QLabel(self.layoutWidget_3)
        self.third_number_info.setMinimumSize(QtCore.QSize(80, 40))
        self.third_number_info.setMaximumSize(QtCore.QSize(80, 16777215))
        self.third_number_info.setStyleSheet("font: 25pt \"Stencil\";\n"
                                             "color:  rgb(5, 102, 141);\n"
                                             "border: 0px;")
        self.third_number_info.setObjectName("third_number_info")
        self.third_number_layout.addWidget(self.third_number_info)
        self.horizontalLayout_10.addLayout(self.third_number_layout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.third_date_layout = QtWidgets.QHBoxLayout()
        self.third_date_layout.setObjectName("third_date_layout")
        self.third_date_info = QtWidgets.QLabel(self.layoutWidget_3)
        self.third_date_info.setMinimumSize(QtCore.QSize(150, 40))
        self.third_date_info.setMaximumSize(QtCore.QSize(250, 16777215))
        self.third_date_info.setStyleSheet("font: 10pt \"Stencil\";\n"
                                           "color:  #00A676;\n"
                                           "border: 0px;")
        self.third_date_info.setObjectName("third_date_info")
        self.third_date_layout.addWidget(self.third_date_info)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.third_date_layout.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.third_date_layout)
        self.third_buttons_layout = QtWidgets.QHBoxLayout()
        self.third_buttons_layout.setObjectName("third_buttons_layout")
        self.third_change_date_but = QtWidgets.QPushButton(self.layoutWidget_3)
        self.third_change_date_but.setMinimumSize(QtCore.QSize(100, 40))
        self.third_change_date_but.setStyleSheet("background-color: rgb(254, 147, 140);\n"
                                                 "font: 15pt  \"Stencil\";\n"
                                                 "color: white;")
        self.third_change_date_but.setObjectName("third_change_date_but")
        self.third_buttons_layout.addWidget(self.third_change_date_but)
        self.third_return_but = QtWidgets.QPushButton(self.layoutWidget_3)
        self.third_return_but.setMinimumSize(QtCore.QSize(100, 40))
        self.third_return_but.setStyleSheet("background-color: rgb(254, 147, 140);\n"
                                            "font: 15pt  \"Stencil\";\n"
                                            "color: white;")
        self.third_return_but.setObjectName("third_return_but")
        self.third_buttons_layout.addWidget(self.third_return_but)
        self.third__show_qr_but = QtWidgets.QPushButton(self.layoutWidget_3)
        self.third__show_qr_but.setMinimumSize(QtCore.QSize(100, 40))
        self.third__show_qr_but.setStyleSheet("background-color: rgb(254, 147, 140);\n"
                                              "font: 15pt  \"Stencil\";\n"
                                              "color: white;")
        self.third__show_qr_but.setObjectName("third__show_qr_but")
        self.third_buttons_layout.addWidget(self.third__show_qr_but)
        self.verticalLayout_3.addLayout(self.third_buttons_layout)
        self.central_tickets_layout.addWidget(self.third_ticket_box)
        self.verticalLayout_5.addLayout(self.central_tickets_layout)
        self.bottom_layout = QtWidgets.QHBoxLayout()
        self.bottom_layout.setObjectName("bottom_layout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottom_layout.addItem(spacerItem3)
        self.buy_tickets_but = QtWidgets.QPushButton(self.layoutWidget)
        self.buy_tickets_but.setMinimumSize(QtCore.QSize(250, 80))
        self.buy_tickets_but.setMaximumSize(QtCore.QSize(250, 80))
        self.buy_tickets_but.setStyleSheet("background-color:#FFB627;\n"
                                           "font: 20pt  \"Stencil\";\n"
                                           "color: white;")
        self.buy_tickets_but.setObjectName("buy_tickets_but")
        self.buy_tickets_but.clicked.connect(lambda: self.controller.showBuyingTicketsScreen())

        self.bottom_layout.addWidget(self.buy_tickets_but)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottom_layout.addItem(spacerItem4)
        self.verticalLayout_5.addLayout(self.bottom_layout)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(UserTicketsScreen)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("UserTicketsScreen", "WaterWorld"))
        self.back_top_but.setText(_translate("UserTicketsScreen", "< BACK"))
        self.top_my_tickets_label.setText(_translate("UserTicketsScreen", "MY TICKETS"))
        self.first_ticket_name_label.setText(_translate("UserTicketsScreen", "TEXT"))
        self.first_number_label.setText(_translate("UserTicketsScreen", "Number:"))
        self.first_number_info.setText(_translate("UserTicketsScreen", "TEXT"))
        self.first_date_info.setText(_translate("UserTicketsScreen", "date text"))
        self.first_change_date_but.setText(_translate("UserTicketsScreen", "CHANGE DATE"))
        self.first_return_but.setText(_translate("UserTicketsScreen", "RETURN"))
        self.first_show_qr_but.setText(_translate("UserTicketsScreen", "SHOW QR"))
        self.second_ticket_name_label.setText(_translate("UserTicketsScreen", "TEXT"))
        self.second_number_label.setText(_translate("UserTicketsScreen", "Number:"))
        self.second_number_info.setText(_translate("UserTicketsScreen", "TEXT"))
        self.second__date_info.setText(_translate("UserTicketsScreen", "date text"))
        self.second_change_date_but.setText(_translate("UserTicketsScreen", "CHANGE DATE"))
        self.second_return_but.setText(_translate("UserTicketsScreen", "RETURN"))
        self.second__show_qr_but.setText(_translate("UserTicketsScreen", "SHOW QR"))
        self.third_ticket_name_label.setText(_translate("UserTicketsScreen", "TEXT"))
        self.third_number_label.setText(_translate("UserTicketsScreen", "Number:"))
        self.third_number_info.setText(_translate("UserTicketsScreen", "TEXT"))
        self.third_date_info.setText(_translate("UserTicketsScreen", "date text"))
        self.third_change_date_but.setText(_translate("UserTicketsScreen", "CHANGE DATE"))
        self.third_return_but.setText(_translate("UserTicketsScreen", "RETURN"))
        self.third__show_qr_but.setText(_translate("UserTicketsScreen", "SHOW QR"))
        self.buy_tickets_but.setText(_translate("UserTicketsScreen", "BUY TICKETS"))

