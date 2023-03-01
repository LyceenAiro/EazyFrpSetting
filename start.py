"""#1 自检及文件读取阶段"""
#初始化
import os
import socket
omkey = "version_230301;frpc_xFrp_v1.4_alpha;LyceenAiro"
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

def portcheck(port):
    #检验端口合法性
    if 65535 >= int(port) >= 1024 :
        return True
    else:
        return False





#开始
print("欢迎使用ParticlesFrp简易配置客户端[v1.4]")
#必要文件读取
try:
    server = open("./config/server.ini","r+",encoding="utf-8")
    server = server.readlines()
    more = open("./config/more.ini","r+",encoding="utf-8")
    more = more.readlines()
    linkexample = open("./config/LinkExample.ini","r+",encoding="utf-8")
    linkexample = linkexample.readlines()
    with open("frpc.exe","r+"):
        print(end="")
    with open("LICENSE","r+"):
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
    linkopen = "linko" + str(linknum)
    try:
        names[linkopen] = open(f"./config/{linkfine}.ini","r+",encoding="utf-8")
        names[linkfine] = names[linkopen].readlines()
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
        "主菜单\n"
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
                "主菜单-连接服务器\n"+
                "[0]返回菜单\n"+
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
                os.system("cls")
                print("当前与服务器的ip地址是"+server[2].split('=')[1])
                ipset = input("配置:")
                flag = ipcheck(ipset)
                if flag == True:
                    server[2] = "server_addr =" + ipset + "\n"
                else:
                    input("IP地址不合法")
                del ipset,flag
            #通讯端口
            elif inp == "2":
                os.system("cls")
                print("当前设置的服务端口是"+server[4].split('=')[1])
                portset = input("配置:")
                flag = portcheck(portset)
                if flag == True:
                    server[4] = "server_port =" + portset + "\n"
                else:
                    input("端口必须在1024~65565的范围内")
                del portset,flag
            #通讯密匙
            elif inp == "3":
                os.system("cls")
                print("请输入密钥")
                portset = input("配置:")
                if portset == "":
                    portset = "#token =\n"
                else:
                    portset = "token =" + portset + "\n"
                server[6] = portset
                del portset
            else:
                input("没有所选的指令")
    elif inp == "1":
        """
        #2-1 映射链接
        #配置与Frp服务器的映射链接
        """
        while True:
            os.system("cls")
            print(
                "主菜单-映射链接\n"+
                "[0]返回菜单\n"+
                "[c][创建新的链接]")
            for i in range(linknum):
                setin = "link" + str(i+1)
                print(f"[{i+1}]"+ 
                    names[setin][1].strip(),
                    names[setin][3].split("=")[1].strip(),
                    names[setin][7].split("=")[1].strip()+" -> "+
                    names[setin][9].split("=")[1].strip())
            inp = input("配置:")
            #返回菜单
            if inp == "0":
                break
            #创建新的链接
            elif inp == "c":
                os.system("cls")
                print("主菜单-映射链接-创建链接")
                creatlink = linkexample
                #链接名配置
                inp = input("链接名称:")
                if inp == "":
                    str(linknum)
                    i = "link" + str(linknum+1)
                    creatlink[1] = "[" + i + "]\n"
                else:
                    creatlink[1] = "[" + inp + "]\n"
                #协议设置
                inp = input("[1]tcp\n[2]udp\n[3]xtcp-host\n[4]xtcp-client\n配置:")
                if inp == "1":
                    creatlink[3] = "type = tcp\n"
                elif inp == "2":
                    creatlink[3] = "type = udp\n"
                elif inp == "3":
                    creatlink[3] = "type = xtcp\n"
                    i = "host"
                elif inp == "4":
                    creatlink[3] = "type = xtcp\n"
                else:
                    continue
                #配置本机网卡
                ip = socket.gethostbyname(socket.gethostname())
                inp = input("配置网卡IP(留空自动获取):")
                if inp == "":
                    creatlink[5] = "local_ip = " + ip + "\n"
                    del ip
                else:
                    del ip
                    flag = ipcheck(inp)
                    if flag == True:
                        creatlink[5] = "local_ip = " + inp + "\n"
                        del flag
                    else:
                        input("IP地址不合法,请重新创建")
                        del flag
                        continue
                #配置本地转发端口
                inp = input("配置本地转发端口:")
                flag = portcheck(inp)
                if flag == True:
                    creatlink[7] = "local_port = " + inp + "\n"
                    del flag
                else:
                    del flag
                    continue
                #配置映射出端口
                inp = input("配置映射端口:")
                flag = portcheck(inp)
                if flag == True:
                    creatlink[9] = "remote_port = " + inp + "\n"
                    del flag
                else:
                    del flag
                    continue
                #拓展配置
                creatlink[14] = "#Frp\n"
                if creatlink[3].split("=")[1] == "xtcp":
                    #配置点对点端密匙
                    inp = input("配置点对点端密匙:")
                    creatlink[11] = "sk = " + inp + "\n"
                    creatlink[13] = "#server_name = \n"
                    creatlink[14] = "#server\n"
                    if i != "host":
                        #配置点对点服务名称
                        inp = input("配置点对点端服务名称:")
                        creatlink[13] = "server_name = " + inp + "\n"
                        creatlink[14] = "#client\n"
                #保存并创建链接
                linknum = linknum + 1
                linkfine = "link" + str(linknum)
                names[linkfine] = creatlink
                del linkfine
                    
            #其他链接配置
            else :
            #try:
                setin = "link" + inp
                names[setin]
                os.system("cls")
                print(f"主菜单-映射链接-{setin}\n"+
                    names[setin][14]+
                    "\n[0]返回"+
                    "\n[1]链接名称",names[setin][1].strip()+
                    "\n[2]协议类型",names[setin][3].split("=")[1].strip()+
                    "\n[3]本机网卡",names[setin][5].split("=")[1].strip()+
                    "\n[4]转发端口",names[setin][7].split("=")[1].strip()+
                    "\n[5]映射端口",names[setin][9].split("=")[1].strip()
                )
                if names[setin][14] == "#client\n":
                    print(
                        "[6]对点密匙",names[setin][11].split("=")[1].strip()+
                        "\n[7]对点服务",names[setin][13].split("=")[1].strip()
                    )
                elif names[setin][14] == "#server\n":
                    print(
                        "[8]对点密匙",names[setin][11].split("=")[1].strip()
                    )
                inp = input("\n配置:")

            #except:
                #input("没有指定的链接")


    elif inp == "2":
        """
        #2-2 其他配置
        #其他软件配置
        """
        while True:
            os.system("cls")
            inp = input("主菜单-其他配置\n[0]返回菜单\n[1]自动回应\n\n配置:")
            #返回菜单
            if inp == "0":
                break
            #配置自动回应
            if inp == "1":
                inp = input("修改自动回应的时间,现在的设置是"+more[1].split('=')[1])
                try:
                    settime = int(inp)
                except:
                    input("你输入的格式错误")
                    continue
                if settime >= 0 :
                    more[1] = "heartbeat_timeout = " + inp + "\n"
                del settime
            if inp == "":
                continue
            else:
                input("没有所选的指令")
    elif inp == "3" or "q":
        """
        #2-3 连接服务器
        #保存配置文件并启动服务
        """
        os.system("cls")
        #保存server.ini
        with open("./config/server.ini","w+",encoding="utf-8") as u:
            for i in server:
                u.write(i)
        #保存more.ini
        with open("./config/more.ini","w+",encoding="utf-8") as u:
            for i in more:
                u.write(i)
        #序列保存Link列表
        pinf = linknum
        while linknum != 0:
            setin = "linko" + str(linknum)
            #保存现存链接
            try:
                for i in names[setin]:
                    names[setin].write(i)
            #保存新建的链接
            except:
                setin = "link" + str(linknum)
                filein = "link" + str(linknum) + ".ini"
                with open(f"./config/{filein}","w+",encoding="utf-8") as u:
                    for i in names[setin]:
                        u.write(i)
            linknum = linknum - 1
        del linknum
        if inp == "q":
            exit()
        break
    elif inp == "":
        #空白内容检测
        continue
    else:
        #无命令
        input("没有所选的指令")





"""
#3 启动程序
#保存设置之后启动frpc并且显示映射信息
"""
#启动服务
os.system("cls")
frpc = server
for i in range(pinf):
    setin = "link" + str(i+1)
    frpc = frpc + names[setin]
frpc = frpc + more
del pinf
with open("frpc.ini","w+",encoding="utf-8") as u:
    for i in frpc:
        u.write(i)
del frpc,server,more
os.system("frpc.exe -c frpc.ini")