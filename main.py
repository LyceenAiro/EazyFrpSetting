from PySide6.QtWidgets import QApplication, QMainWindow
from ui.main_ui import Ui_MainWindow
from signal.main_signal import my_signal

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.band()

    def band(self):
        self.ip = self.ui.server_IP.text()
        self.ui.server_save.clicked.connect(lambda :print(self.ip))

    # def set_server_ip(self, ip:str):
    #     self.ui.server_IP.setText(ip)

    # def server_save(self):
    #     self.ui.server_save.clicked.connect(lambda :print(self.ip))

if __name__ == "__main__":
    app = QApplication([]) # 启动一个应用
    window = MainWindow() # 实例化主窗口
    window.show() # 展示主窗口
    app.exec() # 应用自循环 