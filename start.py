import os
while True:


    """#1 自检及文件读取阶段"""
    #初始化
    import socket
    version = "v1.6_beta"
    author = "LyceenAiro"
    update = "2023-3-27"
    LICENSEs = "MIT"
    names = locals()
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




    #开始
    print(f"欢迎使用Frp简易配置客户端[{version}]")
    #必要文件读取
    try:
        print("(0/5)正在加载server.ini by LyceenAiro/EazyFrpSetting")
        with open("./config/server.ini","r+",encoding="utf-8") as u:
            server = u.readlines()
        print("(1/5)正在加载more.ini by LyceenAiro/EazyFrpSetting")
        with open("./config/more.ini","r+",encoding="utf-8") as u:
            more = u.readlines()
        print("(2/5)正在加载LinkExample.ini by LyceenAiro/EazyFrpSetting")
        with open("./config/LinkExample.ini","r+",encoding="utf-8") as u:
            linkexample = u.readlines()
    except:
        input("发生错误,请检查EazyFrpSetting文件完整性,EFS-github:https://github.com/LyceenAiro/EazyFrpSetting")
        exit()
    try:
        print("(3/5)正在寻找frpc.exe by fatedier/frp")
        with open("frpc.exe","r+"):
            print(end="")
    except:
        input("frpc.exe正在运行或不存在,\nfrp-github:https://github.com/fatedier/frp")
        exit()
    #链接文件读取
    print("(4/5)正在读取link文件")
    linknum = 0
    link = []
    while True:
        linknum = linknum + 1
        linkfine = "link" + str(linknum)
        linkopen = "linko" + str(linknum)
        try:
            names[linkopen] = open(f"./config/{linkfine}.ini","r+",encoding="utf-8")
            names[linkfine] = names[linkopen].readlines()
            names[linkopen].close()
            link.append(linkfine)
        except:
            linknum = linknum - 1
            del linkfine
            print("(5/5)加载完成")
            import time
            time.sleep(0.5)
            del time
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
            "[q]保存并启动\n"+
            "[0]服务连接\n"+
            "[1]映射链接\n"+
            "[2]其他配置\n"+
            "[3]保存并退出"
        )
        inp = input("配置:")
        if inp == "0":
            """
            #2-0 服务连接
            #配置Frp服务器的链接和密匙
            """
            while True:
                os.system("cls")
                print(
                    "主菜单-服务连接\n"+
                    "[q]返回菜单\n"+
                    "[1]通讯地址\n"+
                    "[2]通讯端口\n"+
                    "[3]通讯密匙"
                )
                inp = input("配置:")
                #返回菜单
                if inp == "q":
                    break
                #通讯地址
                elif inp == "1":
                    os.system("cls")
                    print("主菜单-服务连接-通讯地址\n当前与服务器的ip地址是"+server[2].split('=')[1])
                    ipset = input("配置:")
                    flag = ipcheck(ipset)
                    if flag == False:
                        input("IP地址不合法")
                    else:
                        server[2] = "server_addr =" + ipset + "\n"
                    del ipset,flag
                #通讯端口
                elif inp == "2":
                    os.system("cls")
                    print("主菜单-服务连接-通讯端口\n当前设置的服务端口是"+server[4].split('=')[1])
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
                    print("主菜单-服务连接-通讯密钥\n请输入密钥")
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
                    "[q]返回菜单\n"+
                    "[c][创建新的链接]")
                for i in range(linknum):
                    setin = "link" + str(i+1)
                    print(f"[{i+1}]",
                        names[setin][1].strip("[").rstrip("]\n"),"|",
                        names[setin][3].split("=")[1].strip(),"|",
                        names[setin][5].split("=")[1].strip(),"|",
                        names[setin][7].split("=")[1].strip()+" -> "+
                        names[setin][9].split("=")[1].strip())
                inp = input("配置:")
                #返回菜单
                if inp == "q":
                    break
                #创建新的链接
                elif inp == "c":
                    os.system("cls")
                    print("主菜单-映射链接-创建链接")
                    creatlink = linkexample.copy()
                    #链接名配置
                    inp = input("·链接名称(可选):")
                    if inp == "":
                        str(linknum)
                        i = "link" + str(linknum+1)
                        creatlink[1] = "[" + i + "]\n"
                    else:
                        creatlink[1] = "[" + inp + "]\n"
                    #协议设置
                    inp = input("[1]tcp\n[2]udp\n[3]xtcp-host\n[4]xtcp-client\n[5]stcp\n配置:")
                    if inp == "1":
                        creatlink[3] = "type = tcp\n"
                    elif inp == "2":
                        creatlink[3] = "type = udp\n"
                    elif inp == "3":
                        creatlink[3] = "type = xtcp\n"
                        i = "host"
                    elif inp == "4":
                        creatlink[3] = "type = xtcp\n"
                    elif inp == "5":
                        creatlink[3] = "type = stcp\n"
                    else:
                        continue
                    #配置本机网卡
                    ip = socket.gethostbyname(socket.gethostname())
                    inp = input("·配置网卡IP(留空自动获取):")
                    if inp == "":
                        creatlink[5] = "local_ip = " + ip + "\n"
                        print(f"自动获取了IP:{ip}")
                        del ip
                    else:
                        del ip
                        flag = ipcheck(inp)
                        if flag == True:
                            creatlink[5] = "local_ip = " + inp + "\n"
                            del flag
                        else:
                            input("IP地址不合法,请重新创建")
                            del flag,creatlink
                            continue
                    #配置本地转发端口
                    inp = input("·配置本地转发端口:")
                    flag = portcheck(inp)
                    if flag == True:
                        creatlink[7] = "local_port = " + inp + "\n"
                        del flag
                    else:
                        input("端口必须在1024~65565的范围内")
                        del flag,creatlink
                        continue
                    #配置映射出端口
                    inp = input("·配置映射端口:")
                    flag = portcheck(inp)
                    if flag == True:
                        creatlink[9] = "remote_port = " + inp + "\n"
                        del flag
                    else:
                        del flag,creatlink
                        input("端口必须在1024~65565的范围内")
                        continue
                    #拓展配置
                    creatlink[14] = "#Frp\n"
                    if creatlink[3].split("=")[1].strip() == "xtcp":
                        #配置点对点端密匙
                        inp = input("·配置隧道密匙(可选):")
                        if inp == "":
                            creatlink[11] = "sk = " + inp + "\n"
                        else:
                            creatlink[11] = "#sk = \n"
                        creatlink[14] = "#server\n"
                        if i != "host":
                            #配置点对点服务名称
                            inp = input("·配置隧道服务名称:")
                            creatlink[13] = "server_name = " + inp + "\n"
                            creatlink[14] = "#client\n"
                    elif creatlink[3].split("=")[1].strip() == "stcp":
                        inp = input("·配置隧道密匙(可选):")
                        if inp == "":
                            creatlink[11] = "sk = " + inp + "\n"
                        else:
                            creatlink[11] = "#sk = \n"
                        creatlink[14] = "#sFrp\n"
                    #保存并创建链接
                    linknum = linknum + 1
                    linkfine = "link" + str(linknum)
                    names[linkfine] = creatlink
                    linkfine = "linko" + str(linknum)
                    names[linkfine] = "Newlink"
                    del linkfine,creatlink
                else:
                    #其他链接配置
                    try:
                        setin = "link" + inp
                        tryis = names[setin][14]
                        del tryis
                    except:
                        input("没有指定的链接")
                        continue
                    while True:
                        os.system("cls")
                        print(f"主菜单-映射链接-{setin}\n"+names[setin][14]+
                            "[q]返回"+
                            "\n[1]链接名称",names[setin][1].strip("[").rstrip("]\n")+
                            "\n[2]协议类型",names[setin][3].split("=")[1].strip()+
                            "\n[3]本机网卡",names[setin][5].split("=")[1].strip()+
                            "\n[4]转发端口",names[setin][7].split("=")[1].strip()+
                            "\n[5]映射端口",names[setin][9].split("=")[1].strip()
                        )
                        if names[setin][14] == "#client\n":
                            print(
                                "[6]隧道密匙",names[setin][11].split("=")[1].strip()+
                                "\n[7]对点服务",names[setin][13].split("=")[1].strip()
                            )
                        elif names[setin][14] != "#Frp\n":
                            print(
                                "[6]对点密匙",names[setin][11].split("=")[1].strip()
                            )
                        inp = input("\n配置:")
                        if inp == "q":
                            break
                        elif inp == "1":
                            os.system("cls")
                            print(f"主菜单-映射链接-{setin}-链接名称\n当前的配置:"+names[setin][1].strip("[").rstrip("]\n"))
                            inp = input("新的配置:")
                            if inp != "":
                                names[setin][1] = "[" + inp + "]\n"
                            else:
                                input("配置失败,内容不能为空")
                        elif inp == "2":
                            os.system("cls")
                            print(f"主菜单-映射链接-{setin}-协议类型\n当前的配置:"+names[setin][3].split('=')[1].strip()+"\n[1]tcp\n[2]udp\n[3]xtcp-host\n[4]xtcp-client\n[5]stcp")
                            inp = input("新的配置:")
                            if inp == "1":
                                names[setin][3] = "type = tcp\n"
                                names[setin][14] = "#Frp\n"
                            elif inp == "2":
                                names[setin][3] = "type = udp\n"
                                names[setin][14] = "#Frp\n"
                            elif inp == "3":
                                names[setin][3] = "type = xtcp\n"
                                names[setin][14] = "#server\n"
                            elif inp == "4":
                                names[setin][3] = "type = xtcp\n"
                                names[setin][14] = "#client\n"
                            elif inp == "5":
                                names[setin][3] = "type = stcp\n"
                                names[setin][14] = "#sFrp\n"
                        elif inp == "3":
                            os.system("cls")
                            print(f"主菜单-映射链接-{setin}-本机网卡\n当前的配置:"+names[setin][5].split('=')[1].strip())
                            ip = socket.gethostbyname(socket.gethostname())
                            inp = input("新的配置(输入a自动配置):")
                            if inp == "a":
                                names[setin][5] = "local_ip = " + ip + "\n"
                                del ip
                            elif inp == "":
                                del ip
                                input("配置不生效,内容不能为空")
                            else:
                                del ip
                                flag = ipcheck(inp)
                                if flag == True:
                                    names[setin][5] = "local_ip = " + inp + "\n"
                                    del flag
                                else:
                                    input("IP地址不合法")
                                    del flag
                        elif inp == "4":
                            os.system("cls")
                            print(f"主菜单-映射链接-{setin}-转发端口\n当前的配置:"+names[setin][7].split('=')[1].strip())
                            inp =input("新的配置:")
                            flag = portcheck(inp)
                            if flag == True:
                                names[setin][7] = "local_port = " + inp + "\n"
                                del flag
                            else:
                                del flag
                                input("端口必须在1024~65565的范围内")
                        elif inp == "5":
                            os.system("cls")
                            print(f"主菜单-映射链接-{setin}-映射端口\n当前的配置:"+names[setin][9].split('=')[1].strip())
                            inp = input("新的配置:")
                            flag = portcheck(inp)
                            if flag == True:
                                names[setin][9] = "remote_port = " + inp + "\n"
                                del flag
                            else:
                                del flag
                                input("端口必须在1024~65565的范围内")
                        elif names[setin][14].strip() != "#Frp":
                            if inp == "6":
                                os.system("cls")
                                print(f"主菜单-映射链接-{setin}-隧道密匙\n当前的配置:"+names[setin][11].split('=')[1].strip())
                                inp = input("新的配置:")
                                if inp != "":
                                    names[setin][11] = "sk = " + inp + "\n"
                                else:
                                    names[setin][11] = "#sk = \n"
                            elif inp == "7" and names[setin][14].strip() == "#client":
                                os.system("cls")
                                print(f"主菜单-映射链接-{setin}-对点服务\n当前的配置:"+names[setin][13].split('=')[1].strip())
                                inp = input("新的配置:")
                                if inp != "":
                                    names[setin][13] = "server_name = " + inp + "\n"
                                else:
                                    input("配置不生效,内容不能为空")




        elif inp == "2":
            """
            #2-2 其他配置
            #其他软件配置
            """
            while True:
                os.system("cls")
                inp = input("主菜单-其他配置\n[q]返回菜单\n[1]自动回应\n[2]清除链接\n[3]版本信息\n\n配置:")
                #返回菜单
                if inp == "q":
                    break
                #配置自动回应
                elif inp == "1":
                    os.system("cls")
                    inp = input("主菜单-其他配置-自动回应\n修改自动回应的时间,现在的设置是"+more[1].split('=')[1]+"\n配置:")
                    try:
                        settime = int(inp)
                    except:
                        input("你输入的格式错误")
                        continue
                    if settime >= 0 :
                        more[1] = "heartbeat_timeout = " + inp + "\n"
                    del settime
                elif inp == "2":
                    while True:
                        os.system("cls")
                        inp = input("主菜单-其他配置-清除链接\n自动清除所有链接并保存关闭程序,已有的链接数:"+str(linknum)+"\n[iknow]确认删除\n[q]返回\n\n配置:")
                        if inp == "iknow":
                            inp = input("你确定要清除所有链接吗?(y确定)")
                            if inp == "y":
                                for i in range(linknum):
                                    setfile = "link" + str(i+1) + ".ini"
                                    os.remove(f"./config/{setfile}")
                                exit()
                        elif inp == "q":
                            break
                        elif inp == "":
                            continue
                        else:
                            input("没有所选指令")
                elif inp == "3":
                    os.system("cls")
                    print("主菜单-其他配置-版本信息\n版本",version,"\n版期",update,"\n作者",author,"\n许可",LICENSEs)
                    input()
                elif inp == "":
                    continue
                else:
                    input("没有所选的指令")
        elif inp == "3" or "q":
            """
            #2-3 服务连接
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
            while pinf != 0:
                setin = "link" + str(pinf)
                filein = "link" + str(pinf) + ".ini"
                #保存链接
                with open(f"./config/{filein}","w+",encoding="utf-8") as u:
                    for i in names[setin]:
                        u.write(i)
                pinf = pinf - 1
            if inp == "3":
                exit()
            #检测link列表
            elif linknum == 0:
                input("没有需要启动的链接...")
                continue
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
    import time
    os.system("cls")
    #连接可视
    for i in range(linknum):
        setin = "link" + str(i+1)
        #保存链接
        print(time.strftime("%Y/%m/%d %H:%M:%S",time.localtime(time.time())),"[I]",names[setin][1].rstrip("]\n")+":"+names[setin][7].split('=')[1].strip()+"]",end=" ")
        print("映射的地址是",server[2].split('=')[1].strip()+":"+names[setin][9].split('=')[1].strip())
    #启动初始化
    frpc = server
    for i in range(linknum):
        setin = "link" + str(i+1)
        frpc = frpc + names[setin]
    frpc = frpc + more
    with open("frpc.ini","w+",encoding="utf-8") as u:
        for i in frpc:
            u.write(i)
    pinf = linknum
    #缓存清除
    while pinf != 0:
        setin = "link" + str(pinf)
        setin2 = "linko" + str(pinf)
        del names[setin],names[setin2]
        pinf = pinf - 1
    del pinf,setin,setin2,linknum
    del frpc,server,more,linkexample,i,u,link,linkopen,names,filein,inp
    del time,socket,ipcheck,portcheck,version,author,LICENSEs,update
    #启动服务
    os.system("frpc.exe -c frpc.ini")
    inp = input("Frp已结束运行...")