import subprocess
from PySide6.QtCore import QThread, Signal

import requests
from urllib3.exceptions import InsecureRequestWarning

import ping3
import psutil
from time import sleep

import sys
sys.path.append(".")
from makefile.tags import tags


class FrpClient(QThread):
    # 这是一个专门用于启动Frp的subprocess
    started = Signal()
    finished = Signal()
    tell_finished = Signal()
    bandwidth_usage = Signal(list)
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
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        self._process = subprocess.Popen(['frpc', '-c', 'data/frpc.toml'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, startupinfo=startupinfo)
        frpc_pid = self._process.pid
        while self._running:
            for line in self._process.stdout:
                self.log_message.emit(line.decode('utf-8').strip())
                self.log_message.emit("\n")
            # 获取frpc进程的网络流量信息
            for proc in psutil.process_iter(['pid', 'name']):
                if proc.info['pid'] == frpc_pid and proc.info['name'] == 'frpc.exe':
                    frpc_proc = psutil.Process(frpc_pid)
                    frpc_net_io = frpc_proc.io_counters()
                    upload_speed = frpc_net_io.bytes_sent
                    download_speed = frpc_net_io.bytes_recv
                    total_bandwidth = [upload_speed, download_speed]
                    self.bandwidth_usage.emit(total_bandwidth)
                    print("get true")
                    break
            sleep(0.5)

    def stop(self):
        if self._running:
            self._running = False
            self._process.terminate()
            self._thread.quit()
            self._thread.wait()
            self.finished.emit()

class CheckUpdata(QThread):
    # 这是一个专门检查更新的线程
    stopped = Signal()
    started = Signal()
    log_message = Signal(str,bool)

    def __init__(self):
        super().__init__()
        self._process = None
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