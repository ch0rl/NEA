# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\GUIs\settings_v1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings_win(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(482, 271)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 461, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.text_entry = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.text_entry.setObjectName("text_entry")
        self.verticalLayout.addWidget(self.text_entry)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.welc_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.welc_button.setObjectName("welc_button")
        self.horizontalLayout.addWidget(self.welc_button)
        self.no_ans_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.no_ans_button.setObjectName("no_ans_button")
        self.horizontalLayout.addWidget(self.no_ans_button)
        self.trans_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.trans_button.setObjectName("trans_button")
        self.horizontalLayout.addWidget(self.trans_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.help = QtWidgets.QTextEdit(Form)
        self.help.setGeometry(QtCore.QRect(10, 140, 461, 121))
        self.help.setReadOnly(True)
        self.help.setObjectName("help")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Settings"))
        self.label.setText(_translate("Form", "Add to lists:"))
        self.text_entry.setPlaceholderText(_translate("Form", "Type here..."))
        self.welc_button.setText(_translate("Form", "Welcome Message"))
        self.no_ans_button.setText(_translate("Form", "No Answer Message"))
        self.trans_button.setText(_translate("Form", "Translation"))
        self.help.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">Help</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Welcome Message: A message to be shown on startup</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">No Answer Message: A message to be shown when no answer can be found</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Translation: A translation to make text processing easier (in form old:new)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Program must be restarted for changes to take effect</span></p></body></html>"))
