"""#1 自检及文件读取阶段"""
#初始化
import os
import time
import socket
import shutil
omkey = "version_230208;frpc_xFrp_v1.4_Dev;LyceenAiro"
names = locals()
#函数列表
def ipcheck(ip):
    #检验ip地址合法性
    try:
        if len(ip.split("."))==4:
            for i in ip.split(".") :
                try:
                    if not(0<=int(i)<=255):
                        flag = False
                except:
                    flag = False
        else:
            flag = False
    except:
        flag = False
    return flag

#开始
print("欢迎使用ParticlesFrp简易配置客户端[v1.4]")
#必要文件读取
try:
    server = open("./config/server.ini","r+",encoding="utf-8")
    server = server.readlines()
    more = open("./config/more.ini","r+",encoding="utf-8")
    more = more.readlines()
    with open("frpc.exe","r"):
        print(end="")
    with open("LICENSE","r"):
        print(end="")
except:
    input("发生错误,请检查文件完整性")
    exit()
#链接文件读取
linknum = 0
link = []
while True:
    linknum = linknum + 1
    linkfine = "link" + str(linknum)
    try:
        names[linkfine] = open(f"./config/{linkfine}.ini","r+",encoding="utf-8")
        names[linkfine] = names[linkfine].readlines()
        link.append(linkfine)
    except:
        linknum = linknum - 1
        del linkfine
        break




"""
#2 配置阶段
#配置映射链接表
"""
#配置主界面
while True:
    os.system("cls")
    print(
        "[0]连接服务器\n"+
        "[1]映射链接\n"+
        "[2]其他配置\n"+
        "[3]保存并启动\n"+
        "[q]保存并退出"
    )
    inp = input("配置:")
    if inp == "0":
        """
        #2-0 连接服务器
        #配置Frp服务器的链接和密匙
        """
        while True:
            os.system("cls")
            print(
                "[0]返回菜单\n"
                "[1]通讯地址\n"+
                "[2]通讯端口\n"+
                "[3]通讯密匙"
            )
            inp = input("配置:")
            #返回菜单
            if inp == "0":
                break
            #通讯地址
            elif inp == "1":
                ipset = input("配置:")
                flag = ipcheck(ipset)
                if flag == True:
                    ipset = "server_addr =" + ipset
                    server[2] = ipset
                else:
                    input("IP地址不合法")

            #通讯端口
            elif inp == "2":
            #通讯密匙
            elif inp == "3":
            else:
                input("没有所选的指令")
    elif inp == "1":
        """
        #2-1 连接服务器
        #配置Frp服务器的链接和密匙
        """
    elif inp == "2":
        """
        #2-2 连接服务器
        #配置Frp服务器的链接和密匙
        """
    elif inp == "3" or "q":
        """
        #2-3 连接服务器
        #配置Frp服务器的链接和密匙
        """
        if inp == "q":
            exit()
        break
    else:
        input("没有所选的指令")


    






"""
#3 启动程序
#保存设置之后启动frpc并且显示映射信息
"""
#启动服务
os.system("frpc.exe -c frpc.ini")
