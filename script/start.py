import subprocess
from PySide6.QtCore import QThread, Signal

import requests
from urllib3.exceptions import InsecureRequestWarning

import ping3
import psutil
import toml
import os
from time import sleep, time
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

    def __init__(self, log_translate):
        super().__init__()
        self._process = None
        self._thread = None
        self._running = False
        self.log_translate = log_translate

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
            if self.log_translate:
                frp_result = line.decode("utf-8").strip()\
                    .replace("start frpc service for config file [data/frpc.toml]", "正在读取frpc.toml配置文件...")\
                    .replace("try to connect to server...", "正在连接到服务器...")\
                    .replace("login to server success, get run id", "成功登录服务器, 获取连接ID")\
                    .replace("proxy added: ", "添加了链接: ")\
                    .replace("incoming a new work connection for udp proxy", "为udp代理传入新的工作连接")\
                    .replace("start proxy success", "链接开启成功")\
                    .replace("start error: proxy", "链接开启失败")\
                    .replace("] already exists", "] 链接名称已被占用")\
                    .replace("start error: port not allowed", "链接开启失败, 目的端口无权限连接")\
                    .replace("start error: port already used", "链接开启失败, 目的端口已经被占用")\
                    .replace("i/o timeout. With loginFailExit enabled, no additional retries will be attempted", "连接服务器超时, 请检查网络或服务器设置")\
                    .replace("connect to server error", "连接服务器失败")\
                    .replace("no such host", "服务器定向失败, 请检查网络后重试")\
                    .replace("token in login doesn't match token from configuration", "登录服务器失败, token密钥不正确")
            else: 
                frp_result = line.decode("utf-8").strip()
            self.log_message.emit(frp_result)
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
        self._running = False
        self.tags = tags()
    
    def start(self):
        if not self._running:
            self._running = True
            super().start()
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
            self.quit()  # 调用 quit 方法来请求线程退出
            self.wait()
            self.stopped.emit()

class CheckServer(QThread):
    ping_message = Signal(list)
    get_frp = Signal(bool)
    get_token = Signal(bool)
    finished = Signal()

    def __init__(self):
        super().__init__()
        self._process = None
        self._prorun = False
        self._running = False
        self.address = ""

    def run(self):
        self._running = True
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

        if not os.path.exists("frpc.exe"):
            self.finished.emit()
            return

        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        self._process = subprocess.Popen(['frpc', '-c', 'data/server.toml'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, startupinfo=startupinfo)
        self._prorun = True
        for line in self._process.stdout:
            line = line.decode('utf-8')
            if "login to the server failed: dial tcp" in line:
                self.get_frp.emit(False)
                self.get_token.emit(False)
                break
            elif "token in login doesn't match token from configuration" in line:
                self.get_frp.emit(True)
                self.get_token.emit(False)
                break
            elif "login to server success, get run id" in line:
                self.get_frp.emit(True)
                self.get_token.emit(True)
                break
        self.finished.emit()

    def stop(self):
        if self._running:
            self._running = False
            if self._prorun:
                self._process.terminate()
                self._prorun = False


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
        # 初始化模块
        previous_download_bytes = 0
        accumulation_download_bytes = 0
        download_speeds = deque(maxlen=5)
        try:
            with open(f"data/server.toml", "r", encoding="utf-8") as file:
                address = toml.loads(file.read())["serverAddr"]
        except:
            return
        while self._running:
            # 记录tick起始时间
            start_time = time()

            # 获取tick内流量信息
            try:
                frpc_proc = psutil.Process(self.frpc_pid)
            except psutil.NoSuchProcess:
                break
            frpc_net_io = frpc_proc.io_counters()
            current_upload_bytes = frpc_net_io.read_bytes + frpc_net_io.write_bytes
            current_download_bytes = frpc_net_io.other_bytes

            tick_download_bytes = current_download_bytes - previous_download_bytes

            # 获取tick内延迟信息
            server_ping = ping3.ping(address , unit="ms", timeout=0.5)
            
            # 计算流量总bytes值并整理
            accumulation_download_bytes += tick_download_bytes

            if current_upload_bytes >= 1073741824:
                accumulation_upload_str = f"{current_upload_bytes / 1024 / 1024 / 1024:.2f} GB"
            elif current_upload_bytes >= 1048576:
                accumulation_upload_str = f"{current_upload_bytes / 1024 / 1024:.2f} MB"
            elif current_upload_bytes >= 1024:
                accumulation_upload_str = f"{current_upload_bytes / 1024:.2f} KB"
            else:
                accumulation_upload_str = f"{current_upload_bytes} Byte"

            if accumulation_download_bytes >= 1073741824:
                accumulation_download_str = f"{accumulation_download_bytes / 1024 / 1024 / 1024:.2f} GB"
            elif accumulation_download_bytes >= 1048576:
                accumulation_download_str = f"{accumulation_download_bytes / 1024 / 1024:.2f} MB"
            elif accumulation_download_bytes >= 1024:
                accumulation_download_str = f"{accumulation_download_bytes / 1024:.2f} KB"
            else:
                accumulation_download_str = f"{accumulation_download_bytes} Byte"
            
            # 计算流量平均值
            download_mbps = tick_download_bytes * 8 / 1000000
            previous_download_bytes = current_download_bytes
            download_speeds.append(download_mbps)

            if len(download_speeds) == 5:
                average_download_mbps = sum(download_speeds) / 5
            else:
                average_download_mbps = sum(download_speeds) / len(download_speeds)
            
            # 反馈tick数据
            self.bandwidth_usage.emit([server_ping, round(average_download_mbps, 1), accumulation_upload_str, accumulation_download_str])
            
            # 根据运行时长来更新tick速度
            use_time = time() - start_time
            if use_time < 1:
                sleep(1 - use_time)
            else:
                continue
        self.stop()

    def stop(self):
        if self._running:
            self._running = False