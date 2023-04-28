#全局函数
import os
import random
import sys


def restart():
    #重启
    sp = sys.executable
    os.execl(sp, sp, * sys.argv)

#函数列表
def ipcheck(ip):
    #检验ip地址合法性
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
    

def portcheck(port):
    #检验端口合法性
    try:
        if 65535 >= int(port) >= 1024 :
            return True
        else:
            return False
    except:
        return False

def randomstr(str_size,allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))