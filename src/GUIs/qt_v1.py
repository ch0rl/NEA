# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/GUIs/qt_v1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(722, 389)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 721, 31))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.welcome_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.welcome_label.setObjectName("welcome_label")
        self.gridLayout.addWidget(self.welcome_label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 40, 171, 291))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.text_entry = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.text_entry.setAlignment(QtCore.Qt.AlignCenter)
        self.text_entry.setObjectName("text_entry")
        self.gridLayout_2.addWidget(self.text_entry, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.enter_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.enter_button.setObjectName("enter_button")
        self.gridLayout_2.addWidget(self.enter_button, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(190, 40, 521, 291))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.gridLayoutWidget_3)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 517, 287))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.output_text = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.output_text.setGeometry(QtCore.QRect(0, 0, 521, 291))
        self.output_text.setObjectName("output_text")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 722, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NEA"))
        self.welcome_label.setText(_translate("MainWindow", "Welcome message"))
        self.text_entry.setPlaceholderText(_translate("MainWindow", "Type here"))
        self.enter_button.setText(_translate("MainWindow", "Enter"))
