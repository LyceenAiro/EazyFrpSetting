import time
names = locals()

def start1():
    global server,more,linkexample
    try:
        print("(0/5)正在加载server.ini by LyceenAiro/EazyFrpSetting")
        with open("./config/server.ini","r+",encoding="utf-8") as u:
            server = u.readlines()
            testfile = server[0].strip("[").rstrip("]\n")
        print("(1/5)正在加载more.ini by LyceenAiro/EazyFrpSetting")
        with open("./config/more.ini","r+",encoding="utf-8") as u:
            more = u.readlines()
            testfile = int(more[3].split('=')[1].strip())
        print("(2/5)正在加载LinkExample.ini by LyceenAiro/EazyFrpSetting")
        with open("./config/LinkExample.ini","r+",encoding="utf-8") as u:
            linkexample = u.readlines()
            testfile = linkexample[14].strip()
    except:
        input("发生错误,请检查EazyFrpSetting文件完整性\n如果你更新了新版本的启动程序最好同步更新config文件内的文件\nEFS-github:https://github.com/LyceenAiro/EazyFrpSetting")
        exit()
    del testfile

def start2():
    try:
        print("(3/5)正在寻找frpc.exe by fatedier/frp")
        with open("frpc.exe","r+"):
            print(end="")
    except:
        input("frpc.exe正在运行或不存在,请检查frpc.exe是否被安全中心隔离\n如果frpc.exe存在请重新启动该软件\nfrp-github:https://github.com/fatedier/frp")
        exit()

# def start3():
#     #链接文件读取
#     print("(4/5)正在读取link文件")
#     global linknum
#     linknum = 0
#     while True:
#         linknum = linknum + 1
#         linkfine = "link" + str(linknum)
#         linkopen = "linko" + str(linknum)
#         global names[linkfine]
#         try:
#             names[linkopen] = open(f"./config/{linkfine}.ini","r+",encoding="utf-8")
#             names[linkfine] = names[linkopen].readlines()
#             names[linkopen].close()
#             #校准IP
#             if more[5].split('=')[1].strip() == "true":
#                 names[linkfine][5] = "local_ip = " + ip
#                 print("·更新了链接"+names[linkfine][1].strip("[").rstrip("]\n")+"的IP信息")
#         except:
#             linknum = linknum - 1
#             del linkfine
#             print("(5/5)加载完成")
#             time.sleep(0.5)
#             break
