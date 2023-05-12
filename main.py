from PySide6.QtWidgets import QMainWindow, QWidget, QStackedWidget, QPushButton, QVBoxLayout, QApplication
from ui.main_ui import Ui_MainWindow
from ui.titlebar import TitleBar
from signal.main_signal import my_signal
from PySide6.QtCore import Qt
import qdarkstyle

class MainWindow(QMainWindow):

    ##
    ## 主窗口设置
    ##
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.ui.setupUi(self)
        
        title_bar_widget = TitleBar(self)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(title_bar_widget)
        layout.addWidget(QWidget(self))
        self.setLayout(layout)

        self.band()

        self.mouse_press_position = None

    ##
    ## 对象绑定设置
    ##
    def band(self):
        # left
        self.ui.page_server.clicked.connect(self.setserver)
        self.ui.page_link.clicked.connect(self.setlink)
        self.ui.page_link.clicked.connect(self.setother)

        # server
        self.ui.server_save.clicked.connect(self.server_save)

        # window
        # self.ui.minimize_button.clicked.connect(self.showMinimized)
        # self.ui.close_button.clicked.clicked.connect(self.close)
    
    ## 
    ## 设置页面
    ##
    def setserver(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def setlink(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def setother(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    
    ##
    ## 模块
    ##
    def server_save(self):
        ip = self.ui.server_IP.text()
        port = self.ui.server_Port.text()
        token = self.ui.server_token.text()
        print(f"ip:{ip}\nport:{port}\ntoken:{token}")


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
    # app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api="pyside6"))
    window = MainWindow()
    window.show()
    app.exec()