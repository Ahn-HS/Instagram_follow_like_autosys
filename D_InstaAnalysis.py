# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\qdesigner/DInstaAnalysis.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 700)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(580, 80, 208, 307))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabBar::tab\n"
"{ \n"
"height: 35px; width: 103px;\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"color: rgb(255, 116, 151)\n"
"}")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.listwgt_daynpost = QtWidgets.QListWidget(self.tab1)
        self.listwgt_daynpost.setGeometry(QtCore.QRect(0, 0, 201, 266))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        font.setPointSize(12)
        self.listwgt_daynpost.setFont(font)
        self.listwgt_daynpost.setStyleSheet("QTabBar::tab1:selected,  QTabBar::tab1:hover\n"
"{\n"
"color: rgb(255, 187, 254);\n"
"}")
        self.listwgt_daynpost.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listwgt_daynpost.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listwgt_daynpost.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listwgt_daynpost.setObjectName("listwgt_daynpost")
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.listWidget = QtWidgets.QListWidget(self.tab2)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 201, 266))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        self.listWidget.setFont(font)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listWidget.setObjectName("listWidget")
        self.tabWidget.addTab(self.tab2, "")
        self.listwgt_topuser = QtWidgets.QListWidget(Form)
        self.listwgt_topuser.setGeometry(QtCore.QRect(530, 400, 256, 281))
        self.listwgt_topuser.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listwgt_topuser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listwgt_topuser.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.listwgt_topuser.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listwgt_topuser.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listwgt_topuser.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listwgt_topuser.setObjectName("listwgt_topuser")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.listwgt_topuser.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled)
        self.listwgt_topuser.addItem(item)
        self.listwgt_toppost = QtWidgets.QListWidget(Form)
        self.listwgt_toppost.setGeometry(QtCore.QRect(10, 400, 501, 211))
        self.listwgt_toppost.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listwgt_toppost.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listwgt_toppost.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listwgt_toppost.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listwgt_toppost.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listwgt_toppost.setFlow(QtWidgets.QListView.LeftToRight)
        self.listwgt_toppost.setProperty("isWrapping", False)
        self.listwgt_toppost.setViewMode(QtWidgets.QListView.IconMode)
        self.listwgt_toppost.setObjectName("listwgt_toppost")
        self.btn_loaddata = QtWidgets.QPushButton(Form)
        self.btn_loaddata.setGeometry(QtCore.QRect(580, 10, 206, 51))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        font.setPointSize(10)
        self.btn_loaddata.setFont(font)
        self.btn_loaddata.setStyleSheet("QPushButton:pressed\n"
"{\n"
"color: rgb(255, 116, 151);\n"
"\n"
"}")
        self.btn_loaddata.setObjectName("btn_loaddata")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 380, 171, 16))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lbl_test = QtWidgets.QLabel(Form)
        self.lbl_test.setGeometry(QtCore.QRect(360, 100, 201, 271))
        self.lbl_test.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_test.setText("")
        self.lbl_test.setObjectName("lbl_test")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("Form", "게시물"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("Form", "날짜"))
        __sortingEnabled = self.listwgt_topuser.isSortingEnabled()
        self.listwgt_topuser.setSortingEnabled(False)
        item = self.listwgt_topuser.item(0)
        item.setText(_translate("Form", "새 항목"))
        item = self.listwgt_topuser.item(1)
        item.setText(_translate("Form", "새 항목"))
        self.listwgt_topuser.setSortingEnabled(__sortingEnabled)
        self.btn_loaddata.setText(_translate("Form", "현재 계정 정보 불러오기"))
        self.label.setText(_translate("Form", "Top 10"))

