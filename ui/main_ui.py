# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpinBox, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QWidget)
from . import main_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QSize(800, 500))
        MainWindow.setMaximumSize(QSize(800, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(140, 10, 20, 481))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(160, 10, 631, 481))
        self.stackedWidget.setMouseTracking(False)
        self.stackedWidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.stackedWidget.setLayoutDirection(Qt.LeftToRight)
        self.stackedWidget.setAutoFillBackground(False)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.line_5 = QFrame(self.page)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(0, 40, 631, 16))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.label_10 = QLabel(self.page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 0, 431, 31))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_10.setFont(font)
        self.main_start = QPushButton(self.page)
        self.main_start.setObjectName(u"main_start")
        self.main_start.setGeometry(QRect(0, 50, 281, 51))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        self.main_start.setFont(font1)
        self.main_log = QTextEdit(self.page)
        self.main_log.setObjectName(u"main_log")
        self.main_log.setGeometry(QRect(0, 100, 621, 371))
        self.main_clear = QPushButton(self.page)
        self.main_clear.setObjectName(u"main_clear")
        self.main_clear.setGeometry(QRect(560, 50, 61, 51))
        self.main_clear.setFont(font1)
        self.main_stop = QPushButton(self.page)
        self.main_stop.setObjectName(u"main_stop")
        self.main_stop.setGeometry(QRect(280, 50, 281, 51))
        self.main_stop.setFont(font1)
        self.stackedWidget.addWidget(self.page)
        self.main_log.raise_()
        self.line_5.raise_()
        self.label_10.raise_()
        self.main_start.raise_()
        self.main_clear.raise_()
        self.main_stop.raise_()
        self.page0 = QWidget()
        self.page0.setObjectName(u"page0")
        self.line_4 = QFrame(self.page0)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(0, 40, 641, 16))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.label_4 = QLabel(self.page0)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 431, 31))
        self.label_4.setFont(font)
        self.widget = QWidget(self.page0)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(310, 60, 321, 131))
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 71, 16))
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 40, 71, 16))
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 70, 71, 16))
        self.show_IP = QLabel(self.widget)
        self.show_IP.setObjectName(u"show_IP")
        self.show_IP.setGeometry(QRect(80, 10, 231, 16))
        self.show_Port = QLabel(self.widget)
        self.show_Port.setObjectName(u"show_Port")
        self.show_Port.setGeometry(QRect(80, 40, 231, 16))
        self.show_token = QLabel(self.widget)
        self.show_token.setObjectName(u"show_token")
        self.show_token.setGeometry(QRect(80, 70, 231, 16))
        self.widget_2 = QWidget(self.page0)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(20, 60, 231, 131))
        self.server_Port = QLineEdit(self.widget_2)
        self.server_Port.setObjectName(u"server_Port")
        self.server_Port.setGeometry(QRect(80, 40, 131, 20))
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(2, 12, 71, 16))
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(2, 72, 71, 16))
        self.server_IP = QLineEdit(self.widget_2)
        self.server_IP.setObjectName(u"server_IP")
        self.server_IP.setGeometry(QRect(80, 10, 131, 20))
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(2, 42, 71, 16))
        self.server_token = QLineEdit(self.widget_2)
        self.server_token.setObjectName(u"server_token")
        self.server_token.setGeometry(QRect(80, 70, 131, 20))
        self.server_save = QPushButton(self.widget_2)
        self.server_save.setObjectName(u"server_save")
        self.server_save.setGeometry(QRect(10, 100, 201, 24))
        self.server_Port.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.server_token.raise_()
        self.server_save.raise_()
        self.server_IP.raise_()
        self.stackedWidget.addWidget(self.page0)
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.line_3 = QFrame(self.page1)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(0, 40, 641, 16))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.label_5 = QLabel(self.page1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 0, 431, 31))
        self.label_5.setFont(font)
        self.link_create = QPushButton(self.page1)
        self.link_create.setObjectName(u"link_create")
        self.link_create.setGeometry(QRect(520, 60, 101, 41))
        self.link_delete = QPushButton(self.page1)
        self.link_delete.setObjectName(u"link_delete")
        self.link_delete.setGeometry(QRect(320, 60, 101, 41))
        self.link_modify = QPushButton(self.page1)
        self.link_modify.setObjectName(u"link_modify")
        self.link_modify.setGeometry(QRect(420, 60, 101, 41))
        self.linktable = QTableWidget(self.page1)
        self.linktable.setObjectName(u"linktable")
        self.linktable.setGeometry(QRect(0, 100, 621, 371))
        self.stackedWidget.addWidget(self.page1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.line_6 = QFrame(self.page_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(0, 40, 641, 16))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.label_11 = QLabel(self.page_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 0, 431, 31))
        self.label_11.setFont(font)
        self.auto_address = QCheckBox(self.page_2)
        self.auto_address.setObjectName(u"auto_address")
        self.auto_address.setGeometry(QRect(560, 130, 52, 24))
        self.auto_address.setStyleSheet(u"QCheckBox {\n"
"    background-color: #2c2c2c;\n"
"    border-radius: 3px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCheckBox::checked {\n"
"    background-color: #4cd964;\n"
"	border-radius: 3px;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QCheckBox::indicator::checked { \n"
"	image: None;\n"
"	width: 20px; height: 20px;\n"
"	border-radius: 2px;\n"
"	background-color: #ffffff;\n"
"	position: relative;\n"
"	left: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator::unchecked { \n"
"	image: None;\n"
"	width: 20px; height: 20px;\n"
"	border-radius: 2px;\n"
"	background-color: #2196F3;\n"
"}\n"
"")
        self.auto_linkname = QCheckBox(self.page_2)
        self.auto_linkname.setObjectName(u"auto_linkname")
        self.auto_linkname.setGeometry(QRect(560, 60, 52, 24))
        self.auto_linkname.setStyleSheet(u"QCheckBox {\n"
"    background-color: #2c2c2c;\n"
"    border-radius: 3px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCheckBox::checked {\n"
"    background-color: #4cd964;\n"
"	border-radius: 3px;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QCheckBox::indicator::checked { \n"
"	image: None;\n"
"	width: 20px; height: 20px;\n"
"	border-radius: 2px;\n"
"	background-color: #ffffff;\n"
"	position: relative;\n"
"	left: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator::unchecked { \n"
"	image: None;\n"
"	width: 20px; height: 20px;\n"
"	border-radius: 2px;\n"
"	background-color: #2196F3;\n"
"}\n"
"")
        self.auto_heartbeat = QCheckBox(self.page_2)
        self.auto_heartbeat.setObjectName(u"auto_heartbeat")
        self.auto_heartbeat.setGeometry(QRect(560, 180, 52, 24))
        self.auto_heartbeat.setStyleSheet(u"QCheckBox {\n"
"    background-color: #2c2c2c;\n"
"    border-radius: 3px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCheckBox::checked {\n"
"    background-color: #4cd964;\n"
"	border-radius: 3px;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QCheckBox::indicator::checked { \n"
"	image: None;\n"
"	width: 20px; height: 20px;\n"
"	border-radius: 2px;\n"
"	background-color: #ffffff;\n"
"	position: relative;\n"
"	left: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator::unchecked { \n"
"	image: None;\n"
"	width: 20px; height: 20px;\n"
"	border-radius: 2px;\n"
"	background-color: #2196F3;\n"
"}\n"
"")
        self.label_13 = QLabel(self.page_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 55, 161, 31))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_13.setFont(font2)
        self.label_14 = QLabel(self.page_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 90, 111, 21))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_14.setFont(font3)
        self.label_15 = QLabel(self.page_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 130, 161, 31))
        self.label_15.setFont(font2)
        self.label_16 = QLabel(self.page_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 180, 161, 31))
        self.label_16.setFont(font2)
        self.label_17 = QLabel(self.page_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 215, 111, 21))
        self.label_17.setFont(font3)
        self.auto_linkname_box = QSpinBox(self.page_2)
        self.auto_linkname_box.setObjectName(u"auto_linkname_box")
        self.auto_linkname_box.setGeometry(QRect(560, 90, 51, 22))
        self.auto_heartbeat_box = QSpinBox(self.page_2)
        self.auto_heartbeat_box.setObjectName(u"auto_heartbeat_box")
        self.auto_heartbeat_box.setGeometry(QRect(560, 215, 51, 22))
        self.line_7 = QFrame(self.page_2)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(10, 120, 601, 20))
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.line_8 = QFrame(self.page_2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(10, 170, 601, 20))
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.label_18 = QLabel(self.page_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 260, 161, 31))
        self.label_18.setFont(font2)
        self.line_9 = QFrame(self.page_2)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(10, 250, 601, 20))
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)
        self.auto_mini = QCheckBox(self.page_2)
        self.auto_mini.setObjectName(u"auto_mini")
        self.auto_mini.setGeometry(QRect(560, 260, 52, 24))
        self.auto_mini.setStyleSheet(u"QCheckBox {\n"
"    background-color: #2c2c2c;\n"
"    border-radius: 3px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCheckBox::checked {\n"
"    background-color: #4cd964;\n"
"	border-radius: 3px;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QCheckBox::indicator::checked { \n"
"	image: None;\n"
"	width: 20px; height: 20px;\n"
"	border-radius: 2px;\n"
"	background-color: #ffffff;\n"
"	position: relative;\n"
"	left: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator::unchecked { \n"
"	image: None;\n"
"	width: 20px; height: 20px;\n"
"	border-radius: 2px;\n"
"	background-color: #2196F3;\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.page_2)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.line_2 = QFrame(self.page2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 40, 641, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label_6 = QLabel(self.page2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 431, 31))
        self.label_6.setFont(font)
        self.stackedWidget.addWidget(self.page2)
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(580, 0, 221, 31))
        self.window_close = QPushButton(self.widget_3)
        self.window_close.setObjectName(u"window_close")
        self.window_close.setGeometry(QRect(170, 0, 50, 25))
        self.window_close.setContextMenuPolicy(Qt.NoContextMenu)
        self.window_mini = QPushButton(self.widget_3)
        self.window_mini.setObjectName(u"window_mini")
        self.window_mini.setGeometry(QRect(120, 0, 50, 25))
        font4 = QFont()
        font4.setPointSize(9)
        self.window_mini.setFont(font4)
        self.window_mini.raise_()
        self.window_close.raise_()
        self.page_main = QPushButton(self.centralwidget)
        self.page_main.setObjectName(u"page_main")
        self.page_main.setGeometry(QRect(0, 70, 131, 41))
        font5 = QFont()
        font5.setPointSize(10)
        self.page_main.setFont(font5)
        self.page_server = QPushButton(self.centralwidget)
        self.page_server.setObjectName(u"page_server")
        self.page_server.setGeometry(QRect(0, 110, 131, 41))
        self.page_server.setFont(font5)
        self.version = QLabel(self.centralwidget)
        self.version.setObjectName(u"version")
        self.version.setGeometry(QRect(80, 40, 51, 16))
        self.page_other = QPushButton(self.centralwidget)
        self.page_other.setObjectName(u"page_other")
        self.page_other.setGeometry(QRect(0, 190, 131, 41))
        self.page_other.setFont(font5)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 10, 71, 51))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font6 = QFont()
        font6.setPointSize(26)
        font6.setBold(True)
        self.label_12.setFont(font6)
        self.label_12.setTextFormat(Qt.PlainText)
        self.label_12.setWordWrap(False)
        self.page_link = QPushButton(self.centralwidget)
        self.page_link.setObjectName(u"page_link")
        self.page_link.setGeometry(QRect(0, 150, 131, 41))
        self.page_link.setFont(font5)
        self.page_tags = QPushButton(self.centralwidget)
        self.page_tags.setObjectName(u"page_tags")
        self.page_tags.setGeometry(QRect(0, 230, 131, 41))
        self.page_tags.setFont(font5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Frp\u5feb\u901f\u914d\u7f6e", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.main_start.setText("")
        self.main_clear.setText("")
        self.main_stop.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668\u5730\u5740", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668\u5730\u5740", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668\u7aef\u53e3", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668\u5bc6\u94a5", None))
        self.show_IP.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u914d\u7f6e", None))
        self.show_Port.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u914d\u7f6e", None))
        self.show_token.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u914d\u7f6e", None))
        self.server_Port.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u7aef\u53e3\u53f7", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668\u5730\u5740", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668\u5bc6\u94a5", None))
        self.server_IP.setText("")
        self.server_IP.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165IP", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668\u7aef\u53e3", None))
        self.server_token.setPlaceholderText(QCoreApplication.translate("MainWindow", u"token", None))
        self.server_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e\u94fe\u63a5", None))
        self.link_create.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa", None))
        self.link_delete.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.link_modify.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6\u914d\u7f6e", None))
        self.auto_address.setText("")
        self.auto_linkname.setText("")
        self.auto_heartbeat.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u586b\u5199\u94fe\u63a5\u540d", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u957f\u5ea6", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u586b\u5199\u6e90\u5730\u5740", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u5fc3\u8df3\u56de\u5e94", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u5ef6\u65f6", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5c0f\u5316\u6258\u76d8", None))
        self.auto_mini.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.window_close.setText("")
        self.window_mini.setText("")
        self.page_main.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.page_server.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v0.0.0", None))
        self.page_other.setText(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6\u914d\u7f6e", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"FSE", None))
        self.page_link.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e\u94fe\u63a5", None))
        self.page_tags.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

