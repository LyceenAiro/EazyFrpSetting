"""#1 自检阶段"""
#初始化
import os
import time
import socket
import shutil
omkey = "version_230120;frpc_xFrp_v1.3;LyceenAiro"
#开始
print("欢迎使用ParticlesFrp简易配置客户端[v1.3]")
#文件检查
try:
    with open("frpc.exe","r"):
        print("加载frpc.exe")
    with open("./config/frpc_User","r"):
        print("加载frpc_User")
    with open("./config/frpc_P2PUser","r"):
        print("加载frpc_P2PUser")
    with open("./config/frpc_P2PHost","r"):
        print("加载frpc_Host")
except:
    input("发生错误,请检查文件完整性")
    exit()
#配置选择
os.system("cls")
print("\n选择端类型\n[1]转发服务\n[2]P2P主机端\n[3]P2P访问端\n")
inp = input("配置:")
#配置信息设置
if inp == "1":
    mode = "Frp"
    shutil.copyfile("./config/frpc_User","./frpc.ini")
elif inp == "2":
    mode = "xTCP"
    shutil.copyfile("./config/frpc_P2PHost","./frpc.ini")
elif inp == "3":
    mode = "xTCP"
    shutil.copyfile("./config/frpc_P2PUser","./frpc.ini")
else:
    exit()
#文件加载
file = open("frpc.ini","r+",encoding="utf-8")
file_list = file.readlines()
oip = ""
oid = ""
osv = ""

"""
#2 P2P连接xTCP隧道专用模块
#xTCP专用的设置模块
"""
#配置设置
if mode == "xTCP":
    oid = str(file_list[8])
    osv = str(file_list[9])
    oid = oid.strip()
    osv = osv.strip()
    while True:
        os.system("cls")
        print(time.strftime("%Y-%m-%d %H:%M",time.localtime(time.time())),"P2P",oid)
        #源文件序列读取
        print(
            "[0]服务名称",osv+
            "\n[1]通讯地址\n"+
            "[2]通讯端口\n"+
            "[3]通讯密匙\n"+
            "\n[x]协议类型"+file_list[11].split("=")[1]+
            "[4]本机地址"+file_list[13].split("=")[1]+
            "[5]转发端口"+file_list[15].split("=")[1]+
            "[6]映射端口"+file_list[18].split("=")[1]+
            "[7]连接密匙"+file_list[20].split("=")[1]+
            "[8]连接服务"+file_list[22].split("=")[1]+
            "\n[9]保存并启动\n"
            "[q]保存并退出\n"
        )
        inp = input("配置:")
        #退出设置
        if inp == "9" or inp == "q":
            file = open("frpc.ini","w+",encoding="utf-8")
            for i in file_list:
                file.write(i)
            file.close()
            if oid == "#主机端":
                shutil.copyfile("./frpc.ini","./config/frpc_P2PHost")
            else:
                shutil.copyfile("./frpc.ini","./config/frpc_P2PUser")
            if inp == "q":
                exit()
            oip = str(file_list[2].split("=")[1])
            oip = oip.strip()
            ocount = str(file_list[18].split("=")[1])
            ocount = ocount.strip()
            del file_list,inp
            break
        #设置服务名称
        elif inp == "0":
            os.system("cls")
            print("设置启动的服务名称,访问端需要配合主机端的服务名使用")
            count = input("设置:")
            str1 = "[" + count + "]\n"
            file_list[7] = str1
            del count,str1
        #设置通讯地址
        elif inp == "1":
            os.system("cls")
            print("输入与服务器的通讯地址,你现在的地址是"+file_list[2].split("=")[1])
            ip = input("请输入IP地址:")
            #输入纠错
            flag = True
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
            if flag == True:
                str1 = "server_addr = " + ip + "\n"
                file_list[2] = str1
                del flag
            else:
                input("你输入的地址有误")
                str1 = 0
            del ip,str1
        #设置通讯端口
        elif inp == "2":
            os.system("cls")
            print("设置与服务器的通讯端口,你现在的端口是"+file_list[4].split("=")[1])
            count = input("输入端口:")
            #输入纠错
            try:
                if 65535 >= int(count) >= 1024 :
                    str1 = "server_port = " + count + "\n"
                    file_list[4] = str1
                    del count,str1
                else:
                    input("端口范围必须在1024~65535内")
                    del count
            except:
                input("你输入的端口内容错误")
                del count
        #设置通讯密匙
        elif inp == "3":
            os.system("cls")
            tk = file_list[6].split("=")[1]
            tk = tk.split()
            if tk == "无":
                print("设置与服务器的通讯密匙")
                tk = input("密匙:")
            else:
                print("设置与服务器的通讯密匙,你现在的密匙是"+file_list[6].split("=")[1])
                tk = input("密匙:")
            tk = tk.split()
            if tk == "":
                str1 = "#token = 无\n"
                file_list[6] = str1
            else:
                str1 = "token = " + tk + "\n"
                file_list[6] = str1
            del tk,str1
        #设置本机地址
        elif inp == "4":
            os.system("cls")
            print("选定设置IP地址的方式\n[1]自动获取\n[2]手动设置\n")
            exp = input("配置:")
            ip = str1 = "0"
            if exp == "1":
                ip = socket.gethostbyname(socket.gethostname())
                str1 = "local_ip = " + ip + "\n"
                file_list[13] = str1
            elif exp == "2":
                print("输入的IP地址需要与你上网的网卡地址一致")
                ip = input("请输入IP地址:")
                #输入纠错
                flag = True
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
                if flag == True:
                    str1 = "local_ip = " + ip + "\n"
                    file_list[13] = str1
                    del flag
                else:
                    input("你输入的地址有误")
                    str1 = 0
            del exp,ip,str1
        #设置转发端口
        elif inp == "5":
            os.system("cls")
            print("设置由本地转发出的端口\n")
            count = input("输入端口:")
            #输入纠错
            try:
                if 65535 >= int(count) >= 1024 :
                    str1 = "local_port = " + count + "\n"
                    file_list[15] = str1
                    del count,str1
                else:
                    input("端口范围必须在1024~65535内")
                    del count
            except:
                input("你输入的端口内容错误")
                del count
        #端口注释编辑
        elif inp == "#6":
            os.system("cls")
            print(file_list[17])
            newp = input("(新的注释)[输入!save取消]\n#")
            if newp != "!save":
                newp = "#" + newp
                file_list[17] = newp
            del newp
        #设置映射端口
        elif inp == "6":
            os.system("cls")
            print(end=file_list[17])
            print("设置在服务器映射出的端口,需要设置与协议对应的端口\n")
            count = input("输入端口:")
            #输入纠错
            try:
                if 65535 >= int(count) >= 1024 :
                    str1 = "remote_port = " + count + "\n"
                    file_list[18] = str1
                    del count,str1
                else:
                    input("端口范围必须在1024~65535内")
                    del count
            except:
                input("你输入的端口内容错误")
                del count
        #设置连接密匙
        elif inp == "7":
            os.system("cls")
            print("设置与主机端相同的连接密匙才能建立连接")
            count = input("设置:")
            str1 = "sk = " + count + "\n"
            file_list[20] = str1
            del count,str1
        #设置主机服务名称
        elif inp == "8":
            os.system("cls")
            if oid == "#主机端":
                input("主机端设置连接的服务名称是无效的")
            else:
                print("设置与主机端相同的服务名称")
                count = input("设置:")
                str1 = "server_name = " + count + "\n"
                file_list[22] = str1
                del count,str1
        #设置纠错
        else:
            input("无选定指令")





"""
#2-2 Frp中续服务专用模块
#Frp转发专用的设置模块
"""
if mode == "Frp":
    while True:
        os.system("cls")
        print(time.strftime("%Y-%m-%d %H:%M",time.localtime(time.time())),"#转发服务")
        #源文件序列读取
        print(
            "[1]通讯地址\n"+
            "[2]通讯端口\n"+
            "[3]通讯密匙\n"
            "\n[4]协议类型"+file_list[10].split("=")[1]+
            "[5]本机地址"+file_list[12].split("=")[1]+
            "[6]转发端口"+file_list[14].split("=")[1]+
            "[7]映射端口"+file_list[17].split("=")[1]+
            "\n[8]保存并启动\n"
            "[q]保存并退出\n"
        )
        inp = input("配置:")
        #退出设置
        if inp == "8" or inp == "q":
            file = open("frpc.ini","w+",encoding="utf-8")
            for i in file_list:
                file.write(i)
            file.close()
            shutil.copyfile("./frpc.ini","./config/frpc_User")
            if inp == "q":
                exit()
            oip = str(file_list[2].split("=")[1])
            oip = oip.strip()
            ocount = str(file_list[17].split("=")[1])
            ocount = ocount.strip()
            del file_list,inp
            break
        #设置通讯地址
        elif inp == "1":
            os.system("cls")
            print("输入与服务器的通讯地址,你现在的地址是"+file_list[2].split("=")[1])
            ip = input("请输入IP地址:")
            #输入纠错
            flag = True
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
            if flag == True:
                str1 = "server_addr = " + ip + "\n"
                file_list[2] = str1
                del flag
            else:
                input("你输入的地址有误")
                str1 = 0
            del ip,str1
        #设置通讯端口
        elif inp == "2":
            os.system("cls")
            print("设置与服务器的通讯端口,你现在的端口是"+file_list[4].split("=")[1])
            count = input("输入端口:")
            #输入纠错
            try:
                if 65535 >= int(count) >= 1024 :
                    str1 = "server_port = " + count + "\n"
                    file_list[4] = str1
                    del count,str1
                else:
                    input("端口范围必须在1024~65535内")
                    del count
            except:
                input("你输入的端口内容错误")
                del count
        #设置通讯密匙
        elif inp == "3":
            os.system("cls")
            tk = file_list[6].split("=")[1]
            tk = tk.split()
            if tk == "无":
                print("设置与服务器的通讯密匙")
                tk = input("密匙:")
            else:
                print("设置与服务器的通讯密匙,你现在的密匙是"+file_list[6].split("=")[1])
                tk = input("密匙:")
            tk = tk.split()
            if tk == "":
                str1 = "#token = 无\n"
                file_list[6] = str1
            else:
                str1 = "token = " + tk + "\n"
                file_list[6] = str1
            del tk,str1
        #设置协议类型
        elif inp == "4":
            os.system("cls")
            print("选定协议类型,需要与映射端口相同\n[1]tcp\n[2]udp\n")
            exp = input("配置:")
            if exp == "1":
                file_list[10] = "type = tcp\n"
            elif exp == "2":
                file_list[10] = "type = udp\n"
            del exp
        #设置本机地址
        elif inp == "5":
            os.system("cls")
            print("选定设置IP地址的方式\n[1]自动获取\n[2]手动设置\n")
            exp = input("配置:")
            ip = str1 = "0"
            if exp == "1":
                ip = socket.gethostbyname(socket.gethostname())
                str1 = "local_ip = " + ip + "\n"
                file_list[12] = str1
            elif exp == "2":
                print("输入的IP地址需要与你上网的网卡地址一致")
                ip = input("请输入IP地址:")
                #输入纠错
                flag = True
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
                if flag == True:
                    str1 = "local_ip = " + ip + "\n"
                    file_list[12] = str1
                    del flag
                else:
                    input("你输入的地址有误")
                    str1 = 0
            del exp,ip,str1
        #设置转发端口
        elif inp == "6":
            os.system("cls")
            print("设置由本地转发出的端口\n")
            count = input("输入端口:")
            #输入纠错
            try:
                if 65535 >= int(count) >= 1024 :
                    str1 = "local_port = " + count + "\n"
                    file_list[14] = str1
                    del count,str1
                else:
                    input("端口范围必须在1024~65535内")
                    del count
            except:
                input("你输入的端口内容错误")
                del count
        #端口注释编辑
        elif inp == "#7":
            os.system("cls")
            print(file_list[16])
            newp = input("(新的注释)[输入!save取消]\n#")
            if newp != "!save":
                newp = "#" + newp
                file_list[16] = newp
            del newp
        #设置映射端口
        elif inp == "7":
            os.system("cls")
            print(end=file_list[16])
            print("设置在服务器映射出的端口,需要设置与协议对应的端口\n")
            count = input("输入端口:")
            #输入纠错
            try:
                if 65535 >= int(count) >= 1024 :
                    str1 = "remote_port = " + count + "\n"
                    file_list[17] = str1
                    del count,str1
                else:
                    input("端口范围必须在1024~65535内")
                    del count
            except:
                input("你输入的端口内容错误")
                del count
        #设置纠错
        else:
            input("无选定指令")





"""
#3 启动程序
#保存设置之后启动frpc并且显示映射信息
"""
#启动服务
os.system("cls")
if mode == "xTCP":
    print(time.strftime("%Y/%m/%d %H:%M:%S",time.localtime(time.time())),end=f" [I] [server.name] {osv} ")
    if oid == "#主机端":  
        print(f"p2p的映射的地址是 {oip}:{ocount}")
else:
    print(time.strftime("%Y/%m/%d %H:%M:%S",time.localtime(time.time())),end=" [I] [service.ip:count] ")
    print(f"映射的地址是 {oip}:{ocount}")
del mode,oip,ocount,oid,osv,i,omkey,shutil,socket,time
os.system("frpc.exe -c frpc.ini")
input("程序已关闭...")