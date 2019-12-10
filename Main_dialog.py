# -*- coding: utf-8 -*-

import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, Qt
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time, D_InstaManagementSys, D_ManualComment, D_login
from bs4 import BeautifulSoup
import threading
#from InstagramAnalysis import Ui_MainWindow
from InstagramAnalysis import Win_InstagramAnalysis
from DetailedSetting import Win_DetailedSetting
import datetime, os
import math

import loading

import numpy as np

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5 import QtCore, QtGui, QtWidgets
import urllib
import random
import linecache

import pickle

# wdriver.get('https://instagram.com')

# chrome_options.add_argument("headless")
# self.driver = wdriver.PhantomJS('C:\WebDriver\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\Bin\phantomjs')
# drv = self.wdriver.Firefox()
# wdriver.implicitly_wait(3)

class LoginWindow(QDialog, D_login.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__()

        # 로그인을 위한 정보 입력 폼
        self.setupUi(self)
        self.show()
        self.setWindowTitle("Instagram")

        # self.linedit_id.returnPressed.connect(self.linedit_pw.setFocus)

        self.btn_login.clicked.connect(self.btn_login_clicked)
        # self.linedit_id.returnPressed.connect(self.btn_login_clicked)

        # if 자동로그인 check , 파일 오픈해서 정보 가져오기
        #print(linecache.getline('IMSautologin.txt', 1).find('False'))
        if linecache.getline('IMSautologin.txt', 1).find('True') == 0:
            self.chk_autologin.setChecked(True)
            self.linedit_id.setText(linecache.getline('IMSautologin.txt', 2).strip())
            self.linedit_pw.setText(linecache.getline('IMSautologin.txt', 3).strip())

        else:
            self.chk_autologin.setChecked(False)

        self.parentwindow = parent
        # 로그인 한번 시도 후 실패 했을 경우, DB를 다시 불러오지 않음
        self.onefail = False

        try:
            webpage = urllib.request.urlopen("http://just-the-time.appspot.com/")
            internettime = webpage.read().decode('utf-8')
            self.OnlineUTCTime = datetime.datetime.strptime(internettime.strip(), '%Y-%m-%d %H:%M:%S').date()
            # 인터넷 접속 확인
            self.internetstatok = True
            print('internet connection is well')

        except Exception as exep:
            self.internetstatok = False
            print('인터넷 접속이 원활하지 않습니다.')

        self.poploading = loadingwgt(self)
        self.poploading.move((self.width() / 2) - 150, (self.height() / 2) - 75)
        self.poploading.resize(300, 150)

        self.lbl_version.setText("version 1.7")

        # th_check_login = threading.Thread(target=self.th_check_login)
        # th_check_login.daemon = True
        # th_check_login.start()
        # self.statusBar.showMessage("Web Browser is ready.").show()

    def btn_login_clicked(self):
        if not self.poploading.blackorwhite:
            self.lbl_errormsg.setText('')
            # self.parentwindow.start_web.join()
            if self.linedit_id.text().strip() != '' and self.linedit_pw.text().strip() != '':
                # self.poploading.show_loadingwgt.emit()
                self.poploading.show()
                self.poploading.setstatustext()
                if self.parentwindow.start_web.is_alive():
                    self.parentwindow.start_web.join()
                # function 으로 묶어서 불러오기 https://stackoverflow.com/questions/908550/python-getting-date-online
                if self.internetstatok:
                    if not self.onefail:
                        uid_list = WebDriverWait(driver=self.parentwindow.wdriver, timeout=10) \
                            .until(lambda wdriver: self.parentwindow.wdriver.find_element_by_xpath("//div[@id='post-view221137232404']"))
                        self.idfinder = uid_list.text
                    # print(idfinder)
                    uid = self.linedit_id.text().strip()
                    uid_len = len(uid)
                    if self.idfinder.find(uid) > 0:
                        loc_date = self.idfinder.find(uid)
                        due_date = datetime.datetime.strptime(self.idfinder[loc_date + uid_len + 1: loc_date + uid_len + 11], '%Y-%m-%d').date()
                        # due_date = datetime.datetime.strptime('2017-11-11', '%Y-%m-%d').date()
                        allow = due_date - self.OnlineUTCTime
                        if allow.days >= 0:
                            print('기간이 만료되지 않았음')
                            # 아이디 비번 저장에 체크되어 있으면 해당 내용 저장
                            if self.chk_autologin.isChecked():
                                print('아이디 저장 체크')
                                with open('IMSautologin.txt', 'w') as file:
                                    data = ["True\n", self.linedit_id.text() + "\n", self.linedit_pw.text() + "\n"]
                                    file.writelines(data)
                            else:
                                print('아이디 저장 언체크')
                                with open('IMSautologin.txt', 'w') as file:
                                    data = ["False\n", self.linedit_id.text() + "\n", self.linedit_pw.text() + "\n"]
                                    file.writelines(data)

                            self.poploading.set_instalogintext()
                            th_login = threading.Thread(target=self.thread_login)
                            th_login.daemon = True
                            th_login.start()
                            # self.thread_login()
                            # self.handleLogin()

                        else:
                            print('기간 만료')
                            self.poploading.close_lodingwgt.emit()
                            self.lbl_errormsg.setText('본 프로그램의 이용기간이 만료되었습니다.')

                    else:
                        print('본 프로그램의 이용권한이 없습니다.')
                        self.poploading.close_lodingwgt.emit()
                        self.lbl_errormsg.setText('본 프로그램의 이용권한이 없습니다.')
                    # 허용 날짜와 현재 날짜의 비교가 필요함.
                else:
                    # 다시한번 인터넷 시간을 불러옴
                    try:
                        webpage = urllib.request.urlopen("http://just-the-time.appspot.com/")
                        internettime = webpage.read().decode('utf-8')
                        self.OnlineUTCTime = datetime.datetime.strptime(internettime.strip(), '%Y-%m-%d %H:%M:%S').date()
                        # 인터넷 접속이 잘됨을 확인
                        self.internetstatok = True
                        # 재귀함수
                        self.btn_login_clicked()

                    except Exception as exep:
                        # 그래도 못불러온다. 관리자한테 얘기해야한다.
                        self.lbl_errormsg.setText('인터넷 접속이 원활하지 않습니다.')
                        self.close()
                    print()

            else:
                self.lbl_errormsg.setText('아이디 또는 비밀번호를 입력해주세요.')
                #print('아이디 또는 비밀번호를 정확히 입력해주세요.')

    def thread_login(self):
        self.parentwindow.wdriver.get('https://instagram.com')
        try:
            lo_login_button = WebDriverWait(driver=self.parentwindow.wdriver, timeout=5) \
                .until(lambda drv: drv.find_element_by_xpath("//p[@class='_g9ean']/a"))
            lo_login_button.click()
            time.sleep(1)

            # ID 입력부
            lo_user = WebDriverWait(driver=self.parentwindow.wdriver, timeout=5) \
                .until(lambda wdriver: wdriver.find_element_by_xpath("//input[@name='username']"))
            lo_user.send_keys(self.linedit_id.text().strip())  # self.linedit_id.text().strip() # the_yeppun # Do_Gyeongyunzvsom

            # PW 입력부
            lo_pass = WebDriverWait(driver=self.parentwindow.wdriver, timeout=5) \
                .until(lambda wdriver: wdriver.find_element_by_xpath("//input[@name='password']"))
            lo_pass.send_keys(self.linedit_pw.text().strip())  # self.linedit_pw.text().strip() # znzlahdtlf7 # ys2acwsgu9g
            time.sleep(1)

            # 로그인 버튼 클릭
            lo_login_submit = WebDriverWait(driver=self.parentwindow.wdriver, timeout=5) \
                .until(lambda wdriver: wdriver.find_element_by_xpath("//span[@class='_t38eb _ov9ai']/button"))
            # lo_login_submit = WebDriverWait(driver=wdriver, timeout=10) \
            # .until(lambda wdriver: wdriver.find_element_by_xpath("//button[@tabindex='3']"))
            lo_login_submit.click()
            time.sleep(2)

        except:
            self.poploading.close_lodingwgt.emit()
            self.lbl_errormsg.setText('로그인 실패. 로그인이 지연되고 있습니다.')
            self.onefail = True
            print('로그인에 실패하였습니다.')
            return

        # print(self.parentwindow.wdriver.page_source)
        try:
            for index in range(0, 5):
                try:
                    check_login = WebDriverWait(driver=self.parentwindow.wdriver, timeout=5) \
                        .until(lambda wdriver: wdriver.find_element_by_xpath("//html[1]"))
                    check_text = check_login.get_attribute("class")
                    # print(check_login.text)
                    if check_text.find('not-logged-in') >= 0:
                        print('로그인 실패.')
                        #time.sleep(0.5)
                        self.onefail = True
                        # 의심스러운 로그인 시도
                        try:
                            check_block = WebDriverWait(driver=self.parentwindow.wdriver, timeout=1) \
                                .until(lambda wdriver: wdriver.find_element_by_xpath("//p[@class='_fb78b']"))

                            if check_block.text == "의심스러운 로그인 시도":
                                # print('yes right 의심스러운 로그인 시도가 맞습니다.')
                                break
                        except:
                            print()

                    elif check_login.text.find('"status": "fail"') >= 0:
                        # 로그인 실패로
                        self.lbl_errormsg.setText('로그인 실패. 짧은 시간 내 여러번의 로그인 시도로 계정이 제한되었습니다. 관리자에게 문의해 주세요.')
                        self.poploading.close_lodingwgt.emit()
                        break

                    else:
                        try:
                            print('로그인 성공')
                            self.accept()
                            self.parentwindow.flaglogin = True
                            self.parentwindow.loginID = self.linedit_id.text().strip()
                            self.parentwindow.wdriver.get('https://instagram.com/' + self.linedit_id.text().strip())
                            break
                        except:
                            print('로그인 성공 두번째')
                            self.accept()
                            self.parentwindow.flaglogin = True
                            self.parentwindow.loginID = self.linedit_id.text().strip()
                            self.parentwindow.wdriver.get('https://instagram.com/' + self.linedit_id.text().strip())
                            break
                except:
                    self.onefail = True

            if self.onefail:
                # 로그인 실패시, 다시 DB에서 확인하는 것이 아니고, 기존 불러온 데이터로 처리 하기 위함.

                # 실패가 단순히 로그인이 되지 않아서 인지, 블락이 되어서 안되는 것인지 확인하고
                if check_block.text == "의심스러운 로그인 시도":
                    # 이메일 또는 휴대폰을 할지 먼저 선택해야 함.
                    header_text = WebDriverWait(driver=self.parentwindow.wdriver, timeout=3) \
                        .until(lambda wdriver: wdriver.find_element_by_xpath("//div[@class='_bzfgt _mpcv6']/p"))  # _3574j

                    self.poploading.validation_win.emit(header_text.text)

                    # 블락이 되었다면, 프로그램 내에서 풀 수 있도록 함.
                    # WebDriverWait(driver=self.parentwindow.wdriver, timeout=1) \
                    #     .until(lambda wdriver: wdriver.find_element_by_xpath("//button[text()='보안 코드 보내기']")).click()
                    #
                    # WebDriverWait(driver=self.parentwindow.wdriver, timeout=3) \
                    #     .until(lambda wdriver: wdriver.find_element_by_xpath("//h2[text()='보안 코드 입력']"))
                    #
                    # header_text = WebDriverWait(driver=self.parentwindow.wdriver, timeout=3) \
                    #     .until(lambda wdriver: wdriver.find_element_by_xpath("//div[@class='_bzfgt _mpcv6']/p")) # _3574j
                    # self.poploading.validation_win.emit(header_text.text)

                    # 핸드폰 또는 이메일로 인증할 수 있도록 선택할 수 있게
                    # self.lbl_errormsg.setText('의심스러운 로그인 시도가 되었으니 인증을 풀자')
                    # print('의심스러운 로그인 시도가 되었으니 인증을 풀자')
                else:
                    # 아니면 계정 보안 2단계로 코드를 받는 화면인지
                    self.lbl_errormsg.setText('로그인 실패. 본 프로그램을 종료 후 다시 시도해 주세요.')

                # 그냥 진짜 로그인 실패인지

        except:
            self.poploading.close_lodingwgt.emit()
            self.lbl_errormsg.setText('로그인 실패. 아이디 또는 비밀번호가 정확하지 않습니다.')
            self.onefail = True
            # print('로그인에 실패하였습니다.')
        return

    def handleLogin(self):
        # 인증이 완료되었으면 머인화면으로 이동
        self.accept()
        self.parentwindow.flaglogin = True
        self.parentwindow.loginID = self.linedit_id.text().strip()
        self.parentwindow.wdriver.get('https://instagram.com/' + self.linedit_id.text().strip())

        # if self.textName.text().strip() != '' or self.textPass.text().strip() != '':
        # self.m_id = 'the_yeppun' # the_yeppun # Do_Gyeongyunzvsom
        # self.m_pw = 'znzlahdtlf7' # znzlahdtlf7 # ys2acwsgu9g


    def th_check_login(self):
        while not self.parentwindow.flaglogin:
            print('yes')
            #print(self.parentwindow.uid_list)
            try:
                WebDriverWait(driver=self.parentwindow.wdriver, timeout=2) \
                    .until(lambda wdriver: wdriver.find_element_by_xpath("//a[@class='_8scx2 _gvoze coreSpriteDesktopNavProfile']"))
                # print(check_login.text)
                # check_login.click()

                # 로그인된 아이디명을 불러와서 대입
                # uid = self.linedit_id.text().strip()
                # uid_len = len(uid)
                # if self.idfinder.find(uid) > 0:
                #     loc_date = self.idfinder.find(uid)
                #     due_date = datetime.datetime.strptime(
                #         self.idfinder[loc_date + uid_len + 1: loc_date + uid_len + 11], '%Y-%m-%d').date()
                #     # due_date = datetime.datetime.strptime('2017-11-11', '%Y-%m-%d').date()
                #     allow = due_date - self.OnlineUTCTime
                #     if allow.days >= 0:
                #         print('기간이 만료되지 않았음')

                self.parentwindow.testheadless()
                self.accept()
                self.parentwindow.flaglogin = True
                self.parentwindow.loginID = self.linedit_id.text().strip()
                self.parentwindow.wdriver.get('https://instagram.com/' + self.linedit_id.text().strip())
                break
                # if check_text.find('not-logged-in') >= 0:
            except Exception as exep:
                print(exep)
                time.sleep(1)



class InstaManagementSystem(QMainWindow, D_InstaManagementSys.Ui_MainWindow):
    add_wgtlist = pyqtSignal(int, int, str)
    add_log = pyqtSignal(int, str)
    add_amountwork = pyqtSignal(int)
    show_loading = pyqtSignal()
    show_message = pyqtSignal(str, str)

    def __init__(self):
        QMainWindow.__init__(self)

        # 정상적으로 프로그램이 실행되었다.
        print('Instagram Management System Program is booting')
        self.start_web = threading.Thread(target=self.thread_start_webdriver)
        self.start_web.daemon = True
        self.start_web.start()

        self.flaglogin = False
        self.loginID = ''
        self.uid_list = ''
        self.dialogin = LoginWindow(self)
        # 로그인 창에서 로그인이 정상적으로 되지 않았다면 프로그램 종료
        if not self.dialogin.exec_() == QDialog.Accepted:
            print('login is not accept. but')
            if not self.flaglogin:
                print('program shutdown')
                if self.start_web.is_alive():
                    self.start_web.join()
                self.wdriver.close()
                sys.exit(1)
            print('that is going on')

        # 로그인이 정상적으로 되었다면 하위 코드 실행으로 메인 화면

        # QMainWindow.setStyle(QStyleFactory.create('Cleanlooks'))
        # self.setStyle(QStyleFactory.create('WindowsXP'))
        # self.setWindowIcon(QtGui.QIcon('test_icon.png'))

        self.setupUi(self)
        self.show()
        self.statusbar.showMessage("Instagram ID : " + self.loginID + " 으로 접속중")

        # 변수 초기화 작업
        self.linedit_amountcomment.setText('300')
        self.linedit_amountlike.setText('950')
        self.linedit_amoutfollow.setText('450')
        self.stop_thread = True
        self.pause_thread = False
        self.detail_comment = False
        self.set_toggle_comment(self.detail_comment)

        # 리스트 초기화 함수
        self.onearray = []
        self.loc_dictionary = {}
        self.loc_array = []

        # 댓글 직접 작성 유무를 판단하는 변수
        self.flag_manual_comment = False

        # 데이터 값들 초기화 함수
        self.get_today_amount_work()
        self.get_blacktag_workcount()
        self.get_commentntag()

        # 블랙태그의 내용을 담고 있는 리스트 위젯 숨기기, 나중 코딩의 편리함을 위해서
        self.listwgt_hblacktag.hide()

        # 분석툴을 실행했으면 한번만 인스턴스를 실행해서 메모리 leak 방지
        self.analysisyes = False

        # 댓글 기능을 사용할 것인지 아닌지에 대한 변수 True = 사용, False = 미사용
        self.enable_comment = True
        self.enable_follow = True
        self.enable_like = True
        self.enable_unfollow = True

        # 처음 시작시, 작업 정지하기 버튼 비활성화 True = start 활성, stop 비활성 False = start 비활성, stop 활성
        self.btn_start_n_stop_toggle(True)
        self.option_search = 1

        # 기본 검색 결과 테이블 GUI 설정
        self.tabwgt_hashlist.setRowCount(1)
        self.tabwgt_hashlist.setColumnCount(2)
        column_headers = ['해시태그 명', '게시물 개수']
        self.tabwgt_hashlist.setHorizontalHeaderLabels(column_headers)
        self.tabwgt_hashlist.setColumnWidth(0, 190)
        self.tabwgt_hashlist.setColumnWidth(1, 76)

        # 슬랏 & 시그널 모음
        self.add_wgtlist.connect(self.hashtabwgt_add_item)
        self.add_amountwork.connect(self.update_today_amount_work)
        self.add_log.connect(self.write_log)
        self.show_message.connect(self.show_MessageBox)
        #self.write_l = threading.Thread(target=self.write_log(1))
        #write_l = threading.Thread(target=self.write_log())
        #threading.Thread(target=self.round_tag_post)

        # 클릭 이벤트 모음
            ## 태그 및 장소 및 특정인 기반 작업 설정 부분
        self.btn_add_tag.clicked.connect(self.btn_add_tag_clicked)
        self.linedit_hash.returnPressed.connect(self.btn_tag_search_clicked)
        self.btn_srch_hashtag.clicked.connect(self.btn_tag_search_clicked)
        self.btn_add_alltag.clicked.connect(self.btn_add_alltag_clicked)
        self.btn_del_tag.clicked.connect(self.btn_del_tag_clicked)

            ## 댓글 작업 설정 부분
        self.linedit_comment.returnPressed.connect(self.btn_add_comment_clicked)
        self.btn_add_comment.clicked.connect(self.btn_add_comment_clicked)
        self.btn_manualcomment.clicked.connect(self.btn_manualcomment_clicked)
        self.btn_del_comment.clicked.connect(self.btn_del_comment_clicked)
        self.listwgt_comment_tag.itemSelectionChanged.connect(self.selected_comment_tagitem)

            ## 작업 시작 및 정지 및 언팔
        self.btn_start_job.clicked.connect(self.btn_start_job_clicked)
        self.btn_stop_job.clicked.connect(self.btn_stop_job_clicked)
        self.btn_start_unfollowjob.clicked.connect(self.btn_start_unfollowjob_clicked)

            ## 작업량 설정 부분
        self.btn_worktimeset.clicked.connect(self.btn_worktimeset_clicked)


        # 작업 항목 설정 부분 체크박스 클릭 이벤트
        self.chk_comment.clicked.connect(self.comment_checkbox_clicked)
        self.chk_like.clicked.connect(self.like_checkbox_clicked)
        self.chk_follow.clicked.connect(self.follow_checkbox_clicked)
        # self.chk_like.clicked.connect()

        # 메뉴 클릭 이벤트 모음
        # self.actionTools.triggered.connect(self.menu_actiontools_clicked)
        self.actionManual.triggered.connect(self.menu_actionmanual_clicked)
        self.actionDetailsetting.triggered.connect(self.menu_actiondetail_clicked)

        ############################테스트 공간######################
        self.tabwgt_hashlist.setRowCount(1)
        self.tabwgt_hashlist.setItem(0, 0, QTableWidgetItem("사업의 번창을 응원합니다."))
        self.tabwgt_hashlist.setItem(0, 1, QTableWidgetItem("-더 인스타-"))

        # self.btn_start_unfollowjob.clicked.connect(self.thread_module)
        # self.linedit_hash.textChanged.connect(self.test_module)
        # self.linedit_hash.textEdited.connect(self.test_module)


        #self.secondarray = []
        self._popframe = loadingwgt(self)
        self._popframe.move((self.width() / 2) - 75, (self.height() / 2) - 75)
        self._popframe.resize(150, 150)
        self.show_loading.connect(self._popframe.show)

        self.combox_hashorlocation.currentTextChanged.connect(self.search_comboxitem_change)


        # os.system('explorer http://ahs1419083.blog.me/221096104546')
        # self.listwgt_sel_hashlist.itemSelectionChanged.connect(self.selected_comment_tagitem)
        # self.linedit_comment.cursorPosition.connect(self.selected_comment_tagitem)
        # self.linedit_blacktag.returnPressed.connect(self.btn_add_blacktag_clicked)
        # self.btn_add_blacktag.clicked.connect(self.btn_add_blacktag_clicked)
        #############################################################

    def thread_start_webdriver(self):
        chrome_options = Options()
        chrome_options.add_argument('lang=ko')
        # chrome_options.add_argument("--headless")
        self.wdriver = webdriver.Chrome('chromedriver_win32\chromedriver', chrome_options=chrome_options)
        self.wdriver.get('http://blog.naver.com/anhscompany/221137232404')
        self.wdriver.switch_to.frame('mainFrame')
        return

    def testheadless(self):
        from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
        # self.wdriver.quit()
        # executor_url = webdriver.command_executor._url
        # session_id = webdriver.session_id
        # cookies = self.wdriver. .get_cookies()
        executor_url = self.wdriver.command_executor._url
        session_id = self.wdriver.session_id
        # pickle.dump(self.wdriver.get_cookies(), open("cookies.pkl", "wb"))
        cookies_list = self.wdriver.get_cookies()
        cookies_dict = {}
        for cookie in cookies_list:
            cookies_dict[cookie['name']] = cookie['value']
        chrome_options = Options()
        chrome_options.add_argument('--lang=ko')
        # chrome_options.add_argument("headless")
        # self.wdriver = webdriver.Chrome('chromedriver_win32\chromedriver', chrome_options=chrome_options)
        # for cookie in cookies:
        #     self.wdriver.add_cookie(cookie)
        # self.create_driver_session(session_id, executor_url)
        # print(self.driver2.current_url)
        # self.driver2.get('https://instagram.com/')

        self.wdriver2 = webdriver.Chrome('chromedriver_win32\chromedriver', chrome_options=chrome_options)
        # self.wdriver2.get(self.wdriver.current_url)
        # self.wdriver2.session_id = session_id
        # self.wdriver2.command_executor()

        # self.wdriver2 = webdriver.Remote(
        #     command_executor='http://127.0.0.1:4444/wd/hub',
        #     desired_capabilities=DesiredCapabilities.CHROME)
        self.wdriver2 = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
        print('what')
        # self.wdriver2.session_id = cookies_dict.get('sessionid')
        self.wdriver2.session_id = session_id
        #cookies = pickle.load(open("cookies.pkl", "rb"))
        #print('ha')
        print(cookies_dict)
        #self.wdriver2.add_cookie(cookies_dict)
        # for cookie_n, cookie_k in cookies_dict.items():
        #     print('yo')
        #     print(cookie_n)
        #     print(cookie_k)
        #     self.wdriver2.add_cookie({'name' : cookie_n, 'value' : cookie_k})
        # for cookie in cookies:
        #     self.wdriver2.add_cookie()
        #     self.wdriver2.add_cookie(cookie)
        self.wdriver2.get('https://instagram.com/')
        print('no')

            # .Chrome('chromedriver_win32\chromedriver', chrome_options=chrome_options)

    def create_driver_session(self, session_id, executor_url):
        from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

        # Save the original function, so we can revert our patch
        org_command_execute = RemoteWebDriver.execute

        def new_command_execute(self, command, params=None):
            if command == "newSession":
                # Mock the response
                return {'success': 0, 'value': None, 'sessionId': session_id}
            else:
                return org_command_execute(self, command, params)

        # Patch the function before creating the driver object
        RemoteWebDriver.execute = new_command_execute

        self.new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
        self.new_driver.session_id = session_id

        self.new_driver.get('https://instagram.com/')

        # Replace the patched function with original function
        RemoteWebDriver.execute = org_command_execute

        # return new_driver

    def search_comboxitem_change(self):
        if self.combox_hashorlocation.currentText() == '해시태그 명':
            # self.tabwgt_hashlist.setColumnCount(2)
            column_headers = ['해시태그 명', '게시물 개수']
            self.tabwgt_hashlist.setHorizontalHeaderLabels(column_headers)
            self.option_search = 1
        elif self.combox_hashorlocation.currentText() == '장소 명':
            #self.tabwgt_hashlist.setColumnCount(1)
            column_headers = ['장소 명', '상세 위치']
            self.tabwgt_hashlist.setHorizontalHeaderLabels(column_headers)
            # self.tabwgt_hashlist.setColumnWidth(0, 220)
            self.option_search = 2
        else:
            # self.tabwgt_hashlist.setColumnCount(1)
            column_headers = ['아이디', '프로필']
            self.tabwgt_hashlist.setHorizontalHeaderLabels(column_headers)
            self.option_search = 3

    def thread_module(self):
        print('fffffffff')


    def closeEvent(self, event):
        # 오늘의 작업량 저장
        with open('IMSData.txt', 'w') as file:
            data = ["[Last_Time]\n", datetime.datetime.now().strftime('%Y-%m-%d') + "\n", "[Toady_Work_Amount]\n", \
                    str(self.today_follow) + "\n", str(self.today_like) + "\n", str(self.today_comment) + "\n", str(self.today_unfollow)]
            file.writelines(data)

        # 댓글들 저장
        with open('IMSComment.txt', 'w') as file:
            cdata = []
            for index in range(self.listwgt_commentlist.count()):
                cdata.append(self.listwgt_commentlist.item(index).text().strip() + "\n")
            file.writelines(cdata)

        # 태그들 저장
        with open('IMSTag.txt', 'w') as file:
            bdata = []
            for index in range(self.listwgt_sel_hashlist.count()):
                bdata.append(self.listwgt_sel_hashlist.item(index).text().strip() + "\n")
            file.writelines(bdata)

        # 장소태그 사전 저장
        with open('IMSLocdic.txt', 'w+') as file:
            ddata = []
            for key, value in self.loc_dictionary.items():
                # for index in range(len(self.loc_dictionary)):
                ddata.append(key + "/" + value + "\n")
            file.writelines(ddata)

        if self.analysisyes:
            self.wdriver.switch_to_window(self.wdriver.window_handles[1])
            self.wdriver.close()
            self.wdriver.switch_to_window(self.wdriver.window_handles[0])
            self.wdriver.close()
        else:
            self.wdriver.close()

        # 작업량의 정보를 저장하고 닫는다.

    # 진행중에 있는데 하루가 지나서 오늘의 작업량이 업데이트 해야 되는지 체크
    def get_check_todaywork(self):
        now_date = datetime.datetime.now().date()

        linecache.checkcache('IMSData.txt')
        last_date = datetime.datetime.strptime(linecache.getline('IMSData.txt', 2), '%Y-%m-%d ').date()
        oper_day = now_date - last_date

        if oper_day.days > 0:
            result = True
        else:
            result = False

        return result

    def btn_start_job_clicked(self):
        # 제일 처음으로는 self.listwgt_sel_hashlist 에 태그가 존재하는지 유효성 검사
        # 또는 위치 기반으로 태그가 존재하는지 유효성 검사
        if not self.listwgt_sel_hashlist.count() > 0:
            QMessageBox.about(self, "태그 에러", "작업할 태그가 존재하지 않습니다.!!")
            return

        th = threading.Thread(target=self.round_tag_post)
        th.daemon = True
        th.start()

        # 한 태그 당 최대 몇개의 좋아요 팔로우 할지 세부 설정에서 선택할 수 있도록
        # 좋아요가 눌렸는지 안눌렸는지 열어보고 확인
        # 파일로 좋아요 누른 게시글을 관리하면 더 비효율

    def round_tag_post(self):
        # 작업을 시작한 날짜를 변수에 저장
        self.stop_thread = False
        tag_or_spec = True
        self.add_log.emit(4, '')
        self.existcomment = False
        while True:
            # self.listwgt_sel_hashlist에 존재하는 태그 리스트들을 불러온다. for 문으로 순회
            for tag_index in range(0, self.listwgt_sel_hashlist.count()):
                if self.stop_thread:
                    break

                if self.get_check_todaywork():
                    self.get_today_amount_work()

                # 팔로우, 좋아요, 댓글이 모두 False 면 작업 정지
                if not self.enable_like and not self.enable_follow and not self.enable_comment:
                    print("그만")
                    self.stop_thread = True
                    break

                self.btn_start_n_stop_toggle(False)
                self.listwgt_sel_hashlist.setCurrentRow(tag_index)
                what_sel_text = self.listwgt_sel_hashlist.item(tag_index).text()[:4]
                what_sel_tagname = self.listwgt_sel_hashlist.item(tag_index).text()[5:]
                if what_sel_text == '[태그]':
                    herf = 'http://www.instagram.com/explore/tags/' + what_sel_tagname + '/'
                    tag_or_spec = True
                elif what_sel_text == '[장소]':
                    herf = 'http://www.instagram.com/explore/locations/' + self.loc_dictionary[what_sel_tagname]
                    tag_or_spec = True
                else:
                    herf = 'http://www.instagram.com/' + what_sel_tagname + '/'
                    tag_or_spec = False

                # 로그 기록 추가
                self.add_log.emit(8, self.listwgt_sel_hashlist.item(tag_index).text())

                if self.stop_thread:
                    break

                # self.listwgt_sel_hashlist.item(tag_index)
                # 첫번째 태그로 검색한다. herf = /explore/tags/'태그 명'/
                # 두번째 장소로 검색한다. herf = /explore/location/'장소 명'/
                # self.loc_dictionary['목동'] = self.loc_array[self.tabwgt_hashlist.currentRow()]
                # print(self.loc_dictionary['목동'])
                # 세번째 아디로 검색한다. herf = '아이디'

                self.wdriver.get(herf)
                time.sleep(1)
                if tag_or_spec:
                ############################## 태그 및 장소 검색어에 대한 루틴 시작########################################
                    # 처음 들어간 후에 최근 게시물 12개를 먼저 읽어들인다. 한 태그당 최대 50개
                    # scroll_count = 0 -> 더 읽어들이기 버튼이 눌리지 않은 상태로, 인기게시글을 넘어 최신게시글부터 작업 #10
                    # scroll_count = 1 -> 더 읽어들이기 버튼이 눌린 상태로, 인기게시글 9개와 최신게시글 12개를 넘어부터 작업 #22
                    # scroll_count = 2 -> 더 읽어들이기 버튼이 눌린 상태로, 인기게시글 9개와 최신게시글 24개를 넘어부터 작업 #34
                    # m_amount_post -> 사용자로 부터 입력 받은 작업 포스트 양
                    time.sleep(1)
                    scroll_count = self.workamount//12  # 사용자로부터 입력 받은 작업 양으로 계산 바꿈!!!
                    # 더 읽어들이기 버튼을 클릭 후에는 인기(9) + 최신(12) 개 이후의 게시글을 불러와야함, 스크롤을 한번 내린 후에는 추가 12개
                    post_count = 9
                    working_post_count = 1
                    for scount in range(0, scroll_count):
                        # if scount == 0:
                        #     # '더 읽어들이기' 버튼을 누름
                        #     try:
                        #         more_submit = WebDriverWait(driver=wdriver, timeout=10) \
                        #             .until(lambda wdriver: wdriver.find_element_by_xpath("//a[text()='더 읽어들이기']"))
                        #         more_submit.click()
                        #         time.sleep(2)
                        #     except Exception as exep:
                        #         print('what is error : 게시물이 얼마 없어서, 더 읽어들이기 버튼이 없습니다.!')
                        #     scroll_count += 1
                        #
                        # else:
                        # '더 읽어들이기' 버튼이 없어졌기 때문에 바로 아래 코드를 사용
                        self.wdriver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                        time.sleep(2)
                        if self.stop_thread:
                            break

                    black_exist = False
                    # already_like = False
                    if self.stop_thread:
                        break
                    try:
                        selected_tags = WebDriverWait(driver=self.wdriver, timeout=10) \
                            .until(lambda wdriver: wdriver.find_elements_by_xpath("//div[@class='_mck9w _gvoze _f2mse']/a"))

                    except Exception as exep:
                        print('작업할 태그에 대한 내용이 존재하지 않습니다.')
                        continue

                    for post_index in range(post_count, post_count + self.workamount):   # 사용자가 정의할 수 있도록 변수로 받음
                        if not self.enable_like and not self.enable_follow and not self.enable_comment:
                            print("그만")
                            self.stop_thread = True
                            break

                        if self.stop_thread:
                            break

                        time.sleep(3)
                        try:
                            selected_tags[post_index].click()
                        except Exception as exep:
                            print(exep)
                            break

                        # 이미 팔로워가 되어 있다. 또는 좋아요가 되어 있다. 유효성 검사
                        time.sleep(3)
                        if self.stop_thread:
                            break

                        # 해당 게시글에 블랙 태그에 대한 내용이 있는지 검사
                        try:
                            current_post = WebDriverWait(driver=self.wdriver, timeout=10) \
                                .until(lambda wdriver: wdriver.find_elements_by_xpath("//div[@class='_mck9w _gvoze _f2mse']/a/div/div/img"))
                            check_tag_text = current_post[post_index].get_attribute("alt")
                        except Exception as exep:
                            print('페이지가 삭제되어 읽을 수 없음.')
                            break

                        for index in range(self.listwgt_hblacktag.count()):
                            if self.listwgt_hblacktag.item(index).text() in check_tag_text:
                            # if check_tag_text.find(self.listwgt_blacktag.item(index).text()):
                                # 블랙태그로 설정한 내용이 포함되어 있습니다.
                                black_exist = True
                                break

                        # 블랙태그가 포함된 게시글이면 다음 순번 게시글로 이동
                        if black_exist:
                            black_exist = False
                            self.wdriver.back()
                            continue

                        try:
                            get_id = WebDriverWait(driver=self.wdriver, timeout=10) \
                                .until(lambda wdriver: wdriver.find_element_by_xpath("//a[@class='_2g7d5 notranslate _iadoq']"))

                            follow_btn = WebDriverWait(driver=self.wdriver, timeout=10) \
                                .until(lambda wdriver: wdriver.find_element_by_xpath("//span[@class='_fj5rr _ov9ai']/button"))
                            if follow_btn.text == '팔로잉' or not self.enable_follow:    # AttributeError: 'NoneType' object has no attribute 'get_text'
                                # 만약 팔로워가 이미 되어 있다면, 하위 좋아요를 누를지 말지 사용자 선택 체크하기
                                # 팔로우가 되어 있다고 해도, 좋아요가 되어 있을 수도 있고 안 되어 있을 수 있다.
                                print('this account is already followed before')

                            else:
                                # 팔로우가 안되어 있으니 팔로우 하기
                                follow_btn.click()
                                self.add_amountwork.emit(1)
                                self.add_log.emit(1, get_id.text)
                                time.sleep(4)

                        except Exception as exep:
                            print('팔로우 실패')

                        if self.stop_thread:
                            break

                        #####################################좋아요 작업##############################################
                        like_btn = WebDriverWait(driver=self.wdriver, timeout=10) \
                            .until(lambda wdriver: wdriver.find_element_by_xpath("//a[@class='_eszkz _l9yih']/span"))
                        if like_btn.text == '좋아요 취소':
                            # 만약 좋아요가 이미 되어 있다면, 이전에 작업했다는 것으로 판단하여 for문 종료
                            # 이미 작업한 게시글로 판단하고 루틴 종료 후, 다음 태그로 이동
                            # already_like = True
                            break

                        else:
                            # 작업하는 게시글의 게시 사진을 띄우기
                            # print('picture')
                            # like_btn = WebDriverWait(driver=wdriver, timeout=10) \
                            #     .until(lambda wdriver: wdriver.find_element_by_xpath("//span[@class='_8scx2 coreSpriteHeartOpen']"))
                            # print(current_post[post_index].get_attribute("alt"))

                            # 작업하는 게시글의 게시 사진을 띄우기
                            url = current_post[post_index].get_attribute("src")
                            data = urllib.request.urlopen(url).read()
                            image = QtGui.QImage()
                            image.loadFromData(data)
                            ###################################수동 댓글 작성#########################################
                            if self.flag_manual_comment:
                                self.mc.workingid = get_id.text
                                # 직접 댓글 작성하는 화면에 사진과 글감을 띄움
                                self.mc.mc_photozone.setPixmap(QtGui.QPixmap(image))
                                self.mc.mc_photozone.setScaledContents(True)
                                cm_list = WebDriverWait(driver=self.wdriver, timeout=10) \
                                    .until(lambda wdriver: wdriver.find_elements_by_xpath(
                                    "//ul[@class='_b0tqa']/li"))
                                for xin in range(len(cm_list)):
                                    if cm_list[xin].get_attribute("title") == self.loginID:
                                        # 이미 이전에 댓글
                                        self.existcomment = True
                                        break
                                if self.existcomment:
                                    self.existcomment = False
                                    break

                                if not self.mc_first:
                                    self.mc.loading_stop()
                                self.mc_first = False
                                self.mc.mc_posttext.setText(current_post[post_index].get_attribute("alt"))
                                self.mc_complete = True

                                time.sleep(5)
                                ################################좋아요 누름##############################
                                if self.enable_like:
                                    like_btn.click()
                                    time.sleep(2)
                                    self.add_amountwork.emit(2)
                                    self.add_log.emit(2, get_id.text)
                                    print('like is completed')
                                #################################좋아요 종료###############################
                                if self.stop_thread:
                                    break
                                # 무한 대기 사용자가 직접 댓글 입력을 완료할 때까지 기다림
                                while self.mc_complete:
                                    time.sleep(2)
                                # 작성이 완료되어 확인 버튼을 누르고 다음 행동으로

                            ##############################수동 댓글 작성 종료##################################
                            #################################자동 댓글 작성#################################
                            else:
                                self.lbl_picture.setPixmap(QtGui.QPixmap(image))
                                self.lbl_picture.setScaledContents(True)
                                time.sleep(3)
                                ################################좋아요 누름##############################
                                if self.enable_like:
                                    like_btn.click()
                                    time.sleep(1)
                                    self.add_amountwork.emit(2)
                                    self.add_log.emit(2, get_id.text)
                                    time.sleep(5)
                                    print('like is completed')
                                ########################################################################

                                if self.stop_thread:
                                    break

                                # 이미 댓글이 달려있다면,
                                cm_list = WebDriverWait(driver=self.wdriver, timeout=10) \
                                    .until(lambda wdriver: wdriver.find_elements_by_xpath(
                                    "//ul[@class='_b0tqa']/li/a"))
                                for xin in range(len(cm_list)):
                                    if cm_list[xin].get_attribute("title") == self.loginID:
                                        # 이미 이전에 댓글을 달았음
                                        self.existcomment = True
                                        break

                                if self.existcomment:
                                    self.existcomment = False
                                    break

                                comment_count = self.listwgt_commentlist.count()
                                if comment_count > 0 and self.enable_comment:
                                    ran_index = random.randrange(0, comment_count)
                                    # 랜덤으로 댓글을 가져와서 작성할 수 있도록 한다.
                                    try:
                                        comment_text = WebDriverWait(driver=self.wdriver, timeout=10) \
                                            .until(lambda wdriver: wdriver.find_element_by_xpath("//textarea[@class='_bilrf']")).click()
                                        comment_text2 = WebDriverWait(driver=self.wdriver, timeout=10) \
                                            .until(lambda wdriver: wdriver.find_element_by_xpath("//textarea[@class='_bilrf']"))
                                        time.sleep(3)
                                        comment_text2.send_keys(self.listwgt_commentlist.item(ran_index).text())
                                        comment_text2.send_keys(Keys.RETURN)

                                        self.add_amountwork.emit(3)
                                        self.add_log.emit(3, get_id.text)
                                        time.sleep(5)

                                    except Exception as exep:
                                        print('comment error')
                            ######################################자동 댓글 작성 종료####################################
                                # 중간에 댓글 직접달기를 한다면, 새로운 위젯 창을 띄우고
                                # 일정 시간 간격을 가짐
                                time.sleep(4)

                            if self.stop_thread:
                                break
                        ###################################좋아요 작업 종료############################################
                        # 순차적으로 다음 게시글 선택을 위한 뒤로가기
                        self.wdriver.back()
                        # 일정 시간 간격을 가짐
                        time.sleep(5)
                        ################################### 태그 및 장소 검색어에 대한 루틴 종료###############################

                ####################################특정인 팔로워 작업 시작############################################
                else:
                    # 총 1000번을 돌아서 팔로우가 되어 있는지 확인하고, 안되어 있음면 팔로우 되어 있으면 안들어 갈 것
                    if self.stop_thread:
                        break

                    # 특정인 ID 가 비공개 계정이면 해당 작업을 진행할 수 없음
                    try:
                        WebDriverWait(driver=self.wdriver, timeout=10) \
                            .until(lambda wdriver: wdriver.find_elements_by_xpath("//a[@class='_t98z6']"))[0].click()
                        time.sleep(1)
                        # 현재 팔로워들 팝업창에서 팔로우 확인을 위한 변수와 클릭을 위한 변수
                    except Exception as exep:
                        time.sleep(5)
                        self.add_log.emit(10, what_sel_tagname)
                        # self.show_message.emit("계정 오류", "해당 계정이 비공개로 되어 작업을 진행 할 수 없습니다.!")
                        print('what is error : 해당 계정은 비공개 개정으로 작업을 할 수 없습니다.!')
                        continue

                    # 10번 팔로워들 작업을 한 후에 스크롤을 내려줘야 하기 때문에 필요한 변수.
                    total_work_count = 0
                    if self.stop_thread:
                        break

                    for index in range(0, 100000):
                        if self.stop_thread:
                            break

                        if index % 10 == 0:
                            followerscroll = WebDriverWait(driver=self.wdriver, timeout=10) \
                                    .until(lambda wdriver: wdriver.find_element_by_xpath("//div[@class='_gs38e']"))
                            time.sleep(1)

                            self.wdriver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followerscroll)
                            time.sleep(2)

                            if self.stop_thread:
                                break

                        check_follow = WebDriverWait(driver=self.wdriver, timeout=10) \
                            .until(lambda wdriver: wdriver.find_elements_by_xpath("//span[@class='_ov9ai']/button"))
                        time.sleep(1)

                        follower_list = WebDriverWait(driver=self.wdriver, timeout=10) \
                            .until(lambda wdriver: wdriver.find_elements_by_xpath("//div[@class='_2nunc']/a"))
                        time.sleep(1)

                        get_id = follower_list[index].get_attribute("title")
                        time.sleep(1)

                        ####################################목록에서 팔로우가 되어있는지, 않은지 확인################
                        if check_follow[index].text == '팔로잉':
                            continue

                        else:
                            # 그 계정을 팔로우 한다.
                            if self.enable_follow:
                                check_follow[index].click()
                                time.sleep(4)
                                self.add_amountwork.emit(1)
                                self.add_log.emit(1, get_id)

                            # 해당 계정으로 들어간다.
                            follower_list[index].click()
                            time.sleep(4)

                            if self.stop_thread:
                                break

                            ############################게시물이 있는지 확인 후 혹은 비공개 계정인지 확인###################
                            try:
                                selected_tags = WebDriverWait(driver=self.wdriver, timeout=10) \
                                    .until(lambda wdriver: wdriver.find_elements_by_xpath(
                                    "//div[@class='_mck9w _gvoze _f2mse']/a"))

                                # 최근 게시물 1개에 들어간다.
                                selected_tags[0].click()
                                time.sleep(4)

                            except Exception as exep:
                                print('what is error : 해당 계정에 게시물이 존재하지 않습니다.!')
                                self.wdriver.back()
                                continue
                            ###########################################################################################

                            if self.stop_thread:
                                break

                            ###################################좋아요 및 댓글 작업#######################################

                            try:
                                current_post = WebDriverWait(driver=self.wdriver, timeout=10) \
                                    .until(lambda wdriver: wdriver.find_element_by_xpath("//div[@class='_e3il2 _gxii9']/div/img"))
                                # 작업할 게시물의 사진을 보여준다.
                                url = current_post.get_attribute("src")
                                data = urllib.request.urlopen(url).read()
                                image = QtGui.QImage()
                                image.loadFromData(data)

                                if self.flag_manual_comment:
                                    self.mc.workingid = get_id
                                    # 직접 댓글 작성하는 화면에 사진과 글감을 띄움
                                    self.mc.mc_photozone.setPixmap(QtGui.QPixmap(image))
                                    self.mc.mc_photozone.setScaledContents(True)

                                    #이전에 이미 댓글을 달았다면~
                                    cm_list = WebDriverWait(driver=self.wdriver, timeout=10) \
                                        .until(lambda wdriver: wdriver.find_elements_by_xpath(
                                        "//ul[@class='_b0tqa']/li"))
                                    for xin in range(len(cm_list)):
                                        if cm_list[xin].get_attribute("title") == self.loginID:
                                            # 이미 이전에 댓글을 달았음
                                            self.existcomment = True
                                            self.wdriver.back()
                                            break

                                    if self.existcomment:
                                        self.existcomment = False
                                        continue

                                    if not self.mc_first:
                                        self.mc.loading_stop()

                                    self.mc_first = False
                                    self.mc.mc_posttext.setText(current_post.get_attribute("alt"))
                                    self.mc_complete = True
                                    time.sleep(3)

                                else:
                                    self.lbl_picture.setPixmap(QtGui.QPixmap(image))
                                    # if 중간에 댓글 직접달기를 한다면: 댓글 위젯 창에 사진과 글감을 올린다.
                                    self.lbl_picture.setScaledContents(True)
                                    time.sleep(3)

                                if self.stop_thread:
                                    break

                                # 좋아요를 누른다.
                                if self.enable_like:
                                    like_btn = WebDriverWait(driver=self.wdriver, timeout=10) \
                                        .until(lambda wdriver: wdriver.find_element_by_xpath("//a[@class='_eszkz _l9yih']/span"))

                                    like_btn.click()
                                    time.sleep(4)
                                    self.add_amountwork.emit(2)
                                    self.add_log.emit(2, get_id)

                            except Exception as exep:
                                print()

                            # 작업한 게시물로 카운트 한다.
                            total_work_count += 1

                            if self.stop_thread:
                                break

                            #######################################댓글 작업 ###########################################
                            if self.flag_manual_comment:
                                # 무한 대기 사용자가 직접 댓글 입력을 완료할 때까지...
                                while self.mc_complete:
                                    time.sleep(2)
                                # 작성이 완료되어 확인 버튼을 누르고 다음 행동

                            else:
                                # 이전에 이미 댓글을 달았다면~
                                cm_list = WebDriverWait(driver=self.wdriver, timeout=10) \
                                    .until(lambda wdriver: wdriver.find_elements_by_xpath(
                                    "//ul[@class='_b0tqa']/li"))
                                for xin in range(len(cm_list)):
                                    if cm_list[xin].get_attribute("title") == self.loginID:
                                        # 이미 이전에 댓글을 달았음
                                        self.existcomment=True
                                        self.wdriver.back()
                                        break
                                if self.existcomment:
                                    self.existcomment = False
                                    continue

                                comment_count = self.listwgt_commentlist.count()
                                if comment_count > 0 and self.enable_comment:
                                    ran_index = random.randrange(0, comment_count)

                                    try:
                                        # 랜덤으로 댓글을 가져와서 작성할 수 있도록 한다.
                                        comment_text = WebDriverWait(driver=self.wdriver, timeout=10) \
                                            .until(lambda wdriver: wdriver.find_element_by_xpath(
                                            "//textarea[@class='_bilrf']")).click()
                                        comment_text2 = WebDriverWait(driver=self.wdriver, timeout=10) \
                                            .until(lambda wdriver: wdriver.find_element_by_xpath("//textarea[@class='_bilrf']"))
                                        time.sleep(2)
                                        # temp = self.listwgt_commentlist.item(ran_index).text().encode('utf-8')
                                        # temp = u'\ud83d\udc4d'
                                        comment_text2.send_keys(self.listwgt_commentlist.item(ran_index).text())
                                        time.sleep(2)
                                        comment_text2.send_keys(Keys.RETURN)
                                        time.sleep(2)

                                        self.add_amountwork.emit(3)
                                        self.add_log.emit(3, get_id)

                                        if self.stop_thread:
                                            break

                                    except Exception as exep:
                                        print()

                            # 게시글에서 back 한다.
                            self.wdriver.back()
                            time.sleep(4)
                            ######################################댓글 작업 종료########################################
                            if self.stop_thread:
                                break

                            self.wdriver.back()
                            time.sleep(3)

                        # index_count += 1
                        if total_work_count == self.workamount:
                            break

                        if self.stop_thread:
                            break

                    if self.stop_thread:
                        break

                if self.stop_thread:
                    break

            if self.stop_thread:
                self.btn_start_n_stop_toggle(True)
                self.stop_thread = False
                self.add_log.emit(5, ' ')
                self.wdriver.get('https://instagram.com')
                break

    def btn_stop_job_clicked(self):
        if not self.stop_thread:
            self.stop_thread = True
            self.btn_start_n_stop_toggle(True)
            # self.wdriver.get('https://instagram.com')
        #self.listwgt_blacktag.show()
        # th = threading.Thread(target=self.round_tag_post)
        #print('fuckyou')

    def btn_start_n_stop_toggle(self, toggle):
        self.btn_stop_job.setEnabled(not(toggle))
        self.btn_start_job.setEnabled(toggle)
        self.linedit_hash.setEnabled(toggle)
        self.btn_srch_hashtag.setEnabled(toggle)
        self.btn_start_unfollowjob.setEnabled(toggle)


    def write_log(self, what_task, idname=None):
        # 팔로우(1), 좋아요(2), 댓글(3), -작업시작(4), 정지(5), 언팔(6), 검색(7), 다음 태그로 이동(8), 언팔 시작(9), 비공개 계정(10)
        # ## 님을 팔로우함, ## 님을 좋아요함, ## 님에게 댓글을 1 댓글을 씀
        # 작업 시작 함, 작업 정지 함, 언팔, 검색 함
        now = datetime.datetime.now()
        nowDatetime = now.strftime('[%Y.%m.%d %H:%M:%S]')
        if what_task == 1:
            # 팔로우 한 것
            text = nowDatetime + " - " + idname + " 팔로우"
            self.textedit_log.append(text)
        elif what_task == 2:
            # 좋아요 한 것
            text = nowDatetime + " - " + idname + " 좋아요"
            self.textedit_log.append(text)
        elif what_task == 3:
            # 댓글 단 것
            text = nowDatetime + " - " + idname + " 댓글 "
            self.textedit_log.append(text)
        elif what_task == 4:
            # 작업 시작
            text = nowDatetime + " - 작업 시작"
            self.textedit_log.append(text)
        elif what_task == 5:
            # 작업 정지
            text = nowDatetime + " - 작업 정지"
            self.textedit_log.append(text)
        elif what_task == 6:
            # 작업 정지
            text = nowDatetime + " - " + idname + " 언팔 "
            self.textedit_log.append(text)
        elif what_task == 7:
            # 검색
            text = nowDatetime + " - " + idname + " 검색"
            self.textedit_log.append(text)
        elif what_task == 8:
            # 이미 좋아요가 되어 있거나 50개 게시물 작업이 끝나면
            text = nowDatetime + " - " + idname + " 작업 이동"
            self.textedit_log.append(text)
        elif what_task == 9:
            # 이미 좋아요가 되어 있거나 50개 게시물 작업이 끝나면
            text = nowDatetime + " - 언팔 작업 시작"
            self.textedit_log.append(text)
        elif what_task == 10:
            # 이미 좋아요가 되어 있거나 50개 게시물 작업이 끝나면
            text = nowDatetime + " - " + idname + " 비공개 계정으로 다음 작업 이동"
            self.textedit_log.append(text)

        return

    def hashtabwgt_add_item(self, index, index2, itemtext):
        self.tabwgt_hashlist.setItem(index, index2, QTableWidgetItem(itemtext))


    def btn_tag_search_clicked(self):
        th = threading.Thread(target=self.thread_hash_retrieve)
        th.daemon = True
        th.start()
        # self.add_wgtlist.connect(self.hashtabwgt_add_item)

        # self.tag_search_thread = thread_hash_retrieve()

        # self.tag_search_thread.start()

    def thread_hash_retrieve(self):
        self.show_loading.emit()
        self.btn_start_n_stop_toggle(False)

        if self.option_search == 1:
            coustom = "#" + self.linedit_hash.text()
        elif self.option_search == 2:
            coustom = "%" + self.linedit_hash.text()
        else:
            coustom = self.linedit_hash.text()

        try:
            hashtag = WebDriverWait(driver=self.wdriver, timeout=10) \
                .until(lambda wdriver: wdriver.find_element_by_xpath("//input[@class='_avvq0 _o716c']"))
            hashtag.send_keys(' ')
            time.sleep(1)
            hashtag.clear()
            hashtag.clear()
            hashtag.send_keys(coustom.strip())
            time.sleep(1.5)
        except:
            self._popframe.close_lodingwgt.emit()
            self.btn_start_n_stop_toggle(True)

        try:
            searched_tag_name = WebDriverWait(driver=self.wdriver, timeout=5) \
                .until(lambda wdriver: wdriver.find_elements_by_xpath("//span[@class='_sgi9z']"))

            if (len(searched_tag_name) >= 1):

                # 검색된 태그 수 만큼 테이블의 로우를 늘려주고
                self.tabwgt_hashlist.setRowCount(len(searched_tag_name))

                # searched_tag_name = WebDriverWait(driver=wdriver, timeout=10) \
                #     .until(lambda wdriver: wdriver.find_elements_by_xpath("//span[@class='_sgi9z']"))
                # count = 0
                if self.option_search == 1:
                    try:
                        searched_tag_amount = WebDriverWait(driver=self.wdriver, timeout=7) \
                            .until(lambda wdriver: wdriver.find_elements_by_xpath("//div[@class='_sayjy']/span/span"))

                        for item_index in range(len(searched_tag_name)):
                            # 해당 1열에는 태그 이름과 2열에는 게시물 수
                            # 태그일 경우
                            self.add_wgtlist.emit(item_index, 0, searched_tag_name[item_index].text.replace('#', ''))
                            self.add_wgtlist.emit(item_index, 1, searched_tag_amount[item_index].text)

                        send_message = "태그: " + coustom.strip()
                        self.add_log.emit(7, send_message)

                    except Exception as exep:
                        print('what is error : do not load all searched tag..')
                        # self._popframe.close_lodingwgt.emit()
                elif self.option_search == 2:
                    self.loc_array.clear()
                    searched_tag_amount = WebDriverWait(driver=self.wdriver, timeout=7) \
                        .until(lambda wdriver: wdriver.find_elements_by_xpath("//span[@class='_sayjy']"))

                    loc_herf = WebDriverWait(driver=self.wdriver, timeout=7) \
                        .until(lambda wdriver: wdriver.find_elements_by_xpath("//a[@class='_gimca']"))

                    for item_index in range(len(searched_tag_name)):
                        # 해당 1열에는 태그 이름과 2열에는 게시물 수
                        self.add_wgtlist.emit(item_index, 0, searched_tag_name[item_index].text)
                        self.add_wgtlist.emit(item_index, 1, searched_tag_amount[item_index].text)
                        self.loc_array.append(loc_herf[item_index].get_attribute("href")[44:])

                    send_message = "장소: " + coustom.strip()
                    self.add_log.emit(7, send_message)

                else:
                    try:
                        searched_tag_amount = WebDriverWait(driver=self.wdriver, timeout=7) \
                            .until(lambda wdriver: wdriver.find_elements_by_xpath("//span[@class='_sayjy']"))

                        for item_index in range(len(searched_tag_name)):
                            # 해당 1열에는 태그 이름과 2열에는 게시물 수
                            # if not searched_tag_name[item_index].text:
                            self.add_wgtlist.emit(item_index, 0, searched_tag_name[item_index].text.replace('#', ''))
                            # if not searched_tag_amount[item_index].text:
                            try:
                                self.add_wgtlist.emit(item_index, 1, searched_tag_amount[item_index].text)
                            except:
                                print()

                        send_message = "아이디: " + coustom.strip()
                        self.add_log.emit(7, send_message)

                    except Exception as exep:
                        print('what is error : do not load all searched tag..')

                self._popframe.close_lodingwgt.emit()
                self.btn_start_n_stop_toggle(True)

        except Exception as exep:
            print("검색된 해시태그가 없거나 검색이 제대로 이루어 지지 않았음")
            self.show_message.emit("검색 오류", "해당 검색어에 대한 내용이 검색되지 않았습니다.!!")
            self._popframe.close_lodingwgt.emit()
            self.btn_start_n_stop_toggle(True)
            # QMessageBox.about(self, "Error", "There is error! please check hash name and code")

    def radiobtn_follower_clicked(self):
        self.groupbox_follow_based.setEnabled(True)
        self.groupbox_tag_based.setEnabled(False)


    def btn_add_tag_clicked(self):
        # 검색된 태그에서 태그를 선택 후 추가하기 버튼
        # 리스트 박스(self.listwgt_sel_hashlist)에 태그가 추가된다.

        # 테이블에서 선택된 아이템이 있는지 검사. 없다면 아무 동작 하지 않음.
        if self.tabwgt_hashlist.currentRow() == -1:
            QMessageBox.about(self, "선택", "추가할 태그를 먼저 선택하세요.")
            return

        print(self.tabwgt_hashlist.item(self.tabwgt_hashlist.currentRow(), 0).text())
        if not self.tabwgt_hashlist.item(self.tabwgt_hashlist.currentRow(), 0).text():
            return

        # 이미 추가된 태그가 1개 이상 있다면, 중복되는 태그가 있는지 확인
        if not self.listwgt_sel_hashlist.count() < 1:
            table_tag = self.tabwgt_hashlist.item(self.tabwgt_hashlist.currentRow(), 0).text()
            for index in range(self.listwgt_sel_hashlist.count()):
                if table_tag == self.listwgt_sel_hashlist.item(index).text()[5:]:
                    QMessageBox.about(self, "중복", "해당 태그가 이미 리스트에 추가되어 있습니다.")
                    return

        if self.option_search == 1:
            temp_text = "[태그] " + self.tabwgt_hashlist.item(self.tabwgt_hashlist.currentRow(), 0).text()
        elif self.option_search == 2:
            searname = self.tabwgt_hashlist.item(self.tabwgt_hashlist.currentRow(), 0).text()
            temp_text = "[장소] " + searname
            self.loc_dictionary[searname] = self.loc_array[self.tabwgt_hashlist.currentRow()]
            print(self.loc_dictionary[searname])
        else:
            temp_text = "[ID] " + self.tabwgt_hashlist.item(self.tabwgt_hashlist.currentRow(), 0).text()


        self.listwgt_sel_hashlist.addItem(temp_text)
        if self.detail_comment:
            # 상세 댓글 설정 기능이 ON 되어 있다면,
            self.listwgt_comment_tag.addItem(self.tabwgt_hashlist.item(self.tabwgt_hashlist.currentRow(), 0).text())

    # 수동으로 댓글을 작성을 위해서 직접 댓글 작성 버튼 클릭시 호출 함수
    def btn_manualcomment_clicked(self):
        # 직접 작성을 하겠다는 것을 판별할 수 있는 변수
        self.flag_manual_comment = True
        # 사용자가 사진과 글감이 모두 불러 온 후에 작성할 수 있도록 하는 변수
        self.mc_complete = False
        self.mc = Manual_Comment(self)
        self.mc.show()
        self.mc_first = True


    def btn_add_alltag_clicked(self):
        # sel hash tag list 에 아이템이 한 개라도 있으면 중복 검사하며 추가
        if not self.listwgt_sel_hashlist.count() < 1:
            if not self.tabwgt_hashlist.rowCount() < 1:
                for tag_index in range(self.tabwgt_hashlist.rowCount()):
                    table_tag = self.tabwgt_hashlist.item(tag_index, 0).text()
                    if not table_tag == '':
                        validation = True
                        for index in range(self.listwgt_sel_hashlist.count()):
                            if table_tag == self.listwgt_sel_hashlist.item(index).text():
                                # 일치하는 것이 하나 있으면 for 문을 빠져나와서 다음 table item 을 검사한다.
                                validation = False
                                break
                                # table_tag = self.tabwgt_hashlist.item(self.tabwgt_hashlist.currentRow(), 0).text()
                        if validation:
                            if self.option_search == 1:
                                temp_text = "[태그] " + table_tag
                            elif self.option_search == 2:
                                # searname = self.tabwgt_hashlist.item(table_tag, 0).text()
                                temp_text = "[장소] " + table_tag
                                self.loc_dictionary[table_tag] = self.loc_array[tag_index]
                                print(self.loc_dictionary[table_tag])
                            else:
                                temp_text = "[ID] " + table_tag
                            self.listwgt_sel_hashlist.addItem(temp_text)
            return

        # sel hash tag list 에 아이템이 한 개도 없으면 중복 검사 없이 모두 추가
        else:
            for tag_index in range(self.tabwgt_hashlist.rowCount()):
                tagname=self.tabwgt_hashlist.item(tag_index, 0).text()
                if self.option_search == 1:
                    temp_text = "[태그] " + tagname
                elif self.option_search == 2:
                    # searname = self.tabwgt_hashlist.item(table_tag, 0).text()
                    temp_text = "[장소] " + tagname
                    self.loc_dictionary[tagname] = self.loc_array[tag_index]
                    print(self.loc_dictionary[tagname])
                else:
                    temp_text = "[ID] " + tagname
                self.listwgt_sel_hashlist.addItem(temp_text)
                # self.listwgt_sel_hashlist.addItem(self.tabwgt_hashlist.item(tag_index, 0).text())
                if self.detail_comment:
                    # 상세 댓글 설정 기능이 ON 되어 있다면,
                    self.listwgt_comment_tag.addItem(self.tabwgt_hashlist.item(tag_index, 0).text())

    def btn_add_comment_clicked(self):
        if self.listwgt_comment_tag.currentRow() == -1:
            self.listwgt_comment_tag.setCurrentRow(0)

        if self.linedit_comment.text().strip() == '':
            QMessageBox.about(self, "공백 오류", "추가할 댓글에 공백을 입력할 수 없습니다.")
            return
        self.listwgt_commentlist.addItem(self.linedit_comment.text())

        if self.detail_comment:
            # if 해당 태그의 리스트가 존재하는지
            testarray = []
            testarray.append("테스트지")
            testarray.append("테스트얌")
            testarray.append("테스트일껄?")


    def btn_del_comment_clicked(self):
        item = self.listwgt_commentlist.takeItem(self.listwgt_commentlist.currentRow())
        self.listwgt_commentlist.removeItemWidget(item)


    def btn_del_tag_clicked(self):
        # self.listwgt_sel_hashlist.removeItemWidget(self.listwgt_sel_hashlist.selectedItems())
        # print(self.tabwgt_hashlist.rowCount())
        index = self.listwgt_sel_hashlist.currentRow()
        item = self.listwgt_sel_hashlist.takeItem(index)
        # 장소에 대한 삭제면, 딕셔너리도 같이 삭제
        try:
            if '[장소]' in item.text():
                # 해당 장소 태그의 딕셔너리 제거
                del self.loc_dictionary[item.text()[5:]]
        except:
            print()
        self.listwgt_sel_hashlist.removeItemWidget(item)

        if self.detail_comment:
            # 상세 댓글 설정 기능이 ON 되어 있다면,
            citem = self.listwgt_comment_tag.takeItem(index)
            self.listwgt_comment_tag.removeItemWidget(citem)


    def btn_worktimeset_clicked(self):
        self.amountof_comment = int(self.linedit_amountcomment.text())
        self.amountof_like = int(self.linedit_amountlike.text())
        self.amountof_follow = int(self.linedit_amoutfollow.text())

    def menu_actionmanual_clicked(self):
        os.system('explorer http://ahs1419083.blog.me/221143156173')

    def menu_actiontools_closed(self):
        print('close window')

        self.wdriver.switch_to_window(self.wdriver.window_handles[0])

    def menu_actiondetail_clicked(self):
        detailed_setting = Win_DetailedSetting(self)
        detailed_setting.show()

    def get_today_amount_work(self):
        # 처음 프로그램을 구동할 때 호출되는 함수
        # 오늘의 작업량을 불러오고 기준 시간은 한국 시간 자정(12시)로 이때를 지나면 리셋 됨
        # 몇 분마다 체크하는 기능이 필요
        load_date = datetime.datetime.strptime(linecache.getline('IMSData.txt', 2), '%Y-%m-%d ').date()
        now_date = datetime.datetime.now().date()
        result = now_date - load_date
        if result.days > 0:
            self.enable_comment = True
            self.enable_follow = True
            self.enable_like = True
            self.enable_unfollow = True
            # 만약 하루의 날짜가 지났다면, 새로운 카운트 시작
            self.today_follow = 0
            self.today_like = 0
            self.today_comment = 0
            self.today_unfollow = 0
            with open('IMSData.txt', 'w') as file:
                data = ["[Last_Time]\n", datetime.datetime.now().strftime('%Y-%m-%d') + "\n", "[Toady_Work_Amount]\n", \
                        str(self.today_follow) + "\n", str(self.today_like) + "\n", str(self.today_comment) + "\n",
                        str(self.today_unfollow)]
                file.writelines(data)
        else:
            # 만약 하루가 지나지 않았다면, 기존 값 불러옴
            self.today_follow = int(linecache.getline('IMSData.txt', 4))
            self.today_like = int(linecache.getline('IMSData.txt', 5))
            self.today_comment = int(linecache.getline('IMSData.txt', 6))
            self.today_unfollow = int(linecache.getline('IMSData.txt', 7))

        # 사용자가 셋팅한 개수 값을 불러온다.
        self.amountof_comment = int(self.linedit_amountcomment.text())
        self.amountof_like = int(self.linedit_amountlike.text())
        self.amountof_follow = int(self.linedit_amoutfollow.text())

        # 오늘 하루 작업한 양을 불러와야 한다. 임시로 초기화
        # 만약 하루가 지나지 않았다면 이전에 한 작업량에 대해서 저장을 해두어야 한다.


        self.today_text = '팔로우 : ' + str(self.today_follow) + ' 개'
        self.lbl_today_follow.setText(self.today_text)

        self.today_text = '좋아요 : ' + str(self.today_like) + ' 개'
        self.lbl_today_like.setText(self.today_text)

        self.today_text = ' 댓글  : ' + str(self.today_comment) + ' 개'
        self.lbl_today_comment.setText(self.today_text)

        self.today_text = ' 언팔  : ' + str(self.today_unfollow) + ' 개'
        self.lbl_today_unfollow.setText(self.today_text)

    def update_today_amount_work(self, what_task):
        # 시작시 오늘의 작업량 값을 가져옴
        # 작업 때마다 lbl 값을 바꾸어줌
        if what_task == 1:
            if self.today_follow > self.amountof_follow:
                # QMessageBox.about(self, "작업 종료", "오늘의 팔로우 양을 모두 끝내셨습니다.")
                self.enable_follow = False
                return
            self.today_follow += 1
            self.today_text = '팔로우 : ' + str(self.today_follow) + ' 개'
            self.lbl_today_follow.setText(self.today_text)
        elif what_task == 2:
            if self.today_like > self.amountof_like:
                # QMessageBox.about(self, "작업 종료", "오늘의 좋아요 양을 모두 끝내셨습니다.")
                self.enable_like = False
                return
            self.today_like += 1
            self.today_text = '좋아요 : ' + str(self.today_like) + ' 개'
            self.lbl_today_like.setText(self.today_text)
        elif what_task == 3:
            if self.today_comment > self.amountof_comment:
                # QMessageBox.about(self, "작업 종료", "오늘의 댓글 양을 모두 끝내셨습니다.")
                self.enable_comment = False
                return
            self.today_comment += 1
            self.today_text = ' 댓글  : ' + str(self.today_comment) + ' 개'
            self.lbl_today_comment.setText(self.today_text)
        elif what_task == 4:
            if self.today_unfollow > self.amountof_follow:
                # QMessageBox.about(self, "작업 종료", "오늘의 언팔 양을 모두 끝내셨습니다.")
                self.enable_unfollow = False
                return
            self.today_unfollow += 1
            self.today_text = ' 언팔  : ' + str(self.today_unfollow) + ' 개'
            self.lbl_today_unfollow.setText(self.today_text)


    def btn_start_unfollowjob_clicked(self):
        th = threading.Thread(target=self.thread_unfollow)
        th.daemon = True
        th.start()
        self.btn_start_n_stop_toggle(False)

    def thread_unfollow(self):
        try:
            self.stop_thread = False
            self._popframe.set_progressbar()
            self.show_loading.emit()
            self.add_log.emit(9, '')
            self.wdriver.get('https://instagram.com/' + self.loginID)
            time.sleep(2)
        except:
            if self.stop_thread:
                self.btn_start_n_stop_toggle(True)
                self.stop_thread = False
                self._popframe.set_off_progressbar()
                self._popframe.close_lodingwgt.emit()
                self.wdriver.get('https://instagram.com')
                return

        if self.stop_thread:
            self.btn_start_n_stop_toggle(True)
            self.stop_thread = False
            self._popframe.set_off_progressbar()
            self._popframe.close_lodingwgt.emit()
            self.wdriver.get('https://instagram.com')
            return

        try:
            # 팔로워 리스트에 팔로우 숫자를 가져옴
            follower_count = WebDriverWait(driver=self.wdriver, timeout=7) \
                .until(lambda wdriver: wdriver.find_elements_by_xpath("//span[@class='_fd86t']"))

            # 팔로워 목록을 클릭
            WebDriverWait(driver=self.wdriver, timeout=10) \
                .until(lambda wdriver: wdriver.find_elements_by_xpath("//a[@class='_t98z6']"))[0].click()
            time.sleep(1)

            # 스크롤을 팔로워 숫자 만큼 내리고 최대는 1천명 까지이다.
            followerscroll = WebDriverWait(driver=self.wdriver, timeout=10) \
                .until(lambda wdriver: wdriver.find_element_by_xpath("//div[@class='_gs38e']"))
            time.sleep(1)

        except:
            if self.stop_thread:
                self.btn_start_n_stop_toggle(True)
                self.stop_thread = False
                self._popframe.set_off_progressbar()
                self._popframe.close_lodingwgt.emit()
                self.wdriver.get('https://instagram.com')
                return

        if self.stop_thread:
            self.btn_start_n_stop_toggle(True)
            self.stop_thread = False
            self._popframe.set_off_progressbar()
            self._popframe.close_lodingwgt.emit()
            self.wdriver.get('https://instagram.com')
            return

        following_cnt = 0
        if follower_count[2].text.find(',') > 0:
            following_cnt = int(follower_count[2].text.replace(',', '').strip())
            # print(following_cnt)
        else:
            following_cnt = int(follower_count[2].text)
        print(following_cnt)

        # 인스타그램 해당 텍스트에는 139,500 이렇게 쉼표가 들어가있는데 이럴 경우 int 변환 불가
        if follower_count[1].get_attribute("title").find(',') > 0:
            folcount = 1000
        else:
            folcount = int(follower_count[1].get_attribute("title"))

        print(folcount)

        scroll_count = folcount // 10
        # print(scroll_count)
        total_prs = 0
        if scroll_count >= 100:
            overnumber = True
            scroll_prs = 50 / 100
        else:
            overnumber = False
            scroll_prs = 50 / scroll_count

        for scount in range(0, scroll_count):
            if scount >= 100:
                break

            self.wdriver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followerscroll)
            time.sleep(1)
            total_prs += scroll_prs
            print(total_prs)
            self._popframe.update_progress.emit(total_prs)

            if self.stop_thread:
                break

        if self.stop_thread:
            self.btn_start_n_stop_toggle(True)
            self.stop_thread = False
            self._popframe.set_off_progressbar()
            self._popframe.close_lodingwgt.emit()
            self.wdriver.get('https://instagram.com')
            return

        # 현재까지 스크롤한 팔로워 리스트를 불러온다.
        follower_list = WebDriverWait(driver=self.wdriver, timeout=10) \
            .until(lambda wdriver: wdriver.find_elements_by_xpath("//div[@class='_2nunc']/a"))
        if overnumber:
            if len(follower_list) < 500:
                # print('인스타에서 block 으로 제대로 팔로우를 불러오지 못했다.')
                self.show_message.emit("트래픽 초과", "많은 작업량으로 인스타 로딩 트레픽이 초과되었습니다. 잠시 후 다시 시도해주세요.")
                # print('많은 작업량으로 인스타 로딩 트레픽이 초과되었습니다. 잠시 후 다시 시도해주세요.')
                self._popframe.set_off_progressbar()
                self._popframe.close_lodingwgt.emit()
                return

        else:
            if len(follower_list) < (folcount-10):
                # print('인스타에서 block 으로 제대로 팔로우를 불러오지 못했다.')
                self.show_message.emit("트래픽 초과", "많은 작업량으로 인스타 로딩 트레픽이 초과되었습니다. 잠시 후 다시 시도해주세요.")
                self._popframe.set_off_progressbar()
                self._popframe.close_lodingwgt.emit()
                return

        if len(follower_list) >= 1000:
            scroll_prs = 50 / 1000
        else:
            scroll_prs = 50 / len(follower_list)

        id_list = []
        # 일단 max 2천명 정도 가져오자
        for index_count in range(len(follower_list)):
            if index_count == 1000:
                # max 를 넘어섰으니 여기까지만
                break
            print(follower_list[index_count].text)
            # if not follower_list[index_count].text: break
            try:
                id_list.append(follower_list[index_count].text)
                total_prs += scroll_prs
                self._popframe.update_progress.emit(total_prs)
            except:
                total_prs = 100
                self._popframe.update_progress.emit(total_prs)
                break

            if self.stop_thread:
                break

        if self.stop_thread:
            self.btn_start_n_stop_toggle(True)
            self.stop_thread = False
            self._popframe.set_off_progressbar()
            self._popframe.close_lodingwgt.emit()
            self.wdriver.get('https://instagram.com')
            return

        # 다시 뒤로 가서 팔로우 목록으로 간다.
        self.wdriver.back()
        self._popframe.set_off_progressbar()
        #############################팔로우랑 비교할 팔로워 목록 불러오기 ############################################

        while True:
            WebDriverWait(driver=self.wdriver, timeout=10) \
                .until(lambda wdriver: wdriver.find_elements_by_xpath("//a[@class='_t98z6']"))[1].click()
            time.sleep(2)
            if self.stop_thread:
                break

            follower_button_list = None

            for index in range(0, 10000):
                if not self.enable_unfollow:
                    self.show_message.emit("작업량 초과", "오늘의 언팔 작업량을 초과하였습니다.")
                    self.stop_thread = True
                    break

                if self.stop_thread:
                    break
                try:
                    # real_index = index % 10
                    if index % 10 == 0:
                        # self.wdriver.refresh()
                        # time.sleep(2)
                        # WebDriverWait(driver=self.wdriver, timeout=10) \
                        #     .until(lambda wdriver: wdriver.find_elements_by_xpath("//a[@class='_t98z6']"))[1].click()
                        # time.sleep(1)
                        # print('scoll reload')
                        followerscroll = WebDriverWait(driver=self.wdriver, timeout=10) \
                            .until(lambda wdriver: wdriver.find_element_by_xpath("//div[@class='_gs38e']"))
                        time.sleep(1)
                        self.wdriver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followerscroll)
                        time.sleep(5)
                        if self.stop_thread:
                            break

                        # 현재까지 불러온 팔로우!! 목록들을 다시 가져온다,.
                        follower_list = WebDriverWait(driver=self.wdriver, timeout=10) \
                            .until(lambda wdriver: wdriver.find_elements_by_xpath("//div[@class='_2nunc']/a"))
                        time.sleep(1)
                        print('follow list ok')
                        follower_button_list = WebDriverWait(driver=self.wdriver, timeout=10) \
                            .until(lambda wdriver: wdriver.find_elements_by_xpath("//div[@class='_mtnzs']/span/button"))
                        print('follow button list ok')
                        time.sleep(10)

                except:
                    # 알 수 없는 에러가 떴다 그럼 뒤로 가기 하거나, 새롭게 창을 불러오거나
                    # self.wdriver.back()
                    self.wdriver.get('https://instagram.com/' + self.loginID)
                    time.sleep(2)
                    break

                if self.stop_thread:
                    break

                try:
                    if any(follower_list[index].text in temps for temps in id_list):
                        print(follower_list[index].text + '    is exist')
                        # 팔로워 목록에 존재한다. 그럼 넘어감
                        # continue

                    else:
                        # 팔로워 목록에 존재하지 않는다. 그럼 언팔
                        follower_button_list[index].click()
                        time.sleep(1)
                        print('unfollow : ')
                        get_id = follower_list[index].get_attribute("title")
                        print(get_id)
                        time.sleep(1)
                        self.add_amountwork.emit(4)
                        self.add_log.emit(6, get_id)
                        if self.stop_thread:
                            break
                        time.sleep(30)

                except Exception as exep:
                    # 작업이 follower list 에 담을 수 있는 수 초과 또는 오류
                    self.wdriver.back()
                    break

                # 팔로잉 수 만큼 작업이 모두 완료되었으면 종료
                if (following_cnt-1) == index:
                    self.show_message.emit("작업 완료", "언팔 작업을 완료하였습니다.")

                if self.stop_thread:
                    break

            if self.stop_thread:
                break

        if self.stop_thread:
            self.btn_start_n_stop_toggle(True)
            self._popframe.close_lodingwgt.emit()
            self.stop_thread = False
            self.wdriver.get('https://instagram.com')
            return

    def set_toggle_comment(self, detailed):
        if detailed:
            # 디테일 댓글 기능이 활성화 되어있다면, UI 변경
            self.linedit_comment.setGeometry(120, 10, 311, 31)
            self.listwgt_comment_tag.setGeometry(10, 20, 101, 111)
            self.listwgt_commentlist.setGeometry(120, 60, 311, 71)

        else:
            self.listwgt_comment_tag.hide()
            self.linedit_comment.setGeometry(10, 10, 431, 31)
            self.listwgt_commentlist.setGeometry(10, 50, 431, 71)
            # 저장 없이 변경되면 기존에 작성한 댓글들이 모두 삭제됩니다. 저장하시겠습니까 ?
            # 디테일 댓글 기능이 활성화 X, UI 변경


    def selected_comment_tagitem(self):
        #print(self.listwgt_sel_hashlist.currentRow())
        print('yo focus!!! complete!')

    def show_MessageBox(self, title, content):
        QMessageBox.about(self, title, content)

    def window_block(self, title, content):
        QMessageBox.about(self, title, content)

    def comment_checkbox_clicked(self):
        if self.chk_comment.checkState() == 0:
            print('댓글기능 off')
            self.groupbox_comment.setEnabled(False)
            self.enable_comment = False
        else:
            print('댓글기능 on')
            self.groupbox_comment.setEnabled(True)
            self.enable_comment = True

    def like_checkbox_clicked(self):
        if self.chk_like.checkState() == 0:
            print('라이크 기능 off')
            self.enable_like = False

        else:
            print('라이크 기능 on')
            self.enable_like = True

    def follow_checkbox_clicked(self):
        if self.chk_follow.checkState() == 0:
            print('팔로우 기능 off')
            self.enable_follow = False

        else:
            print('팔로우 기능 on')
            self.enable_follow = True

    def manual_lognamount(self):
        print('yes')

    def get_blacktag_workcount(self):
        with open('IMSWorkcount.txt', 'r') as file:
            wline=file.readline()
            self.workamount = int(wline)

        with open('IMSBlockcomment.txt', 'r') as file:
            while True:
                line = file.readline()
                if not line: break
                self.listwgt_hblacktag.addItem(line.strip())

    def get_commentntag(self):
        with open('IMSComment.txt', 'r') as file:
            while True:
                line = file.readline()
                if not line : break
                self.listwgt_commentlist.addItem(line.strip())

        with open('IMSTag.txt', 'r') as file:
            while True:
                line = file.readline()
                if not line : break
                self.listwgt_sel_hashlist.addItem(line.strip())

        with open('IMSLocdic.txt', 'r') as file:
            while True:
                line = file.readline()
                if not line : break
                self.loc_dictionary[line.split('/')[0].strip()] = line.split('/')[1].strip()


    def rsvtime_start(self):
        # 만약에 작업이 동작중이라면, 작업정지를 누른 후에 작업 시작
        if not self.stop_thread:
            # 동작중이다. 멈추고 일정 시간 동안 기다린다.
            self.btn_stop_job_clicked()
            # self.stop_thread = True
            time.sleep(10)

        # 그리고 round 쓰레드를 실행한다.
        th = threading.Thread(target=self.round_tag_post)
        th.daemon = True
        th.start()

    def rsvtime_stop(self):
        if not self.stop_thread:
            # 동작중이다. 멈추고 일정 시간 동안 기다린다.
            self.btn_stop_job_clicked()
            # self.stop_thread = True
            time.sleep(10)

    def rsvtime_start_unfollow(self):
        if not self.stop_thread:
            # 동작중이다. 멈추고 일정 시간 동안 기다린다.
            self.btn_stop_job_clicked()
            # self.stop_thread = True
            time.sleep(10)

        # 그리고 round 쓰레드를 실행한다.
        th = threading.Thread(target=self.thread_unfollow)
        th.daemon = True
        th.start()

    def rsvtime_stop_unfollow(self):
        if not self.stop_thread:
            # 동작중이다. 멈추고 일정 시간 동안 기다린다.
            self.btn_stop_job_clicked()
            time.sleep(10)

class Manual_Comment(QWidget, D_ManualComment.Ui_Form):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("댓글 직접 작성 화면")
        self.show()

        self.parent = parent
        self.workingid = ''

        self.mc_comment.returnPressed.connect(self.btn_complete_comment)
        self.mc_btn_write.clicked.connect(self.btn_complete_comment)

        self._poploading = loadingwgt(self)
        self._poploading.move((self.width() / 2) - 75, (self.height() / 2) - 75)
        self._poploading.resize(150, 150)

    def loading_show(self):
        self._poploading.show()

    def loading_stop(self):
        self._poploading.close_lodingwgt.emit()

    def btn_complete_comment(self):
        if self.parent.mc_complete:
            self.loading_show()
            if self.mc_comment.text().strip() == '':
                self.parent.mc_complete = False

            else:
                try:
                    comment_text = WebDriverWait(driver=self.parent.wdriver, timeout=10) \
                        .until(lambda wdriver: wdriver.find_element_by_xpath(
                        "//textarea[@class='_bilrf']")).click()
                    comment_text2 = WebDriverWait(driver=self.parent.wdriver, timeout=10) \
                        .until(lambda wdriver: wdriver.find_element_by_xpath(
                        "//textarea[@class='_bilrf']"))
                    time.sleep(1)
                    comment_text2.send_keys(self.mc_comment.text())
                    comment_text2.send_keys(Keys.RETURN)
                    time.sleep(2)

                    self.parent.add_amountwork.emit(3)
                    self.parent.add_log.emit(3, self.workingid)
                    print('comment writing is completed manually')

                except Exception as exep:
                    print('comment error')

                self.parent.mc_complete = False


    def closeEvent(self, event):
        self.parent.flag_manual_comment = False
        self.parent.mc_complete = False


class loadingwgt(QWidget):
    close_lodingwgt = pyqtSignal()
    update_progress = pyqtSignal(int)
    validation_win = pyqtSignal(str)

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        # make the window frameless
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.fillColor = QtGui.QColor(30, 30, 30, 120)
        self.penColor = QtGui.QColor("#333333")

        self.par = parent
        # 현재 계정 인증상황인지 아닌지를 알수 있음 True = 인증중 False = 인증중 아님
        self.blackorwhite = False
        self.onefail = False

        self.statustext = QtWidgets.QLabel(self)
        self.statustext.setVisible(False)
        self.statustext.move(0, 130)

        self.subjecttext = QtWidgets.QLabel(self)
        self.subjecttext.setVisible(False)
        self.subjecttext.move(0, 10)

        self.progress = QtWidgets.QProgressBar(self)
        self.progress.setVisible(False)

        self.securitycodeinput = QLineEdit(self)
        self.securitycodeinput.setVisible(False)

        self.secsendbtn = QPushButton('제출', self)
        self.secsendbtn.setVisible(False)

        self.receiv_btn = QPushButton('보안 코드 보내기', self)
        self.receiv_btn.setVisible(False)

        self.rdo_btn = QRadioButton('이메일', self)
        self.rdo_btn.setVisible(False)

        self.rdo_btn_2 = QRadioButton('휴대폰', self)
        self.rdo_btn_2.setVisible(False)

        self.errormsg = QtWidgets.QLabel(self)
        self.errormsg.setVisible(False)
        self.errormsg.setStyleSheet("color: rgb(255, 0, 0);")

        self.close_lodingwgt.connect(self._onclose)
        self.update_progress.connect(self.change_pv_value)
        self.validation_win.connect(self.sel_validation)
        self.secsendbtn.clicked.connect(self.submit_seccode)
        self.receiv_btn.clicked.connect(self.send_seccode)
        # self.show_loadingwgt.connect(self.show)
        #self.SIGNALS = TranslucentWidgetSignals()

    def set_off_progressbar(self):
        self.progress.setVisible(False)
        self.progress.setValue(0)

    def set_progressbar(self):
        self.progress.setVisible(True)
        self.progress.setGeometry(0, 0, 150, 20)
        self.progress.setValue(0)
        self.progress.setStyleSheet("""QProgressBar
        {
            border: 2px solid grey;
            border-radius: 5px;
            text-align: center;
            color: red;
        }
        QProgressBar::chunk 
        { 
            background: black; 
        }
        """)
        # self.progress.move(0, 0)
        # self.resize(300, 200)
        # self.progress.show()
        # self.progress.setValue(100)

    def setstatustext(self):
        self.statustext.setVisible(True)
        self.statustext.setText("프로그램 사용 권한을 확인중입니다.")
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(True)
        self.statustext.setAlignment(Qt.AlignCenter)
        self.statustext.setFont(font)
        self.statustext.setStyleSheet("color: rgb(0, 0, 0)")
        self.statustext.setFixedSize(300, 20)

    def set_instalogintext(self):
        self.statustext.setVisible(True)
        self.statustext.move(0, 130)
        self.statustext.setText("인스타그램 계정에 로그인중입니다.")

    def resizeEvent(self, event):
        s = self.size()
        popup_width = 300
        popup_height = 140
        ow = int(s.width() / 2 - popup_width / 2)
        oh = int(s.height() / 2 - popup_height / 2)
        # self.close_btn.move(ow + 265, oh + 5)

    def sel_validation(self, text):
        self.killTimer(self.timer)
        self.resize(300, 280)
        self.blackorwhite = True

        # 텍스트 계정 보안을 위해~~~~~~코드를 받을 방법을 선택하세요.
        font = QtGui.QFont()
        font.setPixelSize(14)
        font.setBold(False)
        self.statustext.setWordWrap(True)
        self.statustext.setVisible(True)
        self.statustext.setFont(font)
        self.statustext.setFixedSize(300, 40)
        self.statustext.move(0, 45)
        # self.statustext.setFixedSize(300, 20)
        self.statustext.setText(text)

        # 메일 또는 핸드폰 선택을 위한 라디오 버튼 _q0nt5
        radio_text = WebDriverWait(driver=self.par.parentwindow.wdriver, timeout=5) \
            .until(lambda wdriver: wdriver.find_elements_by_xpath("//div[@class='_im958']/label"))
        print(len(radio_text))
        for index in range(len(radio_text)):
            if index == 0:
                self.rdo_btn.setVisible(True)
                self.rdo_btn.setFont(font)
                self.rdo_btn.setFixedSize(300, 30)
                self.rdo_btn.move(50, 90)
                self.rdo_btn.setText(radio_text[index].text)
            else:
                self.rdo_btn_2.setVisible(True)
                self.rdo_btn_2.setFont(font)
                self.rdo_btn_2.setFixedSize(300, 30)
                self.rdo_btn_2.move(50, 110)
                self.rdo_btn_2.setText(radio_text[index].text)

        # 보안 코드 보내기 버튼
        self.receiv_btn.setVisible(True)
        self.receiv_btn.setFixedSize(250, 30)
        self.receiv_btn.move(25, 150)
        self.receiv_btn.setStyleSheet("""QPushButton
                {
                    background-color: rgb(44, 143, 255);
                    color: rgb(255, 255, 255);
                    border: 0px;
                    solid red;
                }
                QPushButton::pressed
                {
                    background-color: rgba(44, 143, 255, 200);
                }
                """)
        self.update()

    def set_validationwin(self, text):

        # 이전 라디오 버튼들과 보안 코드 보내기 버튼 숨김
        self.receiv_btn.setVisible(False)
        self.rdo_btn.setVisible(False)
        self.rdo_btn_2.setVisible(False)

        font = QtGui.QFont()
        font.setPixelSize(20)
        font.setBold(True)
        self.subjecttext.setAlignment(Qt.AlignCenter)
        self.subjecttext.setFont(font)
        self.subjecttext.setStyleSheet("color: rgb(0, 0, 0)")
        self.subjecttext.setFixedSize(300, 20)
        self.subjecttext.setVisible(True)
        self.subjecttext.move(0, 5)
        self.subjecttext.setText("보안 코드 입력")

        self.statustext.setText(text)

        self.securitycodeinput.setVisible(True)
        self.securitycodeinput.setPlaceholderText(" 띄어쓰기 없이 보안코드를 입력해 주세요.")
        self.securitycodeinput.setFixedSize(290, 40)
        self.securitycodeinput.move(5, 110)
        # self.securitycodeinput.setFrame(False)
        self.securitycodeinput.setMaxLength(6)
        font.setPixelSize(15)
        font.setBold(False)
        self.securitycodeinput.setAlignment(Qt.AlignCenter)
        self.securitycodeinput.setFont(font)

        self.secsendbtn.setVisible(True)
        self.secsendbtn.setFixedSize(250, 30)
        self.secsendbtn.move(25, 185)
        self.secsendbtn.setStyleSheet("""QPushButton
        {
            background-color: rgb(44, 143, 255);
            color: rgb(255, 255, 255);
            border: 0px;
            solid red;
        }
        QPushButton::pressed
        {
            background-color: rgba(44, 143, 255, 200);
        }
        """)
        self.update()

    def send_seccode(self):
        # 현재 선택한 라디오 버튼의 값을 불러와서 선택한다.
        try:

            if self.rdo_btn.isChecked():
                # 이메일로 라디오버튼이 선택됬다.
                WebDriverWait(driver=self.par.parentwindow.wdriver, timeout=5) \
                    .until(lambda wdriver: wdriver.find_element_by_xpath("//label[@for='choice_1']")).click()
            else:
                # 휴대폰으로 라디오버튼이 선택됬다.
                WebDriverWait(driver=self.par.parentwindow.wdriver, timeout=5) \
                    .until(lambda wdriver: wdriver.find_element_by_xpath("//label[@for='choice_0']")).click()

            # 보안 코드 보내기 버튼을 클릭한다.
            WebDriverWait(driver=self.par.parentwindow.wdriver, timeout=5) \
                .until(lambda wdriver: wdriver.find_element_by_xpath("//button[text()='보안 코드 보내기']")).click()

            WebDriverWait(driver=self.par.parentwindow.wdriver, timeout=5) \
                .until(lambda wdriver: wdriver.find_element_by_xpath("//h2[text()='보안 코드 입력']"))

            header_text = WebDriverWait(driver=self.par.parentwindow.wdriver, timeout=5) \
                .until(lambda wdriver: wdriver.find_element_by_xpath("//div[@class='_bzfgt _mpcv6']/p"))  # _3574j
            self.set_validationwin(header_text.text)

        except:
            self.statustext.setVisible(False)
            self.receiv_btn.setVisible(False)
            self.rdo_btn.setVisible(False)
            self.rdo_btn_2.setVisible(False)

            self.errormsg.setWordWrap(True)
            self.errormsg.setFixedSize(250, 50)
            self.errormsg.move(25, 80)
            self.errormsg.setVisible(True)
            self.errormsg.setText('인스타그램 인증요청을 실패하였습니다. 프로그램을 종료 후 다시 시도해 주세요.')
        # 다시 원 화면으로 돌아온다 ;;

    def submit_seccode(self):
        # 제출 버튼
        if len(self.securitycodeinput.text()) == 6:
            seccode_input = WebDriverWait(driver=self.par.parentwindow.wdriver, timeout=5) \
                .until(lambda wdriver: wdriver.find_element_by_xpath("//input[@class='_m45dw _o716c']"))
            seccode_input.clear()

            seccode_input.send_keys(self.securitycodeinput.text())

            WebDriverWait(driver=self.par.parentwindow.wdriver, timeout=5) \
                .until(lambda wdriver: wdriver.find_element_by_xpath("//button[text()='제출']")).click()

            # 로그인이 정상적으로 됬는지
            for index in range(0, 8):

                check_login = WebDriverWait(driver=self.par.parentwindow.wdriver, timeout=4) \
                    .until(lambda wdriver: wdriver.find_element_by_xpath("//html[1]"))
                check_text = check_login.get_attribute("class")
                # print(check_login.text)
                if check_text.find('not-logged-in') >= 0:
                    print('로그인 실패.')
                    time.sleep(0.5)
                    self.onefail = True
                elif check_login.text.find('"status": "fail"') >= 0:
                    # 로그인 실패로
                    self.errormsg.setText('로그인 실패. 짧은 시간 내 여러번의 로그인 시도로 계정이 제한되었습니다. 몇 분후에 다시 시도해주세요.')
                    self.poploading.close_lodingwgt.emit()
                    break

                else:
                    print('로그인 성공')
                    self.par.handleLogin()
                    break

            if self.onefail:
                try:
                    # 첫 페이지로 다시 돌아간 경우
                    login_text = WebDriverWait(driver=self.par.parentwindow.wdriver, timeout=3) \
                        .until(lambda drv: drv.find_element_by_xpath("//p[@class='_g9ean']/a"))
                    if login_text.text == '로그인':
                        # 첫페이지로 이동했으니 화면 모두 다 숨기고 hide()
                        self.subjecttext.setVisible(False)
                        self.statustext.setVisible(False)
                        self.securitycodeinput.setVisible(False)
                        self.secsendbtn.setVisible(False)

                        self.errormsg.setWordWrap(True)
                        self.errormsg.setFixedSize(250, 50)
                        self.errormsg.move(25, 80)
                        self.errormsg.setVisible(True)
                        self.errormsg.setText('핸드폰 인스타그램 설정에서 2단계 인증 항목를 비활성화 시켜주신 후 다시 시도해주세요.')
                        # self.hide()
                        # self.blackorwhite = False

                except:
                    # 보안 코드가 틀린 경우
                    self.errormsg.setFixedSize(200, 20)
                    self.errormsg.move(25, 160)
                    self.errormsg.setVisible(True)
                    self.errormsg.setText('보안코드가 정확하지 않습니다.')

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.fillRect(event.rect(), QBrush(QColor(255, 255, 255, 120)))
        painter.setPen(self.penColor)

        if self.blackorwhite:
            # self.statustext.setVisible(False)
            painter.fillRect(event.rect(), QBrush(QColor(255, 255, 255, 240)))
            painter.end()
            return
        for i in range(1, 9):
            if self.counter - i == 0:
                # painter.setBrush(QBrush(QColor(245, 240, 240)))
                painter.setBrush(QBrush(QColor(10, 10, 10)))
            elif self.counter - i == -1:
                painter.setBrush(QBrush(QColor(180, 180, 180)))
            elif self.counter - i == -2:
                painter.setBrush(QBrush(QColor(150, 150, 150)))
            elif self.counter - i == -3:
                painter.setBrush(QBrush(QColor(120, 120, 120)))
            elif self.counter - i == -4:
                painter.setBrush(QBrush(QColor(100, 100, 100)))
            elif self.counter - i == -5:
                painter.setBrush(QBrush(QColor(70, 70, 70)))
            elif self.counter - i == -6:
                painter.setBrush(QBrush(QColor(50, 50, 50)))
            elif self.counter - i == -7:
                painter.setBrush(QBrush(QColor(20, 20, 20)))
            elif self.counter - i == 1:
                painter.setBrush(QBrush(QColor(180, 180, 180)))
            elif self.counter - i == 2:
                painter.setBrush(QBrush(QColor(150, 150, 150)))
            elif self.counter - i == 3:
                painter.setBrush(QBrush(QColor(120, 120, 120)))
            elif self.counter - i == 4:
                painter.setBrush(QBrush(QColor(100, 100, 100)))
            elif self.counter - i == 5:
                painter.setBrush(QBrush(QColor(70, 70, 70)))
            elif self.counter - i == 6:
                painter.setBrush(QBrush(QColor(50, 50, 50)))
            elif self.counter - i == 7:
                painter.setBrush(QBrush(QColor(20, 20, 20)))

            painter.drawEllipse(self.width() / 2 + 40 * math.cos(2 * math.pi * i / 8.0) - 10,
                                self.height() / 2 + 40 * math.sin(2 * math.pi * i / 8.0) - 10, 25, 25)
        painter.end()

    def change_pv_value(self, changevalue):
        self.progress.setValue(changevalue)

    def _onclose(self):
        print("loading widget is closed")
        self.killTimer(self.timer)
        self.hide()

    def showEvent(self, event):
        self.timer = self.startTimer(80)
        self.counter = 1

    def timerEvent(self, event):
        self.counter += 1
        self.update()
        # if self.counter == 60:
        #     self.killTimer(self.timer)
        #     self.hide()
        if self.counter == 9:
            self.counter = 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = InstaManagementSystem()
    # myWindow.show()
    sys.exit(app.exec_())