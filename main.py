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
        pass