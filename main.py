import os
import qdarkstyle
import subprocess
import threading
import configparser

from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidget, QFrame, QVBoxLayout, QApplication, QTableWidgetItem, QDialog, QLabel, QLineEdit, QSizePolicy
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

        # UI初始化
        self.UIinit()

        # 数据读取
        self.datainit()

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

        # link
        self.ui.link_create.clicked.connect(self.on_add_button_clicked)
        self.ui.link_delete.clicked.connect(self.on_delete_button_clicked)
        self.ui.link_modify.clicked.connect(self.on_edit_button_clicked)
        self.ui.linktable.itemSelectionChanged.connect(self.on_table_item_selection_changed)

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
        self.ui.stackedWidget.setCurrentIndex(0)
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
        
        if not os.path.exists("./data/linktable.ini"):
            os.makedirs("./data/linktable.ini")
        self.load_table_data("./data/linktable.ini")

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
        self.ui.linktable.setColumnCount(7)
        self.ui.linktable.horizontalHeader().setDefaultSectionSize(100)
        self.ui.linktable.setColumnWidth(1, 60)
        self.ui.linktable.setHorizontalHeaderLabels(["服务名", "协议", "源地址", "源端口", "目的端口", "密钥", "目的服务"])
        self.ui.linktable.horizontalHeader().setStretchLastSection(True)
        self.ui.linktable.verticalHeader().setVisible(False)
        self.ui.linktable.setSelectionBehavior(QTableWidget.SelectRows)
        self.ui.linktable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.ui.link_delete.setEnabled(False)
        self.ui.link_modify.setEnabled(False)
        
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
        if self.checkfile() == False:
            self.ui.main_log.insertPlainText("necessary settings are still missing.\n")
            return
        self.frpcData_save()
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
        
    def link_ini_save(self):
        link = configparser.ConfigParser()
        linksetup = ["","type","local_ip","local_port","remote_port","sk","server_name"]
        with open("./data/linktable.ini","r+",encoding="utf-8") as u:
            for a in u.readlines():
                b = a.split(",")
                tags = 1
                link.add_section(b[0])
                while not tags >= 7:
                    if b[tags] == "":
                        link[b[0]]["#"+linksetup[tags]] = b[tags]
                    else:
                        link[b[0]][linksetup[tags]] = b[tags]
                    tags += 1
        with open('./data/link.ini', 'w') as configfile:
            link.write(configfile)

    def frpcData_save(self):
        self.link_ini_save()

        with open("./data/server.ini","r+",encoding="utf-8") as u:
            frpc = u.readlines()
        
        with open('./data/link.ini', 'r+', encoding='utf-8') as u:
            frpc += u.readlines()

        with open("./data/frpc.ini","w+",encoding="utf-8") as u:
            for i in frpc:
                u.write(i)
    
    def save_table_data(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            # 写入数据
            for i in range(self.ui.linktable.rowCount()):
                row_data = []
                for j in range(self.ui.linktable.columnCount()):
                    item = self.ui.linktable.item(i, j)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append('')
                    row_data.append(',')
                row_data.append('End')
                f.write(''.join(row_data) + '\n')
    
    def load_table_data(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:            
            # 读取数据
            row = 0
            for line in f:
                data = line.strip().split(',')
                self.ui.linktable.insertRow(row)
                for col, text in enumerate(data):
                    if text == "End":
                        break
                    elif text == "":
                        item = QtWidgets.QTableWidgetItem('')
                    else:
                        item = QtWidgets.QTableWidgetItem(text)
                    self.ui.linktable.setItem(row, col, item)
                row += 1

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
    
    def add_table_row(self, data):
        row_count = self.ui.linktable.rowCount()
        self.ui.linktable.insertRow(row_count)
        for i, item in enumerate(data):
            table_item = QTableWidgetItem(item)
            self.ui.linktable.setItem(row_count, i, table_item)
    
    def on_table_item_selection_changed(self):
        selected_rows = self.ui.linktable.selectionModel().selectedRows()
        if len(selected_rows) > 0:
            self.ui.link_modify.setEnabled(True)
            self.ui.link_delete.setEnabled(True)
        else:
            self.ui.link_modify.setEnabled(False)
            self.ui.link_delete.setEnabled(False)

    def on_edit_button_clicked(self):
        selected_row = self.ui.linktable.selectionModel().selectedRows()[0].row()
        data = [self.ui.linktable.item(selected_row, i).text() for i in range(7)]

        # 创建编辑对话框
        dialog = QDialog(self)
        dialog.setWindowTitle("编辑链接")

        frame = QFrame(dialog)
        frame.setFrameShape(QFrame.Box)
        frame.setStyleSheet("border-radius: 0px")
        frame.setLineWidth(2)
        frame.setFixedSize(200, 270)

        layout = QVBoxLayout()

        label = QLabel("编辑链接")
        layout.addWidget(label)
        
        edit1 = QLineEdit(data[0])
        edit1.setPlaceholderText("服务名称")
        layout.addWidget(edit1)

        edit2 = QLineEdit(data[1])
        edit2.setPlaceholderText("协议")
        layout.addWidget(edit2)

        edit3 = QLineEdit(data[2])
        edit3.setPlaceholderText("源地址")
        layout.addWidget(edit3)

        edit4 = QLineEdit(data[3])
        edit4.setPlaceholderText("源端口")
        layout.addWidget(edit4)

        edit5 = QLineEdit(data[4])
        edit5.setPlaceholderText("目的端口")
        layout.addWidget(edit5)

        edit6 = QLineEdit(data[5])
        edit6.setPlaceholderText("密钥")
        layout.addWidget(edit6)

        edit7 = QLineEdit(data[6])
        edit7.setPlaceholderText("目的服务")
        layout.addWidget(edit7)

        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        layout.addWidget(button_box)

        dialog.setLayout(layout)

        if dialog.exec() == QDialog.Accepted:
            # 更新数据
            self.ui.linktable.setItem(selected_row, 0, QTableWidgetItem(edit1.text()))
            self.ui.linktable.setItem(selected_row, 1, QTableWidgetItem(edit2.text()))
            self.ui.linktable.setItem(selected_row, 2, QTableWidgetItem(edit3.text()))
            self.ui.linktable.setItem(selected_row, 3, QTableWidgetItem(edit4.text()))
            self.ui.linktable.setItem(selected_row, 4, QTableWidgetItem(edit5.text()))
            self.ui.linktable.setItem(selected_row, 5, QTableWidgetItem(edit6.text()))
            self.ui.linktable.setItem(selected_row, 6, QTableWidgetItem(edit7.text()))
            self.save_table_data("./data/linktable.ini")
 
    def on_add_button_clicked(self):
        # 创建添加对话框
        dialog = QDialog(self)
        dialog.setWindowTitle("创建链接")
        dialog.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        frame = QFrame(dialog)
        frame.setFrameShape(QFrame.Box)
        frame.setStyleSheet("border-radius: 0px")
        frame.setLineWidth(2)
        frame.setFixedSize(200, 270)

        layout = QVBoxLayout()

        label = QLabel("创建链接")
        layout.addWidget(label)

        edit1 = QLineEdit()
        edit1.setPlaceholderText("服务名称")
        layout.addWidget(edit1)

        edit2 = QLineEdit()
        edit2.setPlaceholderText("协议")
        layout.addWidget(edit2)

        edit3 = QLineEdit()
        edit3.setPlaceholderText("源地址")
        layout.addWidget(edit3)

        edit4 = QLineEdit()
        edit4.setPlaceholderText("源端口")
        layout.addWidget(edit4)

        edit5 = QLineEdit()
        edit5.setPlaceholderText("目的端口")
        layout.addWidget(edit5)

        edit6 = QLineEdit()
        edit6.setPlaceholderText("密钥")
        layout.addWidget(edit6)

        edit7 = QLineEdit()
        edit7.setPlaceholderText("目的服务")
        layout.addWidget(edit7)

        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        layout.addWidget(button_box)

        dialog.setLayout(layout)

        if dialog.exec() == QDialog.Accepted:
            # 添加数据
            self.add_table_row([edit1.text(), edit2.text(), edit3.text(), edit4.text(), edit5.text(), edit6.text(), edit7.text()])
            self.save_table_data("./data/linktable.ini")

    def on_delete_button_clicked(self):
        selected_rows = self.ui.linktable.selectionModel().selectedRows()
        # 删除选中行
        for row in selected_rows:
            self.ui.linktable.removeRow(row.row())
        
        self.save_table_data("./data/linktable.ini")
   
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

    def checkfile(self):
        if not os.path.exists("./data/server.ini"):
            return False
        # No should check LinkTable
        # Check othersetting

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