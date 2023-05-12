import subprocess
import threading
from PySide6.QtCore import QObject, QThread, Signal
from PySide6.QtWidgets import QMainWindow, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget

class FrpClient(QThread):
    stopped = Signal()
    started = Signal()
    finished = Signal()
    tell_finished = Signal()
    log_message = Signal(str)

    def __init__(self):
        super().__init__()
        self._process = None
        self._thread = None
        self._running = False

    def start(self):
        if not self._running:
            self._running = True
            self._thread = QThread()
            self.moveToThread(self._thread)
            self._thread.started.connect(self.run)
            self._thread.start()
            self.started.emit()

    def run(self):
        self._process = subprocess.Popen(['frpc', '-c', 'data/frpc.ini'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in self._process.stdout:
            self.log_message.emit(line.decode('utf-8').strip())
            self.log_message.emit("\n")
        self.finished.emit()
        self.tell_finished.emit()

    def stop(self):
        if self._running:
            self._running = False
            self._process.terminate()
            self._thread.quit()
            self._thread.wait()
            self.finished.emit()