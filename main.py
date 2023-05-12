import os
import qdarkstyle
import subprocess
import threading

from PySide6.QtWidgets import QMainWindow, QWidget, QStackedWidget, QPushButton, QVBoxLayout, QApplication
from PySide6.QtCore import Qt, QThread
from PySide6.QtGui import QIcon, QPixmap, QColor
from PySide6 import QtWidgets

from ui.main_ui import Ui_MainWindow
from script.start import FrpClient
from makefile.tags import tags

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

        # 数据读取
        self.datainit()
        
        # UI初始化
        self.UIinit()

        # 绑定动作
        self.band()
        self.bandFrp()        

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

        # main
        self.ui.main_start.clicked.connect(self.main_start)
        self.ui.main_stop.clicked.connect(self.main_stop)
        self.ui.main_clear.clicked.connect(self.clear_log)

        # server
        self.ui.server_save.clicked.connect(self.server_save)

        # window
        self.ui.window_mini.clicked.connect(self.showMinimized)
        self.ui.window_close.clicked.connect(self.closewindow)
    
    def bandFrp(self):
        # FrpClient
        self._frp_client = FrpClient()
        self._frp_client.log_message.connect(self.on_log_message)
        self._frp_client.started.connect(self.on_frp_started)
        self._frp_client.finished.connect(self.on_frp_finished)
        self._frp_client.tell_finished.connect(self.on_frp_finished_tell)
        self._frp_client.stopped.connect(self.on_frp_stopped)

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
        self.left_highlight_botton = self.ui.page_main
        self.set_left_highlight_botton()
        self.LinkUISetting()
        self.MainUISetting()
        self.readme()
        # self.ui.stackedWidget.setCurrentIndex(0)
        self.setTabOrder(self.ui.server_IP, self.ui.server_Port)
        self.setTabOrder(self.ui.server_Port, self.ui.server_token)

        
        
    ##
    ## 数据读取
    ##
    def datainit(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        try:
            with open("./data/server.ini","r+",encoding="utf-8") as u:
                server = u.readlines()
            self.ui.show_IP.setText(server[1].split("=")[1].strip())
            self.ui.show_Port.setText(server[2].split("=")[1].strip())
            self.ui.show_token.setText(server[3].split("=")[1].strip())
        except:
            pass

    ##
    ## 自述配置
    ##
    def readme(self):
        self.ui.version.setText(self.tags.version)

    ## 
    ## 按钮设置
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

    def LinkUISetting(self):
        self.botton_highlight_link = QColor(200, 80, 80)
        self.botton_highlight_link2 = QColor(80, 200, 80)
        self.botton_highlight_link3 = QColor(100, 100, 180)
        self.ui.link_delete.setStyleSheet(f"""
                QPushButton {{
                    background-color: transparent;
                    border-radius: 0px;
                }}
                QPushButton:hover {{
                    background-color: {self.botton_highlight_link.name()};
                }}
            """)
        self.ui.link_create.setStyleSheet(f"""
                QPushButton {{
                    background-color: transparent;
                    border-radius: 0px;
                }}
                QPushButton:hover {{
                    background-color: {self.botton_highlight_link2.name()};
                }}
            """)
        self.ui.link_modify.setStyleSheet(f"""
                QPushButton {{
                    background-color: transparent;
                    border-radius: 0px;
                }}
                QPushButton:hover {{
                    background-color: {self.botton_highlight_link3.name()};
                }}
            """)
        self.ui.linktable.setStyleSheet("border-radius: 0px")

    def MainUISetting(self):
        self.background_color_low = QColor(40, 40, 60)
        self.background_color_high = QColor(60, 60, 80)
        self.highlight_color_main_stop = QColor(130, 130, 180)
        self.highlight_color_main_start = QColor(80, 160, 80)
        self.setstarthigh()
        self.ui.main_clear.setStyleSheet(f"""
                QPushButton {{
                    background-color: {self.background_color_high.name()};
                    border-radius: 0px;
                }}
                QPushButton:hover {{
                    background-color: {self.botton_highlight_link.name()};
                }}
            """)
        icon = QIcon("ui/icon/play.png")
        self.ui.main_start.setIcon(icon)
        self.ui.main_start.setIconSize(self.ui.window_close.size())
        icon = QIcon("ui/icon/stop.png")
        self.ui.main_stop.setIcon(icon)
        self.ui.main_stop.setIconSize(self.ui.window_close.size())
        icon = QIcon("ui/icon/trash.png")
        self.ui.main_clear.setIcon(icon)
        self.ui.main_clear.setIconSize(self.ui.window_close.size())
        
        self.ui.main_log.setStyleSheet(f"""
                border-radius: 0px;
                border-color: {self.background_color_high.name()};
            """)
        self.ui.main_log.setReadOnly(True)
        self.ui.main_start.setEnabled(True)
        self.ui.main_stop.setEnabled(False)
    
    def setstarthigh(self):
        self.ui.main_start.setStyleSheet(f"""
                QPushButton {{
                    background-color: {self.background_color_high.name()};
                    border-radius: 0px;
                }}
                QPushButton:hover {{
                    background-color: {self.highlight_color_main_start.name()};
                }}
            """)
        
        self.ui.main_stop.setStyleSheet(f"""
                QPushButton {{
                    background-color: {self.background_color_low.name()};
                    border-radius: 0px;
                }}
                QPushButton:hover {{
                    background-color: {self.highlight_color_main_stop.name()};
                }}
            """)
    
    def setstophigh(self):
        self.ui.main_start.setStyleSheet(f"""
                QPushButton {{
                    background-color: {self.background_color_low.name()};
                    border-radius: 0px;
                }}
                QPushButton:hover {{
                    background-color: {self.highlight_color_main_start.name()};
                }}
            """)
        
        self.ui.main_stop.setStyleSheet(f"""
                QPushButton {{
                    background-color: {self.background_color_high.name()};
                    border-radius: 0px;
                }}
                QPushButton:hover {{
                    background-color: {self.highlight_color_main_stop.name()};
                }}
            """)

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
    
    def closewindow(self):  
        self._frp_client.stop()
        self._frp_client.finished.disconnect()
        self._frp_client.stopped.disconnect()
        self._frp_client.log_message.disconnect()
        self._frp_client.deleteLater()
        self.close()
    ##
    ## 主要模块
    ##
    def main_start(self):
        
        self._frp_client.start()

    
    def main_stop(self):
        self._frp_client.stop()
    
    def clear_log(self):
        self.ui.main_log.setPlainText('')

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
    ## 信号动作
    ##
    def on_log_message(self, message):
        self.ui.main_log.insertPlainText(message)

    def on_frp_started(self):
        self.ui.main_log.insertPlainText("frp client started.\n")
        self.ui.main_start.setEnabled(False)
        self.ui.main_stop.setEnabled(True)
        self.setstophigh()

    def on_frp_finished(self):
        self._frp_client.stop()
        self.ui.main_start.setEnabled(True)
        self.ui.main_stop.setEnabled(False)
        self.setstarthigh()
        self.bandFrp()
    
    def on_frp_finished_tell(self):
        self.ui.main_log.insertPlainText("frp client stopped.\n")

    def on_frp_stopped(self):
        self.ui.main_start.setEnabled(True)
        self.ui.main_stop.setEnabled(False)
        self.setstarthigh()

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