# python模块
import os
import qdarkstyle
import configparser
import string
import random
import toml
from datetime import datetime
import webbrowser
import ui.main_rc

# pyside6模块
from PySide6.QtWidgets import QMainWindow, QTableWidget, QFrame, QVBoxLayout, QApplication, QTableWidgetItem, QDialog, QLabel, QLineEdit, QSystemTrayIcon, QMenu, QWidgetAction, QComboBox, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QColor, QAction, QPixmap
from PySide6 import QtWidgets

# 项目模块
from ui.main_ui import Ui_MainWindow
from script.start import FrpClient ,CheckUpdata, CheckServer, Checkbandwidth
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
        
        # 窗口移动项
        self.mouse_press_position = None
        self.main_log_scrollbar = self.ui.main_log.verticalScrollBar()

        # 预警时钟
        self.warning_clock = 0

        # UI初始化
        self.UIinit()

        # 初始化线程应用
        self.bandCheckupdata()
        self.bandPing()
        self.bandwidth()

        # 数据读取
        self.datainit()

        # 绑定Frp进程
        self.bandFrp()
 
        # 绑定动作
        self.band()



    ##
    ## 对象绑定设置
    ##
    def band(self):
        # 按钮绑定配置
        # 请先读取数据后再初始化按钮动作

        # left
        self.ui.page_main.clicked.connect(self.setmain)
        self.ui.page_server.clicked.connect(self.setserver)
        self.ui.page_link.clicked.connect(self.setlink)
        self.ui.page_other.clicked.connect(self.setother)
        self.ui.page_tags.clicked.connect(self.settags)
        self.ui.updata_tag.clicked.connect(self.open_latest_version)
        self.ui.nofrpc_tag.clicked.connect(self.open_help_nofrpc)
        self.ui.help_button.clicked.connect(self.open_help)

        # main
        self.ui.main_start.clicked.connect(self.main_start)
        self.ui.main_stop.clicked.connect(self.main_stop)
        self.ui.main_clear.clicked.connect(self.clear_log)

        # server
        self.ui.server_save.clicked.connect(self.server_save)
        self.ui.server_clear.clicked.connect(self.clear_server_sertting)
        self.ui.server_check.clicked.connect(self.check_service)

        # link
        self.ui.link_create.clicked.connect(self.on_add_button_clicked)
        self.ui.link_delete.clicked.connect(self.on_delete_button_clicked)
        self.ui.link_modify.clicked.connect(self.on_edit_button_clicked)
        self.ui.link_close.clicked.connect(self.on_close_button_clicked)
        self.ui.link_open.clicked.connect(self.on_open_button_clicked)
        self.ui.linktable.itemSelectionChanged.connect(self.on_table_item_selection_changed)

        # other
        self.ui.auto_linkname.stateChanged.connect(self.save_other_data)
        self.ui.auto_address.stateChanged.connect(self.save_other_data)
        self.ui.auto_bandwidth.stateChanged.connect(self.save_other_data)
        self.ui.auto_mini.stateChanged.connect(self.save_other_data)
        self.ui.auto_updata.stateChanged.connect(self.save_other_data)
        self.ui.mux_set.stateChanged.connect(self.save_other_data)
        self.ui.auto_linkname_box.valueChanged.connect(self.save_other_data)
        self.ui.auto_bandwidth_down.valueChanged.connect(self.save_other_data)
        self.ui.link_protocol.currentIndexChanged.connect(self.save_other_data)
        self.ui.log_translate.stateChanged.connect(self.save_other_data)

        # tags
        self.ui.check_updata.clicked.connect(self.check_updata_start)
        self.ui.check_github.clicked.connect(self.open_github)
        self.ui.check_clear.clicked.connect(self.data_clear)

        # window
        self.ui.window_mini.clicked.connect(self.showMinimized)
        self.ui.window_close.clicked.connect(self.closewindow)
    
    def bandCheckupdata(self):
        # 绑定Checkup线程的信号
        self._check_updata = CheckUpdata()
        self._check_updata.log_message.connect(self.updata_log_message)
        self._check_updata.started.connect(self.updata_started)
        self._check_updata.stopped.connect(self.updata_stopped)
    
    def bandFrp(self):
        # 绑定Frp客户端独立运行的subprocess信号
        self._frp_client = FrpClient(self.log_translate)
        self._frp_client.log_message.connect(self.on_log_message)
        self._frp_client.started.connect(self.on_frp_started)
        self._frp_client.finished.connect(self.on_frp_finished)
        self._frp_client.bandwidth_pid.connect(self.on_frp_pid)

    def bandwidth(self):
        # 绑定更新流量信息的线程信号
        self._bandwidth = Checkbandwidth()
        self._bandwidth.bandwidth_usage.connect(self.on_frp_bandwidth)

    def bandPing(self):
        # 绑定CheckServer线程的信号
        self._CheckServer = CheckServer()
        self._CheckServer.ping_message.connect(self.updata_server_ping)
        self._CheckServer.get_frp.connect(self.updata_frp_service)
        self._CheckServer.get_token.connect(self.updata_token_service)
        self._CheckServer.finished.connect(self.CheckServerShutdown)

    ##
    ## UI变化反馈
    ##
    def unset_left_highlight_botton(self):
        # 取消设置左侧高亮按钮
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
        # 左侧高亮按钮
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
        # 全部UI初始化整理
        # 该项必须放在datainit()前面,否则会导致datainit()的数据被初始化
        self.setWindowIcon(QIcon(":images/icon/logo.png"))
        self.TrayMenuSetting()
        self.FlagsUiSetting()
        self.LeftUISetting()
        self.left_highlight_botton = self.ui.page_main
        self.set_left_highlight_botton()
        self.LinkUISetting()
        self.MainUISetting()
        self.ServerUISetting()
        self.OtherUISetting()
        self.TagsUISetting()
        self.readme()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.setTabOrder(self.ui.server_IP, self.ui.server_Port)
        self.setTabOrder(self.ui.server_Port, self.ui.server_token)
     
    ##
    ## 数据读取
    ##
    def datainit(self):
        # 包含所有存储数据读取
        if not os.path.exists("data"):
            os.makedirs("data")
        if os.path.exists("./data/server.toml"):
            with open("./data/server.toml", "r", encoding="utf8") as file:
                server = toml.loads(file.read())
            self.ui.show_IP.setText(server["serverAddr"])
            self.ui.show_Port.setText(str(server["serverPort"]))
            try:
                if not server["auth"]["token"] == "无配置":
                    self.ui.show_token.setText("已配置")
            except:
                self.ui.show_token.setText("无配置")
        if not os.path.exists("./data/linktable.toml"):
            with open("./data/linktable.toml", "w", encoding="utf8") as f:
                f.write("")
        self.load_table_data()
        self.load_other_data()
        if self.auto_updata == True:
            self.check_updata_start()
        if not os.path.exists("frpc.exe"):
            self.ui.nofrpc_tag.show()

    ##
    ## 自述配置
    ##
    def readme(self):
        # 自述文件初始化
        self.ui.version.setText(self.tags.version)

    ## 
    ## 按钮设置
    ##
    def FlagsUiSetting(self):
        # 自定义导航栏初始化
        icon = QIcon(":images/icon/close.png")
        self.ui.window_close.setIcon(icon)
        self.ui.window_close.setIconSize(self.ui.window_close.size())
        icon = QIcon(":images/icon/mini.png")
        self.ui.window_mini.setIcon(icon)
        self.ui.window_mini.setIconSize(self.ui.window_close.size())
    
    def TrayMenuSetting(self):
        # 创建右键菜单并将其设置为系统托盘图标的菜单
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.windowIcon())
        self.tray_menu = QMenu(self)

        open_window_action = QAction("显示窗口", self)
        open_window_action.triggered.connect(self.showNormal)
        exit_action = QAction("关闭程序", self)
        exit_action.triggered.connect(app.quit)
        self.push_a_action = QAction("启动Frp", self)
        self.push_a_action.triggered.connect(self.main_start)
        self.push_b_action = QAction("停止Frp", self)
        self.push_b_action.triggered.connect(self.main_stop)

        line1 = QFrame(self)
        line1.setFrameShape(QFrame.HLine)
        line1.setFrameShadow(QFrame.Sunken)
        line1.setFixedWidth(100)
        line_action1 = QWidgetAction(self)
        line_action1.setDefaultWidget(line1)
        line2 = QFrame(self)
        line2.setFrameShape(QFrame.HLine)
        line2.setFrameShadow(QFrame.Sunken)
        line2.setFixedWidth(100)
        line_action2 = QWidgetAction(self)
        line_action2.setDefaultWidget(line2)

        self.tray_menu.addAction(open_window_action)
        self.tray_menu.addAction(line_action1)
        self.tray_menu.addAction(self.push_a_action)
        self.tray_menu.addAction(self.push_b_action)
        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_menu.addAction(line_action2)
        self.tray_menu.addAction(exit_action)

        self.tray_icon.show()
        self.tray_icon.activated.connect(self.trayIconActivated)
        self.push_b_action.setEnabled(False)

    def LeftUISetting(self):
        # 左侧栏UI初始化
        self.botton_highlight_color = QColor(130, 130, 130)
        self.botton_highlight_color2 = QColor(100, 100, 180)
        self.botton_highlight_color3 = QColor(100, 100, 210)
        self.ui.updata_tag.hide()
        self.ui.nofrpc_tag.hide()
    
    def ServerUISetting(self):
        # 服务器页面UI初始化
        pixmap = QPixmap(":images/icon/arrow-right.png")
        self.ui.server_seticon.setPixmap(pixmap)
        self.ui.server_seticon.setScaledContents(True)
        self.ui.server_token.setEchoMode(QLineEdit.Password)
        self.setserverbutton()

    def LinkUISetting(self):
        # 配置链接页面UI初始化
        self.botton_highlight_link = QColor(200, 80, 80)
        self.botton_highlight_link2 = QColor(80, 200, 80)
        self.botton_highlight_link3 = QColor(100, 100, 180)
        self.ui.linktable.setStyleSheet("border-radius: 0px")
        self.rows = 10  # 在这里设置列数量
        self.ui.linktable.setColumnCount(self.rows)
        self.ui.linktable.horizontalHeader().setDefaultSectionSize(100)
        self.ui.linktable.setColumnWidth(1, 70)
        self.ui.linktable.setHorizontalHeaderLabels(["服务名", "协议", "源地址", "源端口", "目的端口", "密钥", "目的服务", "链接状态", "区域", "心跳延时"])
        self.ui.linktable.horizontalHeader().setStretchLastSection(True)
        self.ui.linktable.verticalHeader().setVisible(False)
        self.ui.linktable.setSelectionBehavior(QTableWidget.SelectRows)
        self.ui.linktable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.ui.link_delete.setEnabled(False)
        self.ui.link_modify.setEnabled(False)

        self.ui.link_close.hide()
        self.ui.link_open.hide()
        
    def MainUISetting(self):
        # 开始页面UI初始化
        self.background_color_low = QColor(40, 40, 60)
        self.background_color_high = QColor(60, 60, 80)
        self.highlight_color_main_stop = QColor(130, 130, 180)
        self.highlight_color_main_start = QColor(80, 160, 80)
        self.setstarthigh()
        icon = QIcon(":images/icon/play.png")
        self.ui.main_start.setIcon(icon)
        self.ui.main_start.setIconSize(self.ui.window_close.size())
        icon = QIcon(":images/icon/stop.png")
        self.ui.main_stop.setIcon(icon)
        self.ui.main_stop.setIconSize(self.ui.window_close.size())
        icon = QIcon(":images/icon/trash.png")
        self.ui.main_clear.setIcon(icon)
        self.ui.main_clear.setIconSize(self.ui.window_close.size())
        
        self.ui.net_updata.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.net_updata_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.net_updata_str.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.net_updata_str_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.net_downdata.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.net_downdata_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.net_downdata_str.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.ui.main_log.setReadOnly(True)
        self.ui.net_updata.setReadOnly(True)
        self.ui.net_updata_2.setReadOnly(True)
        self.ui.net_updata_str.setReadOnly(True)
        self.ui.net_updata_str_2.setReadOnly(True)
        self.ui.net_downdata.setReadOnly(True)
        self.ui.net_downdata_2.setReadOnly(True)
        self.ui.net_downdata_str.setReadOnly(True)

        self.ui.main_start.setEnabled(True)
        self.ui.main_stop.setEnabled(False)
    
    def OtherUISetting(self):
        self.ui.auto_linkname_box.setMaximum(20)
        self.ui.auto_bandwidth_down.setMaximum(1000000)

    def TagsUISetting(self):
        self.ui.tags_check_updata.hide()
        self.ui.tags_version.setText(self.tags.versionaddit+" "+self.tags.version)
        self.ui.tags_author.setText(self.tags.author)
        self.ui.tags_license.setText(self.tags.licenes)

    def setstarthigh(self):
        # 设置按钮高亮
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
        # 停止按钮高亮
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
    
    def setserverbutton(self):
        self.ui.server_IP.setStyleSheet('''
            QLineEdit {
                border-radius: 0px;
                border: none;
                background-color: rgb(60, 60, 80);
                color: white;
            }
            QLineEdit:focus {
                border-radius: 0px;
                border: none;
                background-color: rgb(80, 80, 90);
                color: white;
            }
        ''')
        self.ui.server_Port.setStyleSheet('''
            QLineEdit {
                border-radius: 0px;
                border: none;
                background-color: rgb(60, 60, 80);
                color: white;
            }
            QLineEdit:focus {
                border-radius: 0px;
                border: none;
                background-color: rgb(80, 80, 90);
                color: white;
            }
        ''')
        self.ui.server_token.setStyleSheet('''
            QLineEdit {
                border-radius: 0px;
                border: none;
                background-color: rgb(60, 60, 80);
                color: white;
            }
            QLineEdit:focus {
                border-radius: 0px;
                border: none;
                background-color: rgb(80, 80, 90);
                color: white;
            }
        ''')


    def setmain(self):
        # 将页面切换到 -> 开始
        self.ui.stackedWidget.setCurrentIndex(0)
        self.unset_left_highlight_botton()
        self.left_highlight_botton = self.ui.page_main
        self.set_left_highlight_botton()

    def setserver(self):
        # 将页面切换到 -> 服务器
        self.ui.stackedWidget.setCurrentIndex(1)
        self.unset_left_highlight_botton()
        self.left_highlight_botton = self.ui.page_server
        self.set_left_highlight_botton()
        if self.ui.show_IP.text() == "无配置":
            self.updata_server_ping([2, "- ms"])
        else:
            self.check_service()

    def setlink(self):
        # 将页面切换到 -> 配置链接
        self.ui.stackedWidget.setCurrentIndex(2)
        self.unset_left_highlight_botton()
        self.left_highlight_botton = self.ui.page_link
        self.set_left_highlight_botton()

    def setother(self):
        # 将页面切换到 -> 其他配置
        self.ui.stackedWidget.setCurrentIndex(3)
        self.unset_left_highlight_botton()
        self.left_highlight_botton = self.ui.page_other
        self.set_left_highlight_botton()

    def settags(self):
        # 将页面切换到 -> 关于
        self.ui.tags_check_updata.hide()
        self.ui.stackedWidget.setCurrentIndex(4)
        self.unset_left_highlight_botton()
        self.left_highlight_botton = self.ui.page_tags
        self.set_left_highlight_botton()
    
    def check_updata_start(self):
        # 开始检查更新
        if self._check_updata.isRunning() == True:
            return
        self._check_updata.start()
        
    
    def closewindow(self):
        # 关闭按钮定义
        if self.auto_mini == True:
            self.hide()
            self.tray_icon.showMessage("EFS", "将在后台运行继续运行", QSystemTrayIcon.Information, 1000)
        else:
            self.shutdown()

    def trayIconActivated(self, reason):
        # 如果用户双击了系统托盘图标，则显示窗口
        if reason == QSystemTrayIcon.DoubleClick:
            self.showNormal()

    ##
    ## 主要模块
    ##
    def main_start(self):
        # 启动Frp客户端
        self.ui.nofrpc_tag.hide()
        if not os.path.exists("frpc.exe"):
            self.ui.nofrpc_tag.show()
            self.ui.main_log.insertPlainText("未找到frpc.exe, 请确认frpc.exe和软件在同一目录\n")
            return
        if self.checkfile() == False:
            self.ui.main_log.insertPlainText("必要的配置还未填写, 无法开启服务\n")
            return
        self.frpcData_save()
        self._frp_client.start()

    def main_stop(self):
        # 关闭Frp客户端
        self._frp_client.stop()
    
    def clear_log(self):
        # 清除启动日志
        self.ui.main_log.setPlainText("")

    def server_save(self):
        # 服务器配置文件保存
        ip = self.ui.server_IP.text()
        port = self.ui.server_Port.text()
        token = self.ui.server_token.text()

        check = True
        if self.portcheck(port, 1, 65565) == False:
            self.ui.server_Port.setStyleSheet("border: 2px solid red; border-radius: 0px;")
            check = False
        if check == False:
            return
        self.ui.server_IP.setStyleSheet("")
        self.ui.server_Port.setStyleSheet("")

        link = {}
        link["serverAddr"] = ip
        link["serverPort"] = int(port)
        if token == "":
            self.ui.show_token.setText("无配置")
        else:
            link["auth"] = {"token": token}
            self.ui.show_token.setText("已配置")
        self.ui.show_IP.setText(ip)
        self.ui.show_Port.setText(port)

        self.ui.server_token.setText("")
        self.setserverbutton()
        with open("./data/server.toml", "w", encoding="utf-8") as file:
            file.write(toml.dumps(link))
        self.check_service()

    def link_ini_save(self):
        # linktable表文件编译
        if os.path.exists("./data/link.toml"):
            if os.path.getmtime("./data/link.toml") > os.path.getmtime("./data/linktable.toml"):
                return
        link = {"proxies" : []}
        linksetup = ["name","type","localIp","localPort","remotePort","secretKey","serverName","healthCheck"]
        with open("./data/linktable.toml","r+",encoding="utf-8") as u:
            for a in u.readlines():
                b = a.split(",")
                if not b[7] == "开启":
                    continue
                tags = 0
                in_proxy = {}
                while not tags >= 7:
                    if b[tags] == "":
                        pass
                    elif "type" == linksetup[tags]:
                        if len(b[tags].split("-")) == 2:
                            in_type = b[tags].split("-")[0]
                        else:
                            in_type = b[tags]
                        in_proxy[linksetup[tags]] = in_type
                    elif "Port" in linksetup[tags]:
                        in_proxy[linksetup[tags]] = int(b[tags])
                    else:
                        in_proxy[linksetup[tags]] = b[tags]
                    tags += 1
                # 第九项数据
                if b[9] in ("默认传输", "kcp传输", "quic传输", ""): # 此处为旧版本的配置文件做了兼容，将在未来取消兼容性
                    pass
                else:
                    in_proxy[linksetup[tags]] = {"type": in_type, "intervalSeconds": int(b[9])}
                link["proxies"].append(in_proxy)
        with open("./data/link.toml", "w", encoding="utf-8") as file:
            file.write(toml.dumps(link))

    def frpcData_save(self):
        # 整理打包frp.toml
        self.link_ini_save()
        if os.path.exists("./data/frpc.toml"):
            datadiff = [os.path.getmtime("./data/frpc.toml") > os.path.getmtime("./data/more.ini"),
                        os.path.getmtime("./data/frpc.toml") > os.path.getmtime("./data/server.toml"),
                        os.path.getmtime("./data/frpc.toml") > os.path.getmtime("./data/link.toml")]
            if all(datadiff):
                return
        self.ui.main_log.insertPlainText("配置文件正在编译...\n")
        if self.mux_set:
            frpc = 'tcpMux = true\n'
        else:
            frpc = 'tcpMux = false\n'

        with open("./data/server.toml","r+",encoding="utf-8") as u:
            frpc += "".join(u.readlines())

        if self.link_protocol == 1:
            frpc += '[transport]\nprotocol = "kcp"\n'
        elif self.link_protocol == 2:
            frpc += '[transport]\nprotocol = "quic"\n'

        with open("./data/link.toml", "r+", encoding="utf-8") as u:
            frpc += "".join(u.readlines())

        with open("./data/frpc.toml","w+",encoding="utf-8") as u:
            for i in frpc:
                u.write(i)
    
    def save_table_data(self):
        # 保存表文件
        with open("./data/linktable.toml", "w", encoding="utf-8") as f:
            # 写入数据
            for i in range(self.ui.linktable.rowCount()):
                row_data = []
                for j in range(self.ui.linktable.columnCount()):
                    item = self.ui.linktable.item(i, j)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append("")
                    row_data.append(",")
                row_data.append("End")
                f.write("".join(row_data) + "\n")
    
    def load_table_data(self):
        # 读取表文件
        def tableerror():
            now = datetime.now()
            time_str = now.strftime("%H%M%S")
            os.rename("./data/linktable.toml", f"./data/linktable_{time_str}.bak")
            with open("./data/linktable.toml", "w", encoding="utf8") as f:
                f.write("")
            self.ui.linktable.clearContents()
            self.ui.linktable.setRowCount(0)
            dialog = QDialog(self)
            dialog.setWindowTitle("发生错误")
            dialog.setWindowFlag(Qt.WindowType.FramelessWindowHint)
            layout = QVBoxLayout()
            label = QLabel("读取链接数据时发生错误")
            layout.addWidget(label, alignment=Qt.AlignHCenter)
            dialog.setLayout(layout)
            button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok)
            layout.addWidget(button_box, alignment=Qt.AlignHCenter)
            button_box.accepted.connect(dialog.accept)
            if dialog.exec() == QDialog.Accepted:
                dialog.deleteLater()
                return
        try:
            with open("./data/linktable.toml", "r", encoding="utf-8") as f:            
                # 读取数据
                row = 0
                for line in f:
                    data = line.strip().split(",")
                    self.ui.linktable.insertRow(row)
                    for col, text in enumerate(data):
                        if col == 8:
                            status = item.text()
                        if text == "End":
                            break
                        elif text == "":
                            item = QtWidgets.QTableWidgetItem("")
                        else:
                            item = QtWidgets.QTableWidgetItem(text)
                        self.ui.linktable.setItem(row, col, item)
                    row_items = [self.ui.linktable.item(row, u) for u in range(self.rows)]
                    if status == "开启":
                        row_items[0].setBackground(QColor(100, 150, 100))
                    else:
                        row_items[0].setBackground(QColor(200, 100, 100))
                    row += 1
        except:
            tableerror()
            return
    
    def save_other_data(self):
        # 保存其他设置的配置文件
        link = configparser.ConfigParser()
        link.add_section("common")
        # 自动填写链接名称
        link["common"]["auto_name_box"] = str(self.ui.auto_linkname_box.value())
        self.auto_linkname_box = self.ui.auto_linkname_box.value()
        if self.ui.auto_linkname.isChecked():
            link["common"]["auto_name"] = "True"
            self.auto_linkname = True
        else:
            link["common"]["auto_name"] = "False"
            self.auto_linkname = False
        self.ui.auto_linkname_box.setReadOnly(not self.auto_linkname)

        # 自动填写源地址
        if self.ui.auto_address.isChecked():
            link["common"]["auto_address"] = "True"
            self.auto_address = True
        else:
            link["common"]["auto_address"] = "False"
            self.auto_address = False

        # 带宽预警
        link["common"]["auto_bandwidth_down"] = str(self.ui.auto_bandwidth_down.value())
        self.auto_bandwidth_down = self.ui.auto_bandwidth_down.value()
        if self.ui.auto_bandwidth.isChecked():
            link["common"]["auto_bandwidth"] = "True"
            self.auto_bandwidth = True
        else:
            link["common"]["auto_bandwidth"] = "False"
            self.auto_bandwidth = False
        self.ui.auto_bandwidth_down.setReadOnly(not self.auto_bandwidth)

        # 最小化托盘
        if self.ui.auto_mini.isChecked():
            link["common"]["auto_mini"] = "True"
            self.auto_mini = True
        else:
            link["common"]["auto_mini"] = "False"
            self.auto_mini = False

        # 检查更新
        if self.ui.auto_updata.isChecked():
            link["common"]["auto_updata"] = "True"
            self.auto_updata = True
        else:
            link["common"]["auto_updata"] = "False"
            self.auto_updata = False
            
        # 链接方式
        if self.ui.link_protocol.currentText() == "默认":
            self.link_protocol = 0
        elif self.ui.link_protocol.currentText() == "KCP":
            self.link_protocol = 1
        elif self.ui.link_protocol.currentText() == "QUIC":
            self.link_protocol = 2
        link["common"]["link_protocol"] = str(self.link_protocol)

        # 端口聚合
        if self.ui.mux_set.isChecked():
            link["common"]["mux_set"] = "True"
            self.mux_set = True
        else:
            link["common"]["mux_set"] = "False"
            self.mux_set = False

        # 日志翻译
        if self.ui.log_translate.isChecked():
            link["common"]["log_translate"] = "True"
            self.log_translate = True
        else:
            link["common"]["log_translate"] = "False"
            self.log_translate = False

        with open("./data/more.ini", "w", encoding="utf-8") as configfile:
            link.write(configfile)

    def load_other_data(self):
        # 读取其他设置的配置文件
        def load_file():
            # 加载配置
            link = configparser.ConfigParser()
            link.read("./data/more.ini","utf-8")
            self.auto_linkname = link.getboolean("common", "auto_name")
            self.auto_linkname_box = link["common"]["auto_name_box"]
            self.auto_address = link.getboolean("common", "auto_address")
            self.auto_bandwidth = link.getboolean("common", "auto_bandwidth")
            self.auto_bandwidth_down = link["common"]["auto_bandwidth_down"]
            self.auto_mini = link.getboolean("common", "auto_mini")
            self.auto_updata = link.getboolean("common", "auto_updata")
            self.link_protocol = link["common"]["link_protocol"]
            self.mux_set = link.getboolean("common", "mux_set")
            self.log_translate = link.getboolean("common", "log_translate")

        if not os.path.exists("./data/more.ini"):
            self.default_other_data()
        try:
            load_file()
        except:
            now = datetime.now()
            time_str = now.strftime("%H%M%S")
            os.rename("./data/more.ini", f"./data/more_{time_str}.bak")
            self.default_other_data()
            load_file()

        self.ui.auto_linkname_box.setValue(int(self.auto_linkname_box))
        self.ui.auto_bandwidth_down.setValue(int(self.auto_bandwidth_down))
        self.ui.link_protocol.setCurrentIndex(int(self.link_protocol))

        self.ui.auto_linkname.setChecked(self.auto_linkname)
        self.ui.auto_address.setChecked(self.auto_address)
        self.ui.auto_bandwidth.setChecked(self.auto_bandwidth)
        self.ui.auto_mini.setChecked(self.auto_mini)
        self.ui.auto_updata.setChecked(self.auto_updata)
        self.ui.mux_set.setChecked(self.mux_set)

        self.ui.auto_linkname_box.setReadOnly(not self.auto_linkname)
        self.ui.auto_bandwidth_down.setReadOnly(not self.auto_bandwidth)

        self.ui.log_translate.setChecked(self.log_translate)
    
    def default_other_data(self):
        # more.ini缺省值
        link = configparser.ConfigParser()
        link.add_section("common")
        link["common"]["auto_name"] = "True"
        link["common"]["auto_name_box"] = "8"
        link["common"]["auto_address"] = "True"
        link["common"]["auto_bandwidth"] = "True"
        link["common"]["auto_bandwidth_down"] = "10"
        link["common"]["auto_mini"] = "True"
        link["common"]["auto_updata"] = "True"
        link["common"]["link_protocol"] = "0"
        link["common"]["mux_set"] = "True"
        link["common"]["log_translate"] = "False"
        with open("./data/more.ini", "w", encoding="utf-8") as configfile:
            link.write(configfile)

    def auto_creat_linkname(self):
        # 自动生成链接名
        chars = string.ascii_uppercase + string.digits
        return "".join(random.choice(chars) for x in range(int(self.auto_linkname_box)))
        
    def open_latest_version(self):
        webbrowser.open("https://github.com/LyceenAiro/EazyFrpSetting/releases/latest")

    def open_help_nofrpc(self):
        webbrowser.open("https://github.com/LyceenAiro/EazyFrpSetting/blob/doc/v3_file/help/nofrpc.md")
    
    def open_github(self):
        webbrowser.open("https://github.com/LyceenAiro/EazyFrpSetting")
    
    def open_help(self):
        webbrowser.open("https://github.com/LyceenAiro/EazyFrpSetting/blob/doc/v3_file/help/help.md")
    
    def data_clear(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("清除数据")
        dialog.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        frame = QFrame(dialog)
        frame.setFrameShape(QFrame.Box)
        frame.setStyleSheet("border-radius: 0px")
        frame.setLineWidth(2)
        frame.setFixedSize(223, 68)

        layout = QVBoxLayout()
        label = QLabel("确定要关闭程序并清除所有数据吗？")
        layout.addWidget(label)
        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        layout.addWidget(button_box, alignment=Qt.AlignHCenter)

        dialog.setLayout(layout)

        if dialog.exec() == QDialog.Accepted:
            folder_path = 'data'
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                except:
                    pass
            self.shutdown()
        else:
            dialog.deleteLater()
            return

    def clear_server_sertting(self):
        self.ui.show_IP.setText("无配置")
        self.ui.show_Port.setText("无配置")
        self.ui.show_token.setText("无配置")
        self.updata_server_ping([2, "- ms"])
        if os.path.exists("./data/server.toml"):
            os.remove("./data/server.toml")

    def shutdown(self):
        # 关闭程序
        self._frp_client.stop()
        self._frp_client.finished.disconnect()
        self._frp_client.log_message.disconnect()
        self._frp_client.deleteLater()
        self._check_updata.stop()
        self._CheckServer.stop()
        self._CheckServer.finished.disconnect()
        self._CheckServer.get_frp.disconnect()
        self._CheckServer.get_token.disconnect()
        self._CheckServer.ping_message.disconnect()
        self._CheckServer.deleteLater()
        self.close()
        app.quit()

    ##
    ## 信号动作
    ##
    def on_log_message(self, message):
        # 当frp日志更新时发送到主窗口 | 变量 -> 信息
        self.ui.main_log.insertPlainText(message)
        self.main_log_scrollbar.setValue(self.main_log_scrollbar.maximum())

    def on_frp_started(self):
        # 当收到Frp启动命令时向窗口的反馈
        if not os.path.exists("frpc.exe"):
            self.ui.nofrpc_tag.show()
            return
        self.ui.main_log.insertPlainText("frp服务已开启\n")
        self.ui.main_start.setEnabled(False)
        self.ui.main_stop.setEnabled(True)
        self.push_a_action.setEnabled(False)
        self.push_b_action.setEnabled(True)
        self.setstophigh()
    
    def on_frp_pid(self, pid):
        if pid == "" or pid < 0:
            return
        self._bandwidth.start(pid)

    def on_frp_finished(self):
        # 当收到frp停止的信号时向窗口反馈
        self._bandwidth.stop()
        self._frp_client.stop()
        self.ui.main_start.setEnabled(True)
        self.ui.main_stop.setEnabled(False)
        self.ui.net_updata.setText("- ms")
        self.ui.net_downdata.setText("- mbps")
        self.push_a_action.setEnabled(True)
        self.push_b_action.setEnabled(False)
        self.ui.main_log.insertPlainText("frp服务已关闭\n")
        self.setstarthigh()
        self.bandFrp()

    def on_frp_bandwidth(self, usage):
        # 更新信息栏
        if usage[0] == None:
            self.ui.net_updata.setText(f"500+ ms")
        else:
            self.ui.net_updata.setText(f"{usage[0]:.1f} ms")
        self.ui.net_downdata.setText(f"{usage[1]} mbps")
        self.ui.net_updata_2.setText(usage[2])
        self.ui.net_downdata_2.setText(usage[3])
        if self.warning_clock > 0 :
            self.warning_clock -= 1
        elif self.auto_bandwidth == True:
            if usage[1] >= int(self.auto_bandwidth_down):
                self.tray_icon.showMessage("带宽预警", f"带宽超过警告阈值\n{usage[1]} mbps\n", QSystemTrayIcon.Information, 1000)
                self.warning_clock = 60

    def updata_started(self):
        # 当检查更新开启时执行
        self.ui.check_updata.setEnabled(False)
        self.ui.tags_check_updata.setText("正在检查更新...")
        self.ui.tags_check_updata.show()
    
    def updata_log_message(self, message, check_bool):
        # 收取更新消息
        self.ui.tags_check_updata.setText(message)
        if check_bool == True:
            self.ui.updata_tag.show()
        self.ui.tags_check_updata.show()
        self._check_updata.stop()

    def updata_stopped(self):
        self.ui.check_updata.setEnabled(True)
        self.bandCheckupdata()
    
    def add_table_row(self, data):
        # 向表写入数据
        row_count = self.ui.linktable.rowCount()
        self.ui.linktable.insertRow(row_count)
        for i, item in enumerate(data):
            table_item = QTableWidgetItem(item)
            self.ui.linktable.setItem(row_count, i, table_item)
    
    def on_table_item_selection_changed(self):
        # 当表中数据发生修改时向窗口反馈
        selected_rows = self.ui.linktable.selectionModel().selectedRows()
        if len(selected_rows) > 0:
            selected_row = selected_rows[0].row()
            data = self.ui.linktable.item(selected_row, 7).text()
            if data == "开启":
                self.ui.link_open.hide()
                self.ui.link_close.show()
            else:
                self.ui.link_open.show()
                self.ui.link_close.hide()
            self.ui.link_modify.setEnabled(True)
            self.ui.link_delete.setEnabled(True)
            
        else:
            self.ui.link_modify.setEnabled(False)
            self.ui.link_delete.setEnabled(False)
            self.ui.link_close.hide()
            self.ui.link_open.hide()

    def on_close_button_clicked(self):
        # 关闭选中的所有链接
        for i in range(len(self.ui.linktable.selectionModel().selectedRows())):
            selected_row = self.ui.linktable.selectionModel().selectedRows()[i].row()
            self.ui.linktable.setItem(selected_row, 7, QTableWidgetItem("关闭"))
            self.save_table_data()
            row_items = [self.ui.linktable.item(selected_row, i) for i in range(self.rows)]
            row_items[0].setBackground(QColor(200, 100, 100))
        self.ui.link_close.hide()
        self.ui.link_open.show()

    def on_open_button_clicked(self):
        # 开启选中的所有链接
        for i in range(len(self.ui.linktable.selectionModel().selectedRows())):
            selected_row = self.ui.linktable.selectionModel().selectedRows()[i].row()
            self.ui.linktable.setItem(selected_row, 7, QTableWidgetItem("开启"))
            self.save_table_data()
            row_items = [self.ui.linktable.item(selected_row, i) for i in range(self.rows)]
            row_items[0].setBackground(QColor(100, 150, 100))
        self.ui.link_close.show()
        self.ui.link_open.hide()

    def on_edit_button_clicked(self):
        # 当编辑按钮被触发时弹出窗口
        # 本函数包含一个子窗口
        def check_in():
            # 纠错
            edits = [edit1, edit3, edit4, edit5]
            for edit in edits:
                edit.setStyleSheet("border-radius: 0px;")
            check = True
            if edit1.text() == "":
                if self.auto_linkname == True:
                    edit1.setText(self.auto_creat_linkname())
                else:
                    edit1.setStyleSheet("border: 1px solid red;")
            if edit3.text() == "":
                if self.auto_address == True:
                    edit3.setText("127.0.0.1")
                else:
                    edit3.setStyleSheet("border: 1px solid red;")
                    check = False
            elif self.ipcheck(edit3.text()) == False:
                edit3.setStyleSheet("border: 1px solid red;")
                check = False
            if self.portcheck(edit4.text(), 1, 65565) == False:
                edit4.setStyleSheet("border: 1px solid red;")
                check = False
            if self.portcheck(edit5.text(), 1, 65565) == False:
                edit5.setStyleSheet("border: 1px solid red;")
                check = False
            if edit2.currentText() in ("tcp", "udp"):
                edit6.setText("")
                edit7.setText("")
            else:
                edit10.setText("")
            if edit10.text() == "":
                pass
            elif self.portcheck(edit10.text(), 0, 999999) == False:
                edit10.setStyleSheet("border: 1px solid red;")
                check = False
            
            elif edit2.currentText() in ("xtcp-host", "stcp-host"):
                edit7.setText("")
            if check == False:
                return
            dialog.accept()
        selected_row = self.ui.linktable.selectionModel().selectedRows()[0].row()
        data = [self.ui.linktable.item(selected_row, i).text() for i in range(self.rows)]
        try:      
            dialog = QDialog(self)
            dialog.setWindowTitle("编辑链接")
            dialog.setWindowFlag(Qt.WindowType.FramelessWindowHint)

            # 使用水平布局
            hlayout1 = QHBoxLayout()
            hlayout2 = QHBoxLayout()
            hlayout3 = QHBoxLayout()
            hlayout4 = QHBoxLayout()
            hlayout5 = QHBoxLayout()

            frame = QFrame(dialog)
            frame.setFrameShape(QFrame.Box)
            frame.setStyleSheet("border-radius: 0px")
            frame.setLineWidth(2)
            frame.setFixedSize(253, 219)

            layout = QVBoxLayout()

            label = QLabel("编辑链接")
            layout.addWidget(label)
            
            edit1 = QLineEdit(data[0])
            if self.auto_linkname == True:
                edit1.setPlaceholderText("服务名称(留空自动生成)")
            else:
                edit1.setPlaceholderText("服务名称")
            edit1.setFixedWidth(145)
            hlayout1.addWidget(edit1)

            edit2 = QComboBox()
            edit2.addItems(["tcp", "udp", "xtcp-host", "xtcp-client", "stcp-host", "stcp-client"])
            edit2.setCurrentText(data[1])
            edit2.setFixedWidth(80)
            hlayout1.addWidget(edit2)

            edit3 = QLineEdit(data[2])
            if self.auto_address == True:
                edit3.setPlaceholderText("源地址(留空自动生成)")
            else:
                edit3.setPlaceholderText("源地址")
            hlayout2.addWidget(edit3)

            edit4 = QLineEdit(data[3])
            edit4.setPlaceholderText("源端口")
            edit4.setMaxLength(5)
            edit4.setFixedWidth(80)
            hlayout2.addWidget(edit4)

            layout.addLayout(hlayout1)
            layout.addLayout(hlayout2)

            edit5 = QLineEdit(data[4])
            edit5.setPlaceholderText("目的端口")
            edit5.setMaxLength(5)
            edit5.setFixedWidth(80)

            edit6 = QLineEdit(data[5])
            edit6.setPlaceholderText("密钥")
            
            hlayout3.addWidget(edit6)
            hlayout3.addWidget(edit5)
            layout.addLayout(hlayout3)

            edit7 = QLineEdit(data[6])
            edit7.setPlaceholderText("目的服务")

            edit10 = QLineEdit(data[9])
            edit10.setPlaceholderText("心跳延时")
            edit4.setMaxLength(5)
            edit10.setFixedWidth(80)

            hlayout4.addWidget(edit7)
            hlayout4.addWidget(edit10)
            layout.addLayout(hlayout4)

            edit8 = QComboBox()
            edit8.addItems(["开启", "关闭"])
            edit8.setCurrentText(data[7])
            edit8.setFixedWidth(80)

            edit9 = QComboBox()
            edit9.addItems(["MainServer"])
            edit9.setCurrentText(data[8])
            
            hlayout5.addWidget(edit9)
            hlayout5.addWidget(edit8)
            layout.addLayout(hlayout5)

        except:
            dialog.deleteLater()
            dialog = QDialog(self)
            dialog.setWindowTitle("无法编辑")
            dialog.setWindowFlag(Qt.WindowType.FramelessWindowHint)

            frame = QFrame(dialog)
            frame.setFrameShape(QFrame.Box)
            frame.setStyleSheet("border-radius: 0px")
            frame.setLineWidth(2)
            frame.setFixedSize(224, 68)

            layout = QVBoxLayout()
            label = QLabel("链接数据不完整或已过时，无法编辑")
            layout.addWidget(label, alignment=Qt.AlignHCenter)
            dialog.setLayout(layout)
            button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok)
            layout.addWidget(button_box, alignment=Qt.AlignHCenter)
            button_box.accepted.connect(dialog.accept)
            if dialog.exec() == QDialog.Accepted:
                row_items = [self.ui.linktable.item(selected_row, i) for i in range(self.rows)]
                for item in row_items:
                    item.setBackground(QColor(150, 150, 100))
                dialog.deleteLater()
                return

        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        button_box.accepted.connect(check_in)
        button_box.rejected.connect(dialog.reject)
        layout.addWidget(button_box, alignment=Qt.AlignHCenter)

        dialog.setLayout(layout)

        if dialog.exec() == QDialog.Accepted:
            # 更新数据
            self.ui.linktable.setItem(selected_row, 0, QTableWidgetItem(edit1.text()))
            self.ui.linktable.setItem(selected_row, 1, QTableWidgetItem(edit2.currentText()))
            self.ui.linktable.setItem(selected_row, 2, QTableWidgetItem(edit3.text()))
            self.ui.linktable.setItem(selected_row, 3, QTableWidgetItem(edit4.text()))
            self.ui.linktable.setItem(selected_row, 4, QTableWidgetItem(edit5.text()))
            self.ui.linktable.setItem(selected_row, 5, QTableWidgetItem(edit6.text()))
            self.ui.linktable.setItem(selected_row, 6, QTableWidgetItem(edit7.text()))
            self.ui.linktable.setItem(selected_row, 7, QTableWidgetItem(edit8.currentText()))
            self.ui.linktable.setItem(selected_row, 8, QTableWidgetItem(edit9.currentText()))
            self.ui.linktable.setItem(selected_row, 9, QTableWidgetItem(edit10.text()))
            self.save_table_data()
            dialog.deleteLater()
        else:
            dialog.deleteLater()
            return

        status = edit8.currentText()
        row_items = [self.ui.linktable.item(selected_row, i) for i in range(self.rows)]
        if status == "开启":
            row_items[0].setBackground(QColor(100, 150, 100))
        else:
            row_items[0].setBackground(QColor(200, 100, 100))
 
    def on_add_button_clicked(self):
        # 当添加按钮被触发时弹出窗口
        # 本函数包含一个子窗口
        def check_in():
            # 纠错
            edits = [edit1, edit3, edit4, edit5]
            for edit in edits:
                edit.setStyleSheet("")
            check = True
            if edit1.text() == "":
                if self.auto_linkname == True:
                    edit1.setText(self.auto_creat_linkname())
                else:
                    edit1.setStyleSheet("border: 1px solid red;")
            if edit3.text() == "":
                if self.auto_address == True:
                    edit3.setText("127.0.0.1")
                else:
                    edit3.setStyleSheet("border: 1px solid red;")
                    check = False
            elif self.ipcheck(edit3.text()) == False:
                edit3.setStyleSheet("border: 1px solid red;")
                check = False
            if self.portcheck(edit4.text(), 1, 65565) == False:
                edit4.setStyleSheet("border: 1px solid red;")
                check = False
            if self.portcheck(edit5.text(), 1, 65565) == False:
                edit5.setStyleSheet("border: 1px solid red;")
                check = False
            if edit10.text() == "":
                pass
            elif self.portcheck(edit10.text(), 0, 999999) == False:
                edit10.setStyleSheet("border: 1px solid red;")
                check = False
            if edit2.currentText() in ("tcp", "udp"):
                edit6.setText("")
                edit7.setText("")
            elif edit2.currentText() in ("xtcp-host", "sctp-host"):
                edit7.setText("")
            if check == False:
                return
            dialog.accept()

        dialog = QDialog(self)
        dialog.setWindowTitle("创建链接")
        dialog.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        # 使用水平布局
        hlayout1 = QHBoxLayout()
        hlayout2 = QHBoxLayout()
        hlayout3 = QHBoxLayout()
        hlayout4 = QHBoxLayout()
        hlayout5 = QHBoxLayout()

        frame = QFrame(dialog)
        frame.setFrameShape(QFrame.Box)
        frame.setStyleSheet("border-radius: 0px")
        frame.setLineWidth(2)
        frame.setFixedSize(253, 219)

        layout = QVBoxLayout()

        label = QLabel("创建链接")
        layout.addWidget(label)

        edit1 = QLineEdit()
        if self.auto_linkname == True:
            edit1.setPlaceholderText("服务名称(留空自动生成)")
        else:
            edit1.setPlaceholderText("服务名称")
        edit1.setFixedWidth(145)  # 这里定义整个宽度
        hlayout1.addWidget(edit1)

        edit2 = QComboBox()
        edit2.addItems(["tcp", "udp", "xtcp-host", "xtcp-client", "stcp-host", "stcp-client"])
        edit2.setFixedWidth(80)
        hlayout1.addWidget(edit2)

        edit3 = QLineEdit()
        if self.auto_address == True:
            edit3.setPlaceholderText("源地址(留空自动生成)")
        else:
            edit3.setPlaceholderText("源地址")
        hlayout2.addWidget(edit3)

        edit4 = QLineEdit()
        edit4.setPlaceholderText("源端口")
        edit4.setMaxLength(5)
        edit4.setFixedWidth(80)
        hlayout2.addWidget(edit4)

        layout.addLayout(hlayout1)
        layout.addLayout(hlayout2)

        edit5 = QLineEdit()
        edit5.setPlaceholderText("目的端口")
        edit5.setMaxLength(5)
        edit5.setFixedWidth(80)

        edit6 = QLineEdit()
        edit6.setPlaceholderText("密钥")

        hlayout3.addWidget(edit6)
        hlayout3.addWidget(edit5)
        layout.addLayout(hlayout3)

        edit7 = QLineEdit()
        edit7.setPlaceholderText("目的服务")

        edit10 = QLineEdit()
        edit10.setPlaceholderText("心跳延时")
        edit10.setMaxLength(6)
        edit10.setFixedWidth(80)
        edit10.setFixedWidth(80)

        hlayout4.addWidget(edit7)
        hlayout4.addWidget(edit10)
        layout.addLayout(hlayout4)

        edit8 = QComboBox()
        edit8.addItems(["开启", "关闭"])
        edit8.setFixedWidth(80)

        edit9 = QComboBox()
        edit9.addItems(["MainServer"])

        hlayout5.addWidget(edit9)
        hlayout5.addWidget(edit8)
        layout.addLayout(hlayout5)

        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        button_box.accepted.connect(check_in)
        button_box.rejected.connect(dialog.reject)
        layout.addWidget(button_box, alignment=Qt.AlignHCenter)

        dialog.setLayout(layout)

        if dialog.exec() == QDialog.Accepted:
            # 添加数据
            self.add_table_row([edit1.text(), edit2.currentText(), edit3.text(), edit4.text(), edit5.text(), edit6.text(), edit7.text(), edit8.currentText(), edit9.currentText(), edit10.text()])
            self.save_table_data()
            dialog.deleteLater()
        else:
            dialog.deleteLater()
            return
        
        status = edit8.currentText()
        row_items = [self.ui.linktable.item(self.ui.linktable.rowCount() - 1, i) for i in range(self.rows)]
        if status == "开启":
            row_items[0].setBackground(QColor(100, 150, 100))
        else:
            row_items[0].setBackground(QColor(200, 100, 100))

    def on_delete_button_clicked(self):
        # 当删除按钮触发时删除选中行
        dialog = QDialog(self)
        dialog.setWindowTitle("删除链接")
        dialog.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        frame = QFrame(dialog)
        frame.setFrameShape(QFrame.Box)
        frame.setStyleSheet("border-radius: 0px")
        frame.setLineWidth(2)
        frame.setFixedSize(196, 68)

        layout = QVBoxLayout()
        label = QLabel("确定要删除选定的链接吗？")
        layout.addWidget(label)
        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        layout.addWidget(button_box, alignment=Qt.AlignHCenter)

        dialog.setLayout(layout)

        if dialog.exec() == QDialog.Accepted:
            selected_rows = self.ui.linktable.selectionModel().selectedRows()
            for row in selected_rows:
                self.ui.linktable.removeRow(row.row())
            self.save_table_data()
            dialog.deleteLater()
        else:
            dialog.deleteLater()
            return
        
    def check_service(self):
        # 检查与服务器的连接状态如何
        get_ip = self.ui.show_IP.text()
        if get_ip == "无配置":
            return
        self.ui.server_service.setStyleSheet('''
            QLabel {
            background-color: rgb(200, 200, 200);
            border-radius: 0px;
            }
            ''')
        self.ui.frp_service.setStyleSheet('''
            QLabel {
            background-color: rgb(200, 200, 200);
            border-radius: 0px;
            }
            ''')
        self.ui.token_service.setStyleSheet('''
            QLabel {
            background-color: rgb(200, 200, 200);
            border-radius: 0px;
            }
            ''')
        self.ui.server_ping.setText("... ms")
        self._CheckServer.address = get_ip
        self._CheckServer.start()
    
    def updata_frp_service(self, isrun):
        if isrun:
            self.ui.frp_service.setStyleSheet('''
            QLabel {
            background-color: rgb(80, 160, 80);
            border-radius: 0px;
            }
            ''')
        else:
            self.ui.frp_service.setStyleSheet('''
            QLabel {
            background-color: rgb(200, 0, 0);
            border-radius: 0px;
            }
            ''')

    def updata_token_service(self, isrun):
        if isrun:
            self.ui.token_service.setStyleSheet('''
            QLabel {
            background-color: rgb(80, 160, 80);
            border-radius: 0px;
            }
            ''')
        else:
            self.ui.token_service.setStyleSheet('''
            QLabel {
            background-color: rgb(200, 0, 0);
            border-radius: 0px;
            }
            ''')
    def updata_server_ping(self, message):
        # 反馈服务器连接状态结果
        self.ui.server_ping.setText(message[1])
        if message[0] == 2:
            self.ui.server_service.setStyleSheet('''
            QLabel {
            background-color: rgb(200, 200, 200);
            border-radius: 0px;
            }
            ''')
            self.ui.frp_service.setStyleSheet('''
            QLabel {
            background-color: rgb(200, 200, 200);
            border-radius: 0px;
            }
            ''')
            self.ui.token_service.setStyleSheet('''
            QLabel {
            background-color: rgb(200, 200, 200);
            border-radius: 0px;
            }
            ''')
        elif message[0] == 0:
            self.ui.server_service.setStyleSheet('''
            QLabel {
            background-color: rgb(200, 0, 0);
            border-radius: 0px;
            }
            ''')
        else:
            self.ui.server_service.setStyleSheet('''
            QLabel {
            background-color: rgb(80, 160, 80);
            border-radius: 0px;
            }
            ''')
        
    def CheckServerShutdown(self):
        self._CheckServer.stop()
            

   
    ##
    ## 判断模块
    ##
    def ipcheck(self, ip):
        # 判断IP地址是否合法
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
        # 判断端口是否合法 | 变量 -> 端口,最小端口,最大端口
        try:
            if high >= int(port) >= low :
                return True
            else:
                return False
        except:
            return False

    def checkfile(self):
        # 检查配置文件是否满足需求
        if not os.path.exists("./data/server.toml"):
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

    # 配置主题
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api="pyside6"))

    window = MainWindow()
    window.show()
    app.exec()