# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\qdesigner/Dlogin.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(342, 465)
        Dialog.setMaximumSize(QtCore.QSize(342, 465))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/instagramapp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 321, 431))
        self.widget.setStyleSheet("QWidget#widget\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.widget.setObjectName("widget")
        self.logo = QtWidgets.QLabel(self.widget)
        self.logo.setGeometry(QtCore.QRect(60, 63, 211, 71))
        self.logo.setStyleSheet("")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/image/instagramlogobig.PNG"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.linedit_id = QtWidgets.QLineEdit(self.widget)
        self.linedit_id.setGeometry(QtCore.QRect(30, 150, 261, 34))
        self.linedit_id.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border: 1px solid rgb(180, 180, 180);")
        self.linedit_id.setInputMethodHints(QtCore.Qt.ImhNone)
        self.linedit_id.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.linedit_id.setClearButtonEnabled(True)
        self.linedit_id.setObjectName("linedit_id")
        self.linedit_pw = QtWidgets.QLineEdit(self.widget)
        self.linedit_pw.setGeometry(QtCore.QRect(30, 192, 261, 34))
        self.linedit_pw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linedit_pw.setObjectName("linedit_pw")
        self.btn_login = QtWidgets.QPushButton(self.widget)
        self.btn_login.setGeometry(QtCore.QRect(30, 240, 261, 31))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        font.setPointSize(11)
        self.btn_login.setFont(font)
        self.btn_login.setAutoFillBackground(False)
        self.btn_login.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(44, 143, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 0px solid red;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgba(44, 143, 255, 200);\n"
"}")
        self.btn_login.setObjectName("btn_login")
        self.chk_autologin = QtWidgets.QCheckBox(self.widget)
        self.chk_autologin.setGeometry(QtCore.QRect(90, 321, 191, 26))
        self.chk_autologin.setObjectName("chk_autologin")
        self.lbl_errormsg = QtWidgets.QLabel(self.widget)
        self.lbl_errormsg.setGeometry(QtCore.QRect(30, 276, 261, 37))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        self.lbl_errormsg.setFont(font)
        self.lbl_errormsg.setStyleSheet("color: rgb(255, 0, 0);")
        self.lbl_errormsg.setText("")
        self.lbl_errormsg.setWordWrap(True)
        self.lbl_errormsg.setObjectName("lbl_errormsg")
        self.lbl_version = QtWidgets.QLabel(self.widget)
        self.lbl_version.setGeometry(QtCore.QRect(217, 403, 101, 21))
        self.lbl_version.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_version.setObjectName("lbl_version")
        self.lbl_version_2 = QtWidgets.QLabel(Dialog)
        self.lbl_version_2.setGeometry(QtCore.QRect(50, 440, 241, 21))
        self.lbl_version_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_version_2.setObjectName("lbl_version_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.linedit_id.setToolTip(_translate("Dialog", "<html><head/><body><p>인스타그램 아이디를 입력해 주세요.</p></body></html>"))
        self.linedit_id.setWhatsThis(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.linedit_id.setPlaceholderText(_translate("Dialog", "인스타그램 계정 아이디"))
        self.linedit_pw.setPlaceholderText(_translate("Dialog", "비밀번호 "))
        self.btn_login.setText(_translate("Dialog", "로그인"))
        self.chk_autologin.setText(_translate("Dialog", "아이디 && 비밀번호 저장"))
        self.lbl_version.setText(_translate("Dialog", "version_1.6"))
        self.lbl_version_2.setText(_translate("Dialog", "ⓒ Theinsta corp. All Right Reserved."))

import instabackground_rc
