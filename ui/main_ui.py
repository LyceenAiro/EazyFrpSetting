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
        self.widget.setGeometry(QRect(390, 60, 231, 191))
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 50, 71, 31))
        self.label_7.setStyleSheet(u"QLabel {\n"
"            background-color: rgb(50, 50, 60);\n"
"            border-radius: 0px;\n"
"}")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 80, 71, 31))
        self.label_8.setStyleSheet(u"QLabel {\n"
"            background-color: rgb(50, 50, 60);\n"
"            border-radius: 0px;\n"
"}")
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 110, 71, 31))
        self.label_9.setStyleSheet(u"QLabel {\n"
"            background-color: rgb(50, 50, 60);\n"
"            border-radius: 0px;\n"
"}")
        self.show_IP = QLabel(self.widget)
        self.show_IP.setObjectName(u"show_IP")
        self.show_IP.setGeometry(QRect(80, 50, 131, 31))
        self.show_IP.setStyleSheet(u"QLabel {\n"
"            background-color: rgb(60, 60, 80);\n"
"            border-radius: 0px;\n"
"}")
        self.show_Port = QLabel(self.widget)
        self.show_Port.setObjectName(u"show_Port")
        self.show_Port.setGeometry(QRect(80, 80, 131, 31))
        self.show_Port.setStyleSheet(u"QLabel {\n"
"            background-color: rgb(60, 60, 80);\n"
"            border-radius: 0px;\n"
"}")
        self.show_token = QLabel(self.widget)
        self.show_token.setObjectName(u"show_token")
        self.show_token.setGeometry(QRect(80, 110, 131, 31))
        self.show_token.setStyleSheet(u"QLabel {\n"
"            background-color: rgb(60, 60, 80);\n"
"            border-radius: 0px;\n"
"}")
        self.server_clear = QPushButton(self.widget)
        self.server_clear.setObjectName(u"server_clear")
        self.server_clear.setGeometry(QRect(10, 140, 201, 31))
        self.server_clear.setStyleSheet(u"QPushButton {\n"
"            background-color: rgb(60, 60, 70);\n"
"            border-radius: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"            background-color: rgb(200, 80, 80);\n"
"}")
        self.label_24 = QLabel(self.widget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(10, 20, 201, 31))
        font2 = QFont()
        font2.setBold(True)
        self.label_24.setFont(font2)
        self.label_24.setStyleSheet(u"QLabel {\n"
"            background-color: rgb(100, 100, 180);\n"
"            border-radius: 0px;\n"
"}")
        self.widget_2 = QWidget(self.page0)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(20, 60, 221, 191))
        self.server_Port = QLineEdit(self.widget_2)
        self.server_Port.setObjectName(u"server_Port")
        self.server_Port.setGeometry(QRect(70, 80, 131, 31))
        self.server_Port.setStyleSheet(u"")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 50, 71, 31))
        self.label.setStyleSheet(u"QLabel {\n"
"            background-color: rgb(50, 50, 60);\n"
"            border-radius: 0px;\n"
"}")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 110, 71, 31))
        self.label_3.setStyleSheet(u"QLabel {\n"
"            background-color: rgb(50, 50, 60);\n"
"            border-radius: 0px;\n"
"}")
        self.server_IP = QLineEdit(self.widget_2)
        self.server_IP.setObjectName(u"server_IP")
        self.server_IP.setGeometry(QRect(70, 50, 131, 31))
        self.server_IP.setStyleSheet(u"")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 80, 71, 31))
        self.label_2.setStyleSheet(u"QLabel {\n"
"            background-color: rgb(50, 50, 60);\n"
"            border-radius: 0px;\n"
"}")
        self.server_token = QLineEdit(self.widget_2)
        self.server_token.setObjectName(u"server_token")
        self.server_token.setGeometry(QRect(70, 110, 131, 31))
        self.server_token.setStyleSheet(u"")
        self.server_save = QPushButton(self.widget_2)
        self.server_save.setObjectName(u"server_save")
        self.server_save.setGeometry(QRect(0, 140, 201, 31))
        self.server_save.setStyleSheet(u"QPushButton {\n"
"            background-color: rgb(60, 60, 70);\n"
"            border-radius: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"            background-color: rgb(80, 160, 80);\n"
"}")
        self.label_23 = QLabel(self.widget_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(0, 20, 201, 31))
        self.label_23.setFont(font2)
        self.label_23.setStyleSheet(u"QLabel {\n"
"            background-color: rgb(100, 100, 180);\n"
"            border-radius: 0px;\n"
"}")
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.server_token.raise_()
        self.server_Port.raise_()
        self.server_IP.raise_()
        self.server_save.raise_()
        self.label_23.raise_()
        self.server_seticon = QLabel(self.page0)
        self.server_seticon.setObjectName(u"server_seticon")
        self.server_seticon.setGeometry(QRect(260, 100, 91, 101))
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
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.label_13.setFont(font3)
        self.label_14 = QLabel(self.page_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 90, 111, 21))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.label_14.setFont(font4)
        self.label_15 = QLabel(self.page_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 130, 161, 31))
        self.label_15.setFont(font3)
        self.label_16 = QLabel(self.page_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 180, 161, 31))
        self.label_16.setFont(font3)
        self.label_17 = QLabel(self.page_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 215, 111, 21))
        self.label_17.setFont(font4)
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
        self.label_18.setFont(font3)
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
        self.auto_updata = QCheckBox(self.page_2)
        self.auto_updata.setObjectName(u"auto_updata")
        self.auto_updata.setGeometry(QRect(560, 310, 52, 24))
        self.auto_updata.setStyleSheet(u"QCheckBox {\n"
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
        self.label_19 = QLabel(self.page_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 310, 161, 31))
        self.label_19.setFont(font3)
        self.line_10 = QFrame(self.page_2)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(10, 300, 601, 20))
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)
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
        self.check_updata = QPushButton(self.page2)
        self.check_updata.setObjectName(u"check_updata")
        self.check_updata.setEnabled(True)
        self.check_updata.setGeometry(QRect(270, 60, 131, 41))
        font5 = QFont()
        font5.setPointSize(10)
        self.check_updata.setFont(font5)
        self.check_updata.setStyleSheet(u"QPushButton {\n"
"            border-radius: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"            background-color: rgb(110, 200, 110);\n"
"}")
        self.tags_version = QLabel(self.page2)
        self.tags_version.setObjectName(u"tags_version")
        self.tags_version.setGeometry(QRect(110, 60, 231, 31))
        font6 = QFont()
        font6.setPointSize(12)
        self.tags_version.setFont(font6)
        self.label_20 = QLabel(self.page2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 60, 91, 31))
        font7 = QFont()
        font7.setPointSize(14)
        self.label_20.setFont(font7)
        self.tags_check_updata = QLabel(self.page2)
        self.tags_check_updata.setObjectName(u"tags_check_updata")
        self.tags_check_updata.setGeometry(QRect(270, 110, 251, 41))
        self.tags_check_updata.setFont(font5)
        self.label_21 = QLabel(self.page2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 140, 91, 31))
        self.label_21.setFont(font7)
        self.tags_license = QLabel(self.page2)
        self.tags_license.setObjectName(u"tags_license")
        self.tags_license.setGeometry(QRect(110, 140, 171, 31))
        self.tags_license.setFont(font6)
        self.check_github = QPushButton(self.page2)
        self.check_github.setObjectName(u"check_github")
        self.check_github.setEnabled(True)
        self.check_github.setGeometry(QRect(10, 220, 131, 41))
        self.check_github.setFont(font5)
        self.check_github.setStyleSheet(u"QPushButton {\n"
"            border-radius: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"            background-color: rgb(100, 100, 180);\n"
"}")
        self.check_clear = QPushButton(self.page2)
        self.check_clear.setObjectName(u"check_clear")
        self.check_clear.setEnabled(True)
        self.check_clear.setGeometry(QRect(160, 220, 131, 41))
        self.check_clear.setFont(font5)
        self.check_clear.setStyleSheet(u"QPushButton {\n"
"            border-radius: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"            background-color: rgb(200, 80, 80);\n"
"}")
        self.tags_author = QLabel(self.page2)
        self.tags_author.setObjectName(u"tags_author")
        self.tags_author.setGeometry(QRect(110, 100, 151, 31))
        self.tags_author.setFont(font6)
        self.label_22 = QLabel(self.page2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 100, 91, 31))
        self.label_22.setFont(font7)
        self.line_11 = QFrame(self.page2)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setGeometry(QRect(0, 190, 641, 16))
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)
        self.stackedWidget.addWidget(self.page2)
        self.line_2.raise_()
        self.label_6.raise_()
        self.tags_version.raise_()
        self.label_20.raise_()
        self.tags_check_updata.raise_()
        self.label_21.raise_()
        self.tags_license.raise_()
        self.check_github.raise_()
        self.check_clear.raise_()
        self.tags_author.raise_()
        self.label_22.raise_()
        self.line_11.raise_()
        self.check_updata.raise_()
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
        font8 = QFont()
        font8.setPointSize(9)
        self.window_mini.setFont(font8)
        self.window_mini.raise_()
        self.window_close.raise_()
        self.page_main = QPushButton(self.centralwidget)
        self.page_main.setObjectName(u"page_main")
        self.page_main.setGeometry(QRect(0, 70, 131, 41))
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
        self.label_12.setGeometry(QRect(8, 10, 73, 51))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font9 = QFont()
        font9.setPointSize(26)
        font9.setBold(True)
        self.label_12.setFont(font9)
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
        self.updata_tag = QPushButton(self.centralwidget)
        self.updata_tag.setObjectName(u"updata_tag")
        self.updata_tag.setEnabled(True)
        self.updata_tag.setGeometry(QRect(0, 290, 131, 41))
        self.updata_tag.setFont(font5)
        self.updata_tag.setStyleSheet(u"QPushButton {\n"
"            background-color: rgb(100, 180, 100);\n"
"            border-radius: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"            background-color: rgb(110, 200, 110);\n"
"}")
        self.nofrpc_tag = QPushButton(self.centralwidget)
        self.nofrpc_tag.setObjectName(u"nofrpc_tag")
        self.nofrpc_tag.setGeometry(QRect(0, 330, 131, 41))
        self.nofrpc_tag.setFont(font5)
        self.nofrpc_tag.setStyleSheet(u"QPushButton {\n"
"            background-color: rgb(200, 100, 100);\n"
"            border-radius: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"            background-color: rgb(220, 110, 110);\n"
"}")
        self.help_button = QPushButton(self.centralwidget)
        self.help_button.setObjectName(u"help_button")
        self.help_button.setGeometry(QRect(0, 440, 131, 41))
        self.help_button.setFont(font5)
        self.help_button.setStyleSheet(u"QPushButton {\n"
"            background-color: transparent;\n"
"            border-radius: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"            background-color: rgb(130, 130, 130);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


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
        self.server_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u914d\u7f6e", None))
        self.server_Port.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u7aef\u53e3\u53f7", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668\u5730\u5740", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668\u5bc6\u94a5", None))
        self.server_IP.setText("")
        self.server_IP.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165IP", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668\u7aef\u53e3", None))
        self.server_token.setPlaceholderText(QCoreApplication.translate("MainWindow", u"token", None))
        self.server_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u914d\u7f6e", None))
        self.server_seticon.setText("")
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
        self.auto_updata.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8\u65f6\u68c0\u67e5\u66f4\u65b0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.check_updata.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.tags_version.setText(QCoreApplication.translate("MainWindow", u"self.tags.version", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u7248\u672c", None))
        self.tags_check_updata.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u8bb8\u53ef", None))
        self.tags_license.setText(QCoreApplication.translate("MainWindow", u"self.tags.license", None))
        self.check_github.setText(QCoreApplication.translate("MainWindow", u"\u6e90\u7801", None))
        self.check_clear.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e", None))
        self.tags_author.setText(QCoreApplication.translate("MainWindow", u"self.tags.author", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u4f5c\u8005", None))
        self.window_close.setText("")
        self.window_mini.setText("")
        self.page_main.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.page_server.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"0.0.0", None))
        self.page_other.setText(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6\u914d\u7f6e", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"EFS", None))
        self.page_link.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e\u94fe\u63a5", None))
        self.page_tags.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.updata_tag.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u7248\u672c\u53ef\u7528", None))
        self.nofrpc_tag.setText(QCoreApplication.translate("MainWindow", u"\u672a\u627e\u5230frpc", None))
        self.help_button.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

