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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 500)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widge_left = QWidget(self.centralwidget)
        self.widge_left.setObjectName(u"widge_left")
        self.widge_left.setGeometry(QRect(10, 10, 120, 481))
        self.page_link = QPushButton(self.widge_left)
        self.page_link.setObjectName(u"page_link")
        self.page_link.setGeometry(QRect(0, 30, 121, 24))
        self.page_server = QPushButton(self.widge_left)
        self.page_server.setObjectName(u"page_server")
        self.page_server.setGeometry(QRect(0, 0, 121, 24))
        self.window_close = QPushButton(self.widge_left)
        self.window_close.setObjectName(u"window_close")
        self.window_close.setGeometry(QRect(0, 420, 121, 24))
        self.window_mini = QPushButton(self.widge_left)
        self.window_mini.setObjectName(u"window_mini")
        self.window_mini.setGeometry(QRect(0, 450, 121, 24))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(130, 10, 20, 481))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(150, 10, 641, 481))
        self.stackedWidget.setMouseTracking(False)
        self.stackedWidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.layoutWidget = QWidget(self.page)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(140, 140, 202, 116))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.server_IP = QLineEdit(self.layoutWidget)
        self.server_IP.setObjectName(u"server_IP")

        self.horizontalLayout.addWidget(self.server_IP)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.server_Port = QLineEdit(self.layoutWidget)
        self.server_Port.setObjectName(u"server_Port")

        self.horizontalLayout_2.addWidget(self.server_Port)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.server_token = QLineEdit(self.layoutWidget)
        self.server_token.setObjectName(u"server_token")

        self.horizontalLayout_3.addWidget(self.server_token)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.server_save = QPushButton(self.layoutWidget)
        self.server_save.setObjectName(u"server_save")

        self.verticalLayout.addWidget(self.server_save)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.lineEdit = QLineEdit(self.page_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(40, 110, 113, 20))
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Frp\u5feb\u901f\u914d\u7f6e", None))
        self.page_link.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e\u94fe\u63a5", None))
        self.page_server.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668\u5730\u5740", None))
        self.window_close.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.window_mini.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5c0f\u5316", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668\u5730\u5740", None))
        self.server_IP.setPlaceholderText(QCoreApplication.translate("MainWindow", u"127.0.0.1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668\u7aef\u53e3", None))
        self.server_Port.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1024-65535", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668\u5bc6\u94a5", None))
        self.server_token.setPlaceholderText(QCoreApplication.translate("MainWindow", u"token", None))
        self.server_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e\u94fe\u63a5", None))
    # retranslateUi

