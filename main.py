from PySide6.QtWidgets import QMainWindow, QWidget, QStackedWidget, QPushButton, QVBoxLayout, QApplication
from ui.main_ui import Ui_MainWindow
from signal.main_signal import my_signal
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):

    ##
    ## 主窗口设置
    ##
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.ui.setupUi(self)
        self.band()

    ##
    ## 对象绑定设置
    ##
    def band(self):
        # left
        self.ui.page_server.clicked.connect(self.setserver)
        self.ui.page_link.clicked.connect(self.setlink)

        # server
        self.ui.server_save.clicked.connect(self.server_save)

        # window
        self.ui.window_mini.clicked.connect(self.showMinimized)
        self.ui.window_close.clicked.connect(self.close)
    
    ## 
    ## 设置页面
    ##
    def setserver(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def setlink(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    
    ##
    ## 模块
    ##
    def server_save(self):
        ip = self.ui.server_IP.text()
        port = self.ui.server_Port.text()
        token = self.ui.server_token.text()
        print(f"ip:{ip}\nport:{port}\ntoken:{token}")

    # def mousePressEvent(self, event):
    #     if event.button() == Qt.


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()