# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scripting_v1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Scripting_UI(object):
    def setupUi(self, Scripting_UI):
        Scripting_UI.setObjectName("Scripting_UI")
        Scripting_UI.resize(623, 502)
        self.label = QtWidgets.QLabel(Scripting_UI)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Scripting_UI)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 601, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.add_action = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_action.setObjectName("add_action")
        self.gridLayout.addWidget(self.add_action, 5, 0, 1, 5)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.name_entry = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.name_entry.setText("")
        self.name_entry.setObjectName("name_entry")
        self.gridLayout.addWidget(self.name_entry, 0, 1, 1, 1)
        self.additional_entry = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.additional_entry.setObjectName("additional_entry")
        self.gridLayout.addWidget(self.additional_entry, 4, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.action_entry = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.action_entry.setCurrentText("")
        self.action_entry.setObjectName("action_entry")
        self.action_entry.addItem("")
        self.action_entry.addItem("")
        self.action_entry.addItem("")
        self.action_entry.addItem("")
        self.gridLayout.addWidget(self.action_entry, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.select_script = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.select_script.setObjectName("select_script")
        self.gridLayout.addWidget(self.select_script, 1, 0, 1, 5)
        self.trigger_entry = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.trigger_entry.setText("")
        self.trigger_entry.setObjectName("trigger_entry")
        self.gridLayout.addWidget(self.trigger_entry, 2, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 3, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.textEdit = QtWidgets.QTextEdit(Scripting_UI)
        self.textEdit.setGeometry(QtCore.QRect(10, 310, 601, 181))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Scripting_UI)
        self.action_entry.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Scripting_UI)

    def retranslateUi(self, Scripting_UI):
        _translate = QtCore.QCoreApplication.translate
        Scripting_UI.setWindowTitle(_translate("Scripting_UI", "Scripting"))
        self.label.setText(_translate("Scripting_UI", "Scripting"))
        self.add_action.setText(_translate("Scripting_UI", "Add action"))
        self.label_3.setText(_translate("Scripting_UI", "Action type:"))
        self.name_entry.setPlaceholderText(_translate("Scripting_UI", "Name of the script"))
        self.additional_entry.setPlaceholderText(_translate("Scripting_UI", "See below"))
        self.label_2.setText(_translate("Scripting_UI", "Trigger:"))
        self.action_entry.setItemText(0, _translate("Scripting_UI", "Response"))
        self.action_entry.setItemText(1, _translate("Scripting_UI", "Format"))
        self.action_entry.setItemText(2, _translate("Scripting_UI", "HTML Request"))
        self.action_entry.setItemText(3, _translate("Scripting_UI", "JSON Request"))
        self.label_5.setText(_translate("Scripting_UI", "Additional:"))
        self.label_4.setText(_translate("Scripting_UI", "Name:"))
        self.select_script.setText(_translate("Scripting_UI", "Select script"))
        self.trigger_entry.setPlaceholderText(_translate("Scripting_UI", "Trigger phrase"))
        self.label_6.setText(_translate("Scripting_UI", "(Use if script is new, or to overwrite the old one)"))
        self.textEdit.setHtml(_translate("Scripting_UI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Additional Information:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Response: </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    text response</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Format: </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    regex pattern</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">HTML/JSON request: </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    url (either fully-qualified url or \'use input\')</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    </span></p></body></html>"))
