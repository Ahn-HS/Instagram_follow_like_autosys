# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\qdesigner/DInstaManagementSys.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1021, 594)
        MainWindow.setMaximumSize(QtCore.QSize(1021, 594))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/instagramapp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow#MainWindow\n"
"{\n"
"border-image: url(:/image/1500x500_hu25.jpg);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupbox_view_workingpost = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox_view_workingpost.setGeometry(QtCore.QRect(720, 29, 281, 511))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupbox_view_workingpost.setFont(font)
        self.groupbox_view_workingpost.setStyleSheet("QGroupBox#groupbox_view_workingpost\n"
"{\n"
"border:1px solid rgb(0, 0, 0);\n"
"}")
        self.groupbox_view_workingpost.setTitle("")
        self.groupbox_view_workingpost.setObjectName("groupbox_view_workingpost")
        self.lbl_picture = QtWidgets.QLabel(self.groupbox_view_workingpost)
        self.lbl_picture.setGeometry(QtCore.QRect(1, 0, 279, 301))
        self.lbl_picture.setText("")
        self.lbl_picture.setObjectName("lbl_picture")
        self.textedit_log = QtWidgets.QTextEdit(self.groupbox_view_workingpost)
        self.textedit_log.setGeometry(QtCore.QRect(0, 310, 281, 201))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(8)
        self.textedit_log.setFont(font)
        self.textedit_log.setStyleSheet("#textedit_log\n"
"{\n"
"border:0.5px solid rgb(141, 141, 141);\n"
"}")
        self.textedit_log.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textedit_log.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textedit_log.setReadOnly(True)
        self.textedit_log.setObjectName("textedit_log")
        self.groupbox_comment = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox_comment.setGeometry(QtCore.QRect(20, 413, 521, 128))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupbox_comment.setFont(font)
        self.groupbox_comment.setStyleSheet("QGroupBox#groupbox_comment\n"
"{\n"
"border:1px solid rgb(0, 0, 0);\n"
"}")
        self.groupbox_comment.setTitle("")
        self.groupbox_comment.setObjectName("groupbox_comment")
        self.btn_manualcomment = QtWidgets.QPushButton(self.groupbox_comment)
        self.btn_manualcomment.setGeometry(QtCore.QRect(450, 80, 61, 41))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        self.btn_manualcomment.setFont(font)
        self.btn_manualcomment.setObjectName("btn_manualcomment")
        self.linedit_comment = QtWidgets.QLineEdit(self.groupbox_comment)
        self.linedit_comment.setGeometry(QtCore.QRect(120, 10, 321, 29))
        self.linedit_comment.setStyleSheet("QLineEdit:focus\n"
"{\n"
"  border: 2px solid red;\n"
"}\n"
"\n"
"")
        self.linedit_comment.setObjectName("linedit_comment")
        self.btn_add_comment = QtWidgets.QPushButton(self.groupbox_comment)
        self.btn_add_comment.setGeometry(QtCore.QRect(450, 10, 61, 31))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        self.btn_add_comment.setFont(font)
        self.btn_add_comment.setObjectName("btn_add_comment")
        self.listwgt_comment_tag = QtWidgets.QListWidget(self.groupbox_comment)
        self.listwgt_comment_tag.setGeometry(QtCore.QRect(10, 10, 101, 111))
        self.listwgt_comment_tag.setStyleSheet("QListWidget#listwgt_comment_tag\n"
"{\n"
"border:0.5px solid rgb(141, 141, 141);\n"
"}")
        self.listwgt_comment_tag.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listwgt_comment_tag.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listwgt_comment_tag.setObjectName("listwgt_comment_tag")
        self.listwgt_commentlist = QtWidgets.QListWidget(self.groupbox_comment)
        self.listwgt_commentlist.setGeometry(QtCore.QRect(120, 50, 321, 71))
        self.listwgt_commentlist.setStyleSheet("QListWidget#listwgt_commentlist\n"
"{\n"
"border:0.5px solid rgb(141, 141, 141);\n"
"}")
        self.listwgt_commentlist.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listwgt_commentlist.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listwgt_commentlist.setObjectName("listwgt_commentlist")
        self.btn_del_comment = QtWidgets.QPushButton(self.groupbox_comment)
        self.btn_del_comment.setGeometry(QtCore.QRect(450, 48, 61, 31))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        self.btn_del_comment.setFont(font)
        self.btn_del_comment.setObjectName("btn_del_comment")
        self.groupbox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox_3.setGeometry(QtCore.QRect(20, 31, 261, 51))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupbox_3.setFont(font)
        self.groupbox_3.setStyleSheet("QGroupBox#groupbox_3\n"
"{\n"
"border:1px solid rgb(0, 0, 0);\n"
"}")
        self.groupbox_3.setTitle("")
        self.groupbox_3.setObjectName("groupbox_3")
        self.chk_follow = QtWidgets.QCheckBox(self.groupbox_3)
        self.chk_follow.setGeometry(QtCore.QRect(27, 18, 71, 16))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        self.chk_follow.setFont(font)
        self.chk_follow.setStyleSheet("")
        self.chk_follow.setChecked(True)
        self.chk_follow.setObjectName("chk_follow")
        self.chk_like = QtWidgets.QCheckBox(self.groupbox_3)
        self.chk_like.setGeometry(QtCore.QRect(107, 18, 71, 16))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        self.chk_like.setFont(font)
        self.chk_like.setChecked(True)
        self.chk_like.setObjectName("chk_like")
        self.chk_comment = QtWidgets.QCheckBox(self.groupbox_3)
        self.chk_comment.setGeometry(QtCore.QRect(187, 18, 61, 16))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        self.chk_comment.setFont(font)
        self.chk_comment.setStyleSheet("")
        self.chk_comment.setIconSize(QtCore.QSize(16, 16))
        self.chk_comment.setChecked(True)
        self.chk_comment.setObjectName("chk_comment")
        self.groupbox_tag_based = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox_tag_based.setGeometry(QtCore.QRect(20, 120, 681, 261))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupbox_tag_based.setFont(font)
        self.groupbox_tag_based.setStyleSheet("QGroupBox#groupbox_tag_based\n"
"{\n"
"border:1px solid rgb(0, 0, 0);\n"
"}")
        self.groupbox_tag_based.setTitle("")
        self.groupbox_tag_based.setFlat(False)
        self.groupbox_tag_based.setObjectName("groupbox_tag_based")
        self.btn_srch_hashtag = QtWidgets.QPushButton(self.groupbox_tag_based)
        self.btn_srch_hashtag.setGeometry(QtCore.QRect(420, 14, 101, 30))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_srch_hashtag.setFont(font)
        self.btn_srch_hashtag.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"  border: 1px solid red;\n"
"background-color: rgba(255, 0, 0,20);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgba(255, 0, 0,80);\n"
"}\n"
"QPushButton\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.btn_srch_hashtag.setDefault(True)
        self.btn_srch_hashtag.setFlat(True)
        self.btn_srch_hashtag.setObjectName("btn_srch_hashtag")
        self.btn_add_tag = QtWidgets.QPushButton(self.groupbox_tag_based)
        self.btn_add_tag.setGeometry(QtCore.QRect(420, 60, 61, 51))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        font.setPointSize(9)
        self.btn_add_tag.setFont(font)
        self.btn_add_tag.setObjectName("btn_add_tag")
        self.btn_del_tag = QtWidgets.QPushButton(self.groupbox_tag_based)
        self.btn_del_tag.setGeometry(QtCore.QRect(420, 190, 61, 51))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        self.btn_del_tag.setFont(font)
        self.btn_del_tag.setObjectName("btn_del_tag")
        self.linedit_hash = QtWidgets.QLineEdit(self.groupbox_tag_based)
        self.linedit_hash.setGeometry(QtCore.QRect(140, 14, 271, 30))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.linedit_hash.setFont(font)
        self.linedit_hash.setStyleSheet("QLineEdit:focus\n"
"{\n"
"  border: 2px solid red;\n"
"}\n"
"\n"
"")
        self.linedit_hash.setAlignment(QtCore.Qt.AlignCenter)
        self.linedit_hash.setObjectName("linedit_hash")
        self.tabwgt_hashlist = QtWidgets.QTableWidget(self.groupbox_tag_based)
        self.tabwgt_hashlist.setGeometry(QtCore.QRect(10, 50, 401, 201))
        self.tabwgt_hashlist.setStyleSheet("#tabwgt_hashlist\n"
"{\n"
"border:0.5px solid rgb(141, 141, 141);\n"
"}")
        self.tabwgt_hashlist.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tabwgt_hashlist.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabwgt_hashlist.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tabwgt_hashlist.setGridStyle(QtCore.Qt.SolidLine)
        self.tabwgt_hashlist.setObjectName("tabwgt_hashlist")
        self.tabwgt_hashlist.setColumnCount(0)
        self.tabwgt_hashlist.setRowCount(0)
        self.tabwgt_hashlist.horizontalHeader().setStretchLastSection(True)
        self.btn_add_alltag = QtWidgets.QPushButton(self.groupbox_tag_based)
        self.btn_add_alltag.setGeometry(QtCore.QRect(420, 124, 61, 51))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        font.setPointSize(9)
        self.btn_add_alltag.setFont(font)
        self.btn_add_alltag.setObjectName("btn_add_alltag")
        self.listwgt_sel_hashlist = QtWidgets.QListWidget(self.groupbox_tag_based)
        self.listwgt_sel_hashlist.setGeometry(QtCore.QRect(490, 50, 181, 201))
        self.listwgt_sel_hashlist.setStyleSheet("#listwgt_sel_hashlist\n"
"{\n"
"border:0.5px solid rgb(141, 141, 141);\n"
"}")
        self.listwgt_sel_hashlist.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listwgt_sel_hashlist.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listwgt_sel_hashlist.setObjectName("listwgt_sel_hashlist")
        self.combox_hashorlocation = QtWidgets.QComboBox(self.groupbox_tag_based)
        self.combox_hashorlocation.setGeometry(QtCore.QRect(13, 12, 121, 31))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.combox_hashorlocation.setFont(font)
        self.combox_hashorlocation.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.combox_hashorlocation.setAutoFillBackground(False)
        self.combox_hashorlocation.setStyleSheet("QComboBox \n"
"{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"} \n"
"QComboBox::selected:item \n"
"{ \n"
"    selection-background-color: rgba(0, 0, 0,0);\n"
"    selection-color: rgba(0, 0, 0, 255);\n"
"}")
        self.combox_hashorlocation.setEditable(False)
        self.combox_hashorlocation.setMaxVisibleItems(3)
        self.combox_hashorlocation.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.combox_hashorlocation.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.combox_hashorlocation.setFrame(False)
        self.combox_hashorlocation.setModelColumn(0)
        self.combox_hashorlocation.setObjectName("combox_hashorlocation")
        self.combox_hashorlocation.addItem("")
        self.combox_hashorlocation.addItem("")
        self.combox_hashorlocation.addItem("")
        self.btn_start_job = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start_job.setGeometry(QtCore.QRect(559, 412, 141, 37))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_start_job.setFont(font)
        self.btn_start_job.setObjectName("btn_start_job")
        self.groupbox_today_working = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox_today_working.setGeometry(QtCore.QRect(570, 29, 131, 81))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupbox_today_working.setFont(font)
        self.groupbox_today_working.setStyleSheet("QGroupBox#groupbox_today_working\n"
"{\n"
"border:1px solid rgb(0, 0, 0);\n"
"}")
        self.groupbox_today_working.setTitle("")
        self.groupbox_today_working.setObjectName("groupbox_today_working")
        self.lbl_today_follow = QtWidgets.QLabel(self.groupbox_today_working)
        self.lbl_today_follow.setGeometry(QtCore.QRect(22, 5, 101, 16))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        self.lbl_today_follow.setFont(font)
        self.lbl_today_follow.setObjectName("lbl_today_follow")
        self.lbl_today_like = QtWidgets.QLabel(self.groupbox_today_working)
        self.lbl_today_like.setGeometry(QtCore.QRect(22, 25, 101, 16))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        self.lbl_today_like.setFont(font)
        self.lbl_today_like.setObjectName("lbl_today_like")
        self.lbl_today_comment = QtWidgets.QLabel(self.groupbox_today_working)
        self.lbl_today_comment.setGeometry(QtCore.QRect(25, 44, 91, 16))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        self.lbl_today_comment.setFont(font)
        self.lbl_today_comment.setObjectName("lbl_today_comment")
        self.lbl_today_unfollow = QtWidgets.QLabel(self.groupbox_today_working)
        self.lbl_today_unfollow.setGeometry(QtCore.QRect(25, 64, 91, 16))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        self.lbl_today_unfollow.setFont(font)
        self.lbl_today_unfollow.setObjectName("lbl_today_unfollow")
        self.btn_start_unfollowjob = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start_unfollowjob.setGeometry(QtCore.QRect(559, 505, 141, 37))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_start_unfollowjob.setFont(font)
        self.btn_start_unfollowjob.setObjectName("btn_start_unfollowjob")
        self.groupbox_amount_working = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox_amount_working.setGeometry(QtCore.QRect(290, 30, 271, 80))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupbox_amount_working.setFont(font)
        self.groupbox_amount_working.setStyleSheet("QGroupBox#groupbox_amount_working\n"
"{\n"
"border:1px solid rgb(0, 0, 0);\n"
"}")
        self.groupbox_amount_working.setTitle("")
        self.groupbox_amount_working.setObjectName("groupbox_amount_working")
        self.btn_worktimeset = QtWidgets.QPushButton(self.groupbox_amount_working)
        self.btn_worktimeset.setGeometry(QtCore.QRect(221, 9, 41, 61))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        self.btn_worktimeset.setFont(font)
        self.btn_worktimeset.setObjectName("btn_worktimeset")
        self.linedit_amoutfollow = QtWidgets.QLineEdit(self.groupbox_amount_working)
        self.linedit_amoutfollow.setGeometry(QtCore.QRect(102, 7, 113, 20))
        self.linedit_amoutfollow.setStyleSheet("QLineEdit:focus\n"
"{\n"
"  border: 2px solid red;\n"
"}\n"
"\n"
"")
        self.linedit_amoutfollow.setObjectName("linedit_amoutfollow")
        self.linedit_amountcomment = QtWidgets.QLineEdit(self.groupbox_amount_working)
        self.linedit_amountcomment.setGeometry(QtCore.QRect(102, 53, 113, 20))
        self.linedit_amountcomment.setStyleSheet("QLineEdit:focus\n"
"{\n"
"  border: 2px solid red;\n"
"}\n"
"\n"
"")
        self.linedit_amountcomment.setObjectName("linedit_amountcomment")
        self.linedit_amountlike = QtWidgets.QLineEdit(self.groupbox_amount_working)
        self.linedit_amountlike.setGeometry(QtCore.QRect(102, 30, 113, 20))
        self.linedit_amountlike.setStyleSheet("QLineEdit:focus\n"
"{\n"
"  border: 2px solid red;\n"
"}\n"
"\n"
"")
        self.linedit_amountlike.setObjectName("linedit_amountlike")
        self.label_7 = QtWidgets.QLabel(self.groupbox_amount_working)
        self.label_7.setGeometry(QtCore.QRect(17, 55, 91, 16))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(self.groupbox_amount_working)
        self.label_5.setGeometry(QtCore.QRect(9, 10, 91, 16))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupbox_amount_working)
        self.label_6.setGeometry(QtCore.QRect(9, 33, 91, 16))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.listwgt_hblacktag = QtWidgets.QListWidget(self.centralwidget)
        self.listwgt_hblacktag.setGeometry(QtCore.QRect(815, 550, 181, 71))
        self.listwgt_hblacktag.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listwgt_hblacktag.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listwgt_hblacktag.setObjectName("listwgt_hblacktag")
        self.btn_stop_job = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop_job.setGeometry(QtCore.QRect(559, 458, 141, 37))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_stop_job.setFont(font)
        self.btn_stop_job.setObjectName("btn_stop_job")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 95, 261, 25))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 388, 141, 25))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(112, 112, 112);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 6, 141, 25))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:rgb(112, 112, 112);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 5, 121, 25))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:rgb(112, 112, 112);\n"
"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(570, 4, 121, 25))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color:rgb(112, 112, 112);\n"
"color: rgb(255, 255, 255);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(720, 4, 231, 25))
        font = QtGui.QFont()
        font.setFamily("11롯데마트행복Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color:rgb(112, 112, 112);\n"
"color: rgb(255, 255, 255);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label.raise_()
        self.groupbox_3.raise_()
        self.groupbox_view_workingpost.raise_()
        self.groupbox_comment.raise_()
        self.groupbox_tag_based.raise_()
        self.btn_start_job.raise_()
        self.groupbox_today_working.raise_()
        self.btn_start_unfollowjob.raise_()
        self.groupbox_amount_working.raise_()
        self.listwgt_hblacktag.raise_()
        self.btn_stop_job.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1021, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionTools = QtWidgets.QAction(MainWindow)
        self.actionTools.setObjectName("actionTools")
        self.actionManual = QtWidgets.QAction(MainWindow)
        self.actionManual.setObjectName("actionManual")
        self.actionSavesetting = QtWidgets.QAction(MainWindow)
        self.actionSavesetting.setObjectName("actionSavesetting")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionTimersetting = QtWidgets.QAction(MainWindow)
        self.actionTimersetting.setObjectName("actionTimersetting")
        self.actionLogout = QtWidgets.QAction(MainWindow)
        self.actionLogout.setObjectName("actionLogout")
        self.actionLoadsetting = QtWidgets.QAction(MainWindow)
        self.actionLoadsetting.setObjectName("actionLoadsetting")
        self.actionDetailsetting = QtWidgets.QAction(MainWindow)
        self.actionDetailsetting.setObjectName("actionDetailsetting")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionDetailsetting)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionManual)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.chk_follow, self.chk_like)
        MainWindow.setTabOrder(self.chk_like, self.chk_comment)
        MainWindow.setTabOrder(self.chk_comment, self.linedit_amoutfollow)
        MainWindow.setTabOrder(self.linedit_amoutfollow, self.linedit_amountlike)
        MainWindow.setTabOrder(self.linedit_amountlike, self.linedit_amountcomment)
        MainWindow.setTabOrder(self.linedit_amountcomment, self.btn_worktimeset)
        MainWindow.setTabOrder(self.btn_worktimeset, self.btn_start_job)
        MainWindow.setTabOrder(self.btn_start_job, self.btn_manualcomment)
        MainWindow.setTabOrder(self.btn_manualcomment, self.linedit_comment)
        MainWindow.setTabOrder(self.linedit_comment, self.btn_add_comment)
        MainWindow.setTabOrder(self.btn_add_comment, self.btn_stop_job)
        MainWindow.setTabOrder(self.btn_stop_job, self.listwgt_hblacktag)
        MainWindow.setTabOrder(self.listwgt_hblacktag, self.linedit_hash)
        MainWindow.setTabOrder(self.linedit_hash, self.btn_srch_hashtag)
        MainWindow.setTabOrder(self.btn_srch_hashtag, self.btn_add_tag)
        MainWindow.setTabOrder(self.btn_add_tag, self.btn_del_tag)
        MainWindow.setTabOrder(self.btn_del_tag, self.tabwgt_hashlist)
        MainWindow.setTabOrder(self.tabwgt_hashlist, self.btn_add_alltag)
        MainWindow.setTabOrder(self.btn_add_alltag, self.listwgt_sel_hashlist)
        MainWindow.setTabOrder(self.listwgt_sel_hashlist, self.btn_start_unfollowjob)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Instagram Account Management System"))
        self.btn_manualcomment.setText(_translate("MainWindow", "직접\n"
"쓰기"))
        self.btn_add_comment.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>댓글 추가</p><p><br/></p></body></html>"))
        self.btn_add_comment.setText(_translate("MainWindow", "추가"))
        self.btn_del_comment.setText(_translate("MainWindow", "삭제"))
        self.chk_follow.setText(_translate("MainWindow", "팔로우"))
        self.chk_like.setText(_translate("MainWindow", "좋아요"))
        self.chk_comment.setText(_translate("MainWindow", "댓글"))
        self.btn_srch_hashtag.setText(_translate("MainWindow", "검색"))
        self.btn_add_tag.setText(_translate("MainWindow", "추가"))
        self.btn_del_tag.setText(_translate("MainWindow", "삭제"))
        self.btn_add_alltag.setText(_translate("MainWindow", "전부\n"
"추가"))
        self.combox_hashorlocation.setCurrentText(_translate("MainWindow", "해시태그 명"))
        self.combox_hashorlocation.setItemText(0, _translate("MainWindow", "해시태그 명"))
        self.combox_hashorlocation.setItemText(1, _translate("MainWindow", "장소 명"))
        self.combox_hashorlocation.setItemText(2, _translate("MainWindow", "특정인 아이디"))
        self.btn_start_job.setText(_translate("MainWindow", "작업 시작하기"))
        self.lbl_today_follow.setText(_translate("MainWindow", "팔로우 : 500 개"))
        self.lbl_today_like.setText(_translate("MainWindow", "좋아요 : 1,000 개"))
        self.lbl_today_comment.setText(_translate("MainWindow", "댓글  : 500 개"))
        self.lbl_today_unfollow.setText(_translate("MainWindow", "언팔  : 500 개"))
        self.btn_start_unfollowjob.setText(_translate("MainWindow", "언팔 시작하기"))
        self.btn_worktimeset.setText(_translate("MainWindow", "설정"))
        self.label_7.setText(_translate("MainWindow", "댓글 작업량  :"))
        self.label_5.setText(_translate("MainWindow", "팔로우 작업량 :"))
        self.label_6.setText(_translate("MainWindow", "좋아요 작업량 :"))
        self.btn_stop_job.setText(_translate("MainWindow", "작업 정지하기"))
        self.label.setText(_translate("MainWindow", "태그 & 위치 & 특정인 기반 작업 설정"))
        self.label_2.setText(_translate("MainWindow", "댓글 작업 설정"))
        self.label_3.setText(_translate("MainWindow", "작업 항목 설정"))
        self.label_4.setText(_translate("MainWindow", "작업량 설정"))
        self.label_8.setText(_translate("MainWindow", "오늘의 작업량"))
        self.label_9.setText(_translate("MainWindow", "현재 작업 중인 게시글 & 기록"))
        self.menuFile.setTitle(_translate("MainWindow", "파일"))
        self.menuHelp.setTitle(_translate("MainWindow", "도움말"))
        self.actionTools.setText(_translate("MainWindow", "분석 도구"))
        self.actionManual.setText(_translate("MainWindow", "사용자 매뉴얼"))
        self.actionSavesetting.setText(_translate("MainWindow", "설정 저장"))
        self.actionExit.setText(_translate("MainWindow", "종료"))
        self.actionTimersetting.setText(_translate("MainWindow", "예약 설정"))
        self.actionLogout.setText(_translate("MainWindow", "로그아웃"))
        self.actionLoadsetting.setText(_translate("MainWindow", "설정 불러오기"))
        self.actionDetailsetting.setText(_translate("MainWindow", "세부 설정"))

import instabackground_rc
