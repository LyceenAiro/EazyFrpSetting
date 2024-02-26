import subprocess
from PySide6.QtCore import QThread, Signal

import requests
from urllib3.exceptions import InsecureRequestWarning

import ping3
import psutil
from time import sleep
from collections import deque

import sys
sys.path.append(".")
from makefile.tags import tags


class FrpClient(QThread):
    # 这是一个专门用于启动Frp的subprocess
    started = Signal()
    finished = Signal()
    log_message = Signal(str)
    bandwidth_pid = Signal(int)

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
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        self._process = subprocess.Popen(['frpc', '-c', 'data/frpc.toml'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, startupinfo=startupinfo)
        self.bandwidth_pid.emit(self._process.pid)
        for line in self._process.stdout:
            self.log_message.emit(line.decode('utf-8').strip())
            self.log_message.emit("\n")
        self.finished.emit()

    def stop(self):
        if self._running:
            self._running = False
            self._process.terminate()
            self._thread.quit()
            self._thread.wait()

class CheckUpdata(QThread):
    # 这是一个专门检查更新的线程
    stopped = Signal()
    started = Signal()
    log_message = Signal(str,bool)

    def __init__(self):
        super().__init__()
        self._thread = None
        self._running = False
        self.tags = tags()
    
    def start(self):
        if not self._running:
            self._running = True
            self._thread = QThread()
            self.moveToThread(self._thread)
            self._thread.started.connect(self.run)
            self._thread.start()
            self.started.emit()

    def run(self):
        # 尝试获取最新版本且附带数据
        # 尝试获取最新版本
        if not tags().versionaddit in ("Release", "alpha", "beta"):
            self.log_message.emit("特殊版本无法检查更新",False)
            return
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        try:
            # 发送 GET 请求获取最新版本号
            response = requests.get("https://api.github.com/repos/LyceenAiro/EazyFrpSetting/releases/latest", verify=False)
            response.raise_for_status()
            # 解析响应 JSON 数据
            data = response.json()
            # 获取最新版本号
            latest_version = data["tag_name"]
            # 如果有新版本可用，则提示用户更新
            if latest_version > self.tags.version:
                self.log_message.emit(f"最新版本 {latest_version}",True)
            else:
                self.log_message.emit("当前已经是最新版本",False)
        except:
            self.log_message.emit("获取更新失败",False) 
    
    def stop(self):
        if self._running:
            self._running = False
            self._thread.quit()
            self._thread.wait()
            self.stopped.emit()

class CheckServer(QThread):
    # 这是一个专门检查服务器连通性的线程
    ping_message = Signal(list)

    def __init__(self):
        super().__init__()
        self._running = False
        self.tags = tags()
    
    def start(self, address):
        if not self._running:
            self._running = True
            super().start()
            self.address = address

    def run(self):
        try:
            result = ping3.ping(self.address , unit="ms", timeout=10)
        except:
            self._running = False
            return
        if not result:
            online = 0
            result = "Fail"
        else:
            online = 1
            result = f"{str(int(result))} ms"
        return_list = [online, result]
        self.ping_message.emit(return_list)

    def stop(self):
        if self._running:
            self._running = False

class Checkbandwidth(QThread):
    # 专门用于检测流量信息的线程
    bandwidth_usage = Signal(list)

    def __init__(self):
        super().__init__()
        self.frpc_pid = None
        self._running = False
        
    def start(self, pid):
        if not self._running:
            self._running = True
            self.frpc_pid = pid
            super().start()

    def run(self):
        previous_upload_bytes = 0
        previous_download_bytes = 0
        upload_speeds = deque(maxlen=5)
        download_speeds = deque(maxlen=5)
        while self._running:
            try:
                frpc_proc = psutil.Process(self.frpc_pid)
            except psutil.NoSuchProcess:
                break
            frpc_net_io = frpc_proc.io_counters()
            current_upload_bytes = frpc_net_io.read_bytes
            current_download_bytes = frpc_net_io.write_bytes

            upload_mbps = (current_upload_bytes - previous_upload_bytes) / 1024 / 1024
            download_mbps = (current_download_bytes - previous_download_bytes) / 1024 / 1024

            previous_upload_bytes = current_upload_bytes
            previous_download_bytes = current_download_bytes

            upload_speeds.append(upload_mbps)
            download_speeds.append(download_mbps)

            if len(upload_speeds) == 5:
                average_upload_mbps = sum(upload_speeds) / 5
                average_download_mbps = sum(download_speeds) / 5
            else:
                average_upload_mbps = sum(upload_speeds) / len(upload_speeds)
                average_download_mbps = sum(download_speeds) / len(upload_speeds)
            self.bandwidth_usage.emit([round(average_upload_mbps, 1), round(average_download_mbps, 1)])
            sleep(1)
        self.stop()

    def stop(self):
        if self._running:
            self._running = False