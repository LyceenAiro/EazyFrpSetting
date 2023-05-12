from PySide6.QtWidgets import QMainWindow, QWidget, QStackedWidget, QPushButton, QVBoxLayout, QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap, QColor
from PySide6 import QtWidgets

from ui.main_ui import Ui_MainWindow
from signal.main_signal import my_signal
from makefile.tags import tags

import qdarkstyle
class MainWindow(QMainWindow):

    ##
    ## 主窗口设置
    ##
    def __init__(self):
        super(MainWindow, self).__init__()
        self.tags = tags()
        self.ui = Ui_MainWindow()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.ui.setupUi(self)
        
        # UI初始化
        self.UIinit()

        # 绑定动作
        self.band()

        # 窗口移动项
        self.mouse_press_position = None

    ##
    ## 对象绑定设置
    ##
    def band(self):
        # left
        self.ui.page_main.clicked.connect(self.setmain)
        self.ui.page_server.clicked.connect(self.setserver)
        self.ui.page_link.clicked.connect(self.setlink)
        self.ui.page_other.clicked.connect(self.setother)
        self.ui.page_tags.clicked.connect(self.settags)

        # server
        self.ui.server_save.clicked.connect(self.server_save)

        # window
        self.ui.window_mini.clicked.connect(self.showMinimized)
        self.ui.window_close.clicked.connect(self.close)

    ##
    ## UI变化反馈
    ##
    def unset_left_highlight_botton(self):
        self.left_highlight_botton.setStyleSheet(f"""
                QPushButton {{
                    background-color: transparent;
                    border-radius: 0px;
                }}
                QPushButton:hover {{
                    background-color: {self.botton_highlight_color.name()};
                }}
            """)
        
    def set_left_highlight_botton(self):
        self.left_highlight_botton.setStyleSheet(f"""
                QPushButton {{
                    background-color: {self.botton_highlight_color2.name()};
                    border-radius: 0px;
                }}
                QPushButton:hover {{
                    background-color: {self.botton_highlight_color3.name()};
                }}
            """)

    ##
    ## 初始化
    ##
    def UIinit(self):
        self.FlagsUiSetting()
        self.LeftUISetting()
        self.readme()
        # self.ui.stackedWidget.setCurrentIndex(0)
        self.setTabOrder(self.ui.server_IP, self.ui.server_Port)
        self.setTabOrder(self.ui.server_Port, self.ui.server_token)
        
    
    ##
    ## 自述配置
    ##
    def readme(self):
        self.ui.version.setText(self.tags.version)

    ## 
    ## 左侧栏设置
    ##
    def LeftUISetting(self):
        self.botton_highlight_color = QColor(130, 130, 130)
        self.botton_highlight_color2 = QColor(100, 100, 180)
        self.botton_highlight_color3 = QColor(100, 100, 210)
        botten = [self.ui.page_server,
                  self.ui.page_link,
                  self.ui.page_other,
                  self.ui.page_tags]
        for i in botten:
            i.setStyleSheet(f"""
                QPushButton {{
                    background-color: transparent;
                    border-radius: 0px;
                }}
                QPushButton:hover {{
                    background-color: {self.botton_highlight_color.name()};
                }}
            """)

        #初始化
        self.left_highlight_botton = self.ui.page_main
        self.set_left_highlight_botton()

    ## 
    ## 标题栏设置
    ##
    def FlagsUiSetting(self):
        highlight_color = QColor(130, 130, 180)
        botten = [self.ui.window_mini,
                  self.ui.window_close]
        for i in botten:
            i.setStyleSheet(f"""
                QPushButton {{
                    background-color: transparent;
                    border-radius: 0px;
                }}
                QPushButton:hover {{
                    background-color: {highlight_color.name()};
                }}
            """)
        icon = QIcon("ui/icon/close.png")
        self.ui.window_close.setIcon(icon)
        self.ui.window_close.setIconSize(self.ui.window_close.size())
        icon = QIcon("ui/icon/mini.png")
        self.ui.window_mini.setIcon(icon)
        self.ui.window_mini.setIconSize(self.ui.window_close.size())

    def setmain(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.unset_left_highlight_botton()
        self.left_highlight_botton = self.ui.page_main
        self.set_left_highlight_botton()

    def setserver(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.unset_left_highlight_botton()
        self.left_highlight_botton = self.ui.page_server
        self.set_left_highlight_botton()

    def setlink(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.unset_left_highlight_botton()
        self.left_highlight_botton = self.ui.page_link
        self.set_left_highlight_botton()

    def setother(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.unset_left_highlight_botton()
        self.left_highlight_botton = self.ui.page_other
        self.set_left_highlight_botton()

    def settags(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.unset_left_highlight_botton()
        self.left_highlight_botton = self.ui.page_tags
        self.set_left_highlight_botton()
    
    ##
    ## 主要模块
    ##
    def server_save(self):
        ip = self.ui.server_IP.text()
        port = self.ui.server_Port.text()
        token = self.ui.server_token.text()

        check = True
        if self.ipcheck(ip) == False:
            self.ui.server_IP.setStyleSheet('border: 2px solid red;')
            check = False
        if self.portcheck(port, 1, 65565) == False:
            self.ui.server_Port.setStyleSheet('border: 2px solid red;')
            check = False
        if check == False:
            return
        self.ui.server_IP.setStyleSheet('')
        self.ui.server_Port.setStyleSheet('')
        server = ["[common]\n",
                  f"server_addr = {ip}\n",
                  f"server_port = {port}\n",
                  f"token = {token}\n"
                  ]
        if token == "":
            server[3] = "#token = 无配置"
            self.ui.show_token.setText("无配置")
        else:
            self.ui.show_token.setText(token)
        with open("./data/server.ini","w+",encoding="utf-8") as u:
            for i in server:
                u.write(i)
        self.ui.show_IP.setText(ip)
        self.ui.show_Port.setText(port)
        

    
    ##
    ## 判断模块
    ##
    def ipcheck(self, ip):
        try:
            if len(ip.split("."))==4:
                for i in ip.split(".") :
                    try:
                        if not(0<=int(i)<=255):
                            return False
                    except:
                        return False
            else:
                return False
        except:
            return False
        
    def portcheck(self, port, low, high):
        try:
            if high >= int(port) >= low :
                return True
            else:
                return False
        except:
            return False


    ##
    ## 窗口移动定义
    ##
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_press_position = event.globalPos() - self.pos()
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_press_position = None
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.mouse_press_position is not None:
            self.move(event.globalPos() - self.mouse_press_position)
            event.accept()


if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api="pyside6"))
    window = MainWindow()
    window.show()
    app.exec()